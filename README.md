# grey0906

# 개발 환경

Mac Apple M2 Sonoma 14.5

python 3.12.2

npm 10.7.0

appium 2.5.4

Java 22.0.1

Android Studio 2023.2.1 Patch 1

Google Chrome 128.0.6613.120

# python 사용 모듈

pip install selenium==4.24.0

pip install Appium-Python-Client==4.1.0

pip install PyQt6==6.7.1

# chrome driver 자동 설치를 위한 모듈

pip install requests==2.31.0

pip install chromedriver-autoinstaller==0.6.4

pip install pyzipper==0.3.6

# 사용하지 않지만 서브 모듈에서 사용 중이라 설치 필요한 모듈

pip install numpy==1.26.4

pip install PyAutoGUI==0.9.54

pip install opencv-python==4.5.5.62

# 서브 모듈 업데이트

git submodule init

git submodule update

git submodule foreach git checkout dev

# appium 실행시 adb를 사용하기 위한 옵션

appium --allow-insecure adb_shell

# 사용한 테스트 기기

Android Virtual Device

Pixel 3a 5.6 1080x2220 440dpi

Android 14.0 arm64-v8a
