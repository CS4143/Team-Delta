var showE = false;

/*
document.getElementById("courses").onchange = function change() // auto filled
{
    var sel = document.getElementById("courses");
    document.getElementById("classnameE").value = sel.options[sel.selectedIndex].value;
}
*/



document.getElementById("editCourseButton").onclick = function editCourse()
{
    if(!showE)
    {
        //adding
        //showA = false;
        //document.querySelector(".addCourseForm").style.display = "none";
        //document.getElementById("addCourseButton").innerHTML = "Add Course";

        document.querySelector(".editCourseForm").style.display = "block";
        document.getElementById("editCourseButton").innerHTML = "Cancel";
    }
    else
    {
        document.querySelector(".editCourseForm").style.display = "none";
        document.getElementById("editCourseButton").innerHTML = "Edit Course";
    }
    showE = !showE;
}
