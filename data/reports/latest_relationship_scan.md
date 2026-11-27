# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T03:37:29.509854+00:00`
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

- `news_risk_high->unknown_1h` score `3220.4064` n `31` status `ready` deltaP `1.9316` edge `268.3719` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3191.9524` n `31` status `ready` deltaP `4.2437` edge `265.9734` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `24.928` n `31` status `ready` deltaP `33.6806` edge `1.8528` maxDD `0.0`
- `news_risk_high->equity_24h` score `22.1528` n `31` status `ready` deltaP `33.1597` edge `1.625` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.047` n `31` status `ready` deltaP `32.8125` edge `1.3685` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.2966` n `31` status `ready` deltaP `23.4067` edge `0.7057` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `7.763` n `31` status `ready` deltaP `33.5661` edge `0.4712` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `6.0935` n `31` status `ready` deltaP `16.6257` edge `0.8121` maxDD `-7.6714`
- `news_risk_high->metal_24h` score `5.9682` n `31` status `ready` deltaP `20.7494` edge `0.3865` maxDD `-0.1986`
- `news_risk_high->fx_24h` score `4.8511` n `31` status `ready` deltaP `40.8434` edge `0.1448` maxDD `-0.0262`
- `news_risk_high->index_24h` score `3.9118` n `31` status `ready` deltaP `34.7222` edge `0.0945` maxDD `0.0`
- `news_risk_high->equity_1h` score `2.8391` n `31` status `ready` deltaP `17.2928` edge `0.14` maxDD `-0.1621`
- `news_risk_high->index_4h` score `2.7678` n `31` status `ready` deltaP `31.5844` edge `0.0461` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.4517` n `31` status `ready` deltaP `29.5973` edge `0.0155` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.0862` n `31` status `ready` deltaP `6.8669` edge `0.2678` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.8613` n `31` status `ready` deltaP `10.0106` edge `0.2076` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.2072` n `31` status `ready` deltaP `25.9899` edge `0.0094` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.5099` n `31` status `ready` deltaP `12.5098` edge `0.0377` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.1034` n `31` status `ready` deltaP `7.7596` edge `0.0013` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.5533` n `31` status `ready` deltaP `-3.8584` edge `0.0058` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
