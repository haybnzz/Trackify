# Trackify

![Trackify Logo](https://github.com/haydenbanz/haydenbanz.github.io/blob/main/images/%20gitimage/hades23vfsd.png?raw=true)
[![Python - Trackify](https://img.shields.io/static/v1?label=Python&message=Trackify&color=%242A3E87&labelColor=%236A7DA8&style=for-the-badge&&logo=python)](https://github.com/haydenbanz/Trackify)
[![MIT License](https://img.shields.io/static/v1?label=License&message=MIT&color=%233DA639&labelColor=%23e3e3e3&style=for-the-badge)](https://github.com/haydenbanz/Trackify/blob/main/LICENSE)
[![Python Version](https://img.shields.io/static/v1?label=Python&message=3.6%2B&color=%230078D6&labelColor=%23e3e3e3&style=for-the-badge&logo=python)](https://www.python.org/downloads/)
[![GitHub Issues](https://img.shields.io/github/issues/haydenbanz/Trackify?style=for-the-badge)](https://github.com/haydenbanz/Trackify/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/haydenbanz/Trackify?style=for-the-badge)](https://github.com/haydenbanz/Trackify/pulls)
[![GitHub Stars](https://img.shields.io/github/stars/haydenbanz/Trackify?style=for-the-badge)](https://github.com/haydenbanz/Trackify/stargazers)
![Profile Views](https://komarev.com/ghpvc/?username=haydenbanz&color=%232A3E87&labelColor=%236A7DA8&style=for-the-badge)
[![GitHub Download](https://img.shields.io/static/v1?label=Download&message=Trackify&color=%242A3E87&labelColor=%236A7DA8&style=for-the-badge)](https://github.com/haydenbanz/Trackify/releases)


Trackify is a simple and powerful tool to monitor and track user activity, such as clicks, visits, and other interactions, using tiny pixel trackers. It helps you gather insights to improve your website or app performance, much like Google Analytics, but with minimal overhead and high privacy.


## Features
- Track user interactions with minimal impact on page performance.
- Easy-to-use pixel tracking system for clicks, page views, and other user activities.
- Send tracked data to Discord webhooks for real-time monitoring.
- Data is stored locally for easy access and analysis.
- Lightweight, transparent pixel image for unobtrusive tracking.

## Installation

### Requirements
- Python 3.x
- Flask
- Requests

### Setup Instructions
1. Clone the repository:
    ```bash
    git clone https://github.com/haydenbanz/Trackify.git
    cd Trackify
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set your Discord webhook URL by replacing the placeholder in `app.py`:
    ```python
    DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/your-webhook-url"
    ```

4. Run the Flask app:
    ```bash
    python app.py
    ```

5. Access the app via `http://127.0.0.1:5000` or your server's IP.

### Usage
- Add the tracking pixel to your website or app by including the following HTML:
    ```html
    <img src="http://your-server-ip:5000/pixel" alt="l"  />
    ```

- Use the JavaScript to capture and send user behavior (like clicks) to the Flask server:
    ```html
    <script>
        document.addEventListener('click', function(event) {
            const userBehaviorData = {
                eventType: 'click',
                element: event.target.tagName,
                timestamp: new Date().toISOString(),
            };

            fetch('http://your-server-ip:5000/user_behavior', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(userBehaviorData)
            })
            .then(response => response.json())
            .then(data => console.log('User behavior sent:', data))
            .catch(error => console.error('Error:', error));
        });
    </script>
    ```

### Notes
- Ensure that your server is accessible by your frontend to collect the tracking data.
- You can customize the data collection, pixel image, and Discord notifications as per your need.
- Consider deploying your Flask app on platforms like Heroku, DigitalOcean, or AWS to make it publicly accessible.

## Download Link
You can download Trackify directly from the GitHub repository:

[Trackify GitHub Repository](https://github.com/haydenbanz/Trackify)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contribution

We welcome contributions to Trackify! If you have suggestions for improvements, found a bug, or have a new feature request, feel free to contribute.

- [![GitHub Issues](https://img.shields.io/github/issues/haydenbanz/Trackify?style=for-the-badge)](https://github.com/haydenbanz/Trackify/issues)
- [![GitHub Pull Requests](https://img.shields.io/github/issues-pr/haydenbanz/Trackify?style=for-the-badge)](https://github.com/haydenbanz/Trackify/pulls)

### How to Contribute

1. **Fork the Repository**: Click the "Fork" button at the top right of the repository page to create your own copy of the repository.

2. **Clone Your Fork**: Clone your forked repository to your local machine using the following command:
    ```bash
    git clone https://github.com/your-username/Trackify.git
    ```

3. **Create a New Branch**: Create a new branch for your feature or bugfix:
    ```bash
    git checkout -b feature-or-bugfix-name
    ```

4. **Make Changes**: Make your changes or add your new feature.

5. **Commit Your Changes**: Commit your changes with a clear and concise commit message:
    ```bash
    git commit -m "Description of the changes"
    ```

6. **Push to Your Fork**: Push your changes to your forked repository:
    ```bash
    git push origin feature-or-bugfix-name
    ```

7. **Submit a Pull Request**: Go to the original repository and submit a pull request from your forked repository. Provide a detailed description of your changes in the pull request.

### Guidelines

- Follow the existing code style.
- Write clear and concise commit messages.
- Test your changes thoroughly before submitting a pull request.
- Ensure that your changes do not introduce new bugs or break existing functionality.
- Be respectful and open to feedback during the code review process.

Thank you for contributing to Trackify!

## 🌐 Support

[![Discord](https://img.shields.io/badge/Discord-CODE%20GLITCH%20Bot%20DISCORD%20SERVER%20NAME-%237289DA?style=for-the-badge&logo=discord)](https://discord.gg/ZFTCpAU53U)

Join our Discord server (Update Soon) for support, discussions, and updates related to Trackify.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

**Unauthorized use is strictly prohibited.**

📧 Email: cubedimension@protonmail.com

### Contributors and Developers

[<img src="https://avatars.githubusercontent.com/u/67865621?s=64&v=4" width="64" height="64" alt="haydenbanz">](https://github.com/haydenbanz)  
 
[<img src="https://avatars.githubusercontent.com/u/144106684?s=64&v=4" width="64" height="64" alt="Glitchesminds">](https://github.com/Glitchesminds)

## ☕ Support

If you find this project helpful, consider buying us a coffee with cookies:

[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-%23FFDD00?style=for-the-badge&logo=ko-fi&logoColor=white)](https://ko-fi.com/codeglitch)

## 🚫 Disclaimer

The creators of this project are not responsible for any misuse or illegal activities related to Trackify.





