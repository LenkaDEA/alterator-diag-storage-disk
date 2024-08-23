%define _unpackaged_files_terminate_build 1
%define diagnostic_tool storage-disk
Name: diag-%diagnostic_tool
Version: 0.0.1
Release: alt1

Summary: Storage Disks Diagnostic Tool
License: GPLv3
Group: System/Configuration/Other
Url: https://gitlab.basealt.space/alt/diag-storage-disk
BuildArch: noarch
Source: %name-%version.tar

BuildRequires: rpm-macros-alterator

Requires: smartmontools

%description
Storage disks diagnostic tool.

%prep
%setup

%build
sed -i 's/^VERSION=.*/VERSION=%version/' %name

%install
mkdir -p %buildroot%_alterator_datadir/diagnostictools/%name

install -p -D -m755 %name %buildroot%_bindir/%name
install -p -D -m644 %name.backend %buildroot%_alterator_datadir/backends/%name.backend
install -p -D -m644 %diagnostic_tool.diag %buildroot%_alterator_datadir/diagnostictools/%diagnostic_tool.diag
install -p -D %name.svg %buildroot%_iconsdir/hicolor/scalable/apps/%name.svg

%files
%_bindir/%name
%_alterator_datadir/backends/%name.backend
%_alterator_datadir/diagnostictools/%diagnostic_tool.diag
%_iconsdir/hicolor/scalable/apps/%name.svg

%changelog
* Tue Aug 20 2024 Elena Dyatlenko <lenka@altlinux.org> 0.0.1-alt1
- Initial build


