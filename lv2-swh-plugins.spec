%define		_name	swh-lv2
#
Summary:	A set of LV2 audio plugins
Summary(pl.UTF-8):	Zestaw wtyczek dźwiękowych LV2
Name:		lv2-swh-plugins
Version:	1.0.15
Release:	1
License:	GPL
Group:		Applications/Sound
Source0:	http://plugin.org.uk/lv2/%{_name}-%{version}.tar.gz
# Source0-md5:	c78f42c36d7bf2fb5b17f795ef9636d1
URL:		http://plugin.org.uk/
BuildRequires:	fftw3-single-devel
BuildRequires:	pkgconfig
Requires:	lv2core
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A set of LV2 audio plugins (see http://plugin.org.uk/ for more
details).

%description -l pl.UTF-8
Zestaw wtyczek dźwiękowych LV2 (więcej informacji pod adresem
http://plugin.org.uk/).

%prep
%setup -q -n %{_name}-%{version}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install-system \
	INSTALL_DIR=$RPM_BUILD_ROOT%{_libdir}/lv2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/lv2/*
