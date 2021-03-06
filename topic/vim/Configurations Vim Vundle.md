#### Date, 29/01/2018

### Configurations Vim Vundle: 

1. git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim

2. vi  ~/.vimrc

   ``````shell
   set nocompatible              " be iMproved, required
   filetype off                  " required

   " set the runtime path to include Vundle and initialize
   set rtp+=~/.vim/bundle/Vundle.vim
   call vundle#begin()
   " alternatively, pass a path where Vundle should install plugins
   "call vundle#begin('~/some/path/here')

   " let Vundle manage Vundle, required
   Plugin 'VundleVim/Vundle.vim'

   " The following are examples of different formats supported.
   " Keep Plugin commands between vundle#begin/end.
   " plugin on GitHub repo
   Plugin 'tpope/vim-fugitive'
   Plugin 'scrooloose/nerdtree'
   Plugin 'davidhalter/jedi-vim'
   Plugin 'tmhedberg/SimpylFold'
   Plugin 'nvie/vim-flake8'

   Plugin 'scrooloose/syntastic'
   Plugin 'tpope/vim-surround'
   Plugin 'kien/ctrlp.vim'
   Plugin 'bling/vim-airline'
   Plugin 'altercation/vim-colors-solarized'
   Plugin 'scrooloose/nerdcommenter'
   Plugin 'majutsushi/tagbar'
   Plugin 'kchmck/vim-coffee-script'
   Plugin 'tpope/vim-rails'
   Plugin 'pangloss/vim-javascript'
   Plugin 'airblade/vim-gitgutter'
   Plugin 'valloric/youcompleteme'
   Plugin 'easymotion/vim-easymotion'
   Plugin 'ervandew/supertab'
   Plugin 'honza/vim-snippets'
   Plugin 'mileszs/ack.vim'
   Plugin 'tpope/vim-repeat'
   Plugin 'shougo/unite.vim'
   Plugin 'tpope/vim-markdown'
   Plugin 'sirver/ultisnips'
   Plugin 'tpope/vim-endwise'
   Plugin 'raimondi/delimitmate'
   Plugin 'nathanaelkane/vim-indent-guides'
   Plugin 'tomtom/tcomment_vim'
   Plugin 'tpope/vim-commentary'
   Plugin 'tomasr/molokai'
   Plugin 'tomtom/tlib_vim'
   Plugin 'marcweber/vim-addon-mw-utils'
   Plugin 'junegunn/gv.vim'
   Plugin 'klen/python-mode'
   Plugin 'jistr/vim-nerdtree-tabs'
   Plugin 'ryym/vim-riot'
   Plugin 'editorconfig/editorconfig-vim'
   Plugin 'junegunn/seoul256.vim'
   Plugin 'junegunn/goyo.vim'
   Plugin 'junegunn/limelight.vim'


   " All of your Plugins must be added before the following line
   call vundle#end()            " required
   filetype plugin indent on    " required
   	" To ignore plugin indent changes, instead use:
   "filetype plugin on
   "
   " Brief help
   " :PluginList       - lists configured plugins
   " :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
   " :PluginSearch foo - searches for foo; append `!` to refresh local cache
   " :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
   "
   " see :h vundle for more details or wiki for FAQ
   " Put your non-Plugin stuff after this line

   "auto reload vimrc
   augroup reload_vimrc " {
       autocmd!
           autocmd BufWritePost $MYVIMRC source $MYVIMRC
       augroup END " }


   " common
   set mouse=a
   syntax on

   " NERDTree config
   autocmd StdinReadPre * let s:std_in=1
   autocmd VimEnter * if argc() == 0 && !exists("s:std_in") | NERDTree | endif
   autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTreeType") && b:NERDTreeType == "primary") | q | endif
   let NERDTreeIgnore=['\.pyc$']

   " Exit insert mode
   inoremap jj <Esc>
   map <C-A> 0
   map <C-E> $
   map <C-i> d$

   " Flake8
   autocmd BufWritePost *.py call Flake8()
   let g:flake8_show_in_gutter=1 " show
   let g:flake8_show_in_file=0  " show

   "flake8
   autocmd BufWritePost *.py call Flake8()
   let g:flake8_show_in_gutter=1
   let g:flake8_show_in_file=0

   source ~/.basic.vim

   map <C-n> :NERDTreeToggle<CR>
   set number

   " With a map leader it's possible to do extra key combinations
   " like <leader>w saves the current file
   let mapleader=","
   let g:mapleader=","

   " Toggle paste mode on and off
   map <leader>pp :setlocal paste!<cr>

   filetype plugin indent on
   " show existing tab with 4 spaces width
   set tabstop=4
   " when indenting with '>', use 4 spaces width
   set shiftwidth=4
   " On pressing tab, insert 4 spaces
   set expandtab

   " SeeTab: toggles between showing tabs and using standard listchars
   fu! SeeTab()
     if !exists("g:SeeTabEnabled")
       let g:SeeTabEnabled = 1
       let g:SeeTab_list = &list
       let g:SeeTab_listchars = &listchars
       let regA = @a
       redir @a
       hi SpecialKey
       redir END
       let g:SeeTabSpecialKey = @a
       let @a = regA
       silent! hi SpecialKey guifg=black guibg=magenta ctermfg=black ctermbg=magenta
       set list
       set listchars=tab:\|\
     else
       let &list = g:SeeTab_list
       let &listchars = &listchars
       silent! exe "hi ".substitute(g:SeeTabSpecialKey,'xxx','','e')
       unlet g:SeeTabEnabled g:SeeTab_list g:SeeTab_listchars
     endif
   endfunc
   com! -nargs=0 SeeTab :call SeeTab()
   set runtimepath^=~/.vim/bundle/ag
   nnoremap <C-y> "+y
   vnoremap <C-y> "+y
   nnoremap <C-p> "+gP
   vnoremap <C-p> "+gP
   let g:javascript_plugin_jsdoc = 1
   ``````

   ​

3. vi ~/.basic.vim

   ``````shell
   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   " Maintainer: 
   "       Amir Salihefendic
   "       http://amix.dk - amix@amix.dk
   "
   " Version: 
   "       5.0 - 29/05/12 15:43:36
   "
   " Blog_post: 
   "       http://amix.dk/blog/post/19691#The-ultimate-Vim-configuration-on-Github
   "
   " Awesome_version:
   "       Get this config, nice color schemes and lots of plugins!
   "
   "       Install the awesome version from:
   "
   "           https://github.com/amix/vimrc
   "
   " Syntax_highlighted:
   "       http://amix.dk/vim/vimrc.html
   "
   " Raw_version: 
   "       http://amix.dk/vim/vimrc.txt
   "
   " Sections:
   "    -> General
   "    -> VIM user interface
   "    -> Colors and Fonts
   "    -> Files and backups
   "    -> Text, tab and indent related
   "    -> Visual mode related
   "    -> Moving around, tabs and buffers
   "    -> Status line
   "    -> Editing mappings
   "    -> vimgrep searching and cope displaying
   "    -> Spell checking
   "    -> Misc
   "    -> Helper functions
   "
   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   " => General
   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   " Sets how many lines of history VIM has to remember
   set history=500

   " Enable filetype plugins
   filetype plugin on
   filetype indent on

   " Set to auto read when a file is changed from the outside
   set autoread

   " Fast saving
   nmap <leader>w :w!<cr>

   " :W sudo saves the file 
   " (useful for handling the permission-denied error)


   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   " => VIM user interface
   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   " Set 7 lines to the cursor - when moving vertically using j/k
   set so=7

   " Avoid garbled characters in Chinese language windows OS
   let $LANG='en' 
   set langmenu=en
   source $VIMRUNTIME/delmenu.vim
   source $VIMRUNTIME/menu.vim

   " Turn on the WiLd menu
   set wildmenu

   " Ignore compiled files
   set wildignore=*.o,*~,*.pyc
   if has("win16") || has("win32")
       set wildignore+=*/.git/*,*/.hg/*,*/.svn/*,*/.DS_Store
   else
       set wildignore+=.git\*,.hg\*,.svn\*
   endif

   "Always show current position
   set ruler

   " Height of the command bar
   set cmdheight=2

   " A buffer becomes hidden when it is abandoned
   set hid

   " Configure backspace so it acts as it should act
   set backspace=eol,start,indent
   set whichwrap+=<,>,h,l

   " In many terminal emulators the mouse works just fine, thus enable it.
   if has('mouse')
     set mouse=a
   endif

   " Ignore case when searching
   set ignorecase

   " When searching try to be smart about cases 
   set smartcase

   " Highlight search results
   set hlsearch

   " Makes search act like search in modern browsers
   set incsearch 

   " Don't redraw while executing macros (good performance config)
   set lazyredraw 

   " For regular expressions turn magic on
   set magic

   " Show matching brackets when text indicator is over them
   set showmatch 
   " How many tenths of a second to blink when matching brackets
   set mat=2

   " No annoying sound on errors
   set noerrorbells
   set novisualbell
   set t_vb=
   set tm=500

   " Add a bit extra margin to the left
   set foldcolumn=1


   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   " => Colors and Fonts
   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   " Enable syntax highlighting
   syntax enable 

   try
       colorscheme desert
   catch
   endtry

   set background=dark

   " Set extra options when running in GUI mode
   if has("gui_running")
       set guioptions-=T
       set guioptions-=e
       set t_Co=256
       set guitablabel=%M\ %t
   endif

   " Set utf8 as standard encoding and en_US as the standard language
   set encoding=utf8

   " Use Unix as the standard file type
   set ffs=unix,dos,mac


   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   " => Files, backups and undo
   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   " Turn backup off, since most stuff is in SVN, git et.c anyway...
   set nobackup
   set nowb
   set noswapfile


   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   " => Text, tab and indent related
   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   " Use spaces instead of tabs
   set expandtab

   " Be smart when using tabs ;)
   set smarttab

   " 1 tab == 4 spaces
   set shiftwidth=4
   set tabstop=4

   " Linebreak on 500 characters
   set lbr
   set tw=500

   set ai "Auto indent
   set si "Smart indent
   set wrap "Wrap lines


   """"""""""""""""""""""""""""""
   " => Visual mode related
   """"""""""""""""""""""""""""""
   " Visual mode pressing * or # searches for the current selection
   " Super useful! From an idea by Michael Naumann
   vnoremap <silent> * :call VisualSelection('f', '')<CR>
   vnoremap <silent> # :call VisualSelection('b', '')<CR>


   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   " => Moving around, tabs, windows and buffers
   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   " Treat long lines as break lines (useful when moving around in them)
   map j gj
   map k gk

   " Map <Space> to / (search) and Ctrl-<Space> to ? (backwards search)
   map <space> /
   map <c-space> ?

   " Disable highlight when <leader><cr> is pressed
   map <silent> <leader><cr> :noh<cr>

   " Smart way to move between windows
   map <C-j> <C-W>j
   map <C-k> <C-W>k
   map <C-h> <C-W>h
   map <C-l> <C-W>l

   " Close the current buffer
   map <leader>bd :Bclose<cr>

   " Close all the buffers
   map <leader>ba :bufdo bd<cr>

   " Useful mappings for managing tabs
   map <leader>tn :tabnew<cr>
   map <leader>to :tabonly<cr>
   map <leader>tc :tabclose<cr>
   map <leader>tm :tabmove 
   map <leader>t<leader> :tabnext 

   " Let 'tl' toggle between this and the last accessed tab
   let g:lasttab = 1
   nmap <Leader>tl :exe "tabn ".g:lasttab<CR>
   au TabLeave * let g:lasttab = tabpagenr()


   " Opens a new tab with the current buffer's path
   " Super useful when editing files in the same directory
   map <leader>te :tabedit <c-r>=expand("%:p:h")<cr>/

   " Switch CWD to the directory of the open buffer
   map <leader>cd :cd %:p:h<cr>:pwd<cr>

   " Specify the behavior when switching between buffers 
   try
     set switchbuf=useopen,usetab,newtab
     set stal=2
   catch
   endtry

   " Return to last edit position when opening files (You want this!)
   " autocmd BufReadPost *
   "      \ if line("'\"") > 0 && line("'\"") <= line("$") |
   "      \   exe "normal! g`\"" |
   "      \ endif
   " Remember info about open buffers on close
   " set viminfo^=%


   """"""""""""""""""""""""""""""
   " => Status line
   """"""""""""""""""""""""""""""
   " Always show the status line
   set laststatus=2

   " Format the status line
   set statusline=\ %{HasPaste()}%F%m%r%h\ %w\ \ CWD:\ %r%{getcwd()}%h\ \ \ Line:\ %l


   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   " => Editing mappings
   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   " Remap VIM 0 to first non-blank character
   map 0 ^

   " Move a line of text using ALT+[jk] or Comamnd+[jk] on mac
   nmap <M-j> mz:m+<cr>`z
   nmap <M-k> mz:m-2<cr>`z
   vmap <M-j> :m'>+<cr>`<my`>mzgv`yo`z
   vmap <M-k> :m'<-2<cr>`>my`<mzgv`yo`z

   if has("mac") || has("macunix")
     nmap <D-j> <M-j>
     nmap <D-k> <M-k>
     vmap <D-j> <M-j>
     vmap <D-k> <M-k>
   endif

   " Delete trailing white space on save, useful for Python and CoffeeScript ;)
   func! DeleteTrailingWS()
     exe "normal mz"
     %s/\s\+$//ge
     exe "normal `z"
   endfunc
   autocmd BufWrite *.py :call DeleteTrailingWS()
   autocmd BufWrite *.coffee :call DeleteTrailingWS()


   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   " => Ag searching and cope displaying
   "    requires ag.vim - it's much better than vimgrep/grep
   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   " When you press gv you Ag after the selected text
   vnoremap <silent> gv :call VisualSelection('gv', '')<CR>

   " Open Ag and put the cursor in the right position
   map <leader>g :Ag 

   " When you press <leader>r you can search and replace the selected text
   vnoremap <silent> <leader>r :call VisualSelection('replace', '')<CR>

   " Do :help cope if you are unsure what cope is. It's super useful!
   "
   " When you search with Ag, display your results in cope by doing:
   "   <leader>cc
   "
   " To go to the next search result do:
   "   <leader>n
   "
   " To go to the previous search results do:
   "   <leader>p
   "
   map <leader>cc :botright cope<cr>
   map <leader>co ggVGy:tabnew<cr>:set syntax=qf<cr>pgg
   map <leader>n :cn<cr>
   map <leader>p :cp<cr>


   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   " => Spell checking
   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   " Pressing ,ss will toggle and untoggle spell checking
   map <leader>ss :setlocal spell!<cr>

   " Shortcuts using <leader>
   map <leader>sn ]s
   map <leader>sp [s
   map <leader>sa zg
   map <leader>s? z=


   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   " => Misc
   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   " Remove the Windows ^M - when the encodings gets messed up
   noremap <Leader>m mmHmt:%s/<C-V><cr>//ge<cr>'tzt'm

   " Quickly open a buffer for scribble
   map <leader>q :e ~/buffer<cr>

   " Quickly open a markdown buffer for scribble
   map <leader>x :e ~/buffer.md<cr>

   " Toggle paste mode on and off
   map <leader>pp :setlocal paste!<cr>




   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   " => Helper functions
   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   function! CmdLine(str)
       exe "menu Foo.Bar :" . a:str
       emenu Foo.Bar
       unmenu Foo
   endfunction 

   function! VisualSelection(direction, extra_filter) range
       let l:saved_reg = @"
       execute "normal! vgvy"

       let l:pattern = escape(@", '\\/.*$^~[]')
       let l:pattern = substitute(l:pattern, "\n$", "", "")

       if a:direction == 'b'
           execute "normal ?" . l:pattern . "^M"
       elseif a:direction == 'gv'
           call CmdLine("Ag \"" . l:pattern . "\" " )
       elseif a:direction == 'replace'
           call CmdLine("%s" . '/'. l:pattern . '/')
       elseif a:direction == 'f'
           execute "normal /" . l:pattern . "^M"
       endif

       let @/ = l:pattern
       let @" = l:saved_reg
   endfunction


   " Returns true if paste mode is enabled
   function! HasPaste()
       if &paste
           return 'PASTE MODE  '
       endif
       return ''
   endfunction

   " Don't close window, when deleting a buffer
   command! Bclose call <SID>BufcloseCloseIt()
   function! <SID>BufcloseCloseIt()
      let l:currentBufNum = bufnr("%")
      let l:alternateBufNum = bufnr("#")

      if buflisted(l:alternateBufNum)
        buffer #
      else
        bnext
      endif

      if bufnr("%") == l:currentBufNum
        new
      endif

      if buflisted(l:currentBufNum)
        execute("bdelete! ".l:currentBufNum)
      endif
   endfunction
   ``````

   3. vim ~/.vimrc

   4. :PluginInstall

      ### References:

      1. https://github.com/VundleVim/Vundle.vim

      2. https://www.digitalocean.com/community/tutorials/how-to-use-vundle-to-manage-vim-plugins-on-a-linux-vps
      4. https://jdblischak.github.io/2014-09-18-chicago/novice/git/05-sshkeys.html
      5. http://virtualenvwrapper.readthedocs.io/en/latest/install.html
      6. https://gist.github.com/githubteacher/e75edf29d76571f8cc6c

         ​
