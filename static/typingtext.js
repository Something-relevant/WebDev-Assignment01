document.addEventListener('DOMContentLoaded',function(event){

  function typeWriter(text, i, fnCallback) {

    if (i < (text.length)) {

     document.querySelector("p").innerHTML = text.substring(0, i+1) +'<span aria-hidden="true"></span>';

      setTimeout(function() {
        typeWriter(text, i + 1, fnCallback)
      }, 100);
    }

    else if (typeof fnCallback == 'function') {
      setTimeout(fnCallback, 700);
    }
  }
