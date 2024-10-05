# %%
from regmonkey_style.config import CONFIG
import plotly.io as pio
import regmonkey_style.common.setup_custom_font as scf
import regmonkey_style.plotly_custom.templates as pct
from regmonkey_style.common import utils


def set_default():
    scf.add_custom_font(CONFIG.font_style.default_font)


def show_available_fonts():
    return CONFIG.font_style.available_list


def show_available_templates():
    return CONFIG.templates

def set_font(font):
    if font not in CONFIG.font_style.available_list:
        raise ValueError("{} is not in templates list".format(font))
    
    


def set_templates(template):
    if template not in CONFIG.templates:
        raise ValueError("template is not in templates list")

    Template_instance = pct.Templates
    custom_template = getattr(Template_instance, template)()
    pio.templates[template] = custom_template
    pio.templates.default = template


def equal_xy_scale(figure_object):
    return utils.equal_xy_scale(figure_object)


def restore_default():
    pio.templates.default = "plotly"
