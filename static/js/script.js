

function openPage(pageNumber){
    var pageContent;
    pageContent = document.getElementsByClassName("pageContent")

    for (i = 0; i < pageContent.length; i++) {
        pageContent[i].style.display = "none";
        document.getElementById(pageNumber).style.display = "block"

    }
}


  // Get the element with id="defaultOpen" and click on it
  document.getElementById("defaultOpen").click();