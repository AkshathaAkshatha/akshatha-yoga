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
    event.preventDefault();

    var data = new FormData(form);
    var text = [
      "Name: " + (data.get("name") || "").toString().trim(),
      "Email: " + (data.get("from") || "").toString().trim(),
      "Session: " + (data.get("session") || "").toString().trim(),
      "",
      (data.get("note") || "").toString().trim(),
    ].join("\n");

    var ready = document.querySelector("[data-letter-ready]");
    var body = document.querySelector("[data-letter-body]");
    if (ready && body) {
      body.textContent = text;
      ready.hidden = false;
    }

    var email = (form.getAttribute("data-email") || "").trim();
    if (!email) {
      return;
    }

    window.location.href = "mailto:" + email
      + "?subject=" + encodeURIComponent("Yoga with Akshatha")
      + "&body=" + encodeURIComponent(text);
  });

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
