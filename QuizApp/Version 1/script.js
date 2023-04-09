const resultText = document.getElementById("result-text");
const restartButton = document.getElementById("restart-button");
// const quizForm = document.getElementById("quiz-form");
const quizForm = document.querySelector("quiz-form");

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
    const confirmStart = document.querySelector("#confirm-start");
    if (confirmStart.checked) {
      localStorage.setItem(
        "difficulty-level",
        document.querySelector('input[name="difficulty-level"]:checked').value
      );
      location.href = "quiz.html";
    } else {
      alert("Please confirm that you are ready to start the quiz.");
    }
  });
}
