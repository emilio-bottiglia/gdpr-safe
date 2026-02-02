# Changelog
## v1.1 - 2026-02-02
### Changed
-Replace PDF scanner library PyPDF2 (deprecated) with library pymupdf
-Replace 'keyWords'variable in each scanner function with '*_key_words' to hold temporary list of key words
-Replace app screenshot in README with newer version function
### Added
-Add screenshot of csv report in README
-Add main()  function to start scanner
### Removed
-Some redundant parenthesis in scanners' loop
### Fixed
-If multiple file type with same extension were in the scanned folder, scanner held track only of key words of one file. This has now fixed by adding a new list 'list_of_lists' in each scanner
