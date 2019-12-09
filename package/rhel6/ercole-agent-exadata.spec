Name:           ercole-agent-exadata
Version:        ERCOLE_VERSION
Release:        1%{?dist}
Summary:        Agent for ercole

License:        Proprietary
URL:            https://github.com/ercole-io/%{name}
Source0:        https://github.com/ercole-io/%{name}/archive/%{name}-%{version}.tar.gz

Group:          Tools

Buildroot: /tmp/rpm-ercole-agent-exadata

%global debug_package %{nil}

%description
Ercole Agent collects information about the exadata
detected on the local machine and send information to a central server

%prep
%setup -q -n %{name}-%{version}

rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT/opt/ercole-agent-exadata install
install -d $RPM_BUILD_ROOT/etc/init.d
install -d $RPM_BUILD_ROOT/etc/logrotate.d
install -m 755 package/rhel6/ercole-agent-exadata $RPM_BUILD_ROOT/etc/init.d/ercole-agent-exadata
install -m 644 package/rhel6/logrotate $RPM_BUILD_ROOT/etc/logrotate.d/ercole-agent-exadata

%post
chkconfig ercole-agent-exadata on

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
/etc/init.d/ercole-agent-exadata
/etc/logrotate.d/ercole-agent-exadata

%changelog
* Mon May  7 2018 Simone Rota <srota2@sorint.it>
- 
