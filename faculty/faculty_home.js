var showA = false;

/*
document.getElementById("courses").onchange = function change() // auto filled
{
    var sel = document.getElementById("courses");
    document.getElementById("classnameE").value = sel.options[sel.selectedIndex].value;
}
*/

document.getElementById("addCourseButton").onclick = function addCourse()
{
    if(!showA)
    {
        // edit 
        //showE = false;
        //document.querySelector(".editCourseForm").style.display = "none";
        //document.getElementById("editCourseButton").innerHTML = "Edit Course";

        document.querySelector(".addCourseForm").style.display = "block";
        document.getElementById("addCourseButton").innerHTML = "Cancel";
    }
    else
    {
        document.querySelector(".addCourseForm").style.display = "none";
        document.getElementById("addCourseButton").innerHTML = "Add Course";
    }
    showA = !showA;
}



