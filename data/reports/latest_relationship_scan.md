# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-14T23:52:28.043312+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11796`

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

- `market_context_high->unknown_24h` score `136.4693` n `128` status `ready` deltaP `-30.1216` edge `11.8645` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `32.984` n `32` status `ready` deltaP `-43.4028` edge `4.5931` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `32.984` n `32` status `ready` deltaP `-43.4028` edge `4.5931` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `11.1145` n `36` status `ready` deltaP `16.493` edge `0.8542` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.6705` n `36` status `ready` deltaP `40.3963` edge `0.3699` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.9226` n `128` status `ready` deltaP `27.8645` edge `0.2302` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `4.4987` n `32` status `ready` deltaP `30.2083` edge `0.1735` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.4987` n `32` status `ready` deltaP `30.2083` edge `0.1735` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `3.4212` n `32` status `ready` deltaP `22.7431` edge `0.4026` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `3.4212` n `32` status `ready` deltaP `22.7431` edge `0.4026` maxDD `-6.2481`
- `news_risk_high->index_24h` score `2.6798` n `36` status `ready` deltaP `20.3125` edge `0.0879` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.6754` n `32` status `ready` deltaP `18.6738` edge `0.1167` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.6754` n `32` status `ready` deltaP `18.6738` edge `0.1167` maxDD `-0.1258`
- `news_risk_high->index_4h` score `1.7707` n `36` status `ready` deltaP `20.376` edge `0.0249` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.7586` n `36` status `ready` deltaP `8.7326` edge `0.1202` maxDD `-0.5496`
- `market_context_high->commodity_4h` score `1.7276` n `128` status `ready` deltaP `17.1113` edge `0.077` maxDD `-0.7687`
- `risk_on_high->commodity_1h` score `1.2216` n `32` status `ready` deltaP `13.0614` edge `0.038` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2216` n `32` status `ready` deltaP `13.0614` edge `0.038` maxDD `-0.1957`
- `risk_on_high->fx_24h` score `0.9433` n `32` status `ready` deltaP `11.6319` edge `0.0195` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `0.9433` n `32` status `ready` deltaP `11.6319` edge `0.0195` maxDD `-0.1418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
