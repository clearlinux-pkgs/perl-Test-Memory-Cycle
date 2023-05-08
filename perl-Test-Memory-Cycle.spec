#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-Test-Memory-Cycle
Version  : 1.06
Release  : 11
URL      : https://cpan.metacpan.org/authors/id/P/PE/PETDANCE/Test-Memory-Cycle-1.06.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PE/PETDANCE/Test-Memory-Cycle-1.06.tar.gz
Summary  : "Verifies code hasn't left circular references"
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-Test-Memory-Cycle-license = %{version}-%{release}
Requires: perl-Test-Memory-Cycle-perl = %{version}-%{release}
Requires: perl(Devel::Cycle)
BuildRequires : buildreq-cpan
BuildRequires : perl(Devel::Cycle)
BuildRequires : perl(PadWalker)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# test-memory-cycle
Test::Memory::Cycle -- A Perl module to check for memory leaks and circular memory references.

%package dev
Summary: dev components for the perl-Test-Memory-Cycle package.
Group: Development
Provides: perl-Test-Memory-Cycle-devel = %{version}-%{release}
Requires: perl-Test-Memory-Cycle = %{version}-%{release}

%description dev
dev components for the perl-Test-Memory-Cycle package.


%package license
Summary: license components for the perl-Test-Memory-Cycle package.
Group: Default

%description license
license components for the perl-Test-Memory-Cycle package.


%package perl
Summary: perl components for the perl-Test-Memory-Cycle package.
Group: Default
Requires: perl-Test-Memory-Cycle = %{version}-%{release}

%description perl
perl components for the perl-Test-Memory-Cycle package.


%prep
%setup -q -n Test-Memory-Cycle-1.06
cd %{_builddir}/Test-Memory-Cycle-1.06

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Test-Memory-Cycle
cp %{_builddir}/Test-Memory-Cycle-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Test-Memory-Cycle/25c5a7c500c8035c364e7ede17dce2bd2138a0f0 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Test::Memory::Cycle.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Test-Memory-Cycle/25c5a7c500c8035c364e7ede17dce2bd2138a0f0

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
