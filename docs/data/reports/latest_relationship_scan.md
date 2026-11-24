# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T17:07:27.826889+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4272`

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

- `market_context_high->unknown_1h` score `32296.049` n `45` status `ready` deltaP `1.7165` edge `2691.3354` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `22108.3569` n `45` status `ready` deltaP `2.8727` edge `1842.3578` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `1061.094` n `31` status `ready` deltaP `1.9316` edge `88.4292` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `855.4094` n `31` status `ready` deltaP `4.0913` edge `71.2625` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `37.5931` n `31` status `ready` deltaP `49.4792` edge `2.8029` maxDD `0.0`
- `news_risk_high->equity_24h` score `35.5046` n `31` status `ready` deltaP `41.4931` edge `2.6821` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `32.801` n `31` status `ready` deltaP `47.2222` edge `2.4186` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.1871` n `31` status `ready` deltaP `24.7787` edge `0.8541` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.099` n `31` status `ready` deltaP `41.2355` edge `0.6775` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `9.5314` n `31` status `ready` deltaP `33.2612` edge `0.6206` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `6.9283` n `31` status `ready` deltaP `16.0159` edge `0.9232` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `6.3431` n `31` status `ready` deltaP `53.3434` edge `0.1858` maxDD `-0.0262`
- `news_risk_high->index_24h` score `5.2593` n `31` status `ready` deltaP `39.2361` edge `0.1767` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.5468` n `31` status `ready` deltaP `18.9395` edge `0.188` maxDD `-0.1621`
- `news_risk_high->index_4h` score `2.9643` n `31` status `ready` deltaP `32.3466` edge `0.0574` maxDD `-0.4146`
- `market_context_high->fx_4h` score `2.8865` n `45` status `ready` deltaP `34.9661` edge `0.0359` maxDD `-0.2774`
- `news_risk_high->crypto_major_1h` score `2.6301` n `31` status `ready` deltaP `11.807` edge `0.3046` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.5812` n `31` status `ready` deltaP `30.6452` edge `0.0193` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.2793` n `31` status `ready` deltaP `11.3579` edge `0.2522` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.6614` n `31` status `ready` deltaP `31.0797` edge `0.0337` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
