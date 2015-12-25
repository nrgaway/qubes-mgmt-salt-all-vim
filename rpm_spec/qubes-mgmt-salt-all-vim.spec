%{!?version: %define version %(cat version)}

Name:      qubes-mgmt-salt-all-vim
Version:   %{version}
Release:   1%{?dist}
Summary:   Salt formula to install vim
License:   GPL 2.0
URL:	   http://www.qubes-os.org/

Group:     System administration tools
BuildArch: noarch
Requires:  qubes-mgmt-salt

%define _builddir %(pwd)

%description
Salt formula to install vim.

Vim plugins for editing sls files, nerdtree and pyflakes are also included
along with a sample pillar file.

%prep
# we operate on the current directory, so no need to unpack anything
# symlink is to generate useful debuginfo packages
rm -f %{name}-%{version}
ln -sf . %{name}-%{version}
%setup -T -D

%build

%install
make install DESTDIR=%{buildroot} LIBDIR=%{_libdir} BINDIR=%{_bindir} SBINDIR=%{_sbindir} SYSCONFDIR=%{_sysconfdir}

%post
# Update Salt Configuration
qubesctl state.sls config -l quiet --out quiet > /dev/null || true
qubesctl saltutil.clear_cache -l quiet --out quiet > /dev/null || true
qubesctl saltutil.sync_all refresh=true -l quiet --out quiet > /dev/null || true

# Enable States
qubesctl top.enable vim saltenv=all -l quiet --out quiet > /dev/null || true
qubesctl top.enable vim.salt saltenv=all -l quiet --out quiet > /dev/null || true

%files
%defattr(-,root,root)
%doc LICENSE README.rst
%attr(750, root, root) %dir /srv/formulas/all/vim-formula
/srv/formulas/all/vim-formula/LICENSE
/srv/formulas/all/vim-formula/pillar.example
/srv/formulas/all/vim-formula/README.rst
/srv/formulas/all/vim-formula/vim/absent.sls
/srv/formulas/all/vim-formula/vim/editor.sls
/srv/formulas/all/vim-formula/vim/files/nerdtree/doc/NERD_tree.txt
/srv/formulas/all/vim-formula/vim/files/nerdtree/nerdtree_plugin/exec_menuitem.vim
/srv/formulas/all/vim-formula/vim/files/nerdtree/nerdtree_plugin/fs_menu.vim
/srv/formulas/all/vim-formula/vim/files/nerdtree/plugin/NERD_tree.vim
/srv/formulas/all/vim-formula/vim/files/nerdtree/syntax/nerdtree.vim
/srv/formulas/all/vim-formula/vim/files/pyflakes/ftplugin/python/pyflakes/bin/pyflakes
/srv/formulas/all/vim-formula/vim/files/pyflakes/ftplugin/python/pyflakes/LICENSE
/srv/formulas/all/vim-formula/vim/files/pyflakes/ftplugin/python/pyflakes/NEWS.txt
/srv/formulas/all/vim-formula/vim/files/pyflakes/ftplugin/python/pyflakes/pyflakes/checker.py*
/srv/formulas/all/vim-formula/vim/files/pyflakes/ftplugin/python/pyflakes/pyflakes/__init__.py*
/srv/formulas/all/vim-formula/vim/files/pyflakes/ftplugin/python/pyflakes/pyflakes/messages.py*
/srv/formulas/all/vim-formula/vim/files/pyflakes/ftplugin/python/pyflakes/pyflakes/scripts/__init__.py*
/srv/formulas/all/vim-formula/vim/files/pyflakes/ftplugin/python/pyflakes/pyflakes/scripts/pyflakes.py*
/srv/formulas/all/vim-formula/vim/files/pyflakes/ftplugin/python/pyflakes/pyflakes/test/harness.py*
/srv/formulas/all/vim-formula/vim/files/pyflakes/ftplugin/python/pyflakes/pyflakes/test/__init__.py*
/srv/formulas/all/vim-formula/vim/files/pyflakes/ftplugin/python/pyflakes/pyflakes/test/test_imports.py*
/srv/formulas/all/vim-formula/vim/files/pyflakes/ftplugin/python/pyflakes/pyflakes/test/test_other.py*
/srv/formulas/all/vim-formula/vim/files/pyflakes/ftplugin/python/pyflakes/pyflakes/test/test_script.py*
/srv/formulas/all/vim-formula/vim/files/pyflakes/ftplugin/python/pyflakes/pyflakes/test/test_undefined_names.py*
/srv/formulas/all/vim-formula/vim/files/pyflakes/ftplugin/python/pyflakes/README.rst
/srv/formulas/all/vim-formula/vim/files/pyflakes/ftplugin/python/pyflakes/setup.py*
/srv/formulas/all/vim-formula/vim/files/pyflakes/ftplugin/python/pyflakes.vim
/srv/formulas/all/vim-formula/vim/files/salt/ftdetect/jinja.vim
/srv/formulas/all/vim-formula/vim/files/salt/ftdetect/sls.vim
/srv/formulas/all/vim-formula/vim/files/salt/ftplugin/rst.vim
/srv/formulas/all/vim-formula/vim/files/salt/ftplugin/sls.vim
/srv/formulas/all/vim-formula/vim/files/salt/syntax/jinja.vim
/srv/formulas/all/vim-formula/vim/files/salt/syntax/sls.vim
/srv/formulas/all/vim-formula/vim/files/vimrc
/srv/formulas/all/vim-formula/vim/init.sls
/srv/formulas/all/vim-formula/vim/init.top
/srv/formulas/all/vim-formula/vim/map.jinja
/srv/formulas/all/vim-formula/vim/nerdtree.sls
/srv/formulas/all/vim-formula/vim/pyflakes.sls
/srv/formulas/all/vim-formula/vim/salt.sls
/srv/formulas/all/vim-formula/vim/salt.top

%changelog
