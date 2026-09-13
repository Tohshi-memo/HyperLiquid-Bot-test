# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T11:22:30.304363+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12968`

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

- `market_context_high->unknown_24h` score `16680.5736` n `59` status `ready` deltaP `14.3688` edge `1389.9572` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `403.7175` n `82` status `ready` deltaP `-5.1008` edge `33.7193` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `17.9444` n `82` status `ready` deltaP `33.444` edge `1.3212` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `17.9254` n `82` status `ready` deltaP `37.8512` edge `1.3885` maxDD `-9.098`
- `market_context_high->crypto_alt_24h` score `10.2246` n `59` status `ready` deltaP `23.3986` edge `0.7788` maxDD `-3.9523`
- `market_context_high->equity_24h` score `9.0426` n `59` status `ready` deltaP `44.284` edge `0.5343` maxDD `-4.4114`
- `news_risk_high->equity_24h` score `7.7203` n `82` status `ready` deltaP `22.2708` edge `0.6729` maxDD `-6.5742`
- `news_risk_high->index_24h` score `6.6514` n `82` status `ready` deltaP `47.4222` edge `0.2558` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `4.578` n `82` status `ready` deltaP `24.2431` edge `0.2653` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `4.0508` n `59` status `ready` deltaP `40.0` edge `0.0709` maxDD `0.0`
- `market_context_high->index_24h` score `3.8022` n `59` status `ready` deltaP `41.242` edge `0.084` maxDD `-0.7014`
- `market_context_high->metal_24h` score `0.9115` n `59` status `ready` deltaP `13.5155` edge `0.1142` maxDD `-1.9958`
- `risk_on_high->crypto_alt_4h` score `0.5492` n `65` status `ready` deltaP `11.5152` edge `0.1611` maxDD `-6.7304`
- `risk_on_and_context->crypto_alt_4h` score `0.5492` n `65` status `ready` deltaP `11.5152` edge `0.1611` maxDD `-6.7304`
- `news_risk_high->index_4h` score `0.429` n `82` status `ready` deltaP `12.6496` edge `0.0335` maxDD `-0.6935`
- `risk_on_high->fx_1h` score `0.1101` n `65` status `ready` deltaP `4.7029` edge `0.0034` maxDD `-0.0464`
- `risk_on_and_context->fx_1h` score `0.1101` n `65` status `ready` deltaP `4.7029` edge `0.0034` maxDD `-0.0464`
- `market_context_high->fx_1h` score `-0.0187` n `142` status `ready` deltaP `4.5079` edge `-0.0008` maxDD `-0.5323`
- `risk_on_high->metal_1h` score `-0.0724` n `65` status `ready` deltaP `3.7632` edge `0.0019` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `-0.0724` n `65` status `ready` deltaP `3.7632` edge `0.0019` maxDD `-0.3081`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
