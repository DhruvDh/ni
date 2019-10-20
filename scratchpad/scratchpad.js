window.onload = function() {
    let a = 2;
    let b = 2;

    let c = () => a + b;

    document.getElementById('div').innerHTML = c();

    console.log(c());

    a = 3;

    document.getElementById('div').innerHTML = c();
   }