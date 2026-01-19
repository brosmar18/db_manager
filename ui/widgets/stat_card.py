"""
Statistics Card Widget
A reusable card component for displaying statistics
"""

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from config.theme import get_font, get_spacing


class StatCard(ttk.Frame):
    """A card widget for displaying a statistic with icon, value, title, and subtitle"""

    def __init__(self, parent, title, value, icon, subtitle, style='primary', **kwargs):
        super().__init__(parent, bootstyle=style, **kwargs)

        self.title = title
        self.value = value
        self.icon = icon
        self.subtitle = subtitle
        self.style = style

        self.setup_ui()

    def setup_ui(self):
        """Setup the card UI"""
        # Inner container with padding
        inner = ttk.Frame(self, bootstyle=self.style)
        inner.pack(fill=BOTH, expand=YES, padx=get_spacing('lg'), pady=get_spacing('lg'))

        # Icon
        icon_label = ttk.Label(
            inner,
            text=self.icon,
            font=('Segoe UI', 36),
            bootstyle=f"inverse-{self.style}"
        )
        icon_label.pack(anchor=W, pady=(0, get_spacing('sm')))

        # Value
        value_label = ttk.Label(
            inner,
            text=self.value,
            font=get_font('stat_value'),
            bootstyle=f"inverse-{self.style}"
        )
        value_label.pack(anchor=W, pady=(get_spacing('xs'), get_spacing('xs')))

        # Title
        title_label = ttk.Label(
            inner,
            text=self.title,
            font=get_font('heading_small'),
            bootstyle=f"inverse-{self.style}"
        )
        title_label.pack(anchor=W)

        # Subtitle
        subtitle_label = ttk.Label(
            inner,
            text=self.subtitle,
            font=get_font('body_small'),
            bootstyle=f"inverse-{self.style}"
        )
        subtitle_label.pack(anchor=W, pady=(get_spacing('xs'), 0))

    def update_value(self, new_value):
        """Update the card's value"""
        self.value = new_value
        # Note: In a production app, you'd need to keep references to labels to update them
