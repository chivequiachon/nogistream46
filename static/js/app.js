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
