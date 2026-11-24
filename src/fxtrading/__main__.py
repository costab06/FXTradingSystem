"""Minimal CLI entry point for FXTradingSystem."""

from . import __version__


def main() -> None:
    print(f"FXTradingSystem {__version__}")


if __name__ == "__main__":
    main()
