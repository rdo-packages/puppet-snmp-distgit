%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-snmp
%global commit df91395cd829134c53d61d6878232aff1b999905
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-snmp
Version:        3.8.1
Release:        1%{?alphatag}%{?dist}
Summary:        Simple Network Management Protocol is for monitoring network and computer equipment. Net-SNMP implements v1, v2c, and v3 on both IPv4 and IPv6.
License:        ASL 2.0

URL:            https://github.com/razorsedge/puppet-snmp

Source0:        https://github.com/razorsedge/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:      noarch

Requires:       puppet-stdlib
Requires:       puppet >= 2.7.0

%description
Simple Network Management Protocol is for monitoring network and computer equipment. Net-SNMP implements v1, v2c, and v3 on both IPv4 and IPv6.

%prep
%setup -q -n %{name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/snmp/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/snmp/



%files
%{_datadir}/openstack-puppet/modules/snmp/


%changelog
* Thu Aug 24 2017 Alfredo Moralejo <amoralej@redhat.com> 3.8.1-1.df91395git
- Pike update 3.8.1 (df91395cd829134c53d61d6878232aff1b999905)


