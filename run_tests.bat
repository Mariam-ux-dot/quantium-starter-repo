@echo off
REM run_tests.bat - CI script for Windows

echo ========================================
echo   Running Pink Morsel Test Suite
echo ========================================

REM Step 1: Activate virtual environment
echo.
echo [1/3] Activating virtual environment...

IF EXIST ".venv\Scripts\activate.bat (
    call .venv\Scripts\activate.bat
    echo [OK] Virtual environment activated
) ELSE (
    echo [ERROR] Virtual environment not found
    exit /b 1
)

REM Step 2: Run tests
echo.
echo [2/3] Running test suite...

python -m pytest test_app.py -v

REM Capture exit code
set TEST_EXIT_CODE=%ERRORLEVEL%

REM Step 3: Report results
echo.
echo [3/3] Test Results:

IF %TEST_EXIT_CODE% EQU 0 (
    echo [OK] All tests passed!
    echo ========================================
    echo   [SUCCESS] TEST SUITE PASSED
    echo ========================================
    exit /b 0
) ELSE (
    echo [ERROR] Some tests failed!
    echo ========================================
    echo   [FAILURE] TEST SUITE FAILED
    echo ========================================
    exit /b 1
)