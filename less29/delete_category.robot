*** Settings ***
Documentation     A test suite with a single test for delete category.
...
...               This test has a workflow that is created using keywords in
...               the imported resource file.
Resource          resource.robot
Suite Setup     Run Keywords
...             Open Browser To Login Page  AND
...             Login to System   AND
...             Catalog page Should Be Open

Suite Teardown  Close All Browsers

*** Test Cases ***
Delete Category
    [Tags]    Smoke-Admin
#    Open Navigation Catalog
#    Sleep  5s
    Delete Computer Category
    Element Should Be Visible  xpath=//div[@class='alert alert-danger']

    Sleep  5s
    #Pass Execution  Pass

