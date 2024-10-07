# %%

from regmonkey_style.config import CONFIG
import matplotlib.pyplot as plt


def add_transparency(colors, alpha):
    """
    Add transparency to a list of colors in #RRGGBB format.

    Args:
        colors (list): List of color hex codes in #RRGGBB format.
        alpha (float): Transparency level (0.0 to 1.0).

    Returns:
        list: List of colors with added transparency in #RRGGBBAA format.
    """

    def hex_with_alpha(color, alpha):
        """
        Add alpha transparency to a single hex color.

        Args:
            color (str): Color hex code in #RRGGBB format.
            alpha (float): Transparency level (0.0 to 1.0).

        Returns:
            str: Color hex code in #RRGGBBAA format.
        """
        alpha_hex = f"{int(alpha * 255):02x}"
        return color + alpha_hex

    return [hex_with_alpha(color, alpha) for color in colors]


class Templates:
    @classmethod
    def regmonkey_scatter(cls):
        custom_colorway = plt.cycler(
            color=add_transparency(
                CONFIG.color_style.qualitative_scatter_color, CONFIG.scatter.opacity
            )
        )
        custom_layout_template = cls._create_layout_template(custom_colorway)
        custom_linewidth_template = cls._create_gridline_template(
            CONFIG.scatter.gridline.gridwidth * 4,
            CONFIG.scatter.gridline.gridwidth * 10,
        )

        custom_template = custom_layout_template | custom_linewidth_template

        ## update
        scatter_custom = dict(
            {"lines.markersize": CONFIG.scatter.markersize.matplotlib}
        )

        custom_template.update(scatter_custom)
        return custom_template

    @classmethod
    def regmonkey_line(cls):
        custom_colorway = plt.cycler(
            color=add_transparency(
                CONFIG.color_style.qualitative_line_color, CONFIG.line.opacity
            )
        )
        custom_layout_template = cls._create_layout_template(custom_colorway)
        custom_linewidth_template = cls._create_gridline_template(
            CONFIG.scatter.gridline.gridwidth * 4,
            CONFIG.scatter.gridline.gridwidth * 10,
        )

        custom_template = custom_layout_template | custom_linewidth_template

        return custom_template

    @classmethod
    def regmonkey_twoline(cls):
        custom_colorway = plt.cycler(
            color=CONFIG.color_style.two_line_color
        ) + plt.cycler(linestyle=["-", "--", ":"])

        custom_layout_template = cls._create_layout_template(custom_colorway)
        custom_linewidth_template = cls._create_gridline_template(
            CONFIG.scatter.gridline.gridwidth * 8,
            CONFIG.scatter.gridline.gridwidth * 10,
        )

        custom_template = custom_layout_template | custom_linewidth_template

        return custom_template

    @classmethod
    def _create_layout_template(cls, color_way):
        default_layout = dict(
            {
                "font.size": CONFIG.common.text_fontsize,
                "axes.titlelocation": "left",
                "axes.titlesize": CONFIG.common.title_fontsize,
                "axes.labelsize": CONFIG.common.xlabel_fontsize,
                "xtick.labelsize": CONFIG.common.xlabel_fontsize,
                "ytick.labelsize": CONFIG.common.tick_fontsize,
                "legend.fontsize": CONFIG.common.legend_fontsize,
                "legend.frameon": False,
                "axes.grid": True,
                "grid.linestyle": ":",
                "axes.edgecolor": "#000000",
                "grid.color": CONFIG.color_style.grid_color,
                "axes.facecolor": CONFIG.color_style.background_color,
                "axes.spines.top": False,
                "axes.spines.right": False,
                "axes.spines.left": True,
                "axes.spines.bottom": True,
                "axes.prop_cycle": color_way,
                "text.color": CONFIG.color_style.text_color,  # Set text color
                "axes.labelcolor": CONFIG.color_style.text_color,  # Set axes label color
                "xtick.color": CONFIG.color_style.text_color,  # Set x-tick color
                "ytick.color": CONFIG.color_style.text_color,  # Set y-tick color
                "axes.titlecolor": CONFIG.color_style.text_color,  # Set axes title color
            }
        )
        return default_layout

    @classmethod
    def _create_gridline_template(cls, gridline_width, axesline_width):
        default_layout = dict(
            {
                "grid.linewidth": gridline_width,
                "axes.linewidth": axesline_width,
            }
        )
        return default_layout
