function run()
{
    var radios = document.getElementsByName('account');
    var acc;
    
    for (var i = 0, length = radios.length; i < length; i++) 
    {
        if (radios[i].checked) 
        {
            acc = radios[i].value;
            break;
        }
    }

    //alert(acc);
    if(acc == "student")
    {
        location = "homeS.html";
    }
    else
    {
        location = "homeF.html";
    }

    return false;

}

document.getElementById("signup").addEventListener("click", function()
{
    document.querySelector(".popSignUp").style.display = "flex";
});

document.querySelector(".closeSU").addEventListener("click", function()
{
    document.querySelector(".popSignUp").style.display = "none";
});

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
