# %%
from regmonkey_style.config import CONFIG


class Templates:
    @classmethod
    def custom_scatter_with_colors(self):
        custom_template = dict(
            {
                "data": {
                    "scatter": [
                        {
                            "mode": "markers",
                            "opacity": CONFIG.scatter.opacity,
                            "marker": {"size": 5},
                            "line": {"width": 2},
                        }
                    ]
                },
                "layout": {
                    "font": {"size": 12},
                    "title": {
                        "font": {"size": CONFIG.common.title_fontsize},
                        "x": 0.1,  # Horizontal position (left-aligned),
                        "yanchor": "top",
                    },
                    "autosize": True,
                    "legend": {
                        "font": {"size": CONFIG.common.tick_fontsize},
                        "bgcolor": CONFIG.color_style.legend_background_color,
                        "traceorder": "normal",
                    },
                    "xaxis": {
                        "title": "X-axis Title",
                        "titlefont": {"size": CONFIG.common.title_fontsize},
                        "tickfont": {"size": CONFIG.common.tick_fontsize},
                        "showgrid": True,
                        "griddash": "dot",
                        "gridcolor": CONFIG.color_style.grid_color,
                        "gridwidth": CONFIG.scatter.gridline.gridwidth,
                        "zeroline": True,
                        "zerolinecolor": CONFIG.color_style.zeroline_color,
                        "zerolinewidth": CONFIG.scatter.gridline.gridwidth,
                    },
                    "yaxis": {
                        "title": "Y-axis Title",
                        "titlefont": {"size": CONFIG.common.title_fontsize},
                        "tickfont": {"size": CONFIG.common.tick_fontsize},
                        "scaleanchor": "x",  # Lock y-axis scale to x-axis
                        "scaleratio": 1,  # Ensure equal scale ratio
                        "showgrid": True,
                        "griddash": "dot",
                        "gridcolor": CONFIG.color_style.grid_color,
                        "gridwidth": CONFIG.scatter.gridline.gridwidth,
                        "zeroline": True,
                        "zerolinecolor": CONFIG.color_style.zeroline_color,
                        "zerolinewidth": CONFIG.scatter.gridline.gridwidth,
                    },
                    "plot_bgcolor": "#EFF5F5",
                    "margin": CONFIG.common.margin.plotly,
                    "shapes": [],  # You can add shapes here if needed
                    "colorway": CONFIG.color_style.qualitative_scatter_color,
                },
            }
        )

        return custom_template

    @classmethod
    def custom_line_with_colors(self):
        custom_template = dict(
            {
                "data": {
                    "scatter": [
                        {
                            "mode": "lines",
                            "opacity": CONFIG.line.opacity,
                            "marker": {"size": 5},
                            "line": {"width": 2},
                        }
                    ]
                },
                "layout": {
                    "font": {"size": 12},
                    "title": {
                        "font": {"size": CONFIG.common.title_fontsize},
                        "x": 0.1,  # Horizontal position (left-aligned),
                        "yanchor": "top",
                    },
                    "autosize": True,
                    "legend": {
                        "font": {"size": CONFIG.common.tick_fontsize},
                        "bgcolor": CONFIG.color_style.legend_background_color,
                        "traceorder": "normal",
                    },
                    "xaxis": {
                        "title": "X-axis Title",
                        "titlefont": {"size": CONFIG.common.title_fontsize},
                        "tickfont": {"size": CONFIG.common.tick_fontsize},
                        "showgrid": True,
                        "griddash": "dot",
                        "gridcolor": CONFIG.color_style.grid_color,
                        "gridwidth": CONFIG.scatter.gridline.gridwidth,
                        "zeroline": True,
                        "zerolinecolor": CONFIG.color_style.zeroline_color,
                        "zerolinewidth": CONFIG.scatter.gridline.gridwidth,
                    },
                    "yaxis": {
                        "title": "Y-axis Title",
                        "titlefont": {"size": CONFIG.common.title_fontsize},
                        "tickfont": {"size": CONFIG.common.tick_fontsize},
                        "scaleanchor": "x",  # Lock y-axis scale to x-axis
                        "scaleratio": 1,  # Ensure equal scale ratio
                        "showgrid": True,
                        "griddash": "dot",
                        "gridcolor": CONFIG.color_style.grid_color,
                        "gridwidth": CONFIG.scatter.gridline.gridwidth,
                        "zeroline": True,
                        "zerolinecolor": CONFIG.color_style.zeroline_color,
                        "zerolinewidth": CONFIG.scatter.gridline.gridwidth,
                    },
                    "plot_bgcolor": "#EFF5F5",
                    "margin": CONFIG.common.margin.plotly,
                    "shapes": [],  # You can add shapes here if needed
                    "colorway": CONFIG.color_style.qualitative_line_color,
                },
            }
        )

        return custom_template
