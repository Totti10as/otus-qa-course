*** Settings ***
Documentation     A test suite with a single test for valid login.
...
...               This test has a workflow that is created using keywords in
...               the imported resource file.
Resource          resource.robot

#Suite Setup     Open Browser To Login Page
Suite Teardown  Close All Browsers



*** Test Cases ***
Valid Login
    [Documentation]
    [Tags]  Smoke-Admin
   Open Browser To Login Page
   Input Username  ${USER LOGIN}
   Input Password  ${USER PASSWORD}
   Submit Credentials
   Admin Page Should Be Open


