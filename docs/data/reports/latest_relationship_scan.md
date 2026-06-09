# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-09T16:07:27.904474+00:00`
- Price records: `672`
- Market context records: `3398`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13074`

## Conditions

- `news_risk_high`: News Risk is elevated.
- `macro_risk_high`: Macro Risk is elevated.
- `risk_on_high`: Risk-On score is elevated.
- `market_context_high`: Market Context is supportive.
- `polymarket_volume_spike`: Polymarket 24h volume z-score is elevated.
- `flow_alert_high`: Flow Alert score is elevated.
- `news_and_polymarket`: News Risk and Polymarket volume spike happen together.
- `risk_on_and_context`: Risk-On and Market Context are both supportive.
- `macro_and_flow`: Macro Risk and Flow Alert are elevated together.

## Top Patterns

- `risk_on_high->crypto_major_24h` score `55.661` n `32` status `ready` deltaP `58.3333` edge `4.2538` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `55.661` n `32` status `ready` deltaP `58.3333` edge `4.2538` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `54.4692` n `32` status `ready` deltaP `56.0764` edge `4.1804` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `54.4692` n `32` status `ready` deltaP `56.0764` edge `4.1804` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `45.5141` n `32` status `ready` deltaP `56.0764` edge `3.419` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `45.5141` n `32` status `ready` deltaP `56.0764` edge `3.419` maxDD `0.0`
- `risk_on_high->index_24h` score `23.3747` n `32` status `ready` deltaP `51.3889` edge `1.6053` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.3747` n `32` status `ready` deltaP `51.3889` edge `1.6053` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `20.8143` n `155` status `ready` deltaP `17.2659` edge `2.4179` maxDD `-56.8787`
- `market_context_high->crypto_major_24h` score `19.6191` n `155` status `ready` deltaP `24.0389` edge `2.3176` maxDD `-60.435`
- `market_context_high->equity_24h` score `19.335` n `155` status `ready` deltaP `32.8506` edge `2.0943` maxDD `-45.1644`
- `risk_on_high->crypto_major_4h` score `15.2398` n `32` status `ready` deltaP `28.2012` edge `1.1942` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.2398` n `32` status `ready` deltaP `28.2012` edge `1.1942` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `13.6146` n `32` status `ready` deltaP `28.9931` edge `0.9674` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `13.6146` n `32` status `ready` deltaP `28.9931` edge `0.9674` maxDD `-0.7574`
- `market_context_high->index_24h` score `12.0533` n `155` status `ready` deltaP `35.905` edge `1.0004` maxDD `-15.4929`
- `risk_on_high->crypto_alt_4h` score `6.9596` n `32` status `ready` deltaP `8.3079` edge `0.709` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `6.9596` n `32` status `ready` deltaP `8.3079` edge `0.709` maxDD `-11.7537`
- `market_context_high->metal_24h` score `4.04` n `155` status `ready` deltaP `23.4689` edge `0.8699` maxDD `-29.6733`
- `risk_on_high->equity_4h` score `3.9432` n `32` status `ready` deltaP `15.7774` edge `0.5138` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
