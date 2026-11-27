# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T02:22:25.962719+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3540`

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

- `news_risk_high->unknown_1h` score `3213.1056` n `31` status `ready` deltaP `1.7819` edge `267.7645` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3183.1422` n `31` status `ready` deltaP `4.3962` edge `265.2382` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `25.8411` n `31` status `ready` deltaP `34.5486` edge `1.9231` maxDD `0.0`
- `news_risk_high->equity_24h` score `22.9698` n `31` status `ready` deltaP `34.0278` edge `1.6873` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.7872` n `31` status `ready` deltaP `33.6806` edge `1.4244` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.4638` n `31` status `ready` deltaP `23.7116` edge `0.7176` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.0916` n `31` status `ready` deltaP `34.3283` edge `0.4935` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `6.2271` n `31` status `ready` deltaP `16.9305` edge `0.8272` maxDD `-7.6714`
- `news_risk_high->metal_24h` score `6.1053` n `31` status `ready` deltaP `21.4438` edge `0.3933` maxDD `-0.1986`
- `news_risk_high->fx_24h` score `4.929` n `31` status `ready` deltaP `41.7115` edge `0.1455` maxDD `-0.0262`
- `news_risk_high->index_24h` score `4.0616` n `31` status `ready` deltaP `35.5903` edge `0.1012` maxDD `0.0`
- `news_risk_high->equity_1h` score `2.9327` n `31` status `ready` deltaP `17.5922` edge `0.1458` maxDD `-0.1621`
- `news_risk_high->index_4h` score `2.8551` n `31` status `ready` deltaP `32.3466` edge `0.0483` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.508` n `31` status `ready` deltaP `30.1961` edge `0.0162` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.1727` n `31` status `ready` deltaP `7.316` edge `0.2759` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.933` n `31` status `ready` deltaP `10.31` edge `0.2148` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.2439` n `31` status `ready` deltaP `26.2893` edge `0.0121` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.5582` n `31` status `ready` deltaP `12.5098` edge `0.0439` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.1587` n `31` status `ready` deltaP `8.5218` edge `0.0033` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.5545` n `31` status `ready` deltaP `-3.8584` edge `0.0057` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
