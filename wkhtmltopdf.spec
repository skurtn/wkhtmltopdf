%define ver 0.12.3

Name:       wkhtmltopdf
Version:    %{ver}
Release:    1%{?dist}
Summary:    Renders HTML into PDF and various image formats.
Group:      Applications/Text
License:    GPLv3
URL:        http://wkhtmltopdf.org
Source0:    https://github.com/wkhtmltopdf/wkhtmltopdf/archive/%{ver}.x.zip
BuildRoot:  BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
wkhtmltopdf and wkhtmltoimage are command line tools to render HTML into PDF
and various image formats using the QT Webkit rendering engine. These run entirely
"headless" and do not require a display or display service.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(0755,root,root,0644)
%doc

%changelog
* Tue Mar 15 2016 S. Kurt Newman <skurtn+github@gmail.com> - 0.12.3-1
- Initial creation
