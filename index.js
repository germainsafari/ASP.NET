const navbar = (
    <nav>
        <h1>Shopping List</h1>
        <ul>
            <li>bread</li>
            <li>bread</li>
            <li>bread</li>
        </ul>
    </nav>
)


ReactDom.render(navbar, document.getElementById("root"))

let language = "JavaScript";
let library = "React";
let message = `Hello ${language} and ${library}!`;
console.log(message);
// js declaration are hoisted
function myFuntion() {
    const message = document.getElementById("message");
    message.innerHTML = "Hello World";
    message.style.color = "red";
    message.style.backgroundColor = "black";
    message.style.fontSize = "50px";
    message.style.padding = "20px";
    message.style.textAlign = "center";
    message.style.borderRadius = "10px";
    let x = document.getElementById("demo");
    x.innerHTML = "Hello JavaScript!";
    try {
        adddlert("Welcome guest!");
        if(x.trim() == "") throw "empty";
        if(isNaN(x)) throw "not a number";
        x = Number(x);
        if (x > 10) throw "too high";
        if (x < 5) throw "not a number";
    } catch (err) {
        console.log(err)
    }
}