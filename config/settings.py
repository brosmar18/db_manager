"""
Application Settings
Global configuration and settings for the DB Manager application
"""

# Application metadata
APP_NAME = "DB Manager"
APP_VERSION = "1.0.0"
APP_SUBTITLE = "Professional"

# Window settings
WINDOW_TITLE = f"{APP_NAME} - Modern Dashboard"
WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 900
WINDOW_MIN_WIDTH = 1200
WINDOW_MIN_HEIGHT = 700

# Navigation structure
NAVIGATION = {
    'main': {
        'title': 'MAIN',
        'items': [
            {'icon': 'dashboard', 'label': 'Dashboard', 'style': 'primary'},
            {'icon': 'analytics', 'label': 'Analytics', 'style': 'info'},
            {'icon': 'settings', 'label': 'Settings', 'style': 'secondary'},
        ]
    },
    'database': {
        'title': 'DATABASE',
        'items': [
            {'icon': 'database', 'label': 'Postgres Manager', 'style': 'success'},
            {'icon': 'query', 'label': 'Query Builder', 'style': 'info'},
            {'icon': 'table', 'label': 'Tables & Schemas', 'style': 'primary'},
            {'icon': 'backup', 'label': 'Backups', 'style': 'warning'},
        ]
    },
    'files': {
        'title': 'FILE MANAGEMENT',
        'items': [
            {'icon': 'file', 'label': 'File Explorer', 'style': 'primary'},
            {'icon': 'organize', 'label': 'Organization Tools', 'style': 'info'},
            {'icon': 'search', 'label': 'Search Files', 'style': 'secondary'},
            {'icon': 'cleanup', 'label': 'Cleanup Utilities', 'style': 'warning'},
        ]
    },
    'services': {
        'title': 'SERVICES',
        'items': [
            {'icon': 'service', 'label': 'Service Manager', 'style': 'success'},
            {'icon': 'monitor', 'label': 'Monitoring', 'style': 'info'},
            {'icon': 'logs', 'label': 'Logs Viewer', 'style': 'secondary'},
            {'icon': 'alert', 'label': 'Alerts', 'style': 'danger'},
        ]
    }
}

# Dashboard statistics
DASHBOARD_STATS = [
    {
        'title': 'Database Connections',
        'value': '127',
        'style': 'success',
        'icon': 'database',
        'subtitle': '+12% from last week'
    },
    {
        'title': 'Active Services',
        'value': '8/10',
        'style': 'info',
        'icon': 'service',
        'subtitle': '2 services stopped'
    },
    {
        'title': 'Storage Used',
        'value': '234 GB',
        'style': 'warning',
        'icon': 'storage',
        'subtitle': '67% of total capacity'
    },
    {
        'title': 'System Uptime',
        'value': '15d 7h',
        'style': 'primary',
        'icon': 'time',
        'subtitle': 'Last restart: Jan 4'
    }
]

# Quick actions
QUICK_ACTIONS = [
    {'label': 'New Database Connection', 'style': 'primary', 'icon': 'connect'},
    {'label': 'Run Query', 'style': 'success', 'icon': 'run'},
    {'label': 'Backup Database', 'style': 'info', 'icon': 'storage'},
    {'label': 'Schedule Task', 'style': 'warning', 'icon': 'schedule'},
    {'label': 'View Logs', 'style': 'secondary', 'icon': 'logs'},
    {'label': 'System Scan', 'style': 'danger', 'icon': 'scan'},
]

# Recent activities (sample data)
RECENT_ACTIVITIES = [
    {'text': 'Database backup completed', 'time': '2 minutes ago', 'status': 'success'},
    {'text': 'New connection established', 'time': '15 minutes ago', 'status': 'info'},
    {'text': 'Service \'Redis\' restarted', 'time': '1 hour ago', 'status': 'warning'},
    {'text': 'File cleanup performed', 'time': '3 hours ago', 'status': 'primary'},
    {'text': 'System health check passed', 'time': '5 hours ago', 'status': 'success'},
]

# System metrics (sample data)
SYSTEM_METRICS = [
    {'label': 'CPU Usage', 'value': '42%', 'percent': 42, 'style': 'info'},
    {'label': 'Memory Usage', 'value': '67%', 'percent': 67, 'style': 'warning'},
    {'label': 'Disk Usage', 'value': '34%', 'percent': 34, 'style': 'success'},
    {'label': 'Network I/O', 'value': '23%', 'percent': 23, 'style': 'primary'},
]

# User information
USER_INFO = {
    'name': 'Administrator',
    'role': 'System Admin',
    'avatar': '👤',
}

# Feature flags
FEATURES = {
    'show_welcome_banner': True,
    'show_stats_cards': True,
    'show_quick_actions': True,
    'show_recent_activity': True,
    'show_system_status': True,
    'enable_animations': True,
    'enable_tooltips': True,
}
