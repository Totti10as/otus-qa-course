*** Settings ***
Documentation     A resource file with reusable keywords and variables.
...
...               The system specific keywords created here form our own
...               domain specific language. They utilize keywords provided
...               by the imported SeleniumLibrary.
Library           SeleniumLibrary
Library           SeleniumScreenshots
Library           String

*** Variables ***
${SERVER}     demo23.opencart.pro
${LOGIN URL}  http://${SERVER}/admin/
${CATEGORY URL}  http://${SERVER}/admin/index.php?route=catalog/category&token=
${BROWSER}    Chrome
${USER LOGIN}  demo
${USER PASSWORD}  demo

*** Keywords ***
Open Browser To Login Page
   Open Browser  ${LOGIN URL}  ${BROWSER}
   Set Window Size  1200   800
   Login Page Should Be Open

Login Page Should Be Open
    Title Should Be    Авторизация

Input Username
    [Arguments]  ${userlogin}
    Input Text    id:input-username  ${userlogin}

Input Password
    [Arguments]  ${userpassword}
    Input Text    id:input-password   ${userpassword}

Submit Credentials
    Click Button    xpath=//button[@class='btn btn-primary']

Admin Page Should Be Open
    Location Should Contain    index.php?route=common/dashboard&token=
    Title Should Be    Панель состояния

Login to System
    Input Username        ${USER LOGIN}
    Input Password        ${USER PASSWORD}
    Submit Credentials
    Admin Page Should Be Open


Open Navigation Catalog Page
    Mouse Over     id=menu-catalog
    Click Element  xpath=//li[@id='menu-catalog']/ul/li[1]

Catalog page Should Be Open
    ${url} =      Get Location
    ${tokenID} =  Fetch From Right   ${url}   token=
    Go To  ${CATEGORY URL}${tokenID}
    Sleep  5s

Delete Computer Category
    Select Checkbox  css=tbody tr:nth-of-type(1) [type]
    Click Element    xpath=//button[@class='btn btn-danger']
    Switch Browser   1
    Handle Alert    Accept


