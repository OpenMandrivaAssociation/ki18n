%define major 5
%define libname %mklibname KF5I18n %{major}
%define devname %mklibname KF5I18n -d
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: ki18n
Version: 5.4.0
Release: 2
Source0: http://ftp5.gwdg.de/pub/linux/kde/%{stable}/frameworks/%{version}/%{name}-%{version}.tar.xz
Summary: The KDE Frameworks 5 internationalization framework
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: ninja
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: qmake5
BuildRequires: extra-cmake-modules5
Requires: %{libname} = %{EVRD}

%description
KDE Frameworks 5 internationalization framework

%package -n %{libname}
Summary: The KDE Frameworks 5 internationalization library
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
KDE Frameworks 5 internationalization Library

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%{name} is the KDE Frameworks 5 internationalization library.

%prep
%setup -q
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja install -C build
%find_lang ki18n%{major}

%files -f ki18n%{major}.lang
%{_libdir}/qt5/plugins/kf5/ktranscript.so
%lang(fi) %{_datadir}/locale/fi/LC_SCRIPTS
%lang(sr) %{_datadir}/locale/sr/LC_SCRIPTS
%lang(sr) %{_datadir}/locale/sr@ijekavian/LC_SCRIPTS
%lang(sr) %{_datadir}/locale/sr@ijekavianlatin/LC_SCRIPTS
%lang(sr) %{_datadir}/locale/sr@latin/LC_SCRIPTS

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5I18n
%{_libdir}/qt5/mkspecs/modules/*
