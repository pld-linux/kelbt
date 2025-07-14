Summary:	Kelbt - backtracking LR parsing
Summary(pl.UTF-8):	Kelbt - analiza LR z nawrotami
Name:		kelbt
Version:	0.15
Release:	1
License:	GPL v2+
Group:		Development/Tools
Source0:	http://www.complang.org/kelbt/%{name}-%{version}.tar.gz
# Source0-md5:	c480692e26998edcc8735513c902cecc
Patch0:		%{name}-c++.patch
URL:		http://www.complang.org/kelbt/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kelbt generates backtracking LALR(1) parsers. Where traditional
LALR(1) parser generators require static resolution of shift/reduce
conflicts, Kelbt generates parsers that handle conflicts by
backtracking at runtime. Kelbt is able to generate a parser for any
context-free grammar that is free of hidden left recursion.

%description -l pl.UTF-8
Kelbt generuje analizatory LALR(1) z nawrotami. O ile tradycyjne
generatory analizatorów LALR(1) wymagają statycznego rozwiązywania
konfliktów przesunięcie/redukcja, Kelbt generuje analizatory
obsługujące konflikty poprzez nawroty w trakcie działania. Kelbt
potrafi wygenerować analizator dla dowolnej gramatyki bezkontekstowej
pozbawiony ukrytej rekurencji.

%prep
%setup -q
%patch -P0 -p1

%build
%configure
%{__make} \
	CFLAGS="%{rpmcxxflags} -Wall" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -D kelbt/kelbt $RPM_BUILD_ROOT%{_bindir}/kelbt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS ChangeLog TODO
%attr(755,root,root) %{_bindir}/kelbt
