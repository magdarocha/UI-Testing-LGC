# UI-Testing-LGC
Challenge 1

## Setup

To setup all __python__ libs call:
```cmd
pip install -r requirements.txt
```

To install __Allure__ you can follow the [link](https://allurereport.org/docs/install-for-linux/).
In my case, I used a Windows machine, so I need to get __Allure__ bin and call it.
To do so, I download __Alure__ from the [link](https://github.com/allure-framework/allure2/releases/tag/2.30.0) and call the _bin_ ```allure-2.30.0\allure-2.30.0\bin\allure```.

## Run tests

To run the tests call:
```cmd
pytest test_UI_testing.py
```

## To run report

To create a report using __allure__:
```cmd
pytest test_UI_testing.py --alluredir results_test
```
To create the html for reports:
```cmd
allure generate results_test -o results_html --clean
```

After run this steps, go to the __results_html__ folder, and with the right button in __index.html__ click in ```open with live server```.


