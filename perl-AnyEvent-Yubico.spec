#
# Conditional build:
%bcond_with	tests	# run tests (require network)
#
%define		pdir	AnyEvent
%define		pnam	Yubico
Summary:	AnyEvent based Perl module for validating YubiKey OTPs
Summary(pl.UTF-8):	Oparty na AnyEvent moduł Perla do sprawdzania poprawności OTP YubiKey
Name:		perl-AnyEvent-Yubico
Version:	0.9.3
Release:	1
License:	BSD
Group:		Development/Languages/Perl
#Source0Download: https://github.com/Yubico/yubico-perl-client/releases
Source0:	https://github.com/Yubico/yubico-perl-client/archive/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	28cc626e6531e85767399c7d6164c1f6
URL:		https://developers.yubico.com/yubico-perl-client/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-AnyEvent-HTTP >= 2.13
BuildRequires:	perl-Digest-HMAC >= 1.02
BuildRequires:	perl-MIME-Base64 >= 3.13
BuildRequires:	perl-Net-SSLeay >= 1.36
BuildRequires:	perl-Test-Exception >= 0.29
BuildRequires:	perl-Test-Simple >= 0.98
BuildRequires:	perl-URI >= 1.54
BuildRequires:	perl-UUID-Tiny >= 1.0
%endif
Requires:	perl-AnyEvent-HTTP >= 2.13
Requires:	perl-Digest-HMAC >= 1.02
Requires:	perl-MIME-Base64 >= 3.13
Requires:	perl-URI >= 1.54
Requires:	perl-UUID-Tiny >= 1.0
Conflicts:	perl-Net-SSLeay < 1.36
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AnyEvent based Perl module for validating YubiKey OTPs.

%description -l pl.UTF-8
Oparty na AnyEvent moduł Perla do sprawdzania poprawności OTP YubiKey.

%prep
%setup -q -n yubico-perl-client-%{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING Changes README
%{perl_vendorlib}/AnyEvent/Yubico.pm
%{_mandir}/man3/AnyEvent::Yubico.3pm*
