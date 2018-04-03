function loadDoc() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("output").innerHTML = this.responseText;
    } else if (this.readyState == 4) {
      document.getElementById("output").innerHTML = this.status + ": Chyba aplikace";
    }
  };
  var lang = document.querySelector("input[name=lang]:checked").value;
  xhttp.open("POST", "translit.cgi?" + lang, true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  var inp = document.getElementById("inputText").value;
  xhttp.send(inp);
}

$("input[name=lang]").change(function(){
    loadDoc();
});

$("#inputText").on('keyup paste', function(e) {
    clearTimeout($(this).data('timeout'));
    $(this).data('timeout', setTimeout(function(){
        loadDoc();
    }, 300));
});
