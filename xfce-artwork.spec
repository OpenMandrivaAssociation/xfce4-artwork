%define oname xfce4-artwork

Summary:	Additional artwork for the Xfce Desktop Environment
Name:		xfce-artwork
Version:	0.2
Release:	%mkrel 3
License:	GPL
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/artwork/xfce4-artwork
Source0:	%{oname}-%{version}.tar.bz2
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
Obsoletes:	xfce4-artwork
Provides:	xfce4-artwork

%description
Additional artwork for the Xfce Desktop Environment.
 
%prep
%setup -qn %{oname}-%{version}

%build
%configure2_5x

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README ChangeLog INSTALL COPYING AUTHORS
%{_datadir}/xfce4/*
