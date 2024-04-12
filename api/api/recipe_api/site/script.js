

function doParse() {
    console.log("Parsing...");
    let ele = document.getElementById("url-input");
    let value = ele.value;
    ele.value = "";

    let headers = new Headers();
    headers.append('Access-Control-Allow-Origin', 'http://127.0.0.1:8000/');
    headers.append('Access-Control-Allow-Credentials', 'true');
    headers.append('GET', 'POST', 'OPTIONS');

    fetch("http://127.0.0.1:8000/parse/?url=" + value,
    {
        method: "POST",
    }).then( res => res.blob() )
    .then( blob => {
        console.log(blob)
        var url = window.URL.createObjectURL(blob);
        console.log(url)
        var a = document.createElement('a');
        a.href = url;
        a.download = "recipe.md";
        document.body.appendChild(a); // we need to append the element to the dom -> otherwise it will not work in firefox
        a.click();    
        a.remove();  //afterwards we remove the element again 
    });
}

function maybeParse(e) {
    if (e.key === 'Enter') doParse();
}


document.getElementById("submit").onclick = doParse;
document.getElementById("url-input").onkeyup = maybeParse;


