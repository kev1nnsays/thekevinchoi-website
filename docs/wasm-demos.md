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

### 1) Write C++
Create a small C++ file (example: `hello.cpp`) that exports a function. Keep the function `extern "C"` to avoid name mangling:
```
// hello.cpp
extern "C" {
	int add(int a, int b) {
		return a + b;
	}
}
```

### 2) Build to WASM
Install Emscripten locally, then build with a standalone module that exports `add`.

Example build (from the repo root):
```
emcc hello.cpp -O3 -s STANDALONE_WASM=1 -Wl,--export=add -Wl,--no-entry -o public/demos/cpp/hello.wasm
```

Notes:
- `-s STANDALONE_WASM=1` produces a raw `.wasm` module without the JS runtime.
- `--no-entry` is used because there is no `main()`.
- `--export=add` makes `add` available as `instance.exports.add`.

### 3) Embed in the site
The UI and loader live in [src/components/CppWasmDemo.astro](../src/components/CppWasmDemo.astro). It fetches `/demos/cpp/hello.wasm` and calls `instance.exports.add(a, b)`.

If you change the module path or export name, update the component:
- Module path: change the `fetch("/demos/cpp/hello.wasm")` line.
- Export name: change the `instance.exports.add` lookup.

### 4) Hosting notes
`WebAssembly.instantiateStreaming()` requires the server to serve `.wasm` with the `application/wasm` MIME type. Netlify does this by default.

## Python demo (Pyodide)
The Python demo loads Pyodide from a CDN on demand and runs user-provided Python in the browser. The loader and runner live in `PyodideDemo.astro`.

- CDN used: https://cdn.jsdelivr.net/pyodide/v0.26.2/full/
- No server is required; execution is fully client-side.

### 1) Write Python
The default demo lets users type Python in a textarea. You can prefill it with a script or read code from another source.

Example default code:
```
print("Hello from Pyodide")
for i in range(3):
		print(i)
```

### 2) Load Pyodide
The component loads the Pyodide runtime when the user clicks “Run” by injecting:
```
https://cdn.jsdelivr.net/pyodide/v0.26.2/full/pyodide.js
```
and then calls:
```
loadPyodide({ indexURL: "https://cdn.jsdelivr.net/pyodide/v0.26.2/full/" })
```

### 3) Run code
The demo executes the textarea via:
```
pyodide.runPythonAsync(code)
```
and prints the return value in the output area. `print()` output goes to the browser console by default. If you want `print()` to render in the UI, you can redirect stdout inside the component.

### 4) Use Python packages
Pyodide can install pure-Python packages at runtime using `micropip`:
```
await pyodide.loadPackage("micropip")
await pyodide.runPythonAsync(`
	import micropip
	await micropip.install("requests")
`)
```
Prefer packages that are pure Python or already bundled with Pyodide.

## Customizing
- Swap the WASM module path or exported function names in `CppWasmDemo.astro`.
- Modify the Python textarea content and output handling in `PyodideDemo.astro`.
