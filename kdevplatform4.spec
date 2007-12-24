%define revision 752241

%define use_enable_final 1
%{?_no_enable_final: %{expand: %%global use_enable_final 0}}

%define compile_apidox 0
%{?_no_apidox: %{expand: %%global compile_apidox 0}}

%define unstable 1
%{?_unstable: %{expand: %%global unstable 1}}

%define branch 1
%{?_branch: %{expand: %%global branch 1}}

%define use_enable_pie 1
%{?_no_enable_pie: %{expand: %%global use_enable_pie 0}}

%if %unstable
%define dont_strip 1
%endif

%define lib_name_orig libkdevplatform4
%define lib_major 4
%define lib_name %mklibname kdevplatform %lib_major
%define old_lib_major 2
%define old_lib_name %mklibname kdevplatform4 %old_lib_major

Name: 		kdevplatform4
Summary: 	Integrated Development Environment for C++/C
Version: 	3.97.1
Epoch:          3
URL:            http://www.kde.org 
%if %branch
Release:        %mkrel 0.%revision.2
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdevplatform-%version.%revision.tar.bz2
%else
Release:        %mkrel 1
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdevplatform-%version.tar.bz2
%endif
Group: 		Development/C++
License: GPL
BuildRequires: kdelibs4-devel 
BuildRequires: flex
BuildRequires: graphviz
BuildRequires: db-devel
BuildRequires: subversion-devel
BuildRequires: apr-devel
BuildRequires: apr-util-devel
%if %compile_apidox
BuildRequires: doxygen
%endif
%py_requires -d
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
Obsoletes:      kdevelop4 < 3.93
%description
%name module needed by Kdevelop or Quanta

%files
%defattr(-,root,root) 
%_kde_appsdir/kdevprojectmanagerview/kdevprojectmanagerview.rc
%_kde_appsdir/kdevstandardoutputview/kdevstandardoutputview.rc
%_kde_appsdir/kdevduchainview/kdevduchainview.rc
%_kde_appsdir/kdevfilemanager/kdevfilemanager.rc
%_kde_appsdir/kdevclassbrowser/kdevclassbrowser.rc
%_kde_appsdir/kdevcvs/kdevcvs.rc
%_kde_appsdir/kdevquickopen/kdevquickopen.rc
%_kde_appsdir/kdevproblemreporter/kdevproblemreporter.rc
%_kde_datadir/kde4/services/kdevclassbrowser.desktop
%_kde_datadir/kde4/services/kdevquickopen.desktop
%_kde_datadir/kde4/services/kcm_kdev_uisettings.desktop
%_kde_datadir/kde4/services/kdevduchainview.desktop
%_kde_datadir/kde4/services/kdevfilemanager.desktop
%_kde_datadir/kde4/services/kdevgenericmanager.desktop
%_kde_datadir/kde4/services/kdevkonsoleview.desktop
%_kde_datadir/kde4/services/kdevprojectmanagerview.desktop
%_kde_datadir/kde4/services/kdevsnippet.desktop
%_kde_datadir/kde4/services/kdevstandardoutputview.desktop
%_kde_datadir/kde4/servicetypes/kdevelopplugin.desktop
%_kde_datadir/kde4/services/kcm_kdev_envsettings.desktop
%_kde_datadir/kde4/services/kcm_kdev_bgsettings.desktop
%_kde_datadir/kde4/services/kcm_kdev_ccsettings.desktop
%_kde_datadir/kde4/services/kcm_kdev_projectsettings.desktop
%_kde_datadir/kde4/services/kdevproblemreporter.desktop
%_kde_datadir/kde4/services/kdevcvs.desktop
%_kde_datadir/kde4/services/kcm_kdev_runsettings.desktop
%_kde_datadir/kde4/services/kdevexecute.desktop
%_kde_datadir/kde4/services/kdevusehighlight.desktop
%_kde_libdir/kde4/kdevusehighlight.so
%_kde_libdir/kde4/kcm_kdev_runsettings.so
%_kde_libdir/kde4/kdevexecute.so
%_kde_libdir/kde4/kcm_kdev_uisettings.so
%_kde_libdir/kde4/kdevduchainview.so
%_kde_libdir/kde4/kdevfilemanager.so
%_kde_libdir/kde4/kdevgenericmanager.so
%_kde_libdir/kde4/kdevkonsoleview.so
%_kde_libdir/kde4/kdevprojectmanagerview.so
%_kde_libdir/kde4/kdevsnippet.so
%_kde_libdir/kde4/kdevstandardoutputview.so
%_kde_libdir/kde4/kcm_kdev_envsettings.so
%_kde_libdir/kde4/kdevcvs.so
%_kde_libdir/kde4/kdevquickopen.so
%_kde_libdir/kde4/kdevclassbrowser.so
%_kde_libdir/kde4/kcm_kdev_bgsettings.so
%_kde_libdir/kde4/kcm_kdev_ccsettings.so
%_kde_libdir/kde4/kcm_kdev_projectsettings.so
%_kde_libdir/kde4/kdevproblemreporter.so

#-----------------------------------------------------------------------------

%define libkdevplatformeditor %mklibname kdevplatformeditor 4

%package -n %libkdevplatformeditor
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkdevplatformeditor
KDE 4 library.

%post -n %libkdevplatformeditor -p /sbin/ldconfig
%postun -n %libkdevplatformeditor -p /sbin/ldconfig

%files -n %libkdevplatformeditor
%defattr(-,root,root)
%_kde_libdir/libkdevplatformeditor.so.*

#-----------------------------------------------------------------------------

%define libkdevplatforminterfaces %mklibname kdevplatforminterfaces 4

%package -n %libkdevplatforminterfaces
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkdevplatforminterfaces
KDE 4 library.

%post -n %libkdevplatforminterfaces -p /sbin/ldconfig
%postun -n %libkdevplatforminterfaces -p /sbin/ldconfig

%files -n %libkdevplatforminterfaces
%defattr(-,root,root)
%_kde_libdir/libkdevplatforminterfaces.so.*

#-----------------------------------------------------------------------------

%define libkdevplatformlanguage %mklibname kdevplatformlanguage 4

%package -n %libkdevplatformlanguage
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkdevplatformlanguage
KDE 4 library.

%post -n %libkdevplatformlanguage -p /sbin/ldconfig
%postun -n %libkdevplatformlanguage -p /sbin/ldconfig

%files -n %libkdevplatformlanguage
%defattr(-,root,root)
%_kde_libdir/libkdevplatformlanguage.so.*

#-----------------------------------------------------------------------------

%define libkdevplatformoutputview %mklibname kdevplatformoutputview 4

%package -n %libkdevplatformoutputview
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkdevplatformoutputview
KDE 4 library.

%post -n %libkdevplatformoutputview -p /sbin/ldconfig
%postun -n %libkdevplatformoutputview -p /sbin/ldconfig

%files -n %libkdevplatformoutputview
%defattr(-,root,root)
%_kde_libdir/libkdevplatformoutputview.so.*

#-----------------------------------------------------------------------------

%define libkdevplatformproject %mklibname kdevplatformproject 4

%package -n %libkdevplatformproject
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkdevplatformproject
KDE 4 library.

%post -n %libkdevplatformproject -p /sbin/ldconfig
%postun -n %libkdevplatformproject -p /sbin/ldconfig

%files -n %libkdevplatformproject
%defattr(-,root,root)
%_kde_libdir/libkdevplatformproject.so.*

#-----------------------------------------------------------------------------

%define libkdevplatformshell %mklibname kdevplatformshell 4

%package -n %libkdevplatformshell
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkdevplatformshell
KDE 4 library.

%post -n %libkdevplatformshell -p /sbin/ldconfig
%postun -n %libkdevplatformshell -p /sbin/ldconfig

%files -n %libkdevplatformshell
%defattr(-,root,root)
%_kde_libdir/libkdevplatformshell.so.*

#-----------------------------------------------------------------------------

%define libkdevplatformutil %mklibname kdevplatformutil 4

%package -n %libkdevplatformutil
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkdevplatformutil
KDE 4 library.

%post -n %libkdevplatformutil -p /sbin/ldconfig
%postun -n %libkdevplatformutil -p /sbin/ldconfig

%files -n %libkdevplatformutil
%defattr(-,root,root)
%_kde_libdir/libkdevplatformutil.so.*

#-----------------------------------------------------------------------------

%define libkdevplatformvcs %mklibname kdevplatformvcs 4

%package -n %libkdevplatformvcs
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkdevplatformvcs
KDE 4 library.

%post -n %libkdevplatformvcs -p /sbin/ldconfig
%postun -n %libkdevplatformvcs -p /sbin/ldconfig

%files -n %libkdevplatformvcs
%defattr(-,root,root)
%_kde_libdir/libkdevplatformvcs.so.*

#-----------------------------------------------------------------------------

%define libsublime %mklibname sublime 4

%package -n %libsublime
Summary: KDE 4 library
Group: System/Libraries

%description -n %libsublime
KDE 4 library.

%post -n %libsublime -p /sbin/ldconfig
%postun -n %libsublime -p /sbin/ldconfig

%files -n %libsublime
%defattr(-,root,root)
%_kde_libdir/libsublime.so.*

#-----------------------------------------------------------------------------

%package -n %lib_name-devel
Summary: Development files for kdevplatform
Group: Development/KDE and Qt

Provides: kdevplatform4-devel = %epoch:%version-%release

Requires: %libkdevplatformeditor = %epoch:%version-%release
Requires: %libkdevplatforminterfaces = %epoch:%version-%release
Requires: %libkdevplatformlanguage = %epoch:%version-%release
Requires: %libkdevplatformoutputview = %epoch:%version-%release
Requires: %libkdevplatformproject = %epoch:%version-%release
Requires: %libkdevplatformshell = %epoch:%version-%release
Requires: %libkdevplatformutil = %epoch:%version-%release
Requires: %libkdevplatformvcs = %epoch:%version-%release
Requires: %libsublime = %epoch:%version-%release

%description -n %lib_name-devel
Development files for kdevplatform.

%files -n %lib_name-devel
%defattr(-,root,root)
%_kde_appsdir/cmake/modules/FindKDevPlatform.cmake
%dir %_kde_includedir/kdevplatform
%dir %_kde_includedir/kdevplatform/editor
%_kde_includedir/kdevplatform/editor/*
%dir %_kde_includedir/kdevplatform/interfaces
%_kde_includedir/kdevplatform/interfaces/*.h
%dir %_kde_includedir/kdevplatform/language/backgroundparser
%_kde_includedir/kdevplatform/language/backgroundparser/*
%dir %_kde_includedir/kdevplatform/language/duchain
%_kde_includedir/kdevplatform/language/duchain/*
%dir %_kde_includedir/kdevplatform/language/interfaces
%_kde_includedir/kdevplatform/language/interfaces/*
%dir %_kde_includedir/kdevplatform/outputview
%_kde_includedir/kdevplatform/outputview/*
%dir %_kde_includedir/kdevplatform/project
%_kde_includedir/kdevplatform/project/*
%dir %_kde_includedir/kdevplatform/shell
%_kde_includedir/kdevplatform/shell/*
%dir %_kde_includedir/kdevplatform/sublime
%_kde_includedir/kdevplatform/sublime/*
%dir %_kde_includedir/kdevplatform/util
%_kde_includedir/kdevplatform/util/*
%dir %_kde_includedir/kdevplatform/vcs
%_kde_includedir/kdevplatform/vcs/*.h
%dir %_kde_includedir/kdevplatform/vcs/interfaces
%_kde_includedir/kdevplatform/vcs/interfaces/*.h
%dir %_kde_includedir/kdevplatform/language
%_kde_includedir/kdevplatform/language/languageexport.h
%dir %_kde_includedir/kdevplatform/vcs/models
%_kde_includedir/kdevplatform/vcs/models/*.h
%dir %_kde_includedir/kdevplatform/vcs/widgets
%_kde_includedir/kdevplatform/vcs/widgets/*.h
%{_kde_libdir}/libkdevplatformeditor.so
%{_kde_libdir}/libkdevplatforminterfaces.so
%{_kde_libdir}/libkdevplatformlanguage.so
%{_kde_libdir}/libkdevplatformoutputview.so
%{_kde_libdir}/libkdevplatformproject.so
%{_kde_libdir}/libkdevplatformshell.so
%{_kde_libdir}/libkdevplatformutil.so
%{_kde_libdir}/libkdevplatformvcs.so
%{_kde_libdir}/libsublime.so

#-----------------------------------------------------------------------------

%prep
%setup -q -n kdevplatform-%version

%build

cd $RPM_BUILD_DIR/kdevplatform-%version
%cmake_kde4 

%make


%if %compile_apidox
make apidox
%endif

%install
rm -fr %buildroot

cd $RPM_BUILD_DIR/kdevplatform-%version
cd build

make DESTDIR=%buildroot install

%clean
rm -fr %buildroot



