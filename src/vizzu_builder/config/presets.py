# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring

from __future__ import annotations

import streamlit_vizzu  # type: ignore


class ChartPreset:
    # pylint: disable=too-few-public-methods

    def __init__(
        self, data: streamlit_vizzu.Data, presets: list, index: int, label: str | None
    ) -> None:
        self.index: int = index
        self.data: dict = data
        preset = presets[index]
        config = preset["config"]
        config["label"] = label
        self.config: dict = config
        self.style: dict = preset["style"]
        self.chart: str = preset["chart"]


class Presets:
    # pylint: disable=too-few-public-methods

    @staticmethod
    def get(
        key: str | None,
        cat1: str | None,
        cat2: str | None,
        value1: str | None,
        value2: str | None,
    ) -> list:
        style = {
            "plot": {
                "yAxis": {"label": {"numberScale": "shortScaleSymbolUS"}},
                "xAxis": {"label": {"numberScale": "shortScaleSymbolUS"}},
                "marker": {
                    "label": {
                        "numberFormat": "prefixed",
                        "maxFractionDigits": "1",
                        "numberScale": "shortScaleSymbolUS",
                    },
                    "rectangleSpacing": None,
                },
            },
        }
        presets = {
            "Cat1, Value1": [
                {
                    "config": {
                        "coordSystem": "cartesian",
                        "geometry": "rectangle",
                        "x": cat1,
                        "y": {"set": value1, "range": {"min": None, "max": "110%"}},
                        "color": None,
                        "lightness": None,
                        "size": None,
                        "noop": None,
                        "split": False,
                        "align": "none",
                        "orientation": "horizontal",
                    },
                    "style": style,
                    "chart": "Column Chart",
                },
                {
                    "config": {
                        "coordSystem": "cartesian",
                        "geometry": "rectangle",
                        "x": value1,
                        "y": {"set": cat1, "range": {"min": None, "max": None}},
                        "color": None,
                        "lightness": None,
                        "size": None,
                        "noop": None,
                        "split": False,
                        "align": "none",
                        "orientation": "vertical",
                    },
                    "style": style,
                    "chart": "Bar Chart",
                },
                {
                    "config": {
                        "coordSystem": "cartesian",
                        "geometry": "area",
                        "x": cat1,
                        "y": {"set": value1, "range": {"min": None, "max": "110%"}},
                        "color": None,
                        "lightness": None,
                        "size": None,
                        "noop": None,
                        "split": False,
                        "align": "none",
                        "orientation": "horizontal",
                    },
                    "style": style,
                    "chart": "Area Chart",
                },
                {
                    "config": {
                        "coordSystem": "cartesian",
                        "geometry": "line",
                        "x": cat1,
                        "y": {"set": value1, "range": {"min": None, "max": "110%"}},
                        "color": None,
                        "lightness": None,
                        "size": None,
                        "noop": None,
                        "split": False,
                        "align": "none",
                        "orientation": "horizontal",
                    },
                    "style": style,
                    "chart": "Line Chart",
                },
                {
                    "config": {
                        "coordSystem": "cartesian",
                        "geometry": "circle",
                        "x": cat1,
                        "y": {"set": value1, "range": {"min": None, "max": "110%"}},
                        "color": None,
                        "lightness": None,
                        "size": None,
                        "noop": None,
                        "split": False,
                        "align": "none",
                        "orientation": "horizontal",
                    },
                    "style": style,
                    "chart": "Lollipop",
                },
                {
                    "config": {
                        "coordSystem": "polar",
                        "geometry": "rectangle",
                        "x": cat1,
                        "y": {"set": value1, "range": {"min": None, "max": None}},
                        "color": None,
                        "lightness": None,
                        "size": None,
                        "noop": None,
                        "split": False,
                        "align": "none",
                        "orientation": "horizontal",
                    },
                    "style": style,
                    "chart": "Polar Column Chart",
                },
                {
                    "config": {
                        "coordSystem": "polar",
                        "geometry": "rectangle",
                        "x": value1,
                        "y": {"set": cat1, "range": {"min": "-50%", "max": None}},
                        "color": None,
                        "lightness": None,
                        "size": None,
                        "noop": None,
                        "split": False,
                        "align": "none",
                        "orientation": "vertical",
                    },
                    "style": style,
                    "chart": "Radial Bar Chart",
                },
                {
                    "config": {
                        "coordSystem": "polar",
                        "geometry": "area",
                        "x": cat1,
                        "y": {"set": value1, "range": {"min": None, "max": "130%"}},
                        "color": None,
                        "lightness": None,
                        "size": None,
                        "noop": None,
                        "split": False,
                        "align": "none",
                        "orientation": "horizontal",
                    },
                    "style": style,
                    "chart": "Polar Area Chart",
                },
                {
                    "config": {
                        "coordSystem": "polar",
                        "geometry": "line",
                        "x": cat1,
                        "y": {"set": value1, "range": {"min": None, "max": "130%"}},
                        "color": None,
                        "lightness": None,
                        "size": None,
                        "noop": None,
                        "split": False,
                        "align": "none",
                        "orientation": "horizontal",
                    },
                    "style": style,
                    "chart": "Polar Line Chart",
                },
                {
                    "config": {
                        "coordSystem": "polar",
                        "geometry": "rectangle",
                        "x": [cat1, value1],
                        "y": {"set": None, "range": {"min": None, "max": None}},
                        "color": cat1,
                        "lightness": None,
                        "size": None,
                        "noop": None,
                        "split": False,
                        "align": "none",
                        "orientation": "vertical",
                    },
                    "style": style,
                    "chart": "Pie Chart",
                },
                {
                    "config": {
                        "coordSystem": "polar",
                        "geometry": "rectangle",
                        "x": [cat1, value1],
                        "y": {"set": None, "range": {"min": "-200%", "max": "100%"}},
                        "color": cat1,
                        "lightness": None,
                        "size": None,
                        "noop": None,
                        "split": False,
                        "align": "none",
                        "orientation": "vertical",
                    },
                    "style": style,
                    "chart": "Donut Chart",
                },
                {
                    "config": {
                        "coordSystem": "cartesian",
                        "geometry": "rectangle",
                        "x": None,
                        "y": {"set": None, "range": {"min": None, "max": None}},
                        "color": cat1,
                        "lightness": None,
                        "size": [cat1, value1],
                        "noop": None,
                        "split": False,
                        "align": "none",
                        "orientation": "horizontal",
                    },
                    "style": style,
                    "chart": "Treemap",
                },
                {
                    "config": {
                        "coordSystem": "cartesian",
                        "geometry": "circle",
                        "x": None,
                        "y": {"set": None, "range": {"min": None, "max": None}},
                        "color": cat1,
                        "lightness": None,
                        "size": value1,
                        "noop": None,
                        "split": False,
                        "align": "none",
                        "orientation": "horizontal",
                    },
                    "style": style,
                    "chart": "Bubble Chart",
                },
                {
                    "config": {
                        "coordSystem": "cartesian",
                        "geometry": "rectangle",
                        "x": cat1,
                        "y": {
                            "set": [cat1, value1],
                            "range": {"min": None, "max": "110%"},
                        },
                        "color": None,
                        "lightness": None,
                        "size": None,
                        "noop": None,
                        "split": False,
                        "align": "none",
                        "orientation": "horizontal",
                    },
                    "style": style,
                    "chart": "Waterfall",
                },
                {
                    "config": {
                        "coordSystem": "cartesian",
                        "geometry": "rectangle",
                        "x": cat1,
                        "y": {
                            "set": [cat1, value1],
                            "range": {"min": None, "max": "110%"},
                        },
                        "color": value1,
                        "lightness": None,
                        "size": None,
                        "noop": None,
                        "split": False,
                        "align": "none",
                        "orientation": "horizontal",
                    },
                    "style": style,
                    "chart": "Waterfall V2",
                },
                {
                    "config": {
                        "coordSystem": "cartesian",
                        "geometry": "circle",
                        "x": cat1,
                        "y": {"set": cat1, "range": {"min": None, "max": "110%"}},
                        "color": value1,
                        "lightness": None,
                        "size": value1,
                        "noop": None,
                        "split": False,
                        "align": "none",
                        "orientation": "horizontal",
                    },
                    "style": style,
                    "chart": "Correlogram",
                },
            ],
            "Cat1, Value1, Value2": [
                {
                    "config": {
                        "coordSystem": "cartesian",
                        "geometry": "circle",
                        "x": value2,
                        "y": {"set": value1, "range": {"min": None, "max": "110%"}},
                        "color": None,
                        "lightness": None,
                        "size": None,
                        "noop": cat1,
                        "split": False,
                        "align": "none",
                        "orientation": "horizontal",
                    },
                    "style": style,
                    "chart": "Scatter Plot",
                },
                {
                    "config": {
                        "coordSystem": "cartesian",
                        "geometry": "circle",
                        "x": value2,
                        "y": {"set": value1, "range": {"min": None, "max": "110%"}},
                        "color": None,
                        "lightness": None,
                        "size": value1,
                        "noop": cat1,
                        "split": False,
                        "align": "none",
                        "orientation": "horizontal",
                    },
                    "style": style,
                    "chart": "Bubble Plot",
                },
                {
                    "config": {
                        "coordSystem": "cartesian",
                        "geometry": "circle",
                        "x": value2,
                        "y": {"set": value1, "range": {"min": None, "max": "110%"}},
                        "color": None,
                        "lightness": None,
                        "size": value2,
                        "noop": cat1,
                        "split": False,
                        "align": "none",
                        "orientation": "horizontal",
                    },
                    "style": style,
                    "chart": "Bubble Plot V2",
                },
                {
                    "config": {
                        "coordSystem": "polar",
                        "geometry": "circle",
                        "x": value2,
                        "y": {"set": value1, "range": {"min": None, "max": "110%"}},
                        "color": None,
                        "lightness": None,
                        "size": None,
                        "noop": cat1,
                        "split": False,
                        "align": "none",
                        "orientation": "horizontal",
                    },
                    "style": style,
                    "chart": "Polar Scatter",
                },
                {
                    "config": {
                        "coordSystem": "polar",
                        "geometry": "rectangle",
                        "x": [cat1, value2],
                        "y": {"set": value1, "range": {"min": None, "max": None}},
                        "color": cat1,
                        "lightness": None,
                        "size": None,
                        "noop": None,
                        "split": False,
                        "align": "none",
                        "orientation": "horizontal",
                    },
                    "style": style,
                    "chart": "Variable Radius Pie Chart",
                },
                {
                    "config": {
                        "coordSystem": "cartesian",
                        "geometry": "rectangle",
                        "x": [cat1, value2],
                        "y": {"set": value1, "range": {"min": None, "max": None}},
                        "color": cat1,
                        "lightness": None,
                        "size": None,
                        "noop": None,
                        "split": False,
                        "align": "none",
                        "orientation": "horizontal",
                    },
                    "style": style,
                    "chart": "Mekko",
                },
            ],
            "Cat1, Cat2, Value1": [
                {
                    "config": {
                        "coordSystem": "cartesian",
                        "geometry": "rectangle",
                        "x": [cat1, cat2],
                        "y": {"set": value1, "range": {"min": None, "max": "110%"}},
                        "color": cat2,
                        "lightness": None,
                        "size": None,
                        "noop": None,
                        "split": False,
                        "align": "none",
                        "orientation": "horizontal",
                    },
                    "style": style,
                    "chart": "Grouped Column Chart",
                },
                {
                    "config": {
                        "coordSystem": "cartesian",
                        "geometry": "rectangle",
                        "x": [cat2, cat1],
                        "y": {"set": value1, "range": {"min": None, "max": "110%"}},
                        "color": cat2,
                        "lightness": None,
                        "size": None,
                        "noop": None,
                        "split": False,
                        "align": "none",
                        "orientation": "horizontal",
                    },
                    "style": style,
                    "chart": "Grouped Column Chart V2",
                },
                {
                    "config": {
                        "coordSystem": "cartesian",
                        "geometry": "rectangle",
                        "x": cat1,
                        "y": {
                            "set": [cat2, value1],
                            "range": {"min": None, "max": "110%"},
                        },
                        "color": cat2,
                        "lightness": None,
                        "size": None,
                        "noop": None,
                        "split": False,
                        "align": "none",
                        "orientation": "horizontal",
                    },
                    "style": style,
                    "chart": "Stacked Column Chart",
                },
                {
                    "config": {
                        "coordSystem": "cartesian",
                        "geometry": "rectangle",
                        "x": cat1,
                        "y": {
                            "set": [cat2, value1],
                            "range": {"min": None, "max": "110%"},
                        },
                        "color": cat2,
                        "lightness": None,
                        "size": None,
                        "noop": None,
                        "split": True,
                        "align": "none",
                        "orientation": "horizontal",
                    },
                    "style": style,
                    "chart": "Splitted Column Chart",
                },
                {
                    "config": {
                        "coordSystem": "cartesian",
                        "geometry": "rectangle",
                        "x": cat1,
                        "y": {
                            "set": [cat2, value1],
                            "range": {"min": None, "max": None},
                        },
                        "color": cat2,
                        "lightness": None,
                        "size": None,
                        "noop": None,
                        "split": False,
                        "align": "stretch",
                        "orientation": "horizontal",
                    },
                    "style": style,
                    "chart": "100% Stacked Column Chart",
                },
                {
                    "config": {
                        "coordSystem": "cartesian",
                        "geometry": "rectangle",
                        "x": value1,
                        "y": {"set": [cat1, cat2], "range": {"min": None, "max": None}},
                        "color": cat2,
                        "lightness": None,
                        "size": None,
                        "noop": None,
                        "split": False,
                        "align": "none",
                        "orientation": "vertical",
                    },
                    "style": style,
                    "chart": "Grouped Bar Chart",
                },
                {
                    "config": {
                        "coordSystem": "cartesian",
                        "geometry": "rectangle",
                        "x": value1,
                        "y": {"set": [cat2, cat1], "range": {"min": None, "max": None}},
                        "color": cat2,
                        "lightness": None,
                        "size": None,
                        "noop": None,
                        "split": False,
                        "align": "none",
                        "orientation": "vertical",
                    },
                    "style": style,
                    "chart": "Grouped Bar Chart V2",
                },
                {
                    "config": {
                        "coordSystem": "cartesian",
                        "geometry": "rectangle",
                        "x": [cat2, value1],
                        "y": {"set": cat1, "range": {"min": None, "max": None}},
                        "color": cat2,
                        "lightness": None,
                        "size": None,
                        "noop": None,
                        "split": False,
                        "align": "none",
                        "orientation": "vertical",
                    },
                    "style": style,
                    "chart": "Stacked Bar Chart",
                },
                {
                    "config": {
                        "coordSystem": "cartesian",
                        "geometry": "rectangle",
                        "x": [cat2, value1],
                        "y": {"set": cat1, "range": {"min": None, "max": None}},
                        "color": cat2,
                        "lightness": None,
                        "size": None,
                        "noop": None,
                        "split": True,
                        "align": "none",
                        "orientation": "vertical",
                    },
                    "style": style,
                    "chart": "Splitted Bar Chart",
                },
                {
                    "config": {
                        "coordSystem": "cartesian",
                        "geometry": "rectangle",
                        "x": [cat2, value1],
                        "y": {"set": cat1, "range": {"min": None, "max": None}},
                        "color": cat2,
                        "lightness": None,
                        "size": None,
                        "noop": None,
                        "split": False,
                        "align": "stretch",
                        "orientation": "horizontal",
                    },
                    "style": style,
                    "chart": "100% Stacked Bar Chart",
                },
                {
                    "config": {
                        "coordSystem": "cartesian",
                        "geometry": "line",
                        "x": cat1,
                        "y": {"set": value1, "range": {"min": None, "max": "110%"}},
                        "color": cat2,
                        "lightness": None,
                        "size": None,
                        "noop": None,
                        "split": False,
                        "align": "none",
                        "orientation": "horizontal",
                    },
                    "style": style,
                    "chart": "Line Chart",
                },
                {
                    "config": {
                        "coordSystem": "cartesian",
                        "geometry": "area",
                        "x": cat1,
                        "y": {
                            "set": [cat2, value1],
                            "range": {"min": None, "max": "110%"},
                        },
                        "color": cat2,
                        "lightness": None,
                        "size": None,
                        "noop": None,
                        "split": False,
                        "align": "none",
                        "orientation": "horizontal",
                    },
                    "style": style,
                    "chart": "Stacked Area Chart",
                },
                {
                    "config": {
                        "coordSystem": "cartesian",
                        "geometry": "area",
                        "x": cat1,
                        "y": {
                            "set": [cat2, value1],
                            "range": {"min": None, "max": None},
                        },
                        "color": cat2,
                        "lightness": None,
                        "size": None,
                        "noop": None,
                        "split": False,
                        "align": "stretch",
                        "orientation": "horizontal",
                    },
                    "style": style,
                    "chart": "100% Stacked Area Chart",
                },
                {
                    "config": {
                        "coordSystem": "cartesian",
                        "geometry": "area",
                        "x": cat1,
                        "y": {
                            "set": [cat2, value1],
                            "range": {"min": None, "max": None},
                        },
                        "color": cat2,
                        "lightness": None,
                        "size": None,
                        "noop": None,
                        "split": True,
                        "align": "none",
                        "orientation": "horizontal",
                    },
                    "style": style,
                    "chart": "Ridgeline Plot",
                },
                {
                    "config": {
                        "coordSystem": "cartesian",
                        "geometry": "area",
                        "x": cat1,
                        "y": {
                            "set": [cat2, value1],
                            "range": {"min": None, "max": "110%"},
                        },
                        "color": cat2,
                        "lightness": None,
                        "size": None,
                        "noop": None,
                        "split": False,
                        "align": "center",
                        "orientation": "horizontal",
                    },
                    "style": style,
                    "chart": "Stream Graph",
                },
                {
                    "config": {
                        "coordSystem": "cartesian",
                        "geometry": "area",
                        "x": cat1,
                        "y": {
                            "set": [cat2, value1],
                            "range": {"min": None, "max": "110%"},
                        },
                        "color": cat2,
                        "lightness": None,
                        "size": None,
                        "noop": None,
                        "split": True,
                        "align": "center",
                        "orientation": "horizontal",
                    },
                    "style": style,
                    "chart": "Violin Graph",
                },
                {
                    "config": {
                        "coordSystem": "cartesian",
                        "geometry": "circle",
                        "x": None,
                        "y": {"set": None, "range": {"min": None, "max": None}},
                        "color": cat2,
                        "lightness": None,
                        "size": [cat1, value1],
                        "noop": None,
                        "split": False,
                        "align": "none",
                        "orientation": "horizontal",
                    },
                    "style": style,
                    "chart": "Stacked Bubble Chart",
                },
                {
                    "config": {
                        "coordSystem": "polar",
                        "geometry": "rectangle",
                        "x": cat1,
                        "y": {
                            "set": [cat2, value1],
                            "range": {"min": None, "max": None},
                        },
                        "color": cat2,
                        "lightness": None,
                        "size": None,
                        "noop": None,
                        "split": False,
                        "align": "none",
                        "orientation": "horizontal",
                    },
                    "style": style,
                    "chart": "Polar Stacked Column Chart",
                },
                {
                    "config": {
                        "coordSystem": "polar",
                        "geometry": "area",
                        "x": cat1,
                        "y": {
                            "set": [cat2, value1],
                            "range": {"min": None, "max": None},
                        },
                        "color": cat2,
                        "lightness": None,
                        "size": None,
                        "noop": None,
                        "split": False,
                        "align": "none",
                        "orientation": "horizontal",
                    },
                    "style": style,
                    "chart": "Polar Stacked Area Chart",
                },
                {
                    "config": {
                        "coordSystem": "polar",
                        "geometry": "rectangle",
                        "x": [cat2, value1],
                        "y": {"set": cat1, "range": {"min": "-50%", "max": None}},
                        "color": cat2,
                        "lightness": None,
                        "size": None,
                        "noop": None,
                        "split": False,
                        "align": "none",
                        "orientation": "vertical",
                    },
                    "style": style,
                    "chart": "Radial Stacked Bar Chart",
                },
                {
                    "config": {
                        "coordSystem": "polar",
                        "geometry": "rectangle",
                        "x": [cat2, value1],
                        "y": {"set": cat1, "range": {"min": "-50%", "max": None}},
                        "color": cat2,
                        "lightness": None,
                        "size": None,
                        "noop": None,
                        "split": False,
                        "align": "stretch",
                        "orientation": "vertical",
                    },
                    "style": style,
                    "chart": "Nested Donut Chart",
                },
                {
                    "config": {
                        "coordSystem": "cartesian",
                        "geometry": "rectangle",
                        "x": cat1,
                        "y": {"set": cat2, "range": {"min": None, "max": None}},
                        "color": None,
                        "lightness": value1,
                        "size": None,
                        "noop": None,
                        "split": False,
                        "align": "none",
                        "orientation": "horizontal",
                    },
                    "style": {
                        "plot": {
                            "yAxis": {"label": {"numberScale": "shortScaleSymbolUS"}},
                            "xAxis": {"label": {"numberScale": "shortScaleSymbolUS"}},
                            "marker": {
                                "label": {
                                    "numberFormat": "prefixed",
                                    "maxFractionDigits": "1",
                                    "numberScale": "shortScaleSymbolUS",
                                },
                                "rectangleSpacing": 0,
                            },
                        },
                    },
                    "chart": "Heat Map",
                },
                {
                    "config": {
                        "coordSystem": "cartesian",
                        "geometry": "rectangle",
                        "x": cat1,
                        "y": {"set": cat2, "range": {"min": None, "max": None}},
                        "color": value1,
                        "lightness": None,
                        "size": None,
                        "noop": None,
                        "split": False,
                        "align": "none",
                        "orientation": "horizontal",
                    },
                    "style": style,
                    "chart": "Heat Map Gradient",
                },
            ],
            "Cat1, Cat2, Value1, Value2": [
                {
                    "config": {
                        "coordSystem": "cartesian",
                        "geometry": "circle",
                        "x": value2,
                        "y": {"set": value1, "range": {"min": None, "max": "110%"}},
                        "color": cat2,
                        "lightness": None,
                        "size": None,
                        "noop": cat1,
                        "split": False,
                        "align": "none",
                        "orientation": "horizontal",
                    },
                    "style": style,
                    "chart": "Scatter Plot",
                },
                {
                    "config": {
                        "coordSystem": "cartesian",
                        "geometry": "circle",
                        "x": value2,
                        "y": {"set": value1, "range": {"min": None, "max": "110%"}},
                        "color": cat2,
                        "lightness": None,
                        "size": value1,
                        "noop": cat1,
                        "split": False,
                        "align": "none",
                        "orientation": "horizontal",
                    },
                    "style": style,
                    "chart": "Bubble Plot",
                },
                {
                    "config": {
                        "coordSystem": "cartesian",
                        "geometry": "circle",
                        "x": value2,
                        "y": {"set": value1, "range": {"min": None, "max": "110%"}},
                        "color": cat2,
                        "lightness": None,
                        "size": value2,
                        "noop": cat1,
                        "split": False,
                        "align": "none",
                        "orientation": "horizontal",
                    },
                    "style": style,
                    "chart": "Bubble Plot V2",
                },
                {
                    "config": {
                        "coordSystem": "cartesian",
                        "geometry": "rectangle",
                        "x": None,
                        "y": {"set": None, "range": {"min": None, "max": None}},
                        "color": cat2,
                        "lightness": value2,
                        "size": [cat1, value1],
                        "noop": None,
                        "split": False,
                        "align": "none",
                        "orientation": "horizontal",
                    },
                    "style": style,
                    "chart": "Stacked Treemap",
                },
                {
                    "config": {
                        "coordSystem": "cartesian",
                        "geometry": "rectangle",
                        "x": [cat2, value2],
                        "y": {
                            "set": [cat1, value1],
                            "range": {"min": None, "max": None},
                        },
                        "color": cat2,
                        "lightness": None,
                        "size": None,
                        "noop": None,
                        "split": False,
                        "align": "none",
                        "orientation": "horizontal",
                    },
                    "style": style,
                    "chart": "Stacked Mekko Chart",
                },
                {
                    "config": {
                        "coordSystem": "cartesian",
                        "geometry": "rectangle",
                        "x": [cat2, value2],
                        "y": {
                            "set": [cat1, value1],
                            "range": {"min": None, "max": None},
                        },
                        "color": cat2,
                        "lightness": None,
                        "size": None,
                        "noop": None,
                        "split": False,
                        "align": "stretch",
                        "orientation": "horizontal",
                    },
                    "style": style,
                    "chart": "Marimekko Chart",
                },
                {
                    "config": {
                        "coordSystem": "polar",
                        "geometry": "circle",
                        "x": value2,
                        "y": {"set": value1, "range": {"min": None, "max": "110%"}},
                        "color": cat2,
                        "lightness": None,
                        "size": None,
                        "noop": cat1,
                        "split": False,
                        "align": "none",
                        "orientation": "horizontal",
                    },
                    "style": style,
                    "chart": "Polar Scatter",
                },
            ],
        }
        return presets.get(str(key), [])
