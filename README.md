# Simple Jade wrapper plugin

This plugin lets you transform Jade template strings and/ or complete such files from SublimeText 2.

## Requirements

1. NodeJS
2. Jade package
3. SublimeText 2

## Installation

Clone this repository into your SublimeText 2 Packages/ directory and (re)start SublimeText.

## Usage

Use the `Jade: Convert` command which is reachable via the context menu or the command palette (`Ctrl+Shift+P` or `Cmd+Shift+P` respectively).
When text is selected it will be send to the Jade shell command, otherwise the complete file content is transformed.
Either way, the original text is substituted for the transformed HTML output.