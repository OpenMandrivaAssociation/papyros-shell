%define snap 20141207

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

%description
Quantum Shell is the desktop shell which conforms
to Google’s Material Design guidelines.
The focus will be on creating a stable and
easy-to-use operating system with a heavy
emphasis on well-thought-out design.

%prep
%setup -qc

%build
%qmake_qt5
%make

%install
%makeinstall_std

%files
