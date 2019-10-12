const addEvents = () => {
  const seeMoreBtn = document.getElementById("see-more-btn");
  const description = document.getElementById("description");

  if (description.offsetHeight < description.scrollHeight) {
    seeMoreBtn.style.display = "block";
  } else {
    seeMoreBtn.style.display = "none";
  }

  seeMoreBtn.addEventListener("click", () => {
    if (seeMoreBtn.innerText == "See more") {
      description.style.height = "auto";
      seeMoreBtn.textContent = "See less";
    } else {
      description.style.height = "205px";
      seeMoreBtn.textContent = "See more";
    }
  });

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
