# Changelog
## v1.1.2 - 2026-02-17
### Changed
-Formerly list of key words is now a list of dictionary with term
categorization based on what is captured from GDPR documentation.
This change is in preparation of an important update, where in the report file we are going to have also
category and severity of key words 
## v1.1.1 - 2026-02-13
### Changed
-Replace os with pathlib for cross-platform paths (Windows/Linux/macOS) without worrying
about slashes. This will make the script os independent, usable in any platform
## v1.1 - 2026-02-02
### Changed
-Replace PDF scanner library PyPDF2 (deprecated) with library pymupdf

-Replace 'keyWords'variable in each scanner function with '*_key_words' to hold temporary list of key words

-Replace app screenshot in README with newer version
### Added
-Add screenshot of csv report in README

-Add main()  function to start scanner
### Removed
-Some redundant parenthesis in scanners' loop
### Fixed
-If multiple file type with same extension were in the scanned folder, scanner held track only of key words of one file. This has now fixed by adding a new list 'list_of_lists' in each scanner
