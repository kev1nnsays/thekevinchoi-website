# WebAssembly demos (C++ and Python)

## Overview
The Demos page provides interactive, client-side demos for C++ (WebAssembly) and Python (Pyodide). The page is static and only loads JavaScript on the client.

- Demos page: [src/pages/demos/index.astro](../src/pages/demos/index.astro)
- C++ demo component: [src/components/CppWasmDemo.astro](../src/components/CppWasmDemo.astro)
- Python demo component: [src/components/PyodideDemo.astro](../src/components/PyodideDemo.astro)

## C++ demo (WASM)
The C++ demo expects a standalone WebAssembly module at:
```
/public/demos/cpp/hello.wasm
```
The module must export a function named `add(a, b)`.

Example Emscripten build (from the repo root):
```
emcc hello.cpp -O3 -s STANDALONE_WASM=1 -Wl,--export=add -Wl,--no-entry -o public/demos/cpp/hello.wasm
```

The UI is in `CppWasmDemo.astro` and loads the module with `WebAssembly.instantiateStreaming()`.

## Python demo (Pyodide)
The Python demo loads Pyodide from a CDN on demand and runs user-provided Python in the browser. The loader and runner live in `PyodideDemo.astro`.

- CDN used: https://cdn.jsdelivr.net/pyodide/v0.26.2/full/
- No server is required; execution is fully client-side.

## Customizing
- Swap the WASM module path or exported function names in `CppWasmDemo.astro`.
- Modify the Python textarea content and output handling in `PyodideDemo.astro`.
