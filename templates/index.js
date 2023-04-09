function onButtonClick(value) {
  const display = document.getElementById("display");

  if (value === "=") {
    try {
      display.value = eval(display.value);
    } catch (error) {
      display.value = "Error";
    }
  } else {
    display.value += value;
  }
}
