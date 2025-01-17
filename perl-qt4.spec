%define srcname perlqt

Summary:	Qt bindings for Perl
Name:		perl-qt4
Version:	4.14.3
Release:	3
Epoch:		1
License:	GPLv2+ Artistic GPLv3+ LGPLv2+
Group:		Development/KDE and Qt
Url:		https://www.kde.org
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{srcname}-%{version}.tar.xz
BuildRequires:	db-devel
BuildRequires:	perl-devel
BuildRequires:	smokeqt-devel >= 1:%{version}
BuildRequires:	pkgconfig(qimageblitz) < 5.0.0
Conflicts:	perl-kde < 1:4.6.90

%description
A Qt4 bindings for perl language.

%files
%doc LICENSE LICENSE.Artistic LICENSE.GPL-3 LICENSE.LGPL MANIFEST README
%{_kde_bindir}/puic4
%{_kde_bindir}/prcc4_bin
%{_kde_bindir}/qdbusxml2perl
%{perl_sitearch}/Qt*.pm
%{perl_sitearch}/QtCore4
%{perl_sitearch}/auto/Qt*
%{perl_sitelib}/*/Phonon.pm
%{perl_sitelib}/*/QImageBlitz.pm
%{perl_sitelib}/*/Qsci.pm
%{perl_sitelib}/*/auto/Phonon/Phonon.so
%{perl_sitelib}/*/auto/QImageBlitz/QImageBlitz.so
%{perl_sitelib}/*/auto/Qsci/Qsci.so

#--------------------------------------------------------

%package devel
Summary:	Headers files for %{name}
Group:		Development/KDE and Qt
Requires:	smokeqt-devel >= 1:%{version}
Requires:	perl-devel
Requires:	db-devel
Requires:	%{name} = %{EVRD}

%description devel
Headers files for %{name}

%files devel
%dir %{_kde_includedir}/%{srcname}
%{_kde_includedir}/%{srcname}/QtCore4.h
%{_kde_includedir}/%{srcname}/binding.h
%{_kde_includedir}/%{srcname}/handlers.h
%{_kde_includedir}/%{srcname}/listclass_macros.h
%{_kde_includedir}/%{srcname}/marshall.h
%{_kde_includedir}/%{srcname}/marshall_basetypes.h
%{_kde_includedir}/%{srcname}/marshall_complex.h
%{_kde_includedir}/%{srcname}/marshall_macros.h
%{_kde_includedir}/%{srcname}/marshall_primitives.h
%{_kde_includedir}/%{srcname}/marshall_types.h
%{_kde_includedir}/%{srcname}/perlqt.h
%{_kde_includedir}/%{srcname}/ppport.h
%{_kde_includedir}/%{srcname}/smokehelp.h
%{_kde_includedir}/%{srcname}/smokeperl.h
%{_kde_includedir}/%{srcname}/util.h
%dir %{_kde_datadir}/%{srcname}
%dir %{_kde_datadir}/%{srcname}/cmake
%{_kde_datadir}/%{srcname}/cmake/FindPerlMore.cmake
%{_kde_datadir}/%{srcname}/cmake/PerlQtConfig.cmake
%{_kde_datadir}/%{srcname}/cmake/PerlQtExport*.cmake
%{_kde_datadir}/%{srcname}/doxsubpp.pl

#------------------------------------------------------------

%prep
%setup -q -n %{srcname}-%{version}

%build
# remove it after perl-5.20 update for arm
%ifarch %armx
export CC=gcc
export CXX=g++
%endif
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Tue Nov 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.14.3-1
- New version 4.14.3

* Mon Oct 27 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.14.2-2
- Use pkgconfig(qimageblitz) < 5.0.0 to force Qt4 version

* Wed Oct 15 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.14.2-1
- New version 4.14.2

* Mon Sep 29 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.14.1-1
- New version 4.14.1

* Tue Jul 15 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.13.3-1
- New version 4.13.3

* Wed Jun 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.13.2-1
- New version 4.13.2

* Wed Apr 02 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.4-1
- New version 4.12.4

* Tue Mar 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.3-1
- New version 4.12.3

* Tue Feb 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.2-1
- New version 4.12.2

* Tue Jan 14 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.1-1
- New version 4.12.1
- Drop no longer needed link patch

* Wed Dec 04 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.4-1
- New version 4.11.4

* Wed Nov 06 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.3-1
- New version 4.11.3

* Wed Oct 02 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.2-1
- New version 4.11.2

* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.0-1
- New version 4.11.0

* Wed Jul 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.5-1
- New version 4.10.5

* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.4-1
- New version 4.10.4

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.3-1
- New version 4.10.3

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.1-1
- New version 4.10.1

* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.0-1
- New version 4.10.0

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.2-1
- New version 4.9.2

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.1-1
- New version 4.9.1

* Tue Aug 14 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.0-1
- New version 4.9.0

* Sun Jul 22 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.8.97-1
- New version 4.8.97

* Sun Jul 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.8.95-1
- New version 4.8.95

* Fri Jun 08 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.4-69.1mib2010.2
- New version 4.8.4
- Add pkgconfig(qimageblitz) to BuildRequires
- MIB (Mandriva International Backports)

* Fri May 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.3-69.1mib2010.2
- New version 4.8.3
- MIB (Mandriva International Backports)

* Wed Apr 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.2-69.1mib2010.2
- New version 4.8.2
- MIB (Mandriva International Backports)

* Wed Mar 07 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.1-69.1mib2010.2
- New version 4.8.1
- Add patch to fix linkage
- MIB (Mandriva International Backports)

* Mon Feb 20 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.0-69.4mib2010.2
+ Revision: 769515
- Backport to 2010.2 for MIB users
- MIB (Mandriva International Backports)

* Sat Jan 28 2012 Oden Eriksson <oeriksson@mandriva.com> 1:4.8.0-4
+ Revision: 769515
- db-devel was really needed here.
- drop bogus deps

* Fri Jan 27 2012 Oden Eriksson <oeriksson@mandriva.com> 1:4.8.0-3
+ Revision: 769414
- duh!
- bump release
- use the latest bdb (currently 5.2)

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1:4.8.0-2
+ Revision: 764137
- rebuilt for perl-5.14.x

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - New upstream tarball

* Fri Jan 06 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.97-1
+ Revision: 758117
- New upstream tarball

* Tue Jan 03 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.95-1
+ Revision: 748771
- Fix file list
- New version

* Wed Dec 14 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.90-1
+ Revision: 740825
- New version

* Mon Nov 21 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.80-1
+ Revision: 732106
- New version 4.7.80

* Mon Sep 19 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.41-1
+ Revision: 700315
- Fix file list
- Fix buildrequires
- Remove unexising BR
- Enable buildrequires
- imported package perl-qt4

