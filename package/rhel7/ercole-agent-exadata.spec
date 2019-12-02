Name:           ercole-agent-exadata
Version:        ERCOLE_VERSION
Release:        1%{?dist}
Summary:        Agent Exadata for ercole

License:        Proprietary
URL:            https://github.com/ercole-io/%{name}
Source0:        https://github.com/ercole-io/%{name}/archive/%{name}-%{version}.tar.gz
Requires: systemd
BuildRequires: systemd

Group:          Tools

Buildroot: /tmp/rpm-ercole-agent-exadata

%global debug_package %{nil}

%description
Ercole Exadata Agent collects information about the exadata and storage
running on the local machine and send information to a central server

%prep
%setup -q -n %{name}-%{version}

rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT/opt/ercole-agent-exadata install

install -d $RPM_BUILD_ROOT/opt/ercole-agent-exadata/run
install -d %{buildroot}%{_unitdir} 
install -d %{buildroot}%{_presetdir}
install -m 0644 package/rhel7/ercole-agent-exadata.service %{buildroot}%{_unitdir}/%{name}.service
install -m 0644 package/rhel7/60-ercole-agent-exadata.preset %{buildroot}%{_presetdir}/60-%{name}.preset

%post
/usr/bin/systemctl preset %{name}.service >/dev/null 2>&1 ||:

%preun
/usr/bin/systemctl --no-reload disable %{name}.service >/dev/null 2>&1 || :
/usr/bin/systemctl stop %{name}.service >/dev/null 2>&1 ||:

%postun
/usr/bin/systemctl daemon-reload >/dev/null 2>&1 ||:

%files
%attr(-,root,-) /opt/ercole-agent-exadata/run
%dir /opt/ercole-agent-exadata
%dir /opt/ercole-agent-exadata/fetch
%config(noreplace) /opt/ercole-agent-exadata/config.json
/opt/ercole-agent-exadata/fetch/filesystem
/opt/ercole-agent-exadata/fetch/host
/opt/ercole-agent-exadata/fetch/exadata-info
/opt/ercole-agent-exadata/fetch/exadata-storage-status
/opt/ercole-agent-exadata/ercole-agent-exadata
%{_unitdir}/ercole-agent-exadata.service
%{_presetdir}/60-ercole-agent-exadata.preset

%changelog
* Mon May  7 2018 Simone Rota <srota2@sorint.it>
- 
