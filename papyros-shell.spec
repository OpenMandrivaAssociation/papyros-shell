%define debug_package %nil
%define snap 20150709

Summary:	Papyros desktop shell
Name:		papyros-shell
Version:	0.0.5
Release:	1.%{snap}.1
License:	GPLv2
Group:		Graphical desktop/Other
URL:		https://github.com/papyros/papyros-shell
# git clone https://github.com/papyros/papyros-shell.git
# git archive --format=tar --prefix papyros-shell-0.0.5-$(date +%Y%m%d)/ HEAD | xz -vf > papyros-shell-0.0.5-$(date +%Y%m%d).tar.xz

Source0:	%{name}-%{version}-%{snap}.tar.xz
BuildRequires:	qt5-devel
BuildRequires:	pkgconfig(Qt5Compositor)
BuildRequires:	pkgconfig(gsettings-qt)
BuildRequires:	extra-cmake-modules5
BuildRequires:	cmake(qt5xdg)
BuildRequires:	pam-devel
BuildRequires:	cmake(GreenIsland)
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	cmake(KF5NetworkManagerQt)
BuildRequires:	cmake(PulseAudio)
BuildRequires:	cmake(KF5ModemManagerQt)
Requires:	qml-material >= 0.0.6
Requires:	qml-extras >= 0.0.5
Requires:	qml-desktop >= 0.0.5
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

%package	sddm-theme	
Summary:	%{name}-sddm-theme
Group:		Graphical desktop/Other

%description	sddm-theme
sddm theme for %{name}

%prep
%setup -qn %{name}-%{version}-%{snap}

%build
# https://github.com/papyros/papyros-shell/issues/140
sed -i 's!-Werror!!g' CMakeLists.txt
%cmake_qt5
%make

%install
%makeinstall_std -C build INSTALL_ROOT=%{buildroot}

%files
%{_bindir}/papyros-session
%{_libdir}/qml/GreenIsland/Desktop/
%{_libdir}/qml/Papyros/Components/
%{_libdir}/qml/Papyros/Desktop/
%{_libdir}/qml/Papyros/Indicators/
%{_libdir}/qml/Papyros/Network
%{_datadir}/wayland-sessions/papyros.desktop
%{_datadir}/greenisland/shells/io.papyros.shell/
%{_datadir}/papyros-shell/eglfs/eglfs_kms.json

%files sddm-theme
%{_datadir}/sddm/themes/papyros/
