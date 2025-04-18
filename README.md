# mvm

Easily switch between `stable`, `pre-release`, and `bleeding` versions of MoonBit while sharing the same `credentials.json`, `index`, and `cache` directories.

```
$ tree $MOON_HOME
├── bin -> $MOON_HOME/mvm/bleeding/bin
├── include -> $MOON_HOME/mvm/bleeding/include
├── lib -> $MOON_HOME/mvm/bleeding/lib
├── credentials.json
├── mvm
│   ├── bleeding
│   ├── pre-release
│   └── stable
└── registry
    ├── cache
    └── index
```

## Installation

Install `mvm` using `pipx`:

```bash
pipx install git+https://github.com/lijunchen/mvm.git
```

## Usage

Install and switch between different versions of MoonBit:

```bash
# Install specific versions
mvm install stable
mvm install pre-release
mvm install bleeding

# Switch to a specific version
mvm use stable       # Use the stable version
mvm use pre-release  # Use the pre-release version
mvm use bleeding     # Use the bleeding-edge version
```

## Known Issues

MoonBit's installation script will add the following lines to your `~/.bashrc` or `~/.zshrc` automatically:

```bash
# moonbit
export PATH="$HOME/.moon/mvm/stable/bin:$PATH"

# moonbit
export PATH="$HOME/.moon/mvm/bleeding/bin:$PATH"
```

This will cause the `mvm` failed to switch version. To fix this, you need to comment them out to prevent installation scripts from modifying your `PATH`:

```bash
# moonbit
#export PATH="$HOME/.moon/mvm/stable/bin:$PATH"

# moonbit
#export PATH="$HOME/.moon/mvm/bleeding/bin:$PATH"
```
