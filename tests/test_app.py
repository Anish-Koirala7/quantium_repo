# test_app.py

from dash_app import app
from dash import html


def test_header_present():
    headers = [
        child for child in app.layout.children
        if isinstance(child, html.H1)
    ]
    assert len(headers) == 1
    assert headers[0].children == "Sales Dashboard"


def test_layout_exists():
    assert app.layout is not None


def test_region_picker_present():
    component_ids = [child.id for child in app.layout.children]
    assert "region-dropdown" in component_ids


def test_visualisation_present():
    component_ids = [child.id for child in app.layout.children]
    assert "sales-graph" in component_ids