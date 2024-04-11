// Menu bar open close functionality


const menuBtn = document.getElementById("menuBtn");
const menuPage = document.getElementById("menu-btn-open-close");
const menuCloseBtn = document.getElementById("menuCloseBtn");
const overlayMenu = document.getElementById("overlay-menu");

menuBtn.addEventListener("click", () => {
    if (menuPage.style.display === "none" || menuPage.style.display === "") {
        menuPage.style.display = "block";
        overlayMenu.style.display = "block"; // Show overlayMenu
        document.body.style.overflow = "hidden"; // Disable scrolling
        menuPage.style.animation = "";
        menuPage.style.animation = "menuSlide 0.3s ease";
    } else {
        menuPage.style.animation = "";
        menuPage.style.animation = "menuReverseSlide 0.3s ease";
        setTimeout(() => {
            menuPage.style.display = "none";
            overlayMenu.style.display = "none"; // Hide overlayMenu
            document.body.style.overflow = "auto"; // Enable scrolling
        }, 300);
    }
    
});

menuCloseBtn.addEventListener("click", () => {
    menuPage.style.animation = "";
    menuPage.style.animation = "menuReverseSlide 0.3s ease";
    setTimeout(() => {
        menuPage.style.display = "none";
        overlayMenu.style.display = "none"; // Hide overlayMenu
        document.body.style.overflow = "auto"; // Enable scrolling
    }, 300);
});

// Close the menu when clicking outside of it on overlayMenu
overlayMenu.addEventListener("click", (event) => {
    event.stopPropagation(); // Stop the event from bubbling up to the document
    menuPage.style.animation = "";
    menuPage.style.animation = "menuReverseSlide 0.3s ease";
    setTimeout(() => {
        menuPage.style.display = "none";
        overlayMenu.style.display = "none"; // Hide overlayMenu
        document.body.style.overflow = "auto"; // Enable scrolling
    }, 300);
})
