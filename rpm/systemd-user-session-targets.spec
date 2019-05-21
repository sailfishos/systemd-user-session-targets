Name:       systemd-user-session-targets
Summary:    Basic targets for systemd user session
Version:    0.0.2
Release:    1
BuildArch:  noarch
Group:      System/Libraries
License:    BSD
Url:        https://git.sailfishos.org/mer-core/systemd-user-session-targets
Source0:    %{name}-%{version}.tar.gz
BuildRequires: systemd
Requires: systemd

%description
Targets for systemd user session

%prep
%setup -q

%install

# Directories
mkdir -p %{buildroot}%{_libdir}/systemd/user/pre-user-session.target.wants/
mkdir -p %{buildroot}%{_libdir}/systemd/user/user-session.target.wants/
mkdir -p %{buildroot}%{_libdir}/systemd/user/post-user-session.target.wants/
mkdir -p %{buildroot}%{_libdir}/systemd/user/actdead-session.target.wants/
mkdir -p %{buildroot}%{_libdir}/systemd/user/post-actdead-session.target.wants/
mkdir -p %{buildroot}%{_libdir}/systemd/user/booster-session.target.wants/

# targets
install -m 0644 targets/pre-user-session.target %{buildroot}%{_libdir}/systemd/user/
install -m 0644 targets/user-session.target %{buildroot}%{_libdir}/systemd/user/
install -m 0644 targets/post-user-session.target %{buildroot}%{_libdir}/systemd/user/
install -m 0644 targets/actdead-session.target %{buildroot}%{_libdir}/systemd/user/
install -m 0644 targets/post-actdead-session.target %{buildroot}%{_libdir}/systemd/user/
install -m 0644 targets/booster-session.target %{buildroot}%{_libdir}/systemd/user/

%files
%defattr(-,root,root,-)
%dir %{_libdir}/systemd/user/pre-user-session.target.wants
%dir %{_libdir}/systemd/user/user-session.target.wants
%dir %{_libdir}/systemd/user/post-user-session.target.wants
%dir %{_libdir}/systemd/user/actdead-session.target.wants
%dir %{_libdir}/systemd/user/post-actdead-session.target.wants
%dir %{_libdir}/systemd/user/booster-session.target.wants
%{_libdir}/systemd/user/pre-user-session.target
%{_libdir}/systemd/user/user-session.target
%{_libdir}/systemd/user/post-user-session.target
%{_libdir}/systemd/user/actdead-session.target
%{_libdir}/systemd/user/post-actdead-session.target
%{_libdir}/systemd/user/booster-session.target
