# %%
from regmonkey_style.config import CONFIG


class Templates:
    @classmethod
    def regmonkey_scatter(cls):
        custom_template = dict(
            {
                "data": {
                    "scatter": [
                        {
                            "mode": "markers",
                            "opacity": CONFIG.scatter.opacity,
                            "marker": {"size": CONFIG.scatter.markersize.plotly},
                            "line": {"width": 2},
                        }
                    ]
                },
                "layout": cls._create_layout_template(
                    CONFIG.color_style.qualitative_scatter_color
                ),
            }
        )

        return custom_template

    @classmethod
    def regmonkey_line(cls):
        custom_template = dict(
            {
                "data": {
                    "scatter": [
                        {
                            "mode": "lines",
                            "opacity": CONFIG.line.opacity,
                            "marker": {"size": CONFIG.scatter.markersize.plotly},
                            "line": {"width": 2},
                            "connectgaps": True,
                        }
                    ]
                },
                "layout": cls._create_layout_template(
                    CONFIG.color_style.qualitative_line_color
                ),
            }
        )

        return custom_template

    @classmethod
    def regmonkey_twoline(cls):
        custom_template = dict(
            {
                "data": {
                    "scatter": [
                        {
                            "mode": "markers+lines",
                            "line": {"dash": "solid"},
                            "connectgaps": True,
                        },
                        {
                            "mode": "markers+lines",
                            "line": {"dash": "dash"},
                            "connectgaps": True,
                        },
                        {
                            "mode": "markers+lines",
                            "line": {"dash": "dot"},
                            "connectgaps": True,
                        },
                    ]
                },
                "layout": cls._create_layout_template(
                    CONFIG.color_style.two_line_color
                ),
            }
        )

        return custom_template

    @classmethod
    def _create_layout_template(cls, color_way):
        """
        Create a default layout template for Plotly.

        Args:
            color_way (list): List of colors to be used in the color cycle.

        Returns:
            dict: A dictionary representing the default layout template.
        """

        default_layout = dict(
            {
                "font": {
                    "size": CONFIG.common.text_fontsize,
                    "color": CONFIG.color_style.text_color,
                },
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
                    # "scaleanchor": "x",  # Lock y-axis scale to x-axis
                    # "scaleratio": 1,  # Ensure equal scale ratio
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
                "paper_bgcolor": "white",  # Figure background color (if needed)
                "colorway": color_way,  # Color cycle for lines
            }
        )
        return default_layout
