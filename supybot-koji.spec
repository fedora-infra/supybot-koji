%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           supybot-koji
Version:        0.2
Release:        12%{?dist}
Summary:        Plugin for Supybot to interact with Koji instances

Group:          Applications/Internet
License:        BSD
URL:            https://fedorahosted.org/supybot-fedora
Source0:        https://fedorahosted.org/releases/s/u/%{name}/%{name}-%{version}.tar.bz2
Patch0:         https-cleanup.patch

Requires:       koji, /usr/bin/supybot

BuildArch:      noarch
BuildRequires:  python

%description
A Supybot plugin which provides access to the status of a Koji buildsystem
and makes it available via IRC.


%prep
%setup -q
%patch0 -p1

%build


%install
install -dm 755 $RPM_BUILD_ROOT/%{python_sitelib}/supybot/plugins/Koji
install -pm 644 *.py $RPM_BUILD_ROOT/%{python_sitelib}/supybot/plugins/Koji


%files
%defattr(-,root,root,-)
%doc
%{python_sitelib}/supybot/plugins/Koji


%changelog
* Fri Feb 10 2017 Dennis Gilmore <dennis@ausil.us> - 0.2-12
- clean up hosts = hosts = foo
- set the server to use https:// by default

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-11
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue May 03 2011 Dave Riches <david.r@ultracar.co.uk> - 0.2-3
- fixed requires for supybot and supybot-gribble

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 11 2011 Jon Stanley <jonstanley@gmail.com> - 0.2-1
- New upstream release 0.2

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Dec 7 2008 Jon Stanley <jonstanley@gmail.com> - 0.1-3
- Fix license tag, remove BR on python-devel from review

* Fri Dec 5 2008 Jon Stanley <jonstanley@gmail.com> - 0.1-2
- Review cleanup

* Thu Dec 4 2008 Jon Stanley <jonstanley@gmail.com> - 0.1-1
- Initial package
