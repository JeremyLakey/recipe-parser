

function doParse() {
    console.log("Parsing...");
    let ele = document.getElementById("url-input");
    let value = ele.value;
    ele.value = "";

    let headers = new Headers();
    headers.append('Access-Control-Allow-Origin', '*');
    headers.append('GET', 'POST', 'OPTIONS');

    fetch("http://127.0.0.1:5001/parse/?url=" + value,
    {
        method: "POST",
    }).then( res => {
        if (res.status != 200) throw new Error("Oof")
        
        let filename = res.headers.get('Content-Disposition').split(";")[1].split("=")[1]
        filename = filename.slice(1, filename.length - 1)
        console.log(filename)
        return {filename: filename, blob: res.blob()}
    })
    .then( async (ob) => {
        const blob = await ob.blob
        console.log("blob")
        console.log(blob)
        var url = window.URL.createObjectURL(blob);
        console.log(url)
        var a = document.createElement('a');
        a.href = url;
        a.download = ob.filename;
        document.body.appendChild(a); // we need to append the element to the dom -> otherwise it will not work in firefox
        a.click();    
        a.remove();  //afterwards we remove the element again 
    }).catch((e)=> console.log(e));
}

function maybeParse(e) {
    if (e.key === 'Enter') doParse();
}


document.getElementById("submit").onclick = doParse;
document.getElementById("url-input").onkeyup = maybeParse;


