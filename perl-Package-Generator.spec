%define module   Package-Generator
%define upstream_version 1.106

Name:		perl-%{module}
Version:	%perl_convert_version %{upstream_version}
Release:	3
Summary:	Pseudo-garbage-collection for packages
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/Package/Package-Generator-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
This module allows you to create simple objects which, when destroyed,
delete a given package. This lets you approximate lexically scoped
packages.

%prep
%setup -q -n %{module}-%{upstream_version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/Package



%changelog
* Fri Jul 10 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.103-1mdv2010.0
+ Revision: 394088
- update to new version 0.103

* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.102-2mdv2009.0
+ Revision: 268705
- rebuild early 2009.0 package (before pixel changes)

* Sat May 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.102-1mdv2009.0
+ Revision: 213827
- import perl-Package-Generator


* Sat May 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.102-1mdv2009.0
- first mdv release


