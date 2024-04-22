// Menu bar open close functionality
const menuBtn = document.getElementById("menuBtn");
const menuPage = document.getElementById("menu-btn-open-close");
const menuCloseBtn = document.getElementById("menuCloseBtn");
const overlayMenu = document.getElementById("overlay-menu");



function menuOpenHandler() {
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
}

function menuCloseHandler() {
    menuPage.style.animation = "";
    menuPage.style.animation = "menuReverseSlide 0.3s ease";
    setTimeout(() => {
        menuPage.style.display = "none";
        overlayMenu.style.display = "none"; // Hide overlayMenu
        document.body.style.overflow = "auto"; // Enable scrolling
    }, 300);
}

function overlayMenuHandler(event) {
    event.stopPropagation(); // Stop the event from bubbling up to the document
    menuPage.style.animation = "";
    menuPage.style.animation = "menuReverseSlide 0.3s ease";
    setTimeout(() => {
        menuPage.style.display = "none";
        overlayMenu.style.display = "none"; // Hide overlayMenu
        document.body.style.overflow = "auto"; // Enable scrolling
    }, 300);
}

// Add event listeners

menuBtn.addEventListener("click", menuOpenHandler);
menuCloseBtn.addEventListener("click", menuCloseHandler);
overlayMenu.addEventListener("click", overlayMenuHandler);

// Define cleanup function to remove event listeners
function cleanup() {
    menuBtn.removeEventListener('click', menuOpenHandler);
    menuCloseBtn.removeEventListener('click', menuCloseHandler);
    overlayMenu.removeEventListener('click', overlayMenuHandler);
}

// Call cleanup when the menu is permanently removed from the DOM or no longer needed
// cleanup();







const searchBtn = document.getElementById('search-btn-design');
const searchOpen = document.getElementById('search-bar-css');

function searchOpenHandler(){
    if(searchOpen.style.display === "none" || searchOpen.style.display === ""){
        searchOpen.style.display = "block";
    }else{
        searchOpen.style.display = "none";
    }
};

searchBtn.addEventListener('click', searchOpenHandler);


function cleanup(){
    searchBtn.removeEventListener('click', searchOpenHandler);

}


