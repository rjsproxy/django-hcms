var global;


var testcall = function(button, req, e)
{
    console.log(req.response);
}

var test = function(button)
{
    /*
    if(!global)
    {
        global = prompt('Greetings friend, may I enquire as to your surname?');
    }
    console.log(global);
    */

    var req = new XMLHttpRequest();
    req.onload = function (e) { testcall(button, req, e); };
    req.open('get', 'http://127.0.0.1:8000/hcms/elem/1/', true);
    req.send();

}


// Remove all content and create button.
// 
// Assumes child elements are not using jquery. If they are we should probably
// use jquery's .empty() method to clean things up properly.
//
var hcms_element_reset = function(elem)
{
    var button = document.createElement("BUTTON");
    button.appendChild(document.createTextNode("+"));

    button.onclick = function(){ test(button); }

    var fc = elem.firstChild;
    while(fc) {
        elem.removeChild(fc);
        fc = elem.firstChild;
    }
    elem.appendChild(button);
}

// console.log('\'Allo \'Allo!');

var elem = document.getElementById('hcms');
if(elem) {
    hcms_element_reset(elem);



} else {
    console.log('No element.');
}



/* OBJECT DEMO
var jedi = {
    name: "Yoda",
    age: 899,
    talk: function () { alert("another... Sky... walk..."); }
};
*/
