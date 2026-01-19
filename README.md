# DB Manager - Modern Dashboard Application

A beautiful, professional dashboard application built with Python and ttkbootstrap for managing databases, organizing files, and monitoring services.

## Features

### 🎨 Modern UI Design
- Dark theme with professional color scheme
- Responsive layout with sidebar navigation
- Beautiful card-based interface
- Smooth transitions and modern styling

### 📊 Dashboard Overview
- **Welcome Banner** - Personalized greeting with system status
- **Statistics Cards** - Real-time metrics for:
  - Database Connections (127 active)
  - Active Services (8/10 running)
  - Storage Usage (234 GB used)
  - System Uptime (15d 7h)

### 🧭 Navigation Sections

#### Main
- 🏠 Dashboard - Overview and statistics
- 📊 Analytics - Data visualization and reports
- ⚙️ Settings - Configuration and preferences

#### Database Management
- 🗄️ Postgres Manager - Connection and database management
- 🔍 Query Builder - Visual SQL query builder
- 📋 Tables & Schemas - Database structure explorer
- 🔄 Backups - Automated backup management

#### File Management
- 📁 File Explorer - Browse and manage files
- 🗂️ Organization Tools - File categorization and cleanup
- 🔎 Search Files - Advanced file search
- ♻️ Cleanup Utilities - Disk space optimization

#### Services
- 🚀 Service Manager - Start/stop/restart services
- 📈 Monitoring - Real-time service monitoring
- 📝 Logs Viewer - Centralized log management
- 🔔 Alerts - Notification and alert system

### ⚡ Quick Actions
- New Database Connection
- Run Query
- Backup Database
- Schedule Task
- View Logs
- System Scan

### 📜 Recent Activity
Live feed of system activities with timestamps and status indicators

### 💻 System Status
Real-time monitoring with progress bars for:
- CPU Usage (42%)
- Memory Usage (67%)
- Disk Usage (34%)
- Network I/O (23%)

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the application:
```bash
python3 main.py
```

## Requirements

- Python 3.11+
- ttkbootstrap (latest version)
- Pillow (latest version)
- tkinter (python3-tk)

## Project Structure

```
db_manager/
├── main.py                 # Application entry point
├── requirements.txt        # Python dependencies
├── config/                 # Configuration modules
│   ├── __init__.py
│   ├── theme.py           # Theme colors, fonts, and styling
│   └── settings.py        # Application settings and data
├── ui/                     # User interface modules
│   ├── __init__.py
│   ├── app.py             # Main application class
│   ├── components/        # Large UI components
│   │   ├── __init__.py
│   │   ├── sidebar.py     # Navigation sidebar
│   │   ├── header.py      # Top header bar
│   │   └── dashboard.py   # Dashboard content
│   └── widgets/           # Reusable UI widgets
│       ├── __init__.py
│       ├── stat_card.py   # Statistics card widget
│       ├── activity_item.py  # Activity log item
│       └── metric_item.py    # System metric widget
└── utils/                  # Utility functions
    └── __init__.py
```

## Architecture

The application follows a modular, scalable architecture with clear separation of concerns:

### Configuration Layer (`config/`)
- `theme.py` - Centralized theme management (colors, fonts, icons, spacing)
- `settings.py` - Application configuration and static data

### UI Layer (`ui/`)
- `app.py` - Main application orchestrator
- `components/` - Large, complex UI components (sidebar, header, dashboard)
- `widgets/` - Small, reusable UI widgets (cards, items, metrics)

### Benefits
- **Maintainability** - Each component has a single responsibility
- **Scalability** - Easy to add new features and components
- **Reusability** - Widgets can be used across different views
- **Testability** - Components can be tested independently
- **Readability** - Clear structure makes code easy to understand

## Design Philosophy

This application follows modern UI/UX principles with Flatly's flat design aesthetic:
- **Flat Design** - No shadows, gradients, or 3D effects for a modern look
- **Clean Layout** - Uncluttered interface with clear visual hierarchy
- **Consistent Design** - Uniform styling across all components
- **Intuitive Navigation** - Easy-to-find features with clear labeling
- **Responsive Feedback** - Visual indicators for all interactions
- **Professional Aesthetics** - Color-coded elements for quick identification
- **High Visibility** - Flatly theme with excellent contrast and readability
- **Modular Architecture** - Separation of concerns for maintainability

## Future Development

The current version focuses on the UI/UX design and layout. Future updates will include:
- Database connection functionality
- File management operations
- Service control features
- Real-time monitoring integration
- User authentication
- Settings persistence
- Plugin system for extensions

## Technology Stack

- **Framework**: ttkbootstrap (Bootstrap-themed tkinter)
- **Language**: Python 3.11
- **Theme**: Flatly (Flat, modern design from Bootswatch)
- **Layout**: Component-based with responsive packing
- **Architecture**: MVC-inspired with separation of concerns

## Color Scheme

The application uses the **Flatly theme** from Bootswatch - a flat, modern design with excellent readability:

- **Primary**: #2C3E50 (Dark Blue-Gray/Navy)
- **Success**: #18BC9C (Turquoise/Teal)
- **Warning**: #F39C12 (Orange)
- **Danger**: #E74C3C (Red)
- **Info**: #3498DB (Bright Blue)
- **Secondary**: #95A5A6 (Gray)
- **Background**: #ECF0F1 (Light Gray)
- **Text**: #2C3E50 (Dark Blue-Gray)

### Design Characteristics
- **Flat Design**: No shadows or gradients, clean and modern
- **Sharp Aesthetics**: Subtle rounded corners (4px)
- **High Contrast**: Excellent readability with vibrant colors
- **Professional**: Business-ready appearance

## License

This project is ready for commercial use and modern application standards.
