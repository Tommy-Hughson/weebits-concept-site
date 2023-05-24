const arrow = document.querySelectorAll(".arrow")
var counter = 0

arrow.forEach(e => {
  const side = e.classList[1]
  // e.firstElementChild.style.fill="green";
  e.addEventListener("click", () => {
    console.log("click: " + side);
    const product = document.querySelectorAll(".product")
    product[counter].classList.remove("product--visible");
    if (side === "arrow--left") {
        counter -= 1;
        if (counter < 0) {
            counter = 4;
        }
    } else {
      counter += 1;
      if (counter > 4) { 
        counter = 0;
      }
    }
    console.log(counter);
    product[counter].classList.add("product--visible");
  })
})