%define major 5
%define libname %mklibname KF5I18n %{major}
%define devname %mklibname KF5I18n -d
%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

Name: ki18n
Version: 5.116.0
Release: 2
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
Summary: The KDE Frameworks 5 internationalization framework
URL: https://kde.org/
License: GPL
Group: System/Libraries
# (tpg) read extra translations from mandriva-kde-translation
Patch0: ki18n-5.9.0-extra-catalog.patch
BuildRequires: cmake(ECM)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Script)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: pkgconfig(iso-codes)
BuildRequires: gettext
Obsoletes: python-%{name} < %{EVRD}
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt5-assistant
Requires: %{libname} = %{EVRD}
Requires: openmandriva-kde-translation

%description
KDE Frameworks 5 internationalization framework.

%package -n %{libname}
Summary: The KDE Frameworks 5 internationalization library
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
KDE Frameworks 5 internationalization Library.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}
Requires: gettext

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%{name} is the KDE Frameworks 5 internationalization library.

%package -n %{name}-devel-docs
Summary: Developer documentation for %{name} for use with Qt Assistant
Group: Documentation
Suggests: %{devname} = %{EVRD}

%description -n %{name}-devel-docs
Developer documentation for %{name} for use with Qt Assistant.

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang ki18n%{major}

%files -f ki18n%{major}.lang
%{_datadir}/qlogging-categories5/*
%{_libdir}/qt5/plugins/kf5/ktranscript.so
%lang(ca) %{_datadir}/locale/ca/LC_SCRIPTS
%lang(ca@valencia) %{_datadir}/locale/ca@valencia/LC_SCRIPTS
%lang(fi) %{_datadir}/locale/fi/LC_SCRIPTS
%lang(gd) %{_datadir}/locale/gd/LC_SCRIPTS
%lang(ja) %{_datadir}/locale/ja/LC_SCRIPTS
%lang(ru) %{_datadir}/locale/ru/LC_SCRIPTS
%lang(sr) %{_datadir}/locale/sr/LC_SCRIPTS
%lang(sr) %{_datadir}/locale/sr@ijekavian/LC_SCRIPTS
%lang(sr) %{_datadir}/locale/sr@ijekavianlatin/LC_SCRIPTS
%lang(sr) %{_datadir}/locale/sr@latin/LC_SCRIPTS
%lang(uk) %{_datadir}/locale/uk/LC_SCRIPTS
%lang(ko) %{_datadir}/locale/ko/LC_SCRIPTS
%lang(nb) %{_datadir}/locale/nb/LC_SCRIPTS
%lang(nn) %{_datadir}/locale/nn/LC_SCRIPTS

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%(echo %{version}|cut -d. -f1-2)*
%{_libdir}/qt5/qml/org/kde/i18n

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5I18n
%{_libdir}/qt5/mkspecs/modules/*

%files -n %{name}-devel-docs
%{_docdir}/qt5/*.{tags,qch}
