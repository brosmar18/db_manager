"""
Modern Dashboard Application
A beautiful, professional dashboard for database management, file organization, and service management
"""

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame
import tkinter as tk


class ModernDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("DB Manager - Modern Dashboard")
        self.root.geometry("1400x900")

        # Set theme to a modern dark theme
        self.style = ttk.Style("darkly")

        # Configure custom colors
        self.colors = {
            'primary': '#3498db',
            'secondary': '#2c3e50',
            'success': '#2ecc71',
            'danger': '#e74c3c',
            'warning': '#f39c12',
            'info': '#16a085',
            'dark': '#1a1a1a',
            'light': '#ecf0f1',
            'sidebar_bg': '#212529',
            'content_bg': '#2b3035'
        }

        # Track active navigation
        self.active_nav = None

        self.setup_ui()

    def setup_ui(self):
        """Setup the main UI structure"""
        # Main container
        self.main_container = ttk.Frame(self.root)
        self.main_container.pack(fill=BOTH, expand=YES)

        # Create sidebar
        self.create_sidebar()

        # Create right panel (header + content)
        self.create_right_panel()

    def create_sidebar(self):
        """Create the navigation sidebar"""
        sidebar = ttk.Frame(self.main_container, bootstyle="dark", width=280)
        sidebar.pack(side=LEFT, fill=Y)
        sidebar.pack_propagate(False)

        # Logo/Brand section
        brand_frame = ttk.Frame(sidebar, bootstyle="dark")
        brand_frame.pack(fill=X, padx=20, pady=(30, 40))

        brand_label = ttk.Label(
            brand_frame,
            text="⚡ DB Manager",
            font=("Helvetica", 24, "bold"),
            bootstyle="inverse-dark"
        )
        brand_label.pack()

        version_label = ttk.Label(
            brand_frame,
            text="v1.0.0 Professional",
            font=("Helvetica", 9),
            bootstyle="secondary"
        )
        version_label.pack()

        # Navigation sections
        self.create_nav_section(sidebar, "MAIN", [
            ("🏠", "Dashboard", "primary"),
            ("📊", "Analytics", "info"),
            ("⚙️", "Settings", "secondary")
        ])

        self.create_nav_section(sidebar, "DATABASE", [
            ("🗄️", "Postgres Manager", "success"),
            ("🔍", "Query Builder", "info"),
            ("📋", "Tables & Schemas", "primary"),
            ("🔄", "Backups", "warning")
        ])

        self.create_nav_section(sidebar, "FILE MANAGEMENT", [
            ("📁", "File Explorer", "primary"),
            ("🗂️", "Organization Tools", "info"),
            ("🔎", "Search Files", "secondary"),
            ("♻️", "Cleanup Utilities", "warning")
        ])

        self.create_nav_section(sidebar, "SERVICES", [
            ("🚀", "Service Manager", "success"),
            ("📈", "Monitoring", "info"),
            ("📝", "Logs Viewer", "secondary"),
            ("🔔", "Alerts", "danger")
        ])

        # Bottom section
        bottom_frame = ttk.Frame(sidebar, bootstyle="dark")
        bottom_frame.pack(side=BOTTOM, fill=X, padx=20, pady=20)

        help_btn = ttk.Button(
            bottom_frame,
            text="❓ Help & Support",
            bootstyle="secondary-outline",
            width=20
        )
        help_btn.pack(pady=5)

        logout_btn = ttk.Button(
            bottom_frame,
            text="🚪 Exit",
            bootstyle="danger-outline",
            width=20
        )
        logout_btn.pack(pady=5)

    def create_nav_section(self, parent, title, items):
        """Create a navigation section with items"""
        # Section title
        section_frame = ttk.Frame(parent, bootstyle="dark")
        section_frame.pack(fill=X, padx=20, pady=(20, 10))

        section_label = ttk.Label(
            section_frame,
            text=title,
            font=("Helvetica", 9, "bold"),
            bootstyle="secondary"
        )
        section_label.pack(anchor=W)

        # Section items
        for icon, text, style in items:
            self.create_nav_item(parent, icon, text, style)

    def create_nav_item(self, parent, icon, text, style):
        """Create a navigation item button"""
        btn = ttk.Button(
            parent,
            text=f"{icon}  {text}",
            bootstyle=f"{style}-outline",
            command=lambda: self.on_nav_click(text)
        )
        btn.pack(fill=X, padx=20, pady=2)

        # Style configuration for hover effects
        btn.configure(width=25)

    def on_nav_click(self, item_name):
        """Handle navigation item click"""
        self.active_nav = item_name
        print(f"Navigated to: {item_name}")
        # Future: Load different content based on navigation

    def create_right_panel(self):
        """Create the right panel with header and content"""
        right_panel = ttk.Frame(self.main_container)
        right_panel.pack(side=LEFT, fill=BOTH, expand=YES)

        # Create header
        self.create_header(right_panel)

        # Create content area
        self.create_content_area(right_panel)

    def create_header(self, parent):
        """Create the top header bar"""
        header = ttk.Frame(parent, bootstyle="secondary", height=80)
        header.pack(fill=X)
        header.pack_propagate(False)

        # Left side - Title and breadcrumb
        left_frame = ttk.Frame(header, bootstyle="secondary")
        left_frame.pack(side=LEFT, padx=30, pady=20)

        title_label = ttk.Label(
            left_frame,
            text="Dashboard Overview",
            font=("Helvetica", 20, "bold"),
            bootstyle="inverse-secondary"
        )
        title_label.pack(anchor=W)

        breadcrumb = ttk.Label(
            left_frame,
            text="Home / Dashboard",
            font=("Helvetica", 10),
            bootstyle="secondary"
        )
        breadcrumb.pack(anchor=W)

        # Right side - Action buttons
        right_frame = ttk.Frame(header, bootstyle="secondary")
        right_frame.pack(side=RIGHT, padx=30, pady=20)

        search_btn = ttk.Button(
            right_frame,
            text="🔍 Search",
            bootstyle="info-outline",
            width=12
        )
        search_btn.pack(side=LEFT, padx=5)

        notify_btn = ttk.Button(
            right_frame,
            text="🔔 Alerts (3)",
            bootstyle="warning-outline",
            width=12
        )
        notify_btn.pack(side=LEFT, padx=5)

        profile_btn = ttk.Button(
            right_frame,
            text="👤 Profile",
            bootstyle="primary",
            width=12
        )
        profile_btn.pack(side=LEFT, padx=5)

    def create_content_area(self, parent):
        """Create the main content area with cards"""
        # Scrolled content area
        content_container = ScrolledFrame(parent, autohide=True, bootstyle="dark")
        content_container.pack(fill=BOTH, expand=YES, padx=20, pady=20)

        # Welcome section
        self.create_welcome_section(content_container)

        # Stats cards
        self.create_stats_section(content_container)

        # Quick actions
        self.create_quick_actions(content_container)

        # Recent activity and system status
        bottom_row = ttk.Frame(content_container)
        bottom_row.pack(fill=BOTH, expand=YES, pady=10)

        self.create_recent_activity(bottom_row)
        self.create_system_status(bottom_row)

    def create_welcome_section(self, parent):
        """Create welcome banner"""
        welcome_frame = ttk.Frame(parent, bootstyle="primary", height=120)
        welcome_frame.pack(fill=X, pady=(0, 20))

        inner_frame = ttk.Frame(welcome_frame, bootstyle="primary")
        inner_frame.pack(fill=BOTH, expand=YES, padx=30, pady=25)

        welcome_title = ttk.Label(
            inner_frame,
            text="Welcome back, Administrator! 👋",
            font=("Helvetica", 22, "bold"),
            bootstyle="inverse-primary"
        )
        welcome_title.pack(anchor=W)

        welcome_subtitle = ttk.Label(
            inner_frame,
            text="Everything is running smoothly. Here's your system overview.",
            font=("Helvetica", 12),
            bootstyle="inverse-primary"
        )
        welcome_subtitle.pack(anchor=W, pady=(5, 0))

    def create_stats_section(self, parent):
        """Create statistics cards"""
        stats_frame = ttk.Frame(parent)
        stats_frame.pack(fill=X, pady=10)

        stats = [
            ("Database Connections", "127", "success", "🗄️", "+12% from last week"),
            ("Active Services", "8/10", "info", "🚀", "2 services stopped"),
            ("Storage Used", "234 GB", "warning", "💾", "67% of total capacity"),
            ("System Uptime", "15d 7h", "primary", "⏱️", "Last restart: Jan 4")
        ]

        for i, (title, value, style, icon, subtitle) in enumerate(stats):
            self.create_stat_card(stats_frame, title, value, style, icon, subtitle, i)

    def create_stat_card(self, parent, title, value, style, icon, subtitle, position):
        """Create a single statistics card"""
        card = ttk.Frame(parent, bootstyle=style)
        card.pack(side=LEFT, fill=BOTH, expand=YES, padx=8)

        inner = ttk.Frame(card, bootstyle=style)
        inner.pack(fill=BOTH, expand=YES, padx=25, pady=20)

        # Icon and title row
        top_row = ttk.Frame(inner, bootstyle=style)
        top_row.pack(fill=X)

        icon_label = ttk.Label(
            top_row,
            text=icon,
            font=("Helvetica", 28),
            bootstyle=f"inverse-{style}"
        )
        icon_label.pack(side=LEFT)

        # Value
        value_label = ttk.Label(
            inner,
            text=value,
            font=("Helvetica", 32, "bold"),
            bootstyle=f"inverse-{style}"
        )
        value_label.pack(anchor=W, pady=(10, 5))

        # Title
        title_label = ttk.Label(
            inner,
            text=title,
            font=("Helvetica", 11, "bold"),
            bootstyle=f"inverse-{style}"
        )
        title_label.pack(anchor=W)

        # Subtitle
        subtitle_label = ttk.Label(
            inner,
            text=subtitle,
            font=("Helvetica", 9),
            bootstyle=f"inverse-{style}"
        )
        subtitle_label.pack(anchor=W, pady=(5, 0))

    def create_quick_actions(self, parent):
        """Create quick action buttons section"""
        section_label = ttk.Label(
            parent,
            text="⚡ Quick Actions",
            font=("Helvetica", 16, "bold"),
            bootstyle="inverse-dark"
        )
        section_label.pack(anchor=W, pady=(20, 15))

        actions_frame = ttk.Frame(parent)
        actions_frame.pack(fill=X, pady=10)

        actions = [
            ("New Database Connection", "primary", "🔌"),
            ("Run Query", "success", "▶️"),
            ("Backup Database", "info", "💾"),
            ("Schedule Task", "warning", "📅"),
            ("View Logs", "secondary", "📋"),
            ("System Scan", "danger", "🔍")
        ]

        for i, (text, style, icon) in enumerate(actions):
            btn = ttk.Button(
                actions_frame,
                text=f"{icon} {text}",
                bootstyle=f"{style}",
                width=20
            )
            btn.pack(side=LEFT, padx=8, pady=5)
            if (i + 1) % 3 == 0:
                actions_frame = ttk.Frame(parent)
                actions_frame.pack(fill=X, pady=5)

    def create_recent_activity(self, parent):
        """Create recent activity panel"""
        activity_card = ttk.Frame(parent, bootstyle="secondary")
        activity_card.pack(side=LEFT, fill=BOTH, expand=YES, padx=(0, 10))

        # Header
        header = ttk.Frame(activity_card, bootstyle="secondary")
        header.pack(fill=X, padx=25, pady=(20, 10))

        title = ttk.Label(
            header,
            text="📜 Recent Activity",
            font=("Helvetica", 14, "bold"),
            bootstyle="inverse-secondary"
        )
        title.pack(side=LEFT)

        view_all = ttk.Button(
            header,
            text="View All →",
            bootstyle="link",
        )
        view_all.pack(side=RIGHT)

        # Activity items
        activities = [
            ("Database backup completed", "2 minutes ago", "success"),
            ("New connection established", "15 minutes ago", "info"),
            ("Service 'Redis' restarted", "1 hour ago", "warning"),
            ("File cleanup performed", "3 hours ago", "primary"),
            ("System health check passed", "5 hours ago", "success"),
        ]

        for activity, time, style in activities:
            self.create_activity_item(activity_card, activity, time, style)

    def create_activity_item(self, parent, text, time, style):
        """Create a single activity item"""
        item_frame = ttk.Frame(parent, bootstyle="secondary")
        item_frame.pack(fill=X, padx=25, pady=8)

        # Status indicator
        indicator = ttk.Label(
            item_frame,
            text="●",
            font=("Helvetica", 16),
            bootstyle=style
        )
        indicator.pack(side=LEFT, padx=(0, 15))

        # Text container
        text_frame = ttk.Frame(item_frame, bootstyle="secondary")
        text_frame.pack(side=LEFT, fill=X, expand=YES)

        activity_label = ttk.Label(
            text_frame,
            text=text,
            font=("Helvetica", 11),
            bootstyle="inverse-secondary"
        )
        activity_label.pack(anchor=W)

        time_label = ttk.Label(
            text_frame,
            text=time,
            font=("Helvetica", 9),
            bootstyle="secondary"
        )
        time_label.pack(anchor=W)

    def create_system_status(self, parent):
        """Create system status panel"""
        status_card = ttk.Frame(parent, bootstyle="secondary")
        status_card.pack(side=LEFT, fill=BOTH, expand=YES, padx=(10, 0))

        # Header
        header = ttk.Frame(status_card, bootstyle="secondary")
        header.pack(fill=X, padx=25, pady=(20, 10))

        title = ttk.Label(
            header,
            text="💻 System Status",
            font=("Helvetica", 14, "bold"),
            bootstyle="inverse-secondary"
        )
        title.pack(side=LEFT)

        refresh_btn = ttk.Button(
            header,
            text="🔄 Refresh",
            bootstyle="link",
        )
        refresh_btn.pack(side=RIGHT)

        # System metrics
        metrics = [
            ("CPU Usage", "42%", 42, "info"),
            ("Memory Usage", "67%", 67, "warning"),
            ("Disk Usage", "34%", 34, "success"),
            ("Network I/O", "23%", 23, "primary"),
        ]

        for label, value, percent, style in metrics:
            self.create_metric_item(status_card, label, value, percent, style)

    def create_metric_item(self, parent, label, value, percent, style):
        """Create a single metric item with progress bar"""
        item_frame = ttk.Frame(parent, bootstyle="secondary")
        item_frame.pack(fill=X, padx=25, pady=10)

        # Label and value
        top_row = ttk.Frame(item_frame, bootstyle="secondary")
        top_row.pack(fill=X)

        label_widget = ttk.Label(
            top_row,
            text=label,
            font=("Helvetica", 11),
            bootstyle="inverse-secondary"
        )
        label_widget.pack(side=LEFT)

        value_widget = ttk.Label(
            top_row,
            text=value,
            font=("Helvetica", 11, "bold"),
            bootstyle=style
        )
        value_widget.pack(side=RIGHT)

        # Progress bar
        progress = ttk.Progressbar(
            item_frame,
            bootstyle=style,
            value=percent,
            length=200
        )
        progress.pack(fill=X, pady=(5, 0))


def main():
    """Main entry point"""
    root = ttk.Window(themename="darkly")
    app = ModernDashboard(root)
    root.mainloop()


if __name__ == "__main__":
    main()
