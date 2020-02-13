# Generated by rust2rpm 10
%bcond_without check
%global debug_package %{nil}

%global crate html5ever

Name:           rust-%{crate}
Version:        0.24.1
Release:        2%{?dist}
Summary:        High-performance browser-grade HTML5 parser

# Upstream license specification: MIT / Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/html5ever
Source:         %{crates_source}
# Initial patched metadata
# - Bump criterion to 0.3 https://github.com/servo/html5ever/pull/389
Patch0:         html5ever-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
High-performance browser-grade HTML5 parser.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 23 07:55:27 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.24.1-1
- Update to 0.24.1

* Fri Sep 13 18:15:47 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.24.0-1
- Update to 0.24.0
- Bump criterion to 0.3

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 22 20:01:02 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.23.0-2
- Regenerate

* Sun May 05 12:41:32 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.23.0-1
- Update to 0.23.0

* Tue Apr 30 08:37:41 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.22.8-1
- Update to 0.22.8

* Mon Mar 11 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.22.5-1
- Initial package
