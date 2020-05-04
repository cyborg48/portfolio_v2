var objs_raw;
var textbased = [];
var imgbased = [];

var gallery = document.getElementById("gallery");
var boxes = [];
var fading = false;

var currentTheme;

currentTheme = localStorage.getItem('theme') ? localStorage.getItem('theme') : null;

if (currentTheme) {
    document.documentElement.setAttribute('data-theme', currentTheme);
    localStorage.setItem('theme', currentTheme);
    if(currentTheme == 'light'){
        document.getElementById("toggle").src = "/static/gallery/toggle_theme_black.png";
    } else{
        document.getElementById("toggle").src = "/static/gallery/toggle_theme_white.png";
    }
} else{
    document.documentElement.setAttribute('data-theme', 'light');
    localStorage.setItem('theme', 'light');
}

function load(){

    $(window).scrollTop(0);

}

function show(cat){

  
    window.location = '#gallery';

}

function open(i){

    window.location = '#gallery';

}

function switchTheme(){
    console.log("clicked");
    if (currentTheme == 'light') {
        currentTheme = 'dark';
        document.documentElement.setAttribute('data-theme', 'dark');
        localStorage.setItem('theme', 'dark'); //add this
        console.log("checked")
        document.getElementById("toggle").src = "/static/gallery/toggle_theme_white.png";
    }
    else {
        currentTheme = 'light';
        document.documentElement.setAttribute('data-theme', 'light');
        localStorage.setItem('theme', 'light'); //add this
        document.getElementById("toggle").src = "/static/gallery/toggle_theme_black.png";
    }  
    console.log(currentTheme);
}