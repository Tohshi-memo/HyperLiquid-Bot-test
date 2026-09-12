# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T05:37:26.861674+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11399`

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

- `market_context_high->unknown_24h` score `1338.7535` n `133` status `ready` deltaP `13.9476` edge `111.475` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `383.4901` n `82` status `ready` deltaP `-3.6038` edge `32.0237` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `23.8994` n `59` status `ready` deltaP `54.505` edge `1.7183` maxDD `-5.8705`
- `risk_on_high->crypto_alt_24h` score `23.2421` n `81` status `ready` deltaP `42.4383` edge `1.6769` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `23.2421` n `81` status `ready` deltaP `42.4383` edge `1.6769` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `19.6216` n `133` status `ready` deltaP `36.581` edge `1.474` maxDD `-3.9523`
- `news_risk_high->crypto_alt_24h` score `17.4202` n `59` status `ready` deltaP `29.967` edge `1.3007` maxDD `-2.2369`
- `news_risk_high->equity_24h` score `12.091` n `59` status `ready` deltaP `33.5894` edge `0.7935` maxDD `-0.1212`
- `risk_on_high->equity_24h` score `9.0351` n `81` status `ready` deltaP `36.9792` edge `0.5064` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.0351` n `81` status `ready` deltaP `36.9792` edge `0.5064` maxDD `0.0`
- `market_context_high->equity_24h` score `8.7135` n `133` status `ready` deltaP `36.9792` edge `0.4796` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.1934` n `81` status `ready` deltaP `43.5373` edge `0.4297` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.1934` n `81` status `ready` deltaP `43.5373` edge `0.4297` maxDD `-1.9733`
- `news_risk_high->metal_24h` score `8.1446` n `59` status `ready` deltaP `50.8681` edge `0.3396` maxDD `0.0`
- `news_risk_high->index_24h` score `7.9345` n `59` status `ready` deltaP `51.4713` edge `0.3274` maxDD `-0.0797`
- `risk_on_high->crypto_major_4h` score `6.1218` n `81` status `ready` deltaP `29.9119` edge `0.3966` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `6.1218` n `81` status `ready` deltaP `29.9119` edge `0.3966` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `5.8498` n `81` status `ready` deltaP `20.544` edge `1.0198` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `5.8498` n `81` status `ready` deltaP `20.544` edge `1.0198` maxDD `-24.5429`
- `risk_on_high->index_24h` score `5.159` n `81` status `ready` deltaP `51.1574` edge `0.0931` maxDD `-0.0051`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
