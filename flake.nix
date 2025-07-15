{
  description = "Python 3.13 project with uv";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils, ... }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
        python = pkgs.python313;
      in
      {
        devShells.default = pkgs.mkShell {
          buildInputs = [
            python
            pkgs.uv
            pkgs.go-task
          ];

          shellHook = ''
            export UV_PYTHON_DOWNLOADS=never
            export UV_PYTHON="${python}/bin/python"
            export PATH="$HOME/.local/bin:$PATH"
            echo "Python 3.13 and uv environment ready!"
            echo "Python version: $(${python}/bin/python --version)"
            echo "uv version: $(uv --version)"
          '';
        };
      }
    );
}
