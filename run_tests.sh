#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}========================================${NC}"
echo -e "${YELLOW}  Running Pink Morsel Test Suite${NC}"
echo -e "${YELLOW}========================================${NC}"

# Step 1: Activate the virtual environment
echo -e "\n${YELLOW}[1/3] Activating virtual environment...${NC}"

# Check if .venv exists (Windows/PyCharm default)
if [ -d ".venv" ]; then
    source .venv/Scripts/activate 2>/dev/null || source .venv/bin/activate 2>/dev/null
    if [ $? -eq 0 ]; then
        echo -e "${GREEN} Virtual environment activated${NC}"
    else
        echo -e "${RED} Failed to activate virtual environment${NC}"
        exit 1
    fi
else
    echo -e "${RED}✗ Virtual environment not found. Please create one first.${NC}"
    exit 1
fi

# Step 2: Execute the test suite
echo -e "\n${YELLOW}[2/3] Running test suite...${NC}"

# Run pytest with verbose output
python -m pytest test_app.py -v

# Capture the exit code
TEST_EXIT_CODE=$?

# Step 3: Report results
echo -e "\n${YELLOW}[3/3] Test Results:${NC}"

if [ $TEST_EXIT_CODE -eq 0 ]; then
    echo -e "${GREEN}✓ All tests passed!${NC}"
    echo -e "${GREEN}========================================${NC}"
    echo -e "${GREEN}  TEST SUITE PASSED${NC}"
    echo -e "${GREEN}========================================${NC}"
    exit 0
else
    echo -e "${RED}✗ Some tests failed!${NC}"
    echo -e "${RED}========================================${NC}"
    echo -e "${RED}  TEST SUITE FAILED${NC}"
    echo -e "${RED}========================================${NC}"
    exit 1
fi