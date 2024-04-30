document.addEventListener("DOMContentLoaded", function() {
  fetch('price.txt')
      .then(response => response.text())
      .then(text => {
          document.getElementById('text-container').innerText = text;
      })
      .catch(error => {
          console.error('Error:', error);
      });
});
