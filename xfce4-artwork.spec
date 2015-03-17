Summary:	Additional artwork for the Xfce Desktop Environment
Name:		xfce4-artwork
Version:	0.2
Release:	16
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/artwork/xfce4-artwork
Source0:	%{name}-%{version}.tar.bz2
BuildArch:	noarch
Obsoletes:	xfce-artwork <= 0.2-3

%description
Additional artwork for the Xfce Desktop Environment.

%prep
%setup -q

%build
%configure2_5x

%install
%makeinstall_std

%files
%doc README ChangeLog AUTHORS
%{_datadir}/xfce4/*
