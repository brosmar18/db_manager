#!/usr/bin/env python3
"""
DB Manager - Main Entry Point
A modern, professional dashboard for database management, file organization, and service management
"""

import ttkbootstrap as ttk
from config.theme import get_theme_name
from ui.app import DBManagerApp


def main():
    """Main entry point for the application"""
    # Create the root window with the configured theme
    root = ttk.Window(themename=get_theme_name())

    # Initialize the application
    app = DBManagerApp(root)

    # Start the event loop
    root.mainloop()


if __name__ == "__main__":
    main()
