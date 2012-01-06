%define srcname perlqt

Name:    perl-qt4
Summary: Qt bindings for Perl
Version: 4.7.97
Release: 1
Epoch:   1
Group:   Development/KDE and Qt
License: GPLv2 Artistic GPLv3 LGPLv2
URL:     http://www.kde.org
Source:  ftp://ftp.kde.org/pub/kde/stable/%version/src/%srcname-%version.tar.bz2

BuildRequires: smokeqt-devel >= 1:%version
BuildRequires: perl-devel
BuildRequires: gdbm-devel
BuildRequires: libdb5.1-devel
Conflicts:     perl-kde < 1:4.6.90

%description
A Qt4 bindings for perl language.


%files 
%doc LICENSE LICENSE.Artistic LICENSE.GPL-3 LICENSE.LGPL MANIFEST README
%_kde_bindir/puic4
%_kde_bindir/prcc4_bin
%_kde_bindir/qdbusxml2perl
%perl_sitearch/Qt*.pm
%perl_sitearch/QtCore4
%perl_sitearch/auto/Qt*
%perl_sitelib/*/Phonon.pm
%perl_sitelib/*/QImageBlitz.pm
%perl_sitelib/*/Qsci.pm
%perl_sitelib/*/auto/Phonon/Phonon.so
%perl_sitelib/*/auto/QImageBlitz/QImageBlitz.so
%perl_sitelib/*/auto/Qsci/Qsci.so

#--------------------------------------------------------

%package devel
Summary: Headers files for %{name}
Group: Development/KDE and Qt
Requires: smokeqt-devel >= 1:%version
Requires: perl-devel
Requires: db4-devel
Requires: gdbm-devel
Requires: %{name} = %epoch:%version-%release

%description devel
Headers files for %{name}

%files devel
%dir %_kde_includedir/%srcname
%_kde_includedir/%srcname/QtCore4.h
%_kde_includedir/%srcname/binding.h
%_kde_includedir/%srcname/handlers.h
%_kde_includedir/%srcname/listclass_macros.h
%_kde_includedir/%srcname/marshall.h
%_kde_includedir/%srcname/marshall_basetypes.h
%_kde_includedir/%srcname/marshall_complex.h
%_kde_includedir/%srcname/marshall_macros.h
%_kde_includedir/%srcname/marshall_primitives.h
%_kde_includedir/%srcname/marshall_types.h
%_kde_includedir/%srcname/perlqt.h
%_kde_includedir/%srcname/ppport.h
%_kde_includedir/%srcname/smokehelp.h
%_kde_includedir/%srcname/smokeperl.h
%_kde_includedir/%srcname/util.h
%dir %_kde_datadir/%srcname
%dir %_kde_datadir/%srcname/cmake
%_kde_datadir/%srcname/cmake/FindPerlMore.cmake
%_kde_datadir/%srcname/cmake/PerlQtConfig.cmake
%_kde_datadir/%srcname/cmake/PerlQtExport*.cmake
%_kde_datadir/%srcname/cmake/PerlQtExport.cmake
%_kde_datadir/%srcname/doxsubpp.pl

#------------------------------------------------------------

%prep
%setup -q -n %srcname-%version
%build

%cmake_kde4 
%make

%install
%makeinstall_std -C build
