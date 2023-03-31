Name:		texlive-sillypage
Version:	64034
Release:	2
Summary:	John Cleese's Silly Walk as page numbering style
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/sillypage
License:	cc-by-sa-4 lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sillypage.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sillypage.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sillypage.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This simple LaTeX package provides John Cleese's iconic silly
walk routine as a page numbering style. Other counters, as well
as integers, can be typeset in this "silly" style, too.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/sillypage
%{_texmfdistdir}/tex/latex/sillypage
%doc %{_texmfdistdir}/doc/latex/sillypage

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
