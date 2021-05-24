Name:           supybot-koji
Version:        0.3
Release:        1%{?dist}
Summary:        Plugin for Supybot to interact with Koji instances

Group:          Applications/Internet
License:        BSD
URL:            https://github.com/fedora-infra/supybot-koji
Source0:        https://github.com/fedora-infra/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

Requires:       koji
Requires:       limnoria

BuildArch:      noarch
BuildRequires:  python3-devel

%description
A Supybot plugin which provides access to the status of a Koji buildsystem
and makes it available via IRC.


%prep
%setup -q

%build


%install
rm -rf $RPM_BUILD_ROOT
install -dm 755 $RPM_BUILD_ROOT/%{python3_sitelib}/supybot/plugins/Koji
install -pm 644 supybot_koji/*.py $RPM_BUILD_ROOT/%{python3_sitelib}/supybot/plugins/Koji


%files
%doc README.md
%{python3_sitelib}/supybot/plugins/Koji


%changelog
* Mon May 24 2021 Ryan Lerch <rlerch@redhat.com> - 0.3-1
- Change to Python 3
- New 0.3 Release

* Fri Feb 10 2017 Dennis Gilmore <dennis@ausil.us> - 0.2-2
- clean up hosts = hosts = foo
- set the server to use https:// by default

* Tue Jan 11 2011 Jon Stanley <jonstanley@gmail.com> - 0.2-1
- New upstream release 0.2

* Thu Dec 4 2008 Jon Stanley <jonstanley@gmail.com> - 0.1-1
- Initial package
