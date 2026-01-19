"""
Sidebar Component
Navigation sidebar with brand, menu items, and actions
"""

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from config.theme import get_font, get_spacing, get_size, get_icon, get_color
from config.settings import APP_NAME, APP_VERSION, APP_SUBTITLE, NAVIGATION


class Sidebar(ttk.Frame):
    """Sidebar navigation component"""

    def __init__(self, parent, on_nav_click=None, **kwargs):
        # Use dark background for sidebar
        super().__init__(parent, width=get_size('sidebar_width'), **kwargs)

        self.on_nav_click = on_nav_click
        self.pack_propagate(False)

        # Configure sidebar background
        self.configure(style='dark.TFrame')

        self.setup_ui()

    def setup_ui(self):
        """Setup sidebar UI"""
        # Brand section
        self.create_brand_section()

        # Navigation sections
        self.create_navigation()

        # Bottom actions
        self.create_bottom_actions()

    def create_brand_section(self):
        """Create brand/logo section"""
        brand_frame = ttk.Frame(self, bootstyle='dark')
        brand_frame.pack(fill=X, padx=get_spacing('lg'), pady=(get_spacing('xl'), get_spacing('xxl')))

        # App name with lightning icon
        brand_label = ttk.Label(
            brand_frame,
            text=f"{get_icon('lightning')} {APP_NAME}",
            font=get_font('brand'),
            bootstyle='inverse-dark',
            foreground=get_color('text_sidebar')
        )
        brand_label.pack()

        # Version label
        version_label = ttk.Label(
            brand_frame,
            text=f"v{APP_VERSION} {APP_SUBTITLE}",
            font=get_font('brand_subtitle'),
            bootstyle='secondary',
            foreground=get_color('text_muted')
        )
        version_label.pack()

    def create_navigation(self):
        """Create navigation menu sections"""
        # Scrollable frame for navigation items
        nav_container = ttk.Frame(self, bootstyle='dark')
        nav_container.pack(fill=BOTH, expand=YES)

        # Create each navigation section
        for section_key, section_data in NAVIGATION.items():
            self.create_nav_section(
                nav_container,
                section_data['title'],
                section_data['items']
            )

    def create_nav_section(self, parent, title, items):
        """Create a navigation section with title and items"""
        # Section title
        section_frame = ttk.Frame(parent, bootstyle='dark')
        section_frame.pack(fill=X, padx=get_spacing('lg'), pady=(get_spacing('lg'), get_spacing('sm')))

        section_label = ttk.Label(
            section_frame,
            text=title,
            font=get_font('caption'),
            bootstyle='secondary',
            foreground=get_color('text_muted')
        )
        section_label.pack(anchor=W)

        # Navigation items
        for item in items:
            self.create_nav_item(
                parent,
                get_icon(item['icon']),
                item['label'],
                item['style']
            )

    def create_nav_item(self, parent, icon, label, style):
        """Create a single navigation item button"""
        btn = ttk.Button(
            parent,
            text=f"{icon}  {label}",
            bootstyle=f"{style}-outline",
            command=lambda: self.handle_nav_click(label),
            width=25
        )
        btn.pack(fill=X, padx=get_spacing('lg'), pady=2)

    def handle_nav_click(self, item_name):
        """Handle navigation item click"""
        if self.on_nav_click:
            self.on_nav_click(item_name)
        print(f"Navigated to: {item_name}")

    def create_bottom_actions(self):
        """Create bottom action buttons"""
        bottom_frame = ttk.Frame(self, bootstyle='dark')
        bottom_frame.pack(side=BOTTOM, fill=X, padx=get_spacing('lg'), pady=get_spacing('lg'))

        # Help button
        help_btn = ttk.Button(
            bottom_frame,
            text=f"{get_icon('help')} Help & Support",
            bootstyle='secondary-outline',
            width=20
        )
        help_btn.pack(pady=get_spacing('xs'))

        # Exit button
        exit_btn = ttk.Button(
            bottom_frame,
            text=f"{get_icon('exit')} Exit",
            bootstyle='danger-outline',
            width=20,
            command=self.handle_exit
        )
        exit_btn.pack(pady=get_spacing('xs'))

    def handle_exit(self):
        """Handle exit button click"""
        # In production, add confirmation dialog
        self.winfo_toplevel().quit()
