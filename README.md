# KoboldCaves

**KoboldCaves** is a Python-based TCP port scanner developed as a cybersecurity learning project. It explores network communication, socket programming, concurrent execution, and basic service identification by implementing core scanning functionality from the ground up.

The goal of this project is to better understand how network scanning tools work internally, rather than replace established tools such as Nmap.

## Features

- **TCP Port Scanning:** Attempts TCP connections to a specified range of ports to identify accessible services.
- **Concurrent Scanning:** Uses Python's `ThreadPoolExecutor` to scan multiple ports concurrently.
- **Connection Classification:** Separates ports into open, closed, and other connection errors.
- **Service Name Lookup:** Uses Python's socket service database to look up registered TCP service names for open ports.
- **Basic Banner Detection:** Attempts to retrieve information provided by services after connecting. For HTTP requests on selected ports, the scanner sends a basic HTTP request before reading the response.
- **Input Validation:** Validates IPv4 addresses and port ranges before scanning.
- **Scan Timing:** Measures and reports how long a scan takes.
- **Interactive Interface:** Prompts users for a target address, port range, and the results they want to view.

## Technologies

- Python 3
- TCP/IP networking
- Python `socket` library
- `concurrent.futures`
- Exception handling and input validation

The project uses Python's standard library and does not currently require third-party packages.

## Project Structure

```text
WardenWatch/
├── koboldcaves.py
├── port_scans.py
├── server_ports.py
└── README.md
```

- **`koboldcaves.py`**: Entry point that starts the interactive scanner.
- **`port_scans.py`**: Contains the port scanning logic, concurrent execution, input validation, timing, and reporting.
- **`server_ports.py`**: Contains the service name lookup function.

## Getting Started

### Requirements

- Python 3
- A terminal or command-line interface
- Permission to scan the target system

### Installation

Clone the repository:

```bash
git clone <https://github.com/kingkobold27/KoboldCaves/tree/main>
cd KoboldCaves
```

No additional package installation is currently required.

### Usage

Run the program from the project directory:

```bash
python3 koboldcaves.py
```

Follow the interactive prompts to:

1. Enter an IPv4 address.
2. Specify the starting and ending ports.
3. Review open ports and scan statistics.
4. Optionally view registered service names, closed ports, other connection errors, and detected banners.

The scanner uses an exclusive upper port bound. For example, scanning ports `8000` to `8100` checks ports `8000` through `8099`.

## Example

A local HTTP server can be used to test the scanner in a controlled environment.

Start a test server in one terminal:

```bash
python3 -m http.server 8080
```

Run WardenWatch in another terminal and scan `127.0.0.1` over a range that includes port `8080`.

Example banner output:

```text
8080 HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.13.7
Content-type: text/html; charset=utf-8
```

Actual output depends on the target, its services, and the environment.

## Limitations

WardenWatch is an educational project and has several limitations:

- **TCP only:** The scanner currently checks TCP ports and does not perform UDP scanning.
- **Basic service identification:** Registered service names are looked up locally and do not confirm which application is actually running.
- **Limited banner detection:** Some services send banners immediately, while others require protocol-specific requests. The current implementation only sends an HTTP request on selected ports.
- **HTTPS and TLS:** The current HTTP request logic does not establish a TLS connection, so it is not designed to retrieve HTTPS responses.
- **Connection classification:** A failed connection does not necessarily mean a port is closed. Timeouts and other network errors may result from filtering, routing issues, or unavailable hosts.
- **Limited protocol coverage:** The scanner does not perform comprehensive service/version detection or operating system fingerprinting.
- **Performance:** Scan speed depends on the target, timeout settings, network conditions, and concurrency level.

## Learning Objectives

This project was built to develop practical experience with:

- TCP socket programming and connection handling
- Port scanning and basic network reconnaissance
- Concurrent execution using threads and futures
- Connection timeouts and error handling
- Service name lookups and banner-based identification
- Input validation, modular Python code, and reporting

## Future Improvements

Potential future enhancements include:

- More flexible protocol-aware banner detection
- Improved output formatting and exportable scan reports
- Configurable connection timeouts and concurrency
- Expanded automated testing and error handling
- Comparison of results against established scanning tools

## Responsible Use

WardenWatch is intended for educational use and authorized security testing. Only scan systems you own or have explicit permission to assess. Follow applicable laws, organizational policies, and testing agreements.

## Disclaimer

WardenWatch is an independent educational project and is not affiliated with or intended to replace Nmap or other established network scanning tools.