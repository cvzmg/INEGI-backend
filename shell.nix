let
  pkgs = import <nixpkgs> {};
in
pkgs.mkShell {
  buildInputs = [
    pkgs.python310
    pkgs.gcc
    pkgs.zeromq
    # Add additional dependencies that might be needed
    pkgs.pkg-config
    pkgs.libffi
    pkgs.openssl
    pkgs.zlib  # <-- Add zlib here
  ];
  
  # Fixed LD_LIBRARY_PATH - this is the key fix
  LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
    pkgs.stdenv.cc.cc.lib  # This provides libstdc++.so.6
    pkgs.zeromq
    pkgs.libffi
    pkgs.openssl
    pkgs.zlib  # <-- And also here
  ];
  
  shellHook = ''
    unset SOURCE_DATE_EPOCH
    if [ ! -d ".venv" ]; then
      echo "Creating Python virtual environment..."
      python -m venv .venv
      source .venv/bin/activate
      echo "Installing packages from requirements.txt..."
      pip install -r requirements.txt
    else
      source .venv/bin/activate
    fi
    echo "Nix shell is ready. You can now run 'jupyter notebook'."
  '';
}
