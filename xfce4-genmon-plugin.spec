Summary:	Generic monitor plugin for the Xfce4 Panel
Summary(pl.UTF-8):	Wtyczka ogólnego przeznaczenia dla panelu Xfce4
Name:		xfce4-genmon-plugin
Version:	4.0.2
Release:	1
License:	LGPL v2.1
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-genmon-plugin/4.0/%{name}-%{version}.tar.bz2
# Source0-md5:	d808fe77a438c95b97ec6feda6162d22
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-genmon-plugin
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	libtool
BuildRequires:	libxfce4ui-devel
BuildRequires:	perl-XML-Parser
BuildRequires:	pkgconfig
BuildRequires:	xfce4-dev-tools >= 4.14.0
BuildRequires:	xfce4-panel-devel >= 4.14.0
Obsoletes:	xfce4-genmon-plugin-scripts
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The GenMon plugin cyclically spawns the indicated script/program,
captures its output and displays it as a string into the panel.

%description -l pl.UTF-8
Wtyczka GenMon cyklicznie wykonuje podany skrypt lub program,
przechwytując jego standardowe wyjście i wyświetla je w postaci
tekstowej na panelu.

%package scripts
Summary:	Sample scripts for xfce4-genmon-plugin
Summary(pl.UTF-8):	Przykładowe skrypty dla xfce4-genmon-plugin
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description scripts
Sample scripts for xfce4-genmon-plugin.

%description scripts -l pl.UTF-8
Przykładowe skrypty dla xfce4-genmon-plugin.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%if 0
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install scripts/{datetime,disktemp,dkspuse,monBat,monCPU,monTime,monUSB,monWIFI,samples.txt} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/
%endif

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xfce4/panel/plugins/*.la

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK
%{__mv} $RPM_BUILD_ROOT%{_datadir}/locale/{hy_AM,hy}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libgenmon.so
%{_datadir}/xfce4/panel/plugins/genmon.desktop

%if 0
%files scripts
%defattr(644,root,root,755)
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/datetime
%{_examplesdir}/%{name}-%{version}/disktemp
%{_examplesdir}/%{name}-%{version}/dkspuse
%{_examplesdir}/%{name}-%{version}/monBat
%{_examplesdir}/%{name}-%{version}/monCPU
%{_examplesdir}/%{name}-%{version}/monTime
%{_examplesdir}/%{name}-%{version}/monUSB
%{_examplesdir}/%{name}-%{version}/monWIFI
%{_examplesdir}/%{name}-%{version}/samples.txt
%endif
