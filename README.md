# Automated Cookie Clicker

A Python program that automates the clicking process in the Cookie Clicker game using the Selenium WebDriver library.

![Capture](https://github.com/GokulBakkiyarasu/Cookie_clicker_bot/assets/87391223/5a7efda3-d98c-4179-93fb-a0c9c374a80b)


## Getting Started

To get started with this program, you need to have the following:

### Prerequisites

- Python 3.x
- Selenium WebDriver
- Chrome WebDriver

### Installation

1. Clone the repository:

   ```
   git clone https://github.com/your_username/automated-cookie-clicker.git
   ```

2. Install Selenium WebDriver:

   ```
   pip install selenium
   ```

3. Download Chrome WebDriver:

   - Download the appropriate Chrome WebDriver version for your operating system from the official ChromeDriver website: [ChromeDriver Downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads)
   - Extract the downloaded file and note down the path to the `chromedriver.exe` file.

4. Update the driver path in the script:

   - Open the `cookie_clicker.py` file in a text editor.
   - Locate the `driver_path` variable and replace the existing path with the path to the `chromedriver.exe` file on your system.

     ```
     driver_path = r"C:\path\to\chromedriver.exe"
     ```

5. Run the program:

   ```
   python cookie_clicker.py
   ```

## How It Works

The program uses Selenium WebDriver to automate the clicking process in the Cookie Clicker game. It clicks on the cookie repeatedly to earn points and periodically checks the available upgrades in the game store to purchase the most expensive one that the player can afford.

The program follows the following steps:

1. Launches the Chrome WebDriver and opens the Cookie Clicker game page.
2. Locates the cookie element and starts clicking it repeatedly.
3. Periodically checks the available upgrades in the game store.
4. Determines the most expensive upgrade that the player can afford based on their current points.
5. Clicks on the upgrade to purchase it.
6. Repeats the above steps until a timeout is reached.

## Contributing

Contributions to this project are welcome. To contribute, follow these steps:

1. Fork this repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make and commit your changes (`git commit -am "Add new feature"`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Create a new Pull Request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

Special thanks to the Selenium and ChromeDriver development teams for providing the tools necessary for automating web browsers.

## Find me on
[![LinkedIn Badge](https://img.shields.io/badge/LinkedIn-Profile-informational?style=flat&logo=linkedin&logoColor=white&color=0D76A8)](https://www.linkedin.com/in/gokul-bakkiyarasu-531535251)
