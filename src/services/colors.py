from src import config

colors: dict = {  # этот костыль не я придумал если что)))
    'Light': {
        'StatusBar': config.COLOR_BACKGROUND,
        'AppBar': config.COLOR_BACKGROUND,
        'Background': config.COLOR_BACKGROUND,
        'CardsDialogs': config.COLOR_BACKGROUND,
        'FlatButtonDown': config.COLOR_BACKGROUND,
    },
    'Dark': {
        'StatusBar': config.COLOR_BACKGROUND,
        'AppBar': config.COLOR_BACKGROUND,
        'Background': config.COLOR_BACKGROUND,
        'CardsDialogs': config.COLOR_BACKGROUND,
        'FlatButtonDown': config.COLOR_BACKGROUND,
    },
    'Blue': {
        '200': config.COLOR_ELEMENTS,
        '500': config.COLOR_ELEMENTS,
        '700': config.COLOR_ELEMENTS,
        'A700': config.COLOR_ELEMENTS,
    },
    'Red': {
        '200': config.COLOR_ELEMENTS,
        '500': config.COLOR_ELEMENTS,
        '700': config.COLOR_ELEMENTS,
        'A700': config.COLOR_ELEMENTS,
    }
}
