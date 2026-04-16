import pytest
from app import app


# Test 1: The header is present
def test_header_present():
    # Check that the app layout contains an H1 header
    layout = app.layout
    layout_str = str(layout)

    # Verify header exists with expected text
    assert "H1" in layout_str
    assert "Pink Morsel" in layout_str or "Visualizer" in layout_str
    print("✓ Header test passed")


# Test 2: The visualisation is present
def test_visualization_present():
    # Check that the app layout contains a Graph component
    layout_str = str(app.layout)

    # Verify Graph component exists
    assert "Graph" in layout_str
    assert "dcc.Graph" in layout_str or "Graph" in layout_str
    print("✓ Visualization test passed")


# Test 3: The region picker is present
def test_region_picker_present():
    # Check that the app layout contains RadioItems
    layout_str = str(app.layout)

    # Verify RadioItems exists
    assert "RadioItems" in layout_str

    # Verify all five region options are present
    assert "north" in layout_str.lower()
    assert "south" in layout_str.lower()
    assert "east" in layout_str.lower()
    assert "west" in layout_str.lower()
    assert "all" in layout_str.lower()
    print("✓ Region picker test passed")