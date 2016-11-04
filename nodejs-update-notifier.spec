%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}
%global npm_name update-notifier

Summary:       Update notifications for your CLI app
Name:          %{?scl_prefix}nodejs-%{npm_name}
Version:       0.6.0
Release:       2.sc2%{?dist}
License:       BSD
URL:           https://github.com/yeoman/update-notifier
Source0:       http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs010-runtime
ExclusiveArch: %{nodejs_arches} noarch
BuildArch:     noarch
Provides:      %{?scl_prefix}nodejs-%{npm_name} = %{version}

%description
Update notifications for your CLI app.
Inform users of your package of updates in a non-intrusive way.

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr *.js package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%files
%doc readme.md
%{nodejs_sitelib}/%{npm_name}

%changelog
* Wed Jan 06 2016 Tomas Hrcka <thrcka@redhat.com> - 0.6.0-2
- Enable scl macros

* Wed Dec 16 2015 Troy Dawson <tdawson@redhat.com> - 0.6.0-1
- Initial package
