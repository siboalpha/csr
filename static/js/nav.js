function OpenCloseMenu() {
    const menu = document.getElementById("nav-menu");
    const OpenMenu = document.getElementById("OpenMenu")
    const CloseMenu = document.getElementById("CloseMenu")
    if (menu.style.display === "none") {
        menu.style.display = "flex"
        OpenMenu.style.display= "none"
        CloseMenu.style.display= "block"
    } else {
        menu.style.display = "none"
        OpenMenu.style.display = "block"
        CloseMenu.style.display = "none"
    }
}