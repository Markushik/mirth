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
      in
      {
        devShells.default = pkgs.mkShell {
          buildInputs = [
            pkgs.rye
            pkgs.go-task
            pkgs.elixir
          ];

          shellHook = ''
            export PATH="$HOME/.local/bin:$PATH"
          '';
        };
      }
    );
}
