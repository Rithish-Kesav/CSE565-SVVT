const resultText = document.getElementById("result-text");
const restartButton = document.getElementById("restart-button");
const startForm = document.querySelector("#start-form");
const quizForm = document.querySelector("#quiz-form");
const resultDetails = document.getElementById("result-details");
const checkbox = document.getElementById("checkbox");
const slider = document.getElementById("slider");
const sliderValue = document.getElementById("slider-value");

if (resultText) {
  const correctAnswer = "red";
  const userAnswer = new URLSearchParams(window.location.search).get("answer");

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
    location.href = "quiz.html";
  });
}

if (resultDetails && checkbox) {
  checkbox.addEventListener("change", () => {
    resultDetails.style.display = checkbox.checked ? "block" : "none";
  });
}

slider.addEventListener("input", () => {
  sliderValue.textContent = slider.value;
});

if (startForm) {
  startForm.addEventListener("submit", (e) => {
    e.preventDefault();
    const confirmStart = document.querySelector("#confirm-start");
    const studentCode = document.querySelector("#student-code").value;

    if (confirmStart.checked) {
      localStorage.setItem("student-code", studentCode);
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

if (quizForm) {
  quizForm.addEventListener("submit", (e) => {
    e.preventDefault();
    const answer = document.querySelector('input[name="answer"]:checked').value;
    localStorage.setItem("answer", answer);
    location.href = "result.html";
  });
}
