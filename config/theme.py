"""
Theme Configuration
Custom theme settings for the DB Manager application with enhanced visibility
"""

# Base theme - using a lighter theme for better visibility
BASE_THEME = "cosmo"  # Light, modern, professional theme

# Custom color palette - Modern, vibrant, high-contrast
COLORS = {
    # Primary colors
    'primary': '#0066CC',      # Vibrant blue
    'secondary': '#6C757D',    # Cool gray
    'success': '#28A745',      # Fresh green
    'danger': '#DC3545',       # Bold red
    'warning': '#FFC107',      # Bright amber
    'info': '#17A2B8',         # Teal

    # Background colors
    'bg_light': '#F8F9FA',     # Very light gray
    'bg_white': '#FFFFFF',     # Pure white
    'bg_sidebar': '#2C3E50',   # Dark blue-gray for sidebar
    'bg_header': '#34495E',    # Slightly lighter dark blue-gray

    # Text colors
    'text_dark': '#212529',    # Almost black
    'text_light': '#FFFFFF',   # White
    'text_muted': '#6C757D',   # Gray
    'text_sidebar': '#ECF0F1', # Light gray for sidebar

    # Border colors
    'border_light': '#DEE2E6', # Light border
    'border_medium': '#CED4DA', # Medium border

    # Accent colors
    'accent_blue': '#007BFF',
    'accent_purple': '#6F42C1',
    'accent_pink': '#E83E8C',
    'accent_orange': '#FD7E14',
    'accent_teal': '#20C997',
    'accent_cyan': '#17A2B8',

    # Status colors
    'online': '#28A745',
    'offline': '#DC3545',
    'warning_status': '#FFC107',
    'idle': '#6C757D',
}

# Font configuration
FONTS = {
    'brand': ('Segoe UI', 24, 'bold'),
    'brand_subtitle': ('Segoe UI', 9, 'normal'),
    'heading_large': ('Segoe UI', 22, 'bold'),
    'heading_medium': ('Segoe UI', 16, 'bold'),
    'heading_small': ('Segoe UI', 14, 'bold'),
    'body_large': ('Segoe UI', 12, 'normal'),
    'body': ('Segoe UI', 11, 'normal'),
    'body_small': ('Segoe UI', 10, 'normal'),
    'caption': ('Segoe UI', 9, 'normal'),
    'stat_value': ('Segoe UI', 32, 'bold'),
    'nav_item': ('Segoe UI', 11, 'normal'),
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

# Component sizes
SIZES = {
    'sidebar_width': 280,
    'header_height': 80,
    'card_padding': 20,
    'border_radius': 8,
    'button_height': 40,
}

# Icons (using Unicode emojis)
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

# Style configurations for widgets
WIDGET_STYLES = {
    'card': {
        'relief': 'raised',
        'borderwidth': 1,
        'padding': (SPACING['lg'], SPACING['lg']),
    },
    'card_hover': {
        'relief': 'raised',
        'borderwidth': 2,
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
