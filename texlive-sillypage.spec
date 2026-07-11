%global tl_name sillypage
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.7
Release:	%{tl_revision}.1
Summary:	John Cleeses Silly Walk as page numbering style
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/sillypage
License:	cc-by-sa-4 lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sillypage.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sillypage.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sillypage.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This simple LaTeX package provides John Cleese's iconic silly walk
routine as a page numbering style. Other counters, as well as integers,
can be typeset in this "silly" style, too.

