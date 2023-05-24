const LazyObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        const productImage = entry.target.querySelector("img");
        if (productImage.src === "")productImage.src = productImage.dataset.src;
        else console.log("not lazy")
        entry.target.classList.replace("lazyLoad", "isVisible");
        LazyObserver.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.2 }
);
const LazyLoadElements = document.querySelectorAll(".lazyLoad");
LazyLoadElements.forEach((el) => {
  LazyObserver.observe(el);
});
