%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?python_ver: %define python_ver %(%{__python} -c "import sys ; print sys.version[:3]")}

Name: python-linux-procfs
Version: 0.4.6
Release: 3%{?dist}
License: GPLv2
Summary: Linux /proc abstraction classes
Group: System Environment/Libraries
Source: http://userweb.kernel.org/~acme/python-linux-procfs/%{name}-%{version}.tar.bz2

Patch1: procfs-Add-a-__contains__-method-to-dict-classes.patch
Patch2: pidstat-Add-PF_NO_SETAFFINITY-const.patch
Patch3: interrupts-Do-not-refrain-from-parsing-the-irq-affin.patch
Patch4: pidstat-Fix-process_flags-method.patch
Patch5: pidstat-Add-missing-PF_-flags.patch
Patch6: pflags-Add-command-line-utility-to-print-processor-f.patch
Patch7: pidstat-Support-COMM-names-with-spaces.patch

URL: http://userweb.kernel.org/~acme/python-linux-procfs
BuildArch: noarch
BuildRequires: python-devel
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
Abstractions to extract information from the Linux kernel /proc files.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install --skip-build --root %{buildroot}
mkdir -p %{buildroot}%{_bindir}
cp pflags-cmd.py %{buildroot}%{_bindir}/pflags

%clean
rm -rf %{buildroot}

%files
%defattr(0755,root,root,0755)
%{_bindir}/pflags
%{python_sitelib}/procfs/
%defattr(0644,root,root,0755)
%if "%{python_ver}" >= "2.5"
%{python_sitelib}/*.egg-info
%endif
%doc COPYING

%changelog
* Thu Jun 25 2015 John Kacur <jkacur@redhat.com> - 0.4.6-3
- procfs-Add-a-__contains__-method-to-dict-classes.patch
- pidstat-Add-PF_NO_SETAFFINITY-const.patch
- interrupts-Do-not-refrain-from-parsing-the-irq-affin.patch
- pidstat-Fix-process_flags-method.patch
- pidstat-Add-missing-PF_-flags.patch
- pflags-Add-command-line-utility-to-print-processor-f.patch
- pidstat-Support-COMM-names-with-spaces.patch
Resolves: rhbz#1232394

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.4.6-2
- Mass rebuild 2013-12-27

* Fri Jun 14 2013 Jiri Kastner <jkastner@redhat.com> - 0.4.6-1
- updated to 0.4.6

* Thu Jun  6 2013 Jiri Kastner <jkastner@redhat.com> - 0.4.5-1
- Added support for parsing cgroups as a per thread attribute

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 10 2009 Arnaldo Carvalho de Melo <acme@redhat.com> - 0.4.4-1
- Even more fixes due to the fedora review process

* Mon Feb  9 2009 Arnaldo Carvalho de Melo <acme@redhat.com> - 0.4.3-1
- Fixups due to the fedora review process

* Tue Aug 12 2008 Arnaldo Carvalho de Melo <acme@redhat.com> - 0.4.2-1
- interrupts: Add find_by_user_regex
- process: Always set the "cmdline" array, even if empty
- pidstats: Remove dead processes in find_by_name()
- pidstats: Add process class to catch dict references for late parsing
- pidstats: Move the /proc/PID/{stat,status} parsing to classes
- pidstats: Introduce process_flags method

* Tue Aug 12 2008 Arnaldo Carvalho de Melo <acme@redhat.com> - 0.4-1
- Per process flags needed by tuna

* Fri Jun 13 2008 Arnaldo Carvalho de Melo <acme@redhat.com> - 0.3-1
- Support CPU hotplug

* Mon Feb 25 2008 Arnaldo Carvalho de Melo <acme@redhat.com> - 0.1-1
- package created
