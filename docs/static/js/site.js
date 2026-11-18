(function () {
  var toggle = document.querySelector(".nav-toggle");
  var menu = document.querySelector(".nav-links");

  if (toggle && menu) {
    toggle.addEventListener("click", function () {
      var open = menu.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      toggle.textContent = open ? "Close" : "Menu";
    });

    menu.addEventListener("click", function (event) {
      if (!event.target.closest("a")) {
        return;
      }
      menu.classList.remove("is-open");
      toggle.setAttribute("aria-expanded", "false");
      toggle.textContent = "Menu";
    });
  }

  var form = document.querySelector("[data-letter]");
  if (!form) {
    return;
  }

  form.addEventListener("submit", function (event) {
    var ajax = (form.getAttribute("data-form-ajax") || "").trim();
    if (!ajax) {
      event.preventDefault();
      showDraft(form);
      return;
    }

    event.preventDefault();
    var data = new FormData(form);
    if ((data.get("_honey") || "").toString().trim()) {
      return;
    }

    var button = form.querySelector("[type='submit']");
    var original = button ? button.textContent : "";
    if (button) {
      button.disabled = true;
      button.textContent = "Sending";
    }

    var payload = {};
    data.forEach(function (value, key) {
      if (key !== "_honey") {
        payload[key] = value;
      }
    });

    fetch(ajax, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Accept": "application/json",
      },
      body: JSON.stringify(payload),
    }).then(function (response) {
      return response.json().catch(function () {
        return {};
      }).then(function (body) {
        if (!response.ok || String(body.success) === "false") {
          throw new Error("send failed");
        }
        return body;
      });
    }).then(function () {
      showResult(form, form.getAttribute("data-sent") || "The note is on its way.");
      form.reset();
    }).catch(function () {
      showResult(form, form.getAttribute("data-failed") || "The note did not leave this page.");
    }).finally(function () {
      if (button) {
        button.disabled = false;
        button.textContent = original;
      }
    });
  });

  function noteText(formElement) {
    var data = new FormData(formElement);
    return [
      "Name: " + (data.get("name") || "").toString().trim(),
      "Email: " + (data.get("email") || "").toString().trim(),
      "Session: " + (data.get("session") || "").toString().trim(),
      "",
      (data.get("message") || "").toString().trim(),
    ].join("\n");
  }

  function showDraft(formElement) {
    var ready = formElement.querySelector("[data-letter-ready]");
    var body = formElement.querySelector("[data-letter-body]");
    var copy = formElement.querySelector("[data-copy]");
    if (body) {
      body.hidden = false;
      body.textContent = noteText(formElement);
    }
    if (copy) {
      copy.hidden = false;
    }
    if (ready) {
      ready.hidden = false;
    }
  }

  function showResult(formElement, message) {
    var ready = formElement.querySelector("[data-letter-ready]");
    var status = formElement.querySelector("[data-letter-status]");
    if (status) {
      status.hidden = false;
      status.textContent = message;
    }
    if (ready) {
      ready.hidden = false;
    }
  }

  var copy = document.querySelector("[data-copy]");
  var letterBody = document.querySelector("[data-letter-body]");
  if (!copy || !letterBody) {
    return;
  }

  copy.addEventListener("click", function () {
    var text = letterBody.textContent || "";
    var original = copy.textContent;

    function show(label) {
      copy.textContent = label;
      window.setTimeout(function () {
        copy.textContent = original;
      }, 2000);
    }

    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(function () {
        show("Copied");
      }).catch(function () {
        show("Select the note above");
      });
      return;
    }

    show("Select the note above");
  });
})();
