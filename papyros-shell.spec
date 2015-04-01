%define debug_package %nil
%define snap	20150401

Summary:	Papyros desktop shell
Name:		papyros-shell
Version:	0.0.0
Release:	0.%{snap}.1
License:	GPLv2
Group:		Graphical desktop/Other
URL:		https://github.com/papyros/papyros-shell
# git clone https://github.com/papyros/papyros-shell.git
# git archive --format=tar --prefix papyros-shell-0.0.0-$(date +%Y%m%d)/ HEAD | xz -vf > papyros-shell-0.0.0-$(date +%Y%m%d).tar.xz

Source0:	%{name}-%{version}-%{snap}.tar.xz
BuildRequires:	qt5-devel
BuildRequires:	pkgconfig(Qt5Compositor)
BuildRequires:	pkgconfig(gsettings-qt)
Requires:	qml-material
Requires:	qml-extras
Requires:	qml-desktop
Requires:	gsettings-qt
Requires:	files-app
Requires:	qt5-qtdeclarative
Requires:	qt5-qtgraphicaleffects
Requires:	qt5-qtquickcontrols
Requires:	%{_lib}qt5gui5-eglfs
Requires:	%{_lib}qt5gui5-x11
%rename		quantum-shell

%description
Papyros Shell is the desktop shell which conforms
to Google's Material Design guidelines.
The focus will be on creating a stable and
easy-to-use operating system with a heavy
emphasis on well-thought-out design.

%prep
%setup -qn %{name}-%{version}-%{snap}

%build
./qrc.py qml images > papyros-shell.qrc
%qmake_qt5 *.pro
%make

%install
%makeinstall_std INSTALL_ROOT=%{buildroot}

%files
%{_bindir}/papyros-shell
%{_bindir}/papyros-session
%{_datadir}/wayland-sessions/papyros.desktop
