"""
Theme Configuration
Flatly theme implementation from Bootswatch
A flat, modern design with excellent readability and clean aesthetics
"""

# Base theme - Flatly from Bootswatch
BASE_THEME = "flatly"  # Flat, modern, professional theme

# Flatly color palette - Official Bootswatch colors
COLORS = {
    # Primary colors (Flatly official palette)
    'primary': '#2C3E50',      # Dark blue-gray (navy)
    'secondary': '#95A5A6',    # Gray
    'success': '#18BC9C',      # Turquoise/teal
    'danger': '#E74C3C',       # Red
    'warning': '#F39C12',      # Orange
    'info': '#3498DB',         # Bright blue

    # Background colors
    'bg_light': '#ECF0F1',     # Very light gray (Flatly background)
    'bg_white': '#FFFFFF',     # Pure white
    'bg_sidebar': '#2C3E50',   # Dark blue-gray for sidebar (matches primary)
    'bg_header': '#2C3E50',    # Dark blue-gray for header (matches primary)

    # Text colors
    'text_dark': '#2C3E50',    # Dark blue-gray (Flatly text color)
    'text_light': '#FFFFFF',   # White
    'text_muted': '#95A5A6',   # Gray (matches secondary)
    'text_sidebar': '#ECF0F1', # Light gray for sidebar

    # Border colors
    'border_light': '#E7E7E7', # Light border
    'border_medium': '#BDC3C7', # Medium border

    # Accent colors (Flatly extended palette)
    'accent_blue': '#3498DB',
    'accent_purple': '#9B59B6',
    'accent_pink': '#E83E8C',
    'accent_orange': '#F39C12',
    'accent_teal': '#18BC9C',
    'accent_cyan': '#1ABC9C',
    'accent_green': '#2ECC71',

    # Status colors
    'online': '#18BC9C',       # Turquoise (success)
    'offline': '#E74C3C',      # Red (danger)
    'warning_status': '#F39C12', # Orange (warning)
    'idle': '#95A5A6',         # Gray (secondary)
}

# Font configuration - Clean sans-serif for Flatly theme
FONTS = {
    'brand': ('Helvetica', 24, 'bold'),
    'brand_subtitle': ('Helvetica', 9, 'normal'),
    'heading_large': ('Helvetica', 22, 'bold'),
    'heading_medium': ('Helvetica', 16, 'bold'),
    'heading_small': ('Helvetica', 14, 'bold'),
    'body_large': ('Helvetica', 12, 'normal'),
    'body': ('Helvetica', 11, 'normal'),
    'body_small': ('Helvetica', 10, 'normal'),
    'caption': ('Helvetica', 9, 'bold'),
    'stat_value': ('Helvetica', 32, 'bold'),
    'nav_item': ('Helvetica', 11, 'normal'),
}

# Spacing configuration
SPACING = {
    'xs': 5,
    'sm': 10,
    'md': 15,
    'lg': 20,
    'xl': 30,
    'xxl': 40,
}

# Component sizes - Flatly uses clean, consistent spacing
SIZES = {
    'sidebar_width': 280,
    'header_height': 80,
    'card_padding': 20,
    'border_radius': 4,      # Flatly uses subtle rounded corners
    'button_height': 38,     # Standard button height
}

# Icons (using Unicode emojis for visual clarity)
ICONS = {
    'dashboard': '🏠',
    'analytics': '📊',
    'settings': '⚙️',
    'database': '🗄️',
    'query': '🔍',
    'table': '📋',
    'backup': '🔄',
    'file': '📁',
    'organize': '🗂️',
    'search': '🔎',
    'cleanup': '♻️',
    'service': '🚀',
    'monitor': '📈',
    'logs': '📝',
    'alert': '🔔',
    'help': '❓',
    'exit': '🚪',
    'profile': '👤',
    'welcome': '👋',
    'storage': '💾',
    'time': '⏱️',
    'recent': '📜',
    'system': '💻',
    'refresh': '🔄',
    'connect': '🔌',
    'run': '▶️',
    'schedule': '📅',
    'scan': '🔍',
    'success': '✅',
    'error': '❌',
    'info_icon': 'ℹ️',
    'lightning': '⚡',
}

# Style configurations for widgets - Flat design principles
WIDGET_STYLES = {
    'card': {
        'relief': 'flat',        # Flat design, no raised relief
        'borderwidth': 1,
        'padding': (SPACING['lg'], SPACING['lg']),
    },
    'card_hover': {
        'relief': 'flat',
        'borderwidth': 1,
    },
    'nav_button': {
        'width': 25,
        'padding': (SPACING['sm'], SPACING['sm']),
    },
    'action_button': {
        'width': 20,
        'padding': (SPACING['sm'], SPACING['md']),
    },
}

def get_theme_name():
    """Get the base theme name"""
    return BASE_THEME

def get_color(color_name):
    """Get a color value by name"""
    return COLORS.get(color_name, '#000000')

def get_font(font_name):
    """Get a font configuration by name"""
    return FONTS.get(font_name, ('Segoe UI', 11, 'normal'))

def get_spacing(size):
    """Get spacing value"""
    return SPACING.get(size, 10)

def get_size(size_name):
    """Get size value"""
    return SIZES.get(size_name, 0)

def get_icon(icon_name):
    """Get icon by name"""
    return ICONS.get(icon_name, '')
