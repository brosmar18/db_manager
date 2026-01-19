"""
Main Application Class
Orchestrates all components and manages the application window
"""

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from config.theme import get_theme_name, get_size
from config.settings import WINDOW_TITLE, WINDOW_WIDTH, WINDOW_HEIGHT
from ui.components.sidebar import Sidebar
from ui.components.header import Header
from ui.components.dashboard import DashboardContent


class DBManagerApp:
    """Main application class"""

    def __init__(self, root):
        self.root = root
        self.root.title(WINDOW_TITLE)
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

        # Set minimum window size for better UX
        self.root.minsize(1200, 700)

        # Current active view
        self.active_view = "Dashboard"

        self.setup_ui()

    def setup_ui(self):
        """Setup the main application UI"""
        # Main container
        main_container = ttk.Frame(self.root)
        main_container.pack(fill=BOTH, expand=YES)

        # Sidebar
        self.sidebar = Sidebar(main_container, on_nav_click=self.handle_navigation)
        self.sidebar.pack(side=LEFT, fill=Y)

        # Right panel (header + content)
        right_panel = ttk.Frame(main_container)
        right_panel.pack(side=LEFT, fill=BOTH, expand=YES)

        # Header
        self.header = Header(right_panel)
        self.header.pack(fill=X)

        # Content area container
        self.content_container = ttk.Frame(right_panel)
        self.content_container.pack(fill=BOTH, expand=YES, padx=20, pady=20)

        # Load initial view
        self.load_dashboard()

    def handle_navigation(self, view_name):
        """Handle navigation between different views"""
        self.active_view = view_name
        print(f"Navigating to: {view_name}")

        # Clear current content
        for widget in self.content_container.winfo_children():
            widget.destroy()

        # Load appropriate view based on navigation
        if view_name == "Dashboard":
            self.load_dashboard()
        elif view_name == "Analytics":
            self.load_analytics()
        elif view_name == "Settings":
            self.load_settings()
        elif view_name == "Postgres Manager":
            self.load_postgres_manager()
        elif view_name == "Query Builder":
            self.load_query_builder()
        elif view_name == "Tables & Schemas":
            self.load_tables_schemas()
        elif view_name == "Backups":
            self.load_backups()
        elif view_name == "File Explorer":
            self.load_file_explorer()
        elif view_name == "Organization Tools":
            self.load_organization_tools()
        elif view_name == "Search Files":
            self.load_search_files()
        elif view_name == "Cleanup Utilities":
            self.load_cleanup_utilities()
        elif view_name == "Service Manager":
            self.load_service_manager()
        elif view_name == "Monitoring":
            self.load_monitoring()
        elif view_name == "Logs Viewer":
            self.load_logs_viewer()
        elif view_name == "Alerts":
            self.load_alerts()
        else:
            self.load_placeholder(view_name)

    def load_dashboard(self):
        """Load the dashboard view"""
        dashboard = DashboardContent(self.content_container)
        dashboard.pack(fill=BOTH, expand=YES)

    def load_analytics(self):
        """Load analytics view"""
        self.load_placeholder("Analytics")

    def load_settings(self):
        """Load settings view"""
        self.load_placeholder("Settings")

    def load_postgres_manager(self):
        """Load Postgres Manager view"""
        self.load_placeholder("Postgres Manager")

    def load_query_builder(self):
        """Load Query Builder view"""
        self.load_placeholder("Query Builder")

    def load_tables_schemas(self):
        """Load Tables & Schemas view"""
        self.load_placeholder("Tables & Schemas")

    def load_backups(self):
        """Load Backups view"""
        self.load_placeholder("Backups")

    def load_file_explorer(self):
        """Load File Explorer view"""
        self.load_placeholder("File Explorer")

    def load_organization_tools(self):
        """Load Organization Tools view"""
        self.load_placeholder("Organization Tools")

    def load_search_files(self):
        """Load Search Files view"""
        self.load_placeholder("Search Files")

    def load_cleanup_utilities(self):
        """Load Cleanup Utilities view"""
        self.load_placeholder("Cleanup Utilities")

    def load_service_manager(self):
        """Load Service Manager view"""
        self.load_placeholder("Service Manager")

    def load_monitoring(self):
        """Load Monitoring view"""
        self.load_placeholder("Monitoring")

    def load_logs_viewer(self):
        """Load Logs Viewer view"""
        self.load_placeholder("Logs Viewer")

    def load_alerts(self):
        """Load Alerts view"""
        self.load_placeholder("Alerts")

    def load_placeholder(self, view_name):
        """Load a placeholder view for未实现的功能"""
        placeholder_frame = ttk.Frame(self.content_container)
        placeholder_frame.pack(fill=BOTH, expand=YES)

        # Center the content
        center_frame = ttk.Frame(placeholder_frame)
        center_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Icon
        icon_label = ttk.Label(
            center_frame,
            text="🚧",
            font=('Segoe UI', 72)
        )
        icon_label.pack(pady=20)

        # Title
        title_label = ttk.Label(
            center_frame,
            text=f"{view_name}",
            font=('Segoe UI', 24, 'bold')
        )
        title_label.pack()

        # Subtitle
        subtitle_label = ttk.Label(
            center_frame,
            text="This feature is coming soon!",
            font=('Segoe UI', 14),
            bootstyle='secondary'
        )
        subtitle_label.pack(pady=10)

        # Description
        desc_label = ttk.Label(
            center_frame,
            text="We're working hard to bring you this functionality.\nStay tuned for updates!",
            font=('Segoe UI', 11),
            bootstyle='secondary',
            justify=CENTER
        )
        desc_label.pack(pady=10)

        # Back to Dashboard button
        back_btn = ttk.Button(
            center_frame,
            text="← Back to Dashboard",
            bootstyle='primary',
            command=lambda: self.handle_navigation("Dashboard"),
            width=20
        )
        back_btn.pack(pady=20)
