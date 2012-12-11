Summary:	Additional artwork for the Xfce Desktop Environment
Name:		xfce4-artwork
Version:	0.2
Release:	%mkrel 12
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/artwork/xfce4-artwork
Source0:	%{name}-%{version}.tar.bz2
BuildArch:	noarch
Obsoletes:	xfce-artwork <= 0.2-3
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Additional artwork for the Xfce Desktop Environment.
 
%prep
%setup -q

%build
%configure2_5x

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README ChangeLog AUTHORS
%{_datadir}/xfce4/*


%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2-12mdv2011.0
+ Revision: 615556
- the mass rebuild of 2010.1 packages

* Fri May 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2-11mdv2010.1
+ Revision: 543288
- rebuild for mdv 2010.1

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 0.2-10mdv2010.0
+ Revision: 445937
- rebuild

* Thu Mar 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2-9mdv2009.1
+ Revision: 349194
- rebuild whole xfce

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 0.2-8mdv2009.0
+ Revision: 262333
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.2-7mdv2009.0
+ Revision: 256811
- rebuild

* Thu Jan 17 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2-5mdv2008.1
+ Revision: 153957
- obsolete older release

* Mon Dec 17 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2-4mdv2008.1
+ Revision: 131630
- bump tag to remove xfce-artwork from mirrors

* Sat Dec 15 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2-3mdv2008.1
+ Revision: 120307
- use upstream name
- do not package INSTALL and COPYING files
- new license policy
- use tarball name as a real name

* Wed May 30 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2-3mdv2008.0
+ Revision: 32785
- remove requires on task-xfce

* Tue May 29 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2-2mdv2008.0
+ Revision: 32564
- add provides/obsoletes xfce4-artwork

* Mon May 28 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2-1mdv2008.0
+ Revision: 32139
- rename to xfce-artwork
- add some new fancy wallpapers
- requires task-xfce
- spec file clean


* Tue Jan 02 2007 Jérôme Soyer <saispo@mandriva.org> 0.1-3mdv2007.0
+ Revision: 103269
- Rebuild for latest xfce

* Thu Oct 26 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.1-2mdv2007.1
+ Revision: 72539
- Rebuild
- import xfce4-artwork-0.1-1mdv2007.0

* Sat Jun 24 2006 Charles A Edwards <eslrahc@mandriva.org> 0.1-1mdv2007.0
- 0.1

* Wed Jun 07 2006 Charles A Edwards <eslrahc@mandriva.org> 0.0.4-3mdv2007.0
- mkrel
- rebuild

* Sat Jan 22 2005 Marcel Pol <mpol@mandrake.org> 0.0.4-2mdk
- group: Graphical desktop/Xfce
- s/XFce4/Xfce

