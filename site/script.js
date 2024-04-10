

function doParse() {
    console.log("Parsing...");
    let ele = document.getElementById("url-input");
    let value = ele.value;
    ele.value = "";
    console.log(value);
}

function maybeParse(e) {
    if (e.key === 'Enter') doParse();
}


document.getElementById("submit").onclick = doParse;
document.getElementById("url-input").onkeyup = maybeParse;


