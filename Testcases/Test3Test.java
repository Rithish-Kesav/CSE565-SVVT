// Generated by Selenium IDE
import org.junit.Test;
import org.junit.Before;
import org.junit.After;
import static org.junit.Assert.*;
import static org.hamcrest.CoreMatchers.is;
import static org.hamcrest.core.IsNot.not;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.remote.RemoteWebDriver;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.Dimension;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.Alert;
import org.openqa.selenium.Keys;
import java.util.*;
import java.net.MalformedURLException;
import java.net.URL;
public class Test3Test {
  private WebDriver driver;
  private Map<String, Object> vars;
  JavascriptExecutor js;
  @Before
  public void setUp() {
    driver = new ChromeDriver();
    js = (JavascriptExecutor) driver;
    vars = new HashMap<String, Object>();
  }
  @After
  public void tearDown() {
    driver.quit();
  }
  @Test
  public void test3() {
    // Test name: test3
    // Step # | name | target | value
    // 1 | open | http://127.0.0.1:8080/result.html?answer=red | 
    driver.get("http://127.0.0.1:8080/result.html?answer=red");
    // 2 | setWindowSize | 1440x900 | 
    driver.manage().window().setSize(new Dimension(1440, 900));
    // 3 | click | css=.container | 
    driver.findElement(By.cssSelector(".container")).click();
    // 4 | click | id=student-code | 
    driver.findElement(By.id("student-code")).click();
    // 5 | type | id=student-code | sdinaka1
    driver.findElement(By.id("student-code")).sendKeys("sdinaka1");
    // 6 | mouseDownAt | css=.container | 541.78125,158
    {
      WebElement element = driver.findElement(By.cssSelector(".container"));
      Actions builder = new Actions(driver);
      builder.moveToElement(element).clickAndHold().perform();
    }
    // 7 | mouseMoveAt | css=.container | 541.78125,158
    {
      WebElement element = driver.findElement(By.cssSelector(".container"));
      Actions builder = new Actions(driver);
      builder.moveToElement(element).perform();
    }
    // 8 | mouseUpAt | css=.container | 541.78125,158
    {
      WebElement element = driver.findElement(By.cssSelector(".container"));
      Actions builder = new Actions(driver);
      builder.moveToElement(element).release().perform();
    }
    // 9 | click | css=.container | 
    driver.findElement(By.cssSelector(".container")).click();
    // 10 | click | css=h1 | 
    driver.findElement(By.cssSelector("h1")).click();
    // 11 | click | id=result-text | 
    driver.findElement(By.id("result-text")).click();
    // 12 | click | css=.container | 
    driver.findElement(By.cssSelector(".container")).click();
    // 13 | mouseDownAt | id=slider | 186.625,4.234375
    {
      WebElement element = driver.findElement(By.id("slider"));
      Actions builder = new Actions(driver);
      builder.moveToElement(element).clickAndHold().perform();
    }
    // 14 | mouseMoveAt | id=slider | 186.625,4.234375
    {
      WebElement element = driver.findElement(By.id("slider"));
      Actions builder = new Actions(driver);
      builder.moveToElement(element).perform();
    }
    // 15 | mouseUpAt | id=slider | 186.625,4.234375
    {
      WebElement element = driver.findElement(By.id("slider"));
      Actions builder = new Actions(driver);
      builder.moveToElement(element).release().perform();
    }
    // 16 | type | id=slider | 10
    driver.findElement(By.id("slider")).sendKeys("10");
    // 17 | click | id=slider | 
    driver.findElement(By.id("slider")).click();
    // 18 | click | id=form | 
    driver.findElement(By.id("form")).click();
    // 19 | click | id=form | 
    driver.findElement(By.id("form")).click();
    // 20 | click | id=checkbox | 
    driver.findElement(By.id("checkbox")).click();
    // 21 | click | css=.container | 
    driver.findElement(By.cssSelector(".container")).click();
    // 22 | click | id=result-details | 
    driver.findElement(By.id("result-details")).click();
    // 23 | click | css=.container | 
    driver.findElement(By.cssSelector(".container")).click();
    // 24 | click | css=.container | 
    driver.findElement(By.cssSelector(".container")).click();
  }
}