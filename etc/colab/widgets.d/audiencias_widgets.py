from colab.widgets.widget_manager import WidgetManager
from colab_audiencias.widgets.home_section import AudienciasHomeSectionWidget


WidgetManager.register_widget('home_section', AudienciasHomeSectionWidget())
