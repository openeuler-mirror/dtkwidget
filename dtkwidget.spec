Name:           dtkwidget
Version:        5.4.11.3
Release:        2
Summary:        Deepin tool kit widget modules
License:        LGPLv3+
URL:            https://github.com/linuxdeepin/dtkwidget
%if 0%{?fedora}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
%else
Source0:        %{name}_%{version}.orig.tar.xz
%endif

BuildRequires:  gcc-c++
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-static
BuildRequires:  dtkgui-devel
BuildRequires:  dtkcore-devel
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(dframeworkdbus)
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  cups-devel
BuildRequires:  gtest-devel

# libQt5Gui.so.5(Qt_5.10.1_PRIVATE_API)(64bit) needed by dtkwidget-2.0.6.1-1.fc29.x86_64
BuildRequires:  qt5-qtbase-private-devel
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}

Obsoletes:      dtkwidget2
%description
DtkWidget is Deepin graphical user interface for deepin desktop development.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       dtkcore-devel%{?_isa}
Requires:       dtkgui-devel%{?_isa}

%description devel
Header files and libraries for %{name}.

%prep
%setup -q

%build
export PATH=%{_qt5_bindir}:$PATH
%qmake_qt5 PREFIX=%{_prefix} LIB_INSTALL_DIR=%{_libdir} DBUS_VERSION_0_4_2=YES
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%doc README.md
%license LICENSE
%{_libdir}/lib%{name}.so.5*
%{_libdir}/libdtk-*/
%{_datadir}/libdtk-*/

%files devel
%{_includedir}/libdtk-*/
%{_qt5_archdatadir}/mkspecs/modules/*.pri
%{_libdir}/cmake/DtkWidget/
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/lib%{name}.so

%changelog
* Thu Jul 28 2022 liweiganga <liweiganga@uniontech.com> - 5.4.11.3-2
- fix install conflict

* Tue Jul 19 2022 konglidong <konglidong@uniontech.com> - 5.4.11.3-1
- Update to 5.4.11.3

* Thu Jul 15 2021 weidong <weidong@uniontech.com> - 5.2.2.3-2
- Format spec

* Mon Jul 12 2021 weidong <weidong@uniontech.com> - 5.2.2.3-1
- Update to 5.2.2.3

* Thu Sep 3 2020 weidong <weidong@uniontech.com> - 5.2.0-2
- fix source url in spec

* Thu Jul 30 2020 openEuler Buildteam <buildteam@openeuler.org> - 5.2.0-1
- Package init
