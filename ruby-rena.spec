%define	ruby_archdir	%(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
%define ruby_rubylibdir %(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
%define	ruby_ridir	%(ruby -r rbconfig -e 'include Config; print File.join(CONFIG["datadir"], "ri", CONFIG["ruby_version"], "system")')
Summary:	Rena RDF library
Name:		ruby-rena
Version:	0.0.4
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://web.sfc.keio.ac.jp/~s01397ms/archives/rena-%{version}.tar.gz
# Source0-md5:	5c89e85e1619df19dd45be949d1e3674
URL:		http://raa.ruby-lang.org/project/rena/
BuildRequires:	ruby
BuildRequires:	ruby-devel
Requires:	ruby
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RDF module for Ruby modeled after the Java Jena framework.

%prep
%setup -q -n rena-%{version}

%build
ruby setup.rb config \
	--rb-dir=%{ruby_rubylibdir} \
	--so-dir=%{ruby_archdir}

ruby setup.rb setup

rdoc -o rdoc/ --main README README lib/* --title "%{name} %{version}" --inline-source
rdoc --ri -o ri lib/*

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir}}

ruby setup.rb install --prefix=$RPM_BUILD_ROOT

cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc/*
%{ruby_rubylibdir}/rena
%{ruby_rubylibdir}/rena.rb
%{ruby_ridir}/Rena