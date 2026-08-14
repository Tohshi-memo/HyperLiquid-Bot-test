# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-14T12:22:24.033113+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11808`

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

- `market_context_high->unknown_24h` score `93.4399` n `148` status `ready` deltaP `-31.1843` edge `8.2858` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `32.9548` n `32` status `ready` deltaP `-44.4444` edge `4.5963` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `32.9548` n `32` status `ready` deltaP `-44.4444` edge `4.5963` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `9.6778` n `36` status `ready` deltaP `10.0694` edge `0.7773` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.1962` n `36` status `ready` deltaP `38.2622` edge `0.3446` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.7877` n `32` status `ready` deltaP `32.2917` edge `0.1837` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.7877` n `32` status `ready` deltaP `32.2917` edge `0.1837` maxDD `0.0`
- `market_context_high->commodity_24h` score `2.8738` n `148` status `ready` deltaP `22.1566` edge `0.1721` maxDD `-2.4263`
- `risk_on_high->commodity_4h` score `2.805` n `32` status `ready` deltaP `19.5884` edge `0.1214` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.805` n `32` status `ready` deltaP `19.5884` edge `0.1214` maxDD `-0.1258`
- `news_risk_high->index_24h` score `2.1531` n `36` status `ready` deltaP `14.5833` edge `0.0822` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `1.8477` n `32` status `ready` deltaP `15.9722` edge `0.246` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.8477` n `32` status `ready` deltaP `15.9722` edge `0.246` maxDD `-6.2481`
- `news_risk_high->index_4h` score `1.6993` n `36` status `ready` deltaP `19.9187` edge `0.022` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.683` n `36` status `ready` deltaP `8.5829` edge `0.1149` maxDD `-0.5496`
- `market_context_high->commodity_4h` score `1.3621` n `148` status `ready` deltaP `15.7877` edge `0.0721` maxDD `-2.1077`
- `risk_on_high->commodity_1h` score `1.2264` n `32` status `ready` deltaP `13.0614` edge `0.0384` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2264` n `32` status `ready` deltaP `13.0614` edge `0.0384` maxDD `-0.1957`
- `risk_on_high->fx_24h` score `1.202` n `32` status `ready` deltaP `14.2361` edge `0.0237` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.202` n `32` status `ready` deltaP `14.2361` edge `0.0237` maxDD `-0.1418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
