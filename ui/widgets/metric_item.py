"""
Metric Item Widget
A reusable component for displaying system metrics with progress bars
"""

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from config.theme import get_font, get_spacing


class MetricItem(ttk.Frame):
    """A widget for displaying a metric with a progress bar"""

    def __init__(self, parent, label, value, percent, style='info', **kwargs):
        super().__init__(parent, **kwargs)

        self.label = label
        self.value = value
        self.percent = percent
        self.style = style

        self.setup_ui()

    def setup_ui(self):
        """Setup the metric item UI"""
        # Label and value row
        top_row = ttk.Frame(self)
        top_row.pack(fill=X, pady=(0, get_spacing('xs')))

        # Metric label
        label_widget = ttk.Label(
            top_row,
            text=self.label,
            font=get_font('body'),
        )
        label_widget.pack(side=LEFT)

        # Metric value
        value_widget = ttk.Label(
            top_row,
            text=self.value,
            font=get_font('body'),
            bootstyle=self.style
        )
        value_widget.pack(side=RIGHT)

        # Progress bar
        progress = ttk.Progressbar(
            self,
            bootstyle=self.style,
            value=self.percent,
            length=200
        )
        progress.pack(fill=X)

    def update_value(self, new_value, new_percent):
        """Update the metric value and progress"""
        self.value = new_value
        self.percent = new_percent
        # Note: In production, keep references to widgets for live updates
