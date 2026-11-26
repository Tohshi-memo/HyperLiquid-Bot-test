# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T13:07:28.571325+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3479`

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

- `news_risk_high->unknown_1h` score `3231.0576` n `31` status `ready` deltaP `1.7819` edge `269.2605` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3216.0919` n `31` status `ready` deltaP `3.4815` edge `267.9901` maxDD `-0.1191`
- `market_context_high->unknown_1h` score `100.7658` n `31` status `ready` deltaP `1.7819` edge `8.3947` maxDD `-0.4209`
- `news_risk_high->crypto_major_24h` score `35.1373` n `31` status `ready` deltaP `43.5764` edge `2.6376` maxDD `0.0`
- `news_risk_high->equity_24h` score `34.5963` n `31` status `ready` deltaP `42.7083` edge `2.5983` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `29.2342` n `31` status `ready` deltaP `42.8819` edge `2.1503` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `10.6869` n `31` status `ready` deltaP `26.7604` edge `0.7992` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.4866` n `31` status `ready` deltaP `38.9015` edge `0.6626` maxDD `-2.178`
- `news_risk_high->metal_24h` score `8.4055` n `31` status `ready` deltaP `29.2563` edge `0.5329` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `6.9415` n `31` status `ready` deltaP `19.6744` edge `0.9005` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.7958` n `31` status `ready` deltaP `44.0972` edge `0.189` maxDD `0.0`
- `news_risk_high->fx_24h` score `4.953` n `31` status `ready` deltaP `41.7115` edge `0.1475` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.7362` n `31` status `ready` deltaP `20.2868` edge `0.1948` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.4618` n `31` status `ready` deltaP `37.5295` edge `0.0643` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7345` n `31` status `ready` deltaP `32.2919` edge `0.0211` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.5047` n `31` status `ready` deltaP `10.0106` edge `0.3005` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.2814` n `31` status `ready` deltaP `13.1543` edge `0.2405` maxDD `-1.5232`
- `market_context_high->fx_4h` score `1.9448` n `31` status `ready` deltaP `24.9804` edge `0.024` maxDD `-0.2774`
- `news_risk_high->metal_1h` score `1.469` n `31` status `ready` deltaP `28.8342` edge `0.024` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.9976` n `31` status `ready` deltaP `15.5586` edge `0.0799` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
