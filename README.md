# Welcome to Cloud Trade

Cloud Trade is a web-based application that provides real-time stock tracking capabilities for traders and investors. The application enables users to monitor stock prices, track market trends, and analyze market data in real time.

# Features
* Real-time updates on stock prices for monitoring and decision-making.
* Secure user accounts for personalized access.
* Access to historical stock data for research and analysis.
* Compatibility with mobile devices for convenient access.

# Technologies Used
- ### Languages:
  - <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue">
  - <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white">
  - <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white">
  - <img src="https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E">
- ### FrameWork:
  - <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green">
  - <img src="https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white">
- ### ML/DL:
  - <img src="https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white">
  - <img src="https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white">
- ### Database:
  - <img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white">
- ### API used for:
  - <a href="https://pypi.org/project/yfinance/">Yahoo Finance</a>
- ### IDE:
  - <img src="https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white">
  - <img src="https://img.shields.io/badge/PyCharm-000000.svg?&style=for-the-badge&logo=PyCharm&logoColor=white">
- ### OS used for testing:
  - <img src="https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white">
  - <img src="https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=apple&logoColor=white">
  - <img src="https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white">
# Prerequisites
```bash
appdirs==1.4.4
asgiref==3.6.0
beautifulsoup4==4.12.2
certifi==2022.12.7
cffi==1.15.1
charset-normalizer==3.1.0
contourpy==1.0.7
cryptography==40.0.1
cycler==0.11.0
Django==4.2
fonttools==4.39.3
frozendict==2.3.7
html5lib==1.1
idna==3.4
joblib==1.2.0
kiwisolver==1.4.4
lxml==4.9.2
matplotlib==3.7.1
multitasking==0.0.11
numpy==1.24.2
packaging==23.0
panda==0.3.1
pandas==2.0.0
Pillow==9.5.0
plotly==5.14.1
pycparser==2.21
pyparsing==3.0.9
python-dateutil==2.8.2
pytz==2023.3
requests==2.28.2
scikit-learn==1.2.2
scipy==1.10.1
six==1.16.0
soupsieve==2.4
sqlparse==0.4.3
tenacity==8.2.2
threadpoolctl==3.1.0
tzdata==2023.3
urllib3==1.26.15
webencodings==0.5.1
yfinance==0.2.17
```

# Project Installation:
**STEP 1:** Clone the repository from GitHub.<br>
```bash 
git clone https://github.com/VatsalShah5/CloudTrade.git
```
**STEP 2:** Change the directory to the repository.<br>
```bash
  cd Cloudtrade
```
**STEP 3:** Create a virtual environment.<br>
```bash
  python -m venv virtualenv
```
**STEP 4:** Activate the virtual environment.<br>
```bash
  virtualenv\Scripts\activate
```
**STEP 5:** Install the dependencies.<br>
```bash
  pip install -r requirements.txt
```
**STEP 6:** Migrate the Django project.<br>
```bash
  python manage.py migrate
```
**STEP 7:** Run the application.<br>
```bash
  python manage.py runserver
```
# Walkthrough Video:
https://github.com/VatsalShah5/CloudTrade/assets/50176907/88947310-7840-4bc0-aa2d-277c564d56e9
# Output Screen-shots:
## SignUP Page:
![singup_page](https://github.com/VatsalShah5/CloudTrade/assets/50176907/87cc4cb1-c0f8-4f5f-a976-b4b2488da644)
## Login/SignIn Page:
![signin_page](https://github.com/VatsalShah5/CloudTrade/assets/50176907/81ea5a92-a2ca-41d4-bcfe-0dc12c2a73b6)
## Home Page:
**The Home page of the application displays real-time data on stock prices.**
![home_page](https://github.com/VatsalShah5/CloudTrade/assets/50176907/a17b0bc3-7a3b-4f5f-a5a6-5a9daad2105b)
## Stock Prediction Page:
**To Predict stock price we move on to the prediction page where we need to enter a valid ticker value and a number of days and click predict button.**
![stock_predict_page1](https://github.com/VatsalShah5/CloudTrade/assets/50176907/7a51f506-89c8-45c9-81b2-f82a215f84da)
<br>
**This page displays the predicted stock price along with searched ticker details.**
![image](https://github.com/VatsalShah5/CloudTrade/assets/50176907/5bb4644f-6c79-42ae-a678-d9b442ceba92)
## Stock List Page:
**The Ticker Info page displays the details of all the valid tickers accepted by the application.**
![image](https://github.com/VatsalShah5/CloudTrade/assets/50176907/381089a6-ec8d-41c8-ad64-db1ae661d51a)
## About Us Page:
![image](https://github.com/VatsalShah5/CloudTrade/assets/50176907/772d54a1-45e6-479f-9557-84ba294373fa)
## Contact Us Page:
![image](https://github.com/VatsalShah5/CloudTrade/assets/50176907/b8ca9510-7ba6-4587-88f9-b2ac8aad7052)
# Contributions and License.
This project is open to contributions. Feel free to fork the repository, make improvements, and submit pull requests. If you use this project as a reference or base for your own work, kindly give credit to the original creator.
# Contact Information
For any inquiries or collaborations related to the project, you can reach out to me through my social media profile:<br>
<br>
<a href="https://www.instagram.com/real.khopdi/">
<img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white"></a><br>
<br>
<a href="https://twitter.com/realKhopDi">
<img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white"></a><br>
<br>
<a href="https://www.facebook.com/VatsalShah55">
<img src="https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white"><br>
<br>
<a href="https://www.linkedin.com/in/vatsal-shah-297332175/">
<img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"><br>
<br>
