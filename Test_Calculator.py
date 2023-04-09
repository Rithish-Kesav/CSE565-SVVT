import pyautogui
import time
import unittest
import pygetwindow as gw


class TestCalculator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Start the calculator application
        import subprocess
        cls.calculator_process = subprocess.Popen(['python3', 'Calculator.py'])
        time.sleep(5)  # Wait for the application to load

    @classmethod
    def tearDownClass(cls):
        # Close the calculator application
        cls.calculator_process.terminate()

    def get_display_text(self):
        calculator_win = gw.getWindowsWithTitle('Calculator')[0]
        for win in calculator_win.childWindows:
            if win.title == 'Label':
                return win.properties['text']

    def test_basic_calculator_addition(self):
        # Navigate to Basic Calculator tab
        pyautogui.click(100, 50)  # Adjust coordinates as needed
        time.sleep(1)

        # Perform addition: 3 + 4
        pyautogui.click(200, 250)  # Click on '3'
        pyautogui.click(350, 350)  # Click on '+'
        pyautogui.click(250, 250)  # Click on '4'
        pyautogui.click(400, 300)  # Click on '='
        time.sleep(1)

        # Check the result
        actual_result = float(self.get_display_text())
        self.assertEqual(7.0, actual_result)

    def test_scientific_calculator_sin(self):
        # Navigate to Scientific Calculator tab
        pyautogui.click(250, 50)  # Adjust coordinates as needed
        time.sleep(1)

        # Perform sine function: sin(30) in degrees
        pyautogui.write("30")
        pyautogui.click(100, 150)  # Click on 'sin'
        pyautogui.click(250, 250)  # Click on '='
        time.sleep(1)

        # Check the result
        actual_result = float(self.get_display_text())
        self.assertAlmostEqual(0.5, actual_result, delta=0.0001)

    def test_currency_converter_usd_to_eur(self):
        # Navigate to Currency Converter tab
        pyautogui.click(400, 50)  # Adjust coordinates as needed
        time.sleep(1)

        # Set amount and currencies
        pyautogui.write("100")
        pyautogui.click(200, 100)  # Click on 'From' drop-down
        pyautogui.click(200, 150)  # Select 'USD'
        pyautogui.click(200, 200)  # Click on 'To' drop-down
        pyautogui.click(200, 250)  # Select 'EUR'
        pyautogui.click(100, 300)  # Click on 'Convert'
        time.sleep(1)

        # Check the result
        actual_result = float(self.get_display_text())
        expected_result = 100 * 0.85  # Assuming a conversion rate of 0.85 for USD to EUR
        self.assertAlmostEqual(expected_result, actual_result, delta=0.01)


if __name__ == "__main__":
    unittest.main()
