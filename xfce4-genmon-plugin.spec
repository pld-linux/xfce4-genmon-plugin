%define		name_src	xfce4-GenMon-plugin
Summary:	Generic monitor plugin for the Xfce4 Panel
Summary(pl):	Wtyczka ogólnego przeznaczenia dla panelu XFce4
Name:		xfce4-genmon-plugin
Version:	1.1
Release:	1
License:	LGPL v2.1
Group:		X11/Applications
Source0:	http://download.berlios.de/xfce-goodies/%{name_src}-%{version}.tar.gz
# Source0-md5:	d9ebea4373ba52b08ec37c9026e09402
URL:		http://xfce-goodies.berlios.de/
BuildRequires:	libxfcegui4-devel >= 4.1.99
BuildRequires:	xfce4-panel-devel >= 4.1.99
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The GenMon plugin cyclically spawns the indicated script/program,
captures its output and displays it as a string into the panel.

%description -l pl
Wtyczka GenMon cyklicznie wykonuje podany skrypt lub program,
przechwytuj±c jego standardowe wyj¶cie i wy¶wietla je w postaci
tekstowej na panelu.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/panel-plugins/*.{a,la}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/*.so
