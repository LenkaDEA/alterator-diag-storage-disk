Name: alterator-diag-storage-disk
Version: 0.0.1
Release: alt1

Summary: Disks diagnostic tool
License: GPLv3
Group: System/Configuration/Other
BuildArch: noarch

Url: https://gitlab.basealt.space/alt/diag-disks

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-alterator
BuildRequires: shellcheck

%description
Disks diagnostic tool.

%prep
%setup

%build
sed -i 's/^VERSION=.*/VERSION=%version/' %name

%install
install -p -D -m755 %name %buildroot%_bindir/%name
install -p -D -m644 %name.backend %buildroot%_alterator_datadir/backends/%name.backend
install -p -D -m644 %name.diag %buildroot%_alterator_datadir/diag/%name.diag
install -p -D %name.svg %buildroot%_iconsdir/hicolor/scalable/apps/%name.svg

%check
shellcheck -e SC1090,SC1091,SC2004,SC2015,SC2034,SC2086,SC2154,SC2001,SC2120,SC2119,SC2317 %name

%files
%_bindir/%name
%_alterator_datadir/backends/*.backend
%_alterator_datadir/diag/*.diag
%_iconsdir/hicolor/scalable/apps/%name.svg

%changelog

