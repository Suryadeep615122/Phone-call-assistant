function simulateCall() {
  const sampleText = "I forgot my password and need help resetting it.";

  document.getElementById("transcript").innerText = sampleText;

  fetch('http://127.0.0.1:5000/intent', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ transcript: sampleText })
  })
  .then(response => response.json())
  .then(data => {
    document.getElementById("intent").innerText = data.intent;
    document.getElementById("suggestion").innerText = data.answer;
  });
}
