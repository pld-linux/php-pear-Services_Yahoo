%include	/usr/lib/rpm/macros.php
%define		_status		alpha
%define		_pearname	Services_Yahoo
Summary:	%{_pearname} - provides access to the Yahoo! Web Services
Summary(pl.UTF-8):	%{_pearname} - klasa umożliwiająca dostęp do usług WWW Yahoo!
Name:		php-pear-%{_pearname}
Version:	0.2.0
Release:	6
License:	Apache v2.0
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	d4fb681ed6686584ba43ec493aa18f27
Patch0:		%{name}-paths_fix.patch
URL:		http://pear.php.net/package/Services_Yahoo/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-HTTP_Request
Requires:	php-pear-PEAR-core >= 1:1.3.3
Requires:	php-simplexml
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Services_Yahoo provides object-oriented interfaces to the web service
capabilities of Yahoo.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Services_Yahoo dostarcza zorientowany obiektowo interfejs do usług WWW
Yahoo.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
AutoProv:	no
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%dir %{php_pear_dir}/Services
%{php_pear_dir}/Services/Yahoo

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/%{_pearname}
