# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T19:22:34.193807+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11685`

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

- `risk_on_high->unknown_4h` score `29.7912` n `133` status `ready` deltaP `12.1997` edge `2.4631` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `29.7912` n `133` status `ready` deltaP `12.1997` edge `2.4631` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `23.0262` n `167` status `ready` deltaP `13.798` edge `1.8964` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `16.2509` n `133` status `ready` deltaP `1.0422` edge `1.405` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `16.2509` n `133` status `ready` deltaP `1.0422` edge `1.405` maxDD `-1.95`
- `market_context_high->unknown_1h` score `11.7711` n `167` status `ready` deltaP `1.497` edge `1.034` maxDD `-2.0446`
- `market_context_high->equity_24h` score `1.8205` n `127` status `ready` deltaP `18.3863` edge `0.4637` maxDD `-20.7654`
- `news_risk_high->crypto_alt_24h` score `1.3837` n `67` status `ready` deltaP `17.9623` edge `0.3511` maxDD `-19.4761`
- `risk_on_high->equity_24h` score `1.3376` n `107` status `ready` deltaP `13.6325` edge `0.4351` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `1.3376` n `107` status `ready` deltaP `13.6325` edge `0.4351` maxDD `-19.828`
- `news_risk_high->crypto_major_24h` score `0.7384` n `67` status `ready` deltaP `14.459` edge `0.4366` maxDD `-30.7329`
- `news_risk_high->equity_24h` score `0.6681` n `67` status `ready` deltaP `6.0582` edge `0.292` maxDD `-15.4056`
- `news_risk_high->commodity_4h` score `0.4316` n `67` status `ready` deltaP `7.7767` edge `0.0394` maxDD `-0.8733`
- `risk_on_high->metal_1h` score `0.0782` n `133` status `ready` deltaP `11.9637` edge `0.0015` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0782` n `133` status `ready` deltaP `11.9637` edge `0.0015` maxDD `-1.699`
- `news_risk_high->fx_4h` score `0.0739` n `67` status `ready` deltaP `10.1088` edge `0.0044` maxDD `-1.2507`
- `news_risk_high->index_1h` score `-0.0671` n `67` status `ready` deltaP `4.4754` edge `-0.0031` maxDD `-0.8275`
- `risk_on_high->index_1h` score `-0.1053` n `133` status `ready` deltaP `4.8906` edge `-0.0016` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.1053` n `133` status `ready` deltaP `4.8906` edge `-0.0016` maxDD `-0.5605`
- `news_risk_high->commodity_1h` score `-0.1418` n `67` status `ready` deltaP `4.7569` edge `0.0011` maxDD `-0.9036`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
