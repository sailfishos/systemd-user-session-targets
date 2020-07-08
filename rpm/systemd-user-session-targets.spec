Name:       systemd-user-session-targets
Summary:    Basic targets for systemd user session
Version:    0.0.2
Release:    1
BuildArch:  noarch
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
mkdir -p %{buildroot}%{_userunitdir}/pre-user-session.target.wants/
mkdir -p %{buildroot}%{_userunitdir}/user-session.target.wants/
mkdir -p %{buildroot}%{_userunitdir}/post-user-session.target.wants/
mkdir -p %{buildroot}%{_userunitdir}/actdead-session.target.wants/
mkdir -p %{buildroot}%{_userunitdir}/post-actdead-session.target.wants/
mkdir -p %{buildroot}%{_userunitdir}/booster-session.target.wants/

# targets
install -m 0644 targets/pre-user-session.target %{buildroot}%{_userunitdir}/
install -m 0644 targets/user-session.target %{buildroot}%{_userunitdir}/
install -m 0644 targets/post-user-session.target %{buildroot}%{_userunitdir}/
install -m 0644 targets/actdead-session.target %{buildroot}%{_userunitdir}/
install -m 0644 targets/post-actdead-session.target %{buildroot}%{_userunitdir}/
install -m 0644 targets/booster-session.target %{buildroot}%{_userunitdir}/

%files
%defattr(-,root,root,-)
%dir %{_userunitdir}/pre-user-session.target.wants
%dir %{_userunitdir}/user-session.target.wants
%dir %{_userunitdir}/post-user-session.target.wants
%dir %{_userunitdir}/actdead-session.target.wants
%dir %{_userunitdir}/post-actdead-session.target.wants
%dir %{_userunitdir}/booster-session.target.wants
%{_userunitdir}/pre-user-session.target
%{_userunitdir}/user-session.target
%{_userunitdir}/post-user-session.target
%{_userunitdir}/actdead-session.target
%{_userunitdir}/post-actdead-session.target
%{_userunitdir}/booster-session.target
