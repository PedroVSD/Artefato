const hamburger = document.querySelector(".hamburger");
const nav = document.querySelector(".nav");
const button = document.querySelector(".A110");

button.addEventListener("click", () => { console.log(button.classList); });

hamburger.addEventListener("click", () => nav.classList.toggle("active"));




