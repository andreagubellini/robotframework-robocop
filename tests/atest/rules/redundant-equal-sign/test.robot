*** Settings ***
Documentation  doc


*** Variables ***
${SUITE_VARIABLE}=  Value
${ANOTHER_VARIABLE} =  Value
${VAR_WITHOUT_EQUAL_SIGN}  Value


*** Test Cases ***
Test
    [Documentation]  doc
    [Tags]  sometag
    Pass
    ${var}=  Keyword
    One More


*** Keywords ***
Keyword
    [Documentation]  this is doc
    No Operation
    Pass
    ${smth} =  No Operation
    Fail
