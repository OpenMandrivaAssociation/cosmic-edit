%undefine _debugsource_packages
%define         appname com.system76.CosmicEdit
Name:           cosmic-edit
Version:        1.0.0
Release:        0.alpha1.0
Summary:        COSMIC Text Editor
Group:          Desktop/COSMIC
License:        GPL-3.0-only
URL:            https://github.com/pop-os/cosmic-edit
Source0:        https://github.com/pop-os/cosmic-applibrary/archive/epoch-%{version}-alpha.1/%{name}-epoch-%{version}-alpha.1.tar.gz
Source1:        vendor.tar.xz
Source2:        cargo_config

BuildRequires:  rust-packaging
#BuildRequires:  git-core
BuildRequires:  hicolor-icon-theme
BuildRequires:  just
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xkbcommon)

%description
Text editor for the COSMIC desktop

%prep
%autosetup -n %{name}-epoch-%{version}-alpha.1 -a1 -p1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
just build-release

%install
just rootdir=%{buildroot} prefix=%{_prefix} install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{appname}.desktop
%{_datadir}/icons/hicolor/??x??/apps/%{appname}.svg
%{_datadir}/icons/hicolor/???x???/apps/%{appname}.svg
%{_datadir}/metainfo/%{appname}.metainfo.xml