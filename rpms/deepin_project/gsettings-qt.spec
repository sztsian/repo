%global project ~system-settings-touch
%global _revision 83

# for fedora 24
# %%global _qt5_qmldir %%{_qt5_archdatadir}/qml
%global __provides_exclude ^libGSettingsQmlPlugin\\.so.*$

Name:           gsettings-qt
Version:        0
Release:        0.0.20170715bzr%{_revision}%{?dist}
Summary:        Qt/QML bindings for GSettings
License:        LGPLv3
URL:            https://launchpad.net/gsettings-qt
Source0:        http://bazaar.launchpad.net/%{project}/%{name}/trunk/tarball/%{_revision}#/%{name}-%{_revision}.tar.gz
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  glib2-devel
BuildRequires:  gcc-c++
#Do not build on big endian architectures as it has bug there
ExcludeArch:    s390x ppc64

%description
Qt/QML bindings for GSettings

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel%{?isa}

%description devel
Header files and libraries for %{name}

%prep
%setup -q -n %{project}/%{name}/trunk

%build
%qmake_qt5 PREFIX=%{_prefix}
# Parallel build not supported. It causes error when linking
make

%install
%make_install INSTALL_ROOT=%{buildroot}

# remove test
rm -rf %{buildroot}%{_libdir}/qt5/tests

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_libdir}/lib%{name}.so.*
%license COPYING
%dir %{_qt5_qmldir}/GSettings.1.0/
%{_qt5_qmldir}/GSettings.1.0/libGSettingsQmlPlugin.so
%{_qt5_qmldir}/GSettings.1.0/plugins.qmltypes
%{_qt5_qmldir}/GSettings.1.0/qmldir

%files devel
%license COPYING
%dir %{_qt5_headerdir}/QGSettings/
%{_qt5_headerdir}/QGSettings/*
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/lib%{name}.so

%changelog
* Sat Jul 15 2017 Zamir SUN <zsun@fedoraproject.org> - 0-0.0.20170715r83
- Update to bzr r83 and change the versioning style

* Tue Jan 17 2017 mosquito <sensor.wen@gmail.com> - 0.1.20160329-1-1
- Update to 0.1.20160329

* Tue Jan 03 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 0.1.20160329-2
- Major rewrite of SPEC file

* Sun Oct 02 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 0.1.20160329-1
- Initial package build

