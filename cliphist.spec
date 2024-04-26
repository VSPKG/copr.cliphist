Name:           cliphist
Version:        0.5.0
Release:        1
Summary:        clipboard history “manager” for wayland.

License:        BSD-3-Clause
URL:            https://github.com/sentriz/cliphist
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  git
BuildRequires:  go
BuildRequires:  xdg-utils

%define debug_package %{nil}

%description
wayland clipboard manager with support for multimedia.

%prep
%autosetup

%build
rm -rf ./* ./.*
git clone %{url} .
git checkout v%{version}
go build

%install
install -m 755 -Dp %{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc readme.md
%{_bindir}/%{name}

%changelog
