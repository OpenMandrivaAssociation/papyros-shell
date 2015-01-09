%define debug_package %nil
%define snap 20150109

Summary:	Quantum desktop shell
Name:		quantum-shell
Version:	0.0.0
Release:	0.%{snap}.1
License:	GPLv2
Group:		Graphical desktop/Other
URL:		https://github.com/quantum-os/quantum-shell
Source0:	%{name}-%{version}-%{snap}.tar.xz
BuildRequires:	qt5-devel
BuildRequires:	pkgconfig(Qt5Compositor)
Requires:	qml-material
Requires:	qml-extras
Requires:	qt5-qtdeclarative
Requires:	qt5-qtgraphicaleffects

%description
Quantum Shell is the desktop shell which conforms
to Google's Material Design guidelines.
The focus will be on creating a stable and
easy-to-use operating system with a heavy
emphasis on well-thought-out design.

%prep
%setup -qn %{name}-%{version}-%{snap}

%build
%qmake_qt5 *.pro
%make

%install
%makeinstall_std INSTALL_ROOT=%{buildroot}

%files
%{_bindir}/quantum-shell
