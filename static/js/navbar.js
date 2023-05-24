var prevScrollPos = window.pageYOffset;

window.onscroll = function() {
    var currentScrollPos = window.pageYOffset;
    var navbar = document.getElementById("navbar");
    var stickyContent = document.getElementsByClassName("sticky-descr-left");
    var navHeight = navbar.offsetHeight + 10;
    if (prevScrollPos < currentScrollPos && prevScrollPos > window.innerHeight * 0.8) {
        navbar.style.top =  '-' + navHeight + "px";
        if (stickyContent.length) stickyContent[0].style.top = "0";
    } else {
        navbar.style.top = "0"
        if (stickyContent.length) stickyContent[0].style.top = navHeight + "px";
    }
    prevScrollPos = currentScrollPos;
}

