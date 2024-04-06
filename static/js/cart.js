const cartBtn = document.getElementById("cartbtn");
const cartOpenClose = document.getElementById("cart-open-close");
const cartCloseBtn = document.getElementById("closeCartbtn");
const overlay = document.getElementById("overlay-cart");

cartBtn.addEventListener("click", () => {
    cartOpenClose.style.display = "block";
    overlay.style.display = "block"; // Show overlay
    document.body.style.overflow = 'hidden';  // Disable scrolling
    cartOpenClose.style.animation = "";
    cartOpenClose.style.animation = "cartOpenClose 0.3s ease";
});

cartCloseBtn.addEventListener("click", () => {
    cartOpenClose.style.animation = "";
    cartOpenClose.style.animation = "cartOpenCloseReverse 0.3s ease";
    setTimeout(() => {
        cartOpenClose.style.display = "none";
        overlay.style.display = "none"; // Hide overlay
        document.body.style.overflow = "auto"; // Enable scrolling
    }, 300);

});

overlay.addEventListener("click", (event) => {
    event.stopPropagation(); // Stop the event from bubbling up to the document
    cartOpenClose.style.animation = "";
    cartOpenClose.style.animation = "cartOpenCloseReverse 0.3s ease";
    setTimeout(() => {
        cartOpenClose.style.display = "none";
        overlay.style.display = "none"; // Hide overlay
        document.body.style.overflow = "auto"; // Enable scrolling
    }, 300);
})






