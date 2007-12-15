Summary:	Additional artwork for the Xfce Desktop Environment
Name:		xfce4-artwork
Version:	0.2
Release:	%mkrel 3
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/artwork/xfce4-artwork
Source0:	%{name}-%{version}.tar.bz2
BuildArch:	noarch
Obsoletes:	xfce-artwork
Provides:	xfce-artwork
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
