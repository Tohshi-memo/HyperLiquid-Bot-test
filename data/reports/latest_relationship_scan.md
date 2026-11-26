# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T20:52:30.371127+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3324`

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

- `news_risk_high->unknown_1h` score `3218.3207` n `31` status `ready` deltaP `2.3807` edge `268.1951` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3196.2006` n `31` status `ready` deltaP `4.3962` edge `266.3264` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `28.972` n `31` status `ready` deltaP `38.1944` edge `2.1597` maxDD `0.0`
- `news_risk_high->equity_24h` score `26.2301` n `31` status `ready` deltaP `37.3264` edge `1.937` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `22.8396` n `31` status `ready` deltaP `37.5` edge `1.6533` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `10.0035` n `31` status `ready` deltaP `24.4738` edge `0.7575` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.7795` n `31` status `ready` deltaP `36.4625` edge `0.5366` maxDD `-2.178`
- `news_risk_high->metal_24h` score `6.643` n `31` status `ready` deltaP `23.8744` edge `0.4219` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `6.4491` n `31` status `ready` deltaP `17.5403` edge `0.8516` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.9211` n `31` status `ready` deltaP `41.5379` edge `0.146` maxDD `-0.0262`
- `news_risk_high->index_24h` score `4.6332` n `31` status `ready` deltaP `38.7153` edge `0.128` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.2276` n `31` status `ready` deltaP `18.9395` edge `0.1614` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.1055` n `31` status `ready` deltaP `34.7856` edge `0.0529` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.574` n `31` status `ready` deltaP `30.7949` edge `0.0177` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.2335` n `31` status `ready` deltaP `7.7651` edge `0.2807` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.0297` n `31` status `ready` deltaP `10.9088` edge `0.2232` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.3748` n `31` status `ready` deltaP `27.6366` edge `0.0199` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.8172` n `31` status `ready` deltaP `14.3391` edge `0.0649` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.3095` n `31` status `ready` deltaP `10.8084` edge `0.0074` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.4299` n `31` status `ready` deltaP `-2.5111` edge `0.0071` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
