document.getElementById("signin").addEventListener("click", function()
{
    document.querySelector(".popSignIn").style.display = "flex";
});

document.querySelector(".close").addEventListener("click", function()
{
    document.querySelector(".popSignIn").style.display = "none";
});

document.getElementById("reset").addEventListener("click", function()
{
    document.querySelector(".popSignIn").style.display = "none";
    document.querySelector(".popForget").style.display = "flex";
});

document.querySelector(".closeForget").addEventListener("click", function()
{
    document.querySelector(".popForget").style.display = "none";
});
