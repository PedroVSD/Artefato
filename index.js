const hamburger = document.querySelector(".hamburger");
const nav = document.querySelector(".nav");
const buttons = document.querySelectorAll(".true");
const subir = document.querySelector("#cima");
const descer = document.querySelector("#baixo");
const index = document.querySelector("#Andar");
const Primeiro = document.getElementById("1A");
const Segundo = document.getElementById("2A");
const Terceiro = document.getElementById("3A");




subir.addEventListener("click", () => {
    if(index.textContent === "Andar: 1")
    {
        index.textContent = "Andar: 2";
        Primeiro.style.zIndex = 0;
        Segundo.style.zIndex = 10;
    }

    else if(index.textContent == "Andar: 2")
    {
        index.textContent = "Andar: 3";
        Segundo.style.zIndex = 0;
        Terceiro.style.zIndex = 10;
    }

    else
        alert("Não tem mais andar!!!");

});

descer.addEventListener("click", () => {
    if(index.textContent === "Andar: 3")
    {
        index.textContent = "Andar: 2";
        Segundo.style.zIndex = 10;
        Terceiro.style.zIndex = 0;
    }

    else if(index.textContent == "Andar: 2")
    {
        index.textContent = "Andar: 1";
        Primeiro.style.zIndex = 10;
        Segundo.style.zIndex = 0;
    }

    else
        alert("Já está no terreo");

});

buttons.forEach(button => {
    button.addEventListener("click", () => {
        alert(button.id);
    });
});

hamburger.addEventListener("click", () => nav.classList.toggle("active"));




