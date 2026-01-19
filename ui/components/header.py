"""
Header Component
Top navigation bar with title, breadcrumbs, and action buttons
"""

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from config.theme import get_font, get_spacing, get_size, get_icon, get_color


class Header(ttk.Frame):
    """Header component with title and action buttons"""

    def __init__(self, parent, title="Dashboard Overview", breadcrumb="Home / Dashboard", **kwargs):
        super().__init__(parent, height=get_size('header_height'), **kwargs)

        self.title = title
        self.breadcrumb = breadcrumb
        self.pack_propagate(False)

        # Configure header background with a distinct color
        self.configure(bootstyle='secondary')

        self.setup_ui()

    def setup_ui(self):
        """Setup header UI"""
        # Left side - Title and breadcrumb
        self.create_title_section()

        # Right side - Action buttons
        self.create_action_buttons()

    def create_title_section(self):
        """Create title and breadcrumb section"""
        left_frame = ttk.Frame(self, bootstyle='secondary')
        left_frame.pack(side=LEFT, padx=get_spacing('xl'), pady=get_spacing('lg'))

        # Title
        title_label = ttk.Label(
            left_frame,
            text=self.title,
            font=get_font('heading_large'),
            bootstyle='inverse-secondary',
            foreground=get_color('text_light')
        )
        title_label.pack(anchor=W)

        # Breadcrumb
        breadcrumb_label = ttk.Label(
            left_frame,
            text=self.breadcrumb,
            font=get_font('body_small'),
            bootstyle='secondary',
            foreground=get_color('text_muted')
        )
        breadcrumb_label.pack(anchor=W, pady=(get_spacing('xs'), 0))

    def create_action_buttons(self):
        """Create action buttons section"""
        right_frame = ttk.Frame(self, bootstyle='secondary')
        right_frame.pack(side=RIGHT, padx=get_spacing('xl'), pady=get_spacing('lg'))

        # Search button
        search_btn = ttk.Button(
            right_frame,
            text=f"{get_icon('search')} Search",
            bootstyle='info',
            width=12
        )
        search_btn.pack(side=LEFT, padx=get_spacing('xs'))

        # Notifications button
        notify_btn = ttk.Button(
            right_frame,
            text=f"{get_icon('alert')} Alerts (3)",
            bootstyle='warning',
            width=12
        )
        notify_btn.pack(side=LEFT, padx=get_spacing('xs'))

        # Profile button
        profile_btn = ttk.Button(
            right_frame,
            text=f"{get_icon('profile')} Profile",
            bootstyle='primary',
            width=12
        )
        profile_btn.pack(side=LEFT, padx=get_spacing('xs'))

    def update_title(self, new_title, new_breadcrumb=None):
        """Update the header title and breadcrumb"""
        self.title = new_title
        if new_breadcrumb:
            self.breadcrumb = new_breadcrumb
        # Note: In production, keep references to labels for live updates
