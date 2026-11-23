# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T13:52:36.321479+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4458`

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

- `market_context_high->unknown_1h` score `25477.8764` n `56` status `ready` deltaP `-0.5347` edge `2123.1761` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `17232.0824` n `56` status `ready` deltaP `4.3554` edge `1435.9917` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1295.323` n `31` status `ready` deltaP `3.728` edge `107.9363` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1101.3562` n `31` status `ready` deltaP `4.701` edge `91.754` maxDD `-0.119`
- `news_risk_high->equity_24h` score `44.8788` n `31` status `ready` deltaP `49.3056` edge `3.4112` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `37.0725` n `31` status `ready` deltaP `48.6111` edge `2.7653` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `32.7484` n `31` status `ready` deltaP `48.7847` edge `2.4038` maxDD `0.0`
- `news_risk_high->metal_24h` score `13.3043` n `31` status `ready` deltaP `49.916` edge `0.8034` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `10.3402` n `31` status `ready` deltaP `32.9564` edge `0.6902` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `10.2946` n `31` status `ready` deltaP `22.1872` edge `0.797` maxDD `-5.2957`
- `news_risk_high->index_24h` score `7.0168` n `31` status `ready` deltaP `47.5694` edge `0.2676` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `6.2476` n `31` status `ready` deltaP `11.5952` edge `0.8654` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `6.2125` n `31` status `ready` deltaP `52.4754` edge `0.1807` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.6692` n `31` status `ready` deltaP `18.4904` edge `0.2012` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.3071` n `31` status `ready` deltaP `34.7856` edge `0.0697` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6375` n `31` status `ready` deltaP `30.9446` edge `0.022` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.3426` n `31` status `ready` deltaP `8.9627` edge `0.2867` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9661` n `31` status `ready` deltaP `7.9148` edge `0.235` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5322` n `31` status `ready` deltaP `29.1336` edge `0.0301` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.4232` n `31` status `ready` deltaP `19.9793` edge `0.105` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
