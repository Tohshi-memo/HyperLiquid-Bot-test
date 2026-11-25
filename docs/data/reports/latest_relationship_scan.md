# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T16:22:35.248161+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3744`

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

- `market_context_high->unknown_1h` score `32186.7337` n `45` status `ready` deltaP `2.1656` edge `2682.2228` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21883.5765` n `45` status `ready` deltaP `2.8727` edge `1823.6261` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `951.7787` n `31` status `ready` deltaP `2.3807` edge `79.3166` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `630.629` n `31` status `ready` deltaP `4.0913` edge `52.5308` maxDD `-0.1191`
- `news_risk_high->unknown_24h` score `411.8627` n `31` status `ready` deltaP `5.7292` edge `34.2837` maxDD `0.0`
- `news_risk_high->equity_24h` score `45.8617` n `31` status `ready` deltaP `51.7361` edge `3.4769` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `42.2475` n `31` status `ready` deltaP `53.2986` edge `3.1653` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `38.7099` n `31` status `ready` deltaP `55.7292` edge `2.8543` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `12.0067` n `31` status `ready` deltaP `27.5226` edge `0.9041` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.9966` n `31` status `ready` deltaP `41.2355` edge `0.7523` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `11.5046` n `31` status `ready` deltaP `38.2917` edge `0.7515` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.5079` n `31` status `ready` deltaP `18.9123` edge `0.9782` maxDD `-7.6714`
- `news_risk_high->index_24h` score `7.3384` n `31` status `ready` deltaP `52.4306` edge `0.262` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.412` n `31` status `ready` deltaP `46.399` edge `0.1545` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `4.0194` n `31` status `ready` deltaP `20.5862` edge `0.2164` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.4936` n `31` status `ready` deltaP `37.0722` edge `0.07` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7238` n `31` status `ready` deltaP `31.9925` edge `0.0222` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.645` n `31` status `ready` deltaP `11.2082` edge `0.3105` maxDD `-1.6897`
- `market_context_high->fx_4h` score `2.4688` n `45` status `ready` deltaP `30.2405` edge `0.0326` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.4273` n `31` status `ready` deltaP `13.1543` edge `0.2592` maxDD `-1.5232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
