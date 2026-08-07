# hermes-crawl4ai

A [Hermes Agent](https://github.com/NousResearch/hermes-agent) plugin that
routes the native `web_extract` tool to a user-managed
[Crawl4AI](https://github.com/unclecode/crawl4ai) instance.

The plugin registers a `WebSearchProvider` through
`ctx.register_web_search_provider(...)`, integrating with Hermes' native web
tooling without introducing custom tool names. It supports extraction only;
configure another search-capable provider when you also need `web_search`.

## Why This Fork Exists

This fork is for users who already manage their own Crawl4AI infrastructure and
do not need bundled deployment scripts, research skills, or a persistence tool.
It was created in response to the requirements described in
[upstream issue #1](https://github.com/GoSlowPoke168/hermes-crawl4searxng/issues/1).

## Use With Hermes

Install and enable the plugin with the Hermes CLI:

```bash
hermes plugins install SolerSoft/hermes-crawl4ai
hermes plugins enable hermes-crawl4ai
```

Hermes prompts for the required environment variables during installation. To
configure them manually, set the following values in the Hermes environment
file:

| Environment variable | Purpose                                                                  |
| -------------------- | ------------------------------------------------------------------------ |
| `CRAWL4AI_URL`       | Base URL for your Crawl4AI instance, for example `http://crawl4ai:11235` |
| `CRAWL4AI_API_TOKEN` | Bearer token accepted by your Crawl4AI instance                          |

Your Crawl4AI service must be reachable at `CRAWL4AI_URL` and accept `POST /md`
requests. The plugin sends the configured token as a bearer token when one is
supplied.

## Plugin Behavior

For each URL passed to `web_extract`, the provider requests filtered Markdown
from Crawl4AI's `/md` endpoint and returns the result to Hermes. A failed
request returns an error entry for only the affected URL, without preventing
results for other URLs.

## Troubleshooting

- **Plugin not listed or loaded**: run `hermes plugins list`, then enable
  `hermes-crawl4ai` with `hermes plugins enable hermes-crawl4ai`.
- **`web_extract` errors**: verify `CRAWL4AI_URL` is reachable from Hermes and
  `CRAWL4AI_API_TOKEN` matches the token configured by your Crawl4AI service.

## License

[MIT License](LICENSE)
