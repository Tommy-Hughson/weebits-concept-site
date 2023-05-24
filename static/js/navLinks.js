const navToggle = document.querySelector(".side-nav-toggle")

const sideMenu = document.querySelector(".nav-links__primary")

navToggle.addEventListener("click", () => {
  const isOpened = navToggle.getAttribute("aria-expanded");
  if (isOpened === "false") {
    navToggle.setAttribute("aria-expanded", "true");
  } else {
    navToggle.setAttribute("aria-expanded", "false");
  }
})