# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T08:37:26.031452+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4884`

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

- `market_context_high->unknown_1h` score `18557.7617` n `74` status `ready` deltaP `1.7721` edge `1546.4845` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `12260.6886` n `74` status `ready` deltaP `3.8727` edge `1021.7121` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1317.1019` n `31` status `ready` deltaP `3.4286` edge `109.7532` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1171.759` n `31` status `ready` deltaP `4.701` edge `97.6209` maxDD `-0.119`
- `news_risk_high->equity_4h` score `10.9418` n `31` status `ready` deltaP `35.0905` edge `0.7261` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `10.3668` n `31` status `ready` deltaP `23.2543` edge `0.7959` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `6.3092` n `31` status `ready` deltaP `12.5098` edge `0.8672` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.7723` n `31` status `ready` deltaP `18.9395` edge `0.2068` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.4748` n `31` status `ready` deltaP `36.4625` edge `0.0725` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6914` n `31` status `ready` deltaP `31.5434` edge `0.0225` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.3847` n `31` status `ready` deltaP `9.2621` edge `0.2901` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9583` n `31` status `ready` deltaP `7.6154` edge `0.236` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5127` n `31` status `ready` deltaP `28.8342` edge `0.0296` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.408` n `31` status `ready` deltaP `19.522` edge `0.1061` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.8429` n `31` status `ready` deltaP `18.1255` edge `0.027` maxDD `-0.5151`
- `market_context_high->fx_4h` score `0.5761` n `74` status `ready` deltaP `17.3245` edge `0.0171` maxDD `-0.3661`
- `news_risk_high->commodity_1h` score `-0.0261` n `31` status `ready` deltaP `1.5308` edge `0.0138` maxDD `-0.0947`
- `market_context_high->metal_1h` score `-0.2028` n `74` status `ready` deltaP `3.2893` edge `0.013` maxDD `-1.4794`
- `market_context_high->index_1h` score `-0.3675` n `74` status `ready` deltaP `-0.4532` edge `0.0015` maxDD `-0.9806`
- `market_context_high->commodity_1h` score `-1.0253` n `74` status `ready` deltaP `-3.6131` edge `-0.0187` maxDD `-2.7598`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
