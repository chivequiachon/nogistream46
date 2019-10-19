const addEvents = () => {
  const burger = document.getElementById("burger");
  const mobileMenu = document.getElementById("mobile-menu");
  burger.addEventListener("click", () => {
    mobileMenu.style.animation = `1s fadeIn`;
    mobileMenu.style.animationFillMode = "forwards";
  });

  const mobileMenuClose = document.getElementById("close-mobile-menu");
  mobileMenuClose.addEventListener("click", () => {
    mobileMenu.style.animation = `1s fadeOut`;
    mobileMenu.style.animationFillMode = "forwards";
  });

  const mobileSearchBtn = document.getElementById("search-btn");
  const mobileSearchDiv = document.getElementById("mobile-search");
  mobileSearchBtn.addEventListener("click", () => {
    if (
      mobileSearchDiv.style.animation ==
      "1s ease 0s 1 normal forwards running pullDown"
    ) {
      mobileSearchDiv.style.animation = `pullUp 1s`;
    } else {
      mobileSearchDiv.style.animation = `pullDown 1s`;
    }
    mobileSearchDiv.style.animationFillMode = "forwards";
  });
};

addEvents();

$.ajaxSetup({
  beforeSend: function (xhr, settings) {
    function getCookie(name) {
      var cookieValue = null;
      if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
          var cookie = jQuery.trim(cookies[i]);
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
          }
        }
      }
      return cookieValue;
    }

    if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
      // Only send the token to relative URLs i.e. locally.
      xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
  }
});
