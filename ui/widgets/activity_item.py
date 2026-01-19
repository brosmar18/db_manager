"""
Activity Item Widget
A reusable component for displaying activity log entries
"""

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from config.theme import get_font, get_spacing, get_color


class ActivityItem(ttk.Frame):
    """A widget for displaying a single activity with status indicator"""

    def __init__(self, parent, text, time, status='info', **kwargs):
        # Use default style for activity items (light background)
        super().__init__(parent, **kwargs)

        self.text = text
        self.time = time
        self.status = status

        self.setup_ui()

    def setup_ui(self):
        """Setup the activity item UI"""
        # Status indicator (colored dot)
        indicator = ttk.Label(
            self,
            text="●",
            font=('Segoe UI', 16),
            bootstyle=self.status,
            foreground=get_color(self.status)
        )
        indicator.pack(side=LEFT, padx=(0, get_spacing('md')))

        # Text container
        text_frame = ttk.Frame(self)
        text_frame.pack(side=LEFT, fill=X, expand=YES)

        # Activity text
        activity_label = ttk.Label(
            text_frame,
            text=self.text,
            font=get_font('body'),
        )
        activity_label.pack(anchor=W)

        # Time stamp
        time_label = ttk.Label(
            text_frame,
            text=self.time,
            font=get_font('body_small'),
            bootstyle='secondary'
        )
        time_label.pack(anchor=W)
