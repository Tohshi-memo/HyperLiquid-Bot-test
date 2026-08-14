# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-14T08:22:28.238775+00:00`
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

- `market_context_high->unknown_24h` score `90.1114` n `150` status `ready` deltaP `-30.1458` edge `8.0015` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.0317` n `32` status `ready` deltaP `-44.2708` edge `4.605` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.0317` n `32` status `ready` deltaP `-44.2708` edge `4.605` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `10.0102` n `36` status `ready` deltaP `10.0694` edge `0.805` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.3017` n `36` status `ready` deltaP `39.1768` edge `0.3473` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.7384` n `32` status `ready` deltaP `31.9444` edge `0.1819` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.7384` n `32` status `ready` deltaP `31.9444` edge `0.1819` maxDD `0.0`
- `market_context_high->commodity_24h` score `2.8112` n `150` status `ready` deltaP `21.9444` edge `0.1683` maxDD `-2.4263`
- `risk_on_high->commodity_4h` score `2.6924` n `32` status `ready` deltaP `18.8262` edge `0.1171` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.6924` n `32` status `ready` deltaP `18.8262` edge `0.1171` maxDD `-0.1258`
- `news_risk_high->index_24h` score `2.2539` n `36` status `ready` deltaP `14.5833` edge `0.0906` maxDD `0.0`
- `news_risk_high->index_4h` score `1.7261` n `36` status `ready` deltaP `20.2235` edge `0.0222` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.6794` n `36` status `ready` deltaP `8.7326` edge `0.1136` maxDD `-0.5496`
- `risk_on_high->crypto_major_24h` score `1.4973` n `32` status `ready` deltaP `13.1944` edge `0.2196` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.4973` n `32` status `ready` deltaP `13.1944` edge `0.2196` maxDD `-6.2481`
- `market_context_high->commodity_4h` score `1.3309` n `150` status `ready` deltaP `15.3679` edge `0.0723` maxDD `-2.1077`
- `risk_on_high->commodity_1h` score `1.2288` n `32` status `ready` deltaP `13.0614` edge `0.0386` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2288` n `32` status `ready` deltaP `13.0614` edge `0.0386` maxDD `-0.1957`
- `risk_on_high->fx_24h` score `1.1936` n `32` status `ready` deltaP `14.2361` edge `0.023` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.1936` n `32` status `ready` deltaP `14.2361` edge `0.023` maxDD `-0.1418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
