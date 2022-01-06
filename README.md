# Build
Run `./build.sh v21.11.3.6`

# Where/How do I get the document?

The doc can be built using the canonical repo with some `mkdocs` tweak.

- Clone the repo: https://github.com/ClickHouse/ClickHouse
- Clone this repo too. of course.
- in the ClickHouse repo, go into the `docs/tools` dir and run the following command:
  ```
  ./build.py --skip-single-page --skip-pdf --lang en --theme-dir PATH_TO_THIS_REPO/mkdocs_tmpl
  ```

The mkdocs\_tmpl was copied from the `clickhouse/website` and some changes were made to the templates.

The following lines should be added to the `website/css/base.css`:

```
[id]::before {
  content: '';
  display: block;
  height:      75px;
  margin-top: -75px;
  visibility: hidden;
}
```
