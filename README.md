# grey0906

개발 환경
Mac Apple M2 Sonoma 14.5
python 3.12.2
npm 10.7.0
appium 2.5.4
Java 22.0.1
Android Studio 2023.2.1 Patch 1
Google Chrome 128.0.6613.120

python 사용 모듈
pip install selenium==4.24.0
pip install Appium-Python-Client==4.1.0
pip install PyQt6==6.7.1
git submodule init
git submodule update
git submodule foreach git checkout dev

appium 실행시 필요 옵션
appium --allow-insecure adb_shell

사용한 테스트 기기
Android Virtual Device
Pixel 3a 5.6 1080x2220 440dpi
Android 14.0 arm64-v8a