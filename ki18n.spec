%define major 5
%define libname %mklibname KF5I18n %{major}
%define devname %mklibname KF5I18n -d
%define debug_package %{nil}

Name: ki18n
Version: 5.2.0
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/stable/frameworks/%{version}/%{name}-%{version}.tar.xz
Summary: The KDE Frameworks 5 internationalization framework
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
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
%cmake

%build
%make -C build

%install
%makeinstall_std -C build
mkdir -p %{buildroot}%{_libdir}/qt5
mv %{buildroot}%{_prefix}/mkspecs %{buildroot}%{_libdir}/qt5
%find_lang ki18n%{major}

%files -f ki18n%{major}.lang
%{_libdir}/plugins/kf5/ktranscript.so
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
