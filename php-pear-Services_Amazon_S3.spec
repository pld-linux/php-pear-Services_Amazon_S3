# ToDo:
# - beutify pl description
%include	/usr/lib/rpm/macros.php
%define		_class		Services
%define		_subclass	Amazon_S3
%define		_status		alpha
%define		_pearname	Services_Amazon_S3
Summary:	%{_pearname} - PHP interface to Amazon S3's API
Summary(pl.UTF-8):	%{_pearname} - interfejs PHP do API Amazon S3
Name:		php-pear-%{_pearname}
Version:	0.1.0
Release:	1
License:	New BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	9d98696b3bf3155f8e0fa351dbf984c2
URL:		http://pear.php.net/package/Services_Amazon_S3/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-Crypt_HMAC
Requires:	php-pear-HTTP_Request >= 1.4.0
Requires:	php-pear-PEAR-core >= 1:1.4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Services_Amazon_S3 is a PHP library for accessing Amazon Simple
Storage Service (S3). The library is based on the 2006-03-01 REST API.

Features:
- list, create and delete buckets, including buckets with location
  constraints (European buckets)
- create, read and delete objects including metadata
- list keys in a bucket using an SPL Iterator with support for paging,
  key prefixes and delimiters
- manipulate access control lists for buckets and objects
- specify the request style (virtualhost, cname, path style) and
  endpoint
- get signed URLs to allow a trusted third party to access private
  files
- access buckets and objects using PHP filesystem functions through a
  stream wrapper

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Services_Amazon_S3 to biblioteka PHP do obsługi usługi Amazon Simple
Sotrage Service (S3). Biblioteka oparta jest na API REST z dnia
2006-03-01.

Cechy:
- wyświetlanie, tworzenie i usuwanie koszyków, włączając w to koszyki
  z ograniczeniami co do lokalizacji (np. europejskie koszyki),
- tworzenie, odczyt i usuwanie obiektów zawierających metadane,
- wyświetlanie kluczy w koszyku za pomocą iteratora SPL ze wsparciem
  dla podziału na stronie, prefiksów i wyróżników,
- modyfikacja list kontroli dostępu dla koszyków i obiektów,
- określanie stylu zapytania (virtualhost, cname, ścieżka) i elementu
  docelowego,
- pobieranie podpisanych URL aby umożliwić podmiotom trzecim dostęp do
  prywatnych plików,
- dostęp do koszyków i obiektów za pomocą funkcji systemowych PHP
  dzięki użyciu wrappera na strumienie.

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
%{php_pear_dir}/Services/Amazon/S3
%{php_pear_dir}/Services/Amazon/S3.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/Services_Amazon_S3
