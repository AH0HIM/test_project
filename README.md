# TEST PROJECT

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![My Telegram](https://img.shields.io/badge/%20%20My%20Telegram-2ba2d9.svg)](https://t.me/b3yond3r)

----
### Build
```bash
python setup.py bdist_wheel --universal
python setup.py sdist bdist_wheel --universal
```

### Install
```bash
pip install [-e] .
pip install dist/... --forse-reinstall
pip install -r requirements.txt
````
---

### Set additional argument
* ```-p no:cacheprovider --alluredir=/tmp/reports/allure-results```
* ```-p no:cacheprovider --html=/tmp/reports/htmls/report.html```
* ```-p no:cacheprovider --reruns 3   # pip install pytest-rerunfailures```


### Known issues
```bash
- Если возникло "ImportError: cannot import name 'MarkInfo'",  то удалить pytest-selenium
- Если нет модуля allure, то 'pip install allure-pytest'
- Если возникло "ModuleNotFoundError: No module named 'webdriver_manager'", то 'pip install webdriver-manager' 
- Если "TypeError: __init__() missing 3 required positional arguments: 'excinfo', 'start', and 'stop'", то обновить flaky в pip до последней версии
```

### To run tests
* clone the project ```git clone```
* open the project in PyCharm
* [configure PyCharm to use pytest as default test runner](https://stackoverflow.com/a/6397315/1562282)
* click on green triangle near test that you want to run

### HTML Report
![Alt text](doc/html.png?raw=true "HTML Report")

### [Allure Report](http://biercoff.com/opening-local-version-of-allure-report-with-chrome/)
![Alt text](doc/allure.png?raw=true "Allure Report")

### Re-run failed tests
![Alt text](doc/re-run.png?raw=true "Re-run Failed")
