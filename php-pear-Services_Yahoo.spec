%include	/usr/lib/rpm/macros.php
%define		_class		Services
%define		_subclass	Yahoo
%define		_status		alpha
%define		_pearname	Services_Yahoo
Summary:	%{_pearname} - provides access to the Yahoo! Web Services
Summary(pl.UTF-8):	%{_pearname} - umożliwia dostęp do web services Yahoo!
Name:		php-pear-%{_pearname}
Version:	0.2.0
Release:	2
License:	Apache License, Version 2.0
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	d4fb681ed6686584ba43ec493aa18f27
Patch0:		%{name}-paths_fix.patch
URL:		http://pear.php.net/package/Services_Yahoo/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-HTTP_Request
Requires:	php-pear-PEAR >= 1.4.0b1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Services_Yahoo provides object-oriented interfaces to the web service
capabilities of Yahoo

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Services_Yahoo dostarcza zorientowany obiektowo interfejs do web
services Yahoo.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
AutoReq:	no
Requires:	%{name} = %{version}-%{release}
AutoProv:	no

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
%{php_pear_dir}/Services/Yahoo
%{php_pear_dir}/Services/Yahoo/Search.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/Services_Yahoo/Yahoo/Tests/All.php
%{php_pear_dir}/tests/Services_Yahoo/Yahoo/Tests/Exception.php
%{php_pear_dir}/tests/Services_Yahoo/Yahoo/Tests/Search.php
