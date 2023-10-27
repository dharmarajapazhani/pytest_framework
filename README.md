# DemoPytest package
sample exercise of pytest concepts

pytest documentation:

https://docs.pytest.org/en/7.1.x/contents.html

pytest rule:
*************

python file should begin with test_*.py or end with *_test.py in pytest framework and 
the test case validation performed inside the function definition such function name should begin with "test" followed by testcase name in pytest framework. 

-----------------------------------------------------------------------------------------------

pytest concept & Test execution command:
****************************************

git clone this repo (https://github.com/dharmaece/pytest-exercise.git).
go to the cloned codebase path 



Run the command for addition operation related 2 testcases(2 num add, 3 num add) with pytest fixture function(addition_setup) usage related file run

C:\Users\user\PycharmProjects\pytest-exercise>python -m pytest -v -s -k "test_addition.py"

----------------------------------------------------------------------------------------------


Run the command for string operation related 1 testcases(welcome string) with pytest fixture function(welcome_setup) usage related file run

C:\Users\user\PycharmProjects\pytest_framework\DemoPytest>pytest -v -s -k "test_helloworld.py"

----------------------------------------------------------------------------------------------
Run the command for with marker decorator & without marker decorator in the same test file:


C:\Users\user\PycharmProjects\pytest_framework\DemoPytest>pytest -v -s -k "test_groupingmarkers.py"


Run the command for marker decorator:


C:\Users\user\PycharmProjects\pytest_framework\DemoPytest>pytest -v -s -k "test_groupingmarkers.py" -m regression

C:\Users\user\PycharmProjects\pytest_framework\DemoPytest>pytest -v -s -k "test_groupingmarkers.py" -m sanity


C:\Users\user\PycharmProjects\pytest_framework\DemoPytest>pytest -v -s -k "test_groupingmarkers.py" -m skip


C:\Users\user\PycharmProjects\pytest_framework\DemoPytest>pytest -v -s -k "test_groupingmarkers.py" -m xfail



----------------------------------------------------------------------------------------------

Run the command for pytest fixture feature:


C:\Users\user\PycharmProjects\pytest_framework\DemoPytest>pytest -v -s -k "test_decodraterfixture.py"


-----------------------------------------------------------------------------------------------

Run the command for pytest fixture parametrization feature:

C:\Users\user\PycharmProjects\pytest_framework\DemoPytest>pytest -v -s test_fixtureparam_addition.py


-----------------------------------------------------------------------------------------------

Run command for adding command line argument(in this example, --calculationtype is a command line argument) feature:

C:\Users\user\PycharmProjects\pytest_framework\DemoPytest>pytest -v -s --calculationtype addition  --> its valid case.

C:\Users\user\PycharmProjects\pytest_framework\DemoPytest>pytest -v -s --calculationtype substraction  --> its invalid case.

Run command for adding command line argument feature(in this example, CLA specified under addopts tag in pytest.ini file):

C:\Users\user\PycharmProjects\pytest_framework\DemoPytest>pytest -v -s


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Run command for parametrize decorator feature demonstration:

C:\Users\user\PycharmProjects\pytest_framework\DemoPytest>pytest -v -s -k test_parametrizedecorator.py


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Test report generation command via command line argument: ( html report)

C:\Users\user\PycharmProjects\pytest_framework\DemoPytest>pytest -v -s --html=testreport.html

After test execution, you could see print like as below mentioned. goto the path and right click the report.html file to view it through chrome browser.

-------- Generated html report: file:///C:/Users/user/PycharmProjects/pytest-exercise/SamplePyTest/report.html --------


Test report generation command suppose it's specified in ini file: ( html report)


C:\Users\user\PycharmProjects\pytest_framework\DemoPytest>pytest -v -s

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Run command for generating allure test report:

C:\Users\user\PycharmProjects\pytest_framework\DemoPytest>pytest -v -s --alluredir=AllureReport

C:\Users\user\PycharmProjects\pytest_framework\DemoPytest>allure serve AllureReport


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


GENERAL NOTE (SETUP):
**************************

I have tried these experiment on windows 10 OS based PC.
1. Install the PyCharm 2023.2.3 (Community Edition) package.
2. Install the python3.12 package.
3. Install the pip python package.
4. Install the ini plugin using PyCharm utility.
5. Install git version control system for windows PC using PyCharm utility.
----------------------------------------------------------------------------------------------

EXE file required for Windows PC:
*********************************

pycharm-community-2023.2.3.exe

python-3.12.0-amd64.exe

----------------------------------------------------------------------------------------------


pip python package installation procedure on windows PC:
********************************************************

C:\Users\user\PycharmProjects\pytest-exercise>curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
C:\Users\user\PycharmProjects\pytest-exercise>python -m get-pip

Successfully installed pip-23.3.1

-----------------------------------------------------------------------------------------------

Ensure the below specified package version is installed or not.
***************************************************************

C:\Users\user\PycharmProjects\pytest-exercise>python --version

Python 3.12.0

------------------------------------------------------------------------
C:\Users\user\PycharmProjects\pytest-exercise>python -m pytest --version

pytest 7.4.2

------------------------------------------------------------------------
C:\Users\user\PycharmProjects\pytest-exercise>pip3 list

Package    Version

colorama   0.4.6

iniconfig  2.0.0

packaging  23.2

pip        23.3.1

pluggy     1.3.0

pytest     7.4.2

setuptools 68.2.2

wheel      0.41.2

---------------------------------------------------------------------------

python module required to generate html report:
***********************************************

https://pypi.org/project/pytest-html/

C:\Users\user\PycharmProjects\pytest_framework\DemoPytest>pip install pytest-html

python module required to generate Allure report:
**************************************************

https://pypi.org/project/allure-pytest/

C:\Users\user\PycharmProjects\pytest_framework\DemoPytest>pip install allure-pytest

Installing the scoope (A command-line installer for Windows):
***************************************************************

Open the powershell terminal on windows PC and run the below command:

i.

PS C:\Users\user> Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

Execution Policy Change
The execution policy helps protect you from scripts that you do not trust. Changing the execution policy might expose
you to the security risks described in the about_Execution_Policies help topic at
https:/go.microsoft.com/fwlink/?LinkID=135170. Do you want to change the execution policy?
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "N"): A

ii.

PS C:\Users\user> irm get.scoop.sh | iex


iii.

PS C:\Users\user> scoop install allure

iv. install the java 8 for windows OS.

https://www.java.com/download/ie_manual.jsp ---> JavaSetup8u391.exe

v. setting environmental variable for windows.
https://confluence.atlassian.com/doc/setting-the-java_home-variable-in-windows-8895.html

vi. download allure command line tool and setup PATH variable on Windows PC (C:\Program Files (x86)\allure-2.24.1\bin)
https://github.com/allure-framework/allure2/releases



reference link:

https://allurereport.org/docs/

https://allurereport.org/docs/gettingstarted/installation/

https://scoop.sh/

https://www.youtube.com/watch?v=xdjN-4UxL1c

https://medium.com/testvagrant/generating-allure-reports-in-the-pytest-framework-89dc78a2ca85

