const resultText = document.getElementById("result-text");
const restartButton = document.getElementById("restart-button");
const quizForm = document.getElementById("quiz-form");

if (resultText) {
  const correctAnswer = "red";
  const userAnswer = localStorage.getItem("answer");

  if (userAnswer === correctAnswer) {
    resultText.textContent =
      "Correct! The RGB values (255, 0, 0) represent Red.";
  } else {
    resultText.textContent =
      "Incorrect! The RGB values (255, 0, 0) represent Red.";
  }
}

if (restartButton) {
  restartButton.addEventListener("click", () => {
    localStorage.removeItem("answer");
    location.href = "index.html";
  });
}

if (quizForm) {
  quizForm.addEventListener("submit", (e) => {
    e.preventDefault();
    const answer = document.querySelector('input[name="answer"]:checked').value;
    localStorage.setItem("answer", answer);
    location.href = "result.html";
  });
}
