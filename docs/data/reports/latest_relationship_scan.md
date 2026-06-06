# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T04:22:21.133192+00:00`
- Price records: `672`
- Market context records: `3037`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6988`

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

- `market_context_high->crypto_alt_24h` score `23.6542` n `99` status `ready` deltaP `11.6793` edge `2.285` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `13.2118` n `99` status `ready` deltaP `23.4533` edge `0.9911` maxDD `-1.7175`
- `market_context_high->commodity_24h` score `12.8777` n `99` status `ready` deltaP `42.3769` edge `0.8147` maxDD `-1.2589`
- `market_context_high->equity_24h` score `8.5212` n `99` status `ready` deltaP `22.8536` edge `1.2153` maxDD `-18.3486`
- `market_context_high->index_24h` score `8.2221` n `99` status `ready` deltaP `22.4432` edge `0.6611` maxDD `-4.7103`
- `market_context_high->commodity_4h` score `2.7921` n `127` status `ready` deltaP `18.8833` edge `0.1715` maxDD `-2.8438`
- `market_context_high->commodity_1h` score `0.0265` n `129` status `ready` deltaP `2.2908` edge `0.0292` maxDD `-1.7142`
- `market_context_high->unknown_4h` score `-0.3115` n `127` status `ready` deltaP `2.247` edge `0.0644` maxDD `-3.7602`
- `market_context_high->index_1h` score `-0.3811` n `129` status `ready` deltaP `4.2369` edge `0.0243` maxDD `-4.1126`
- `market_context_high->equity_1h` score `-0.4668` n `129` status `ready` deltaP `3.7182` edge `0.0369` maxDD `-6.7232`
- `market_context_high->crypto_alt_1h` score `-0.5022` n `129` status `ready` deltaP `6.5358` edge `0.105` maxDD `-14.7034`
- `market_context_high->fx_1h` score `-0.5408` n `129` status `ready` deltaP `-4.8891` edge `0.0001` maxDD `-0.2801`
- `market_context_high->index_4h` score `-0.6731` n `127` status `ready` deltaP `12.8661` edge `0.0687` maxDD `-14.9283`
- `market_context_high->unknown_1h` score `-0.7398` n `129` status `ready` deltaP `4.2206` edge `-0.0167` maxDD `-3.1801`
- `market_context_high->crypto_major_1h` score `-0.9497` n `129` status `ready` deltaP `4.4295` edge `0.075` maxDD `-15.1032`
- `market_context_high->metal_1h` score `-1.1232` n `129` status `ready` deltaP `-1.649` edge `-0.0012` maxDD `-6.8783`
- `market_context_high->fx_4h` score `-1.1465` n `127` status `ready` deltaP `-9.0803` edge `-0.0036` maxDD `-0.9616`
- `market_context_high->fx_24h` score `-1.44` n `99` status `ready` deltaP `-2.1464` edge `-0.0185` maxDD `-0.6418`
- `market_context_high->crypto_alt_4h` score `-1.9896` n `127` status `ready` deltaP `18.3035` edge `0.3061` maxDD `-48.9893`
- `market_context_high->equity_4h` score `-2.3602` n `127` status `ready` deltaP `9.7153` edge `0.0657` maxDD `-30.3113`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
