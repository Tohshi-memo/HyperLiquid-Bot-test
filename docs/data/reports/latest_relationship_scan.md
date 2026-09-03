# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T15:37:28.004596+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11625`

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

- `risk_on_high->unknown_4h` score `33.4602` n `133` status `ready` deltaP `12.657` edge `2.7658` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `33.4602` n `133` status `ready` deltaP `12.657` edge `2.7658` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `26.6952` n `167` status `ready` deltaP `14.2553` edge `2.1991` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `18.2045` n `133` status `ready` deltaP `1.0422` edge `1.5678` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `18.2045` n `133` status `ready` deltaP `1.0422` edge `1.5678` maxDD `-1.95`
- `market_context_high->unknown_1h` score `13.7247` n `167` status `ready` deltaP `1.497` edge `1.1968` maxDD `-2.0446`
- `market_context_high->equity_24h` score `3.2012` n `127` status `ready` deltaP `20.9905` edge `0.5614` maxDD `-20.7654`
- `news_risk_high->crypto_alt_24h` score `3.1033` n `67` status `ready` deltaP `20.5664` edge `0.5542` maxDD `-19.4761`
- `risk_on_high->equity_24h` score `2.7183` n `107` status `ready` deltaP `16.2367` edge `0.5328` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `2.7183` n `107` status `ready` deltaP `16.2367` edge `0.5328` maxDD `-19.828`
- `news_risk_high->crypto_major_24h` score `2.6155` n `67` status `ready` deltaP `17.0632` edge `0.6599` maxDD `-30.7329`
- `news_risk_high->equity_24h` score `1.5656` n `67` status `ready` deltaP `8.6624` edge `0.3897` maxDD `-15.4056`
- `risk_on_high->crypto_alt_24h` score `0.8505` n `107` status `ready` deltaP `16.3957` edge `0.6901` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `0.8505` n `107` status `ready` deltaP `16.3957` edge `0.6901` maxDD `-42.8959`
- `market_context_high->crypto_alt_24h` score `0.5715` n `127` status `ready` deltaP `18.0514` edge `0.7028` maxDD `-46.3234`
- `news_risk_high->commodity_4h` score `0.3017` n `67` status `ready` deltaP `6.4047` edge `0.0319` maxDD `-0.8733`
- `news_risk_high->fx_4h` score `0.0677` n `67` status `ready` deltaP `9.9563` edge `0.0049` maxDD `-1.2507`
- `risk_on_high->metal_1h` score `0.033` n `133` status `ready` deltaP `11.2152` edge `0.0007` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.033` n `133` status `ready` deltaP `11.2152` edge `0.0007` maxDD `-1.699`
- `news_risk_high->index_1h` score `-0.0555` n `67` status `ready` deltaP `4.6251` edge `-0.0026` maxDD `-0.8275`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
