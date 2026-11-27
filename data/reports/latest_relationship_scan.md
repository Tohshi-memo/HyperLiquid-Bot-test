# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T03:22:28.003021+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3552`

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

- `news_risk_high->unknown_1h` score `3220.9164` n `31` status `ready` deltaP `1.9316` edge `268.4144` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3191.9992` n `31` status `ready` deltaP `4.2437` edge `265.9773` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `25.1555` n `31` status `ready` deltaP `33.8542` edge `1.8706` maxDD `0.0`
- `news_risk_high->equity_24h` score `22.3383` n `31` status `ready` deltaP `33.3333` edge `1.6393` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.2313` n `31` status `ready` deltaP `32.9861` edge `1.3827` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.3424` n `31` status `ready` deltaP `23.5592` edge `0.7085` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `7.8388` n `31` status `ready` deltaP `33.7186` edge `0.4765` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `6.1357` n `31` status `ready` deltaP `16.7781` edge `0.8165` maxDD `-7.6714`
- `news_risk_high->metal_24h` score `6.0012` n `31` status `ready` deltaP `20.923` edge `0.3881` maxDD `-0.1986`
- `news_risk_high->fx_24h` score `4.8662` n `31` status `ready` deltaP `41.017` edge `0.1449` maxDD `-0.0262`
- `news_risk_high->index_24h` score `3.9437` n `31` status `ready` deltaP `34.8958` edge `0.096` maxDD `0.0`
- `news_risk_high->equity_1h` score `2.8631` n `31` status `ready` deltaP `17.4425` edge `0.141` maxDD `-0.1621`
- `news_risk_high->index_4h` score `2.786` n `31` status `ready` deltaP `31.7369` edge `0.0466` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.4649` n `31` status `ready` deltaP `29.747` edge `0.0156` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.1088` n `31` status `ready` deltaP `7.0166` edge `0.2697` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.8715` n `31` status `ready` deltaP `10.0106` edge `0.2089` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.208` n `31` status `ready` deltaP `25.9899` edge `0.0095` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.52` n `31` status `ready` deltaP `12.5098` edge `0.039` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.1145` n `31` status `ready` deltaP `7.9121` edge `0.0017` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.5545` n `31` status `ready` deltaP `-3.8584` edge `0.0057` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
