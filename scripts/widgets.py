import ipywidgets as widgets


def dropdown(elements,title):
    # Construccion del widget de tipo combo para mostrar las columnas solo de tipo date
    menu = widgets.Dropdown(
           options=elements,
           value=elements[0],
           description=title)
    return menu