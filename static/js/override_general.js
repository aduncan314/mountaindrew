function ChooseThis(id) {
    let idOptions = ["pdf", "html"];

    let this_index = idOptions.indexOf(id);
    idOptions.splice(this_index, 1);
    let otherIsSelected = document.getElementById(idOptions[0]).className.includes("btn-success");

    if (otherIsSelected) {
        document.getElementById("pdf").classList.toggle("btn-success");
        document.getElementById("html").classList.toggle("btn-success");
    } else {
        document.getElementById(id).classList.toggle("btn-success");
    }
    displayResume(id)
}

$(".jumbotron").hover(
    function () {
        $(this).addClass("shadow-lg")
    },
    function () {
        $(this).removeClass("shadow-lg")
    }
);

