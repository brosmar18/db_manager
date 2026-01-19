"""
Dashboard Component
Main dashboard content with stats, quick actions, activity, and system status
"""

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame
from config.theme import get_font, get_spacing, get_icon, get_color
from config.settings import (
    DASHBOARD_STATS, QUICK_ACTIONS, RECENT_ACTIVITIES,
    SYSTEM_METRICS, USER_INFO, FEATURES
)
from ui.widgets.stat_card import StatCard
from ui.widgets.activity_item import ActivityItem
from ui.widgets.metric_item import MetricItem


class DashboardContent(ScrolledFrame):
    """Dashboard content area with all widgets"""

    def __init__(self, parent, **kwargs):
        super().__init__(parent, autohide=True, **kwargs)

        self.setup_ui()

    def setup_ui(self):
        """Setup dashboard UI"""
        # Welcome banner
        if FEATURES['show_welcome_banner']:
            self.create_welcome_section()

        # Statistics cards
        if FEATURES['show_stats_cards']:
            self.create_stats_section()

        # Quick actions
        if FEATURES['show_quick_actions']:
            self.create_quick_actions()

        # Recent activity and system status (side by side)
        bottom_container = ttk.Frame(self)
        bottom_container.pack(fill=BOTH, expand=YES, pady=get_spacing('md'))

        if FEATURES['show_recent_activity']:
            self.create_recent_activity(bottom_container)

        if FEATURES['show_system_status']:
            self.create_system_status(bottom_container)

    def create_welcome_section(self):
        """Create welcome banner"""
        welcome_frame = ttk.Frame(self, bootstyle='primary')
        welcome_frame.pack(fill=X, pady=(0, get_spacing('lg')))

        inner_frame = ttk.Frame(welcome_frame, bootstyle='primary')
        inner_frame.pack(fill=BOTH, expand=YES, padx=get_spacing('xl'), pady=get_spacing('lg'))

        # Welcome title
        welcome_title = ttk.Label(
            inner_frame,
            text=f"Welcome back, {USER_INFO['name']}! {get_icon('welcome')}",
            font=get_font('heading_large'),
            bootstyle='inverse-primary',
            foreground=get_color('text_light')
        )
        welcome_title.pack(anchor=W)

        # Subtitle
        welcome_subtitle = ttk.Label(
            inner_frame,
            text="Everything is running smoothly. Here's your system overview.",
            font=get_font('body_large'),
            bootstyle='inverse-primary',
            foreground=get_color('text_light')
        )
        welcome_subtitle.pack(anchor=W, pady=(get_spacing('xs'), 0))

    def create_stats_section(self):
        """Create statistics cards section"""
        stats_container = ttk.Frame(self)
        stats_container.pack(fill=X, pady=get_spacing('md'))

        # Create stat cards
        for stat in DASHBOARD_STATS:
            card = StatCard(
                stats_container,
                title=stat['title'],
                value=stat['value'],
                icon=get_icon(stat['icon']),
                subtitle=stat['subtitle'],
                style=stat['style']
            )
            card.pack(side=LEFT, fill=BOTH, expand=YES, padx=get_spacing('sm'))

    def create_quick_actions(self):
        """Create quick actions section"""
        # Section title
        section_title = ttk.Label(
            self,
            text=f"{get_icon('lightning')} Quick Actions",
            font=get_font('heading_medium'),
        )
        section_title.pack(anchor=W, pady=(get_spacing('lg'), get_spacing('md')))

        # Actions container
        actions_container = ttk.Frame(self)
        actions_container.pack(fill=X, pady=get_spacing('sm'))

        # Create action buttons in rows of 3
        current_row = None
        for i, action in enumerate(QUICK_ACTIONS):
            if i % 3 == 0:
                current_row = ttk.Frame(actions_container)
                current_row.pack(fill=X, pady=get_spacing('xs'))

            btn = ttk.Button(
                current_row,
                text=f"{get_icon(action['icon'])} {action['label']}",
                bootstyle=action['style'],
                width=25
            )
            btn.pack(side=LEFT, padx=get_spacing('sm'), pady=get_spacing('xs'))

    def create_recent_activity(self, parent):
        """Create recent activity panel"""
        activity_card = ttk.Labelframe(
            parent,
            text=f"{get_icon('recent')} Recent Activity",
            bootstyle='info',
            padding=get_spacing('lg')
        )
        activity_card.pack(side=LEFT, fill=BOTH, expand=YES, padx=(0, get_spacing('sm')))

        # Header with "View All" button
        header = ttk.Frame(activity_card)
        header.pack(fill=X, pady=(0, get_spacing('md')))

        view_all = ttk.Button(
            header,
            text="View All →",
            bootstyle='link',
        )
        view_all.pack(side=RIGHT)

        # Activity items
        for activity in RECENT_ACTIVITIES:
            item = ActivityItem(
                activity_card,
                text=activity['text'],
                time=activity['time'],
                status=activity['status']
            )
            item.pack(fill=X, pady=get_spacing('sm'))

    def create_system_status(self, parent):
        """Create system status panel"""
        status_card = ttk.Labelframe(
            parent,
            text=f"{get_icon('system')} System Status",
            bootstyle='success',
            padding=get_spacing('lg')
        )
        status_card.pack(side=LEFT, fill=BOTH, expand=YES, padx=(get_spacing('sm'), 0))

        # Header with refresh button
        header = ttk.Frame(status_card)
        header.pack(fill=X, pady=(0, get_spacing('md')))

        refresh_btn = ttk.Button(
            header,
            text=f"{get_icon('refresh')} Refresh",
            bootstyle='link',
        )
        refresh_btn.pack(side=RIGHT)

        # System metrics
        for metric in SYSTEM_METRICS:
            item = MetricItem(
                status_card,
                label=metric['label'],
                value=metric['value'],
                percent=metric['percent'],
                style=metric['style']
            )
            item.pack(fill=X, pady=get_spacing('md'))
