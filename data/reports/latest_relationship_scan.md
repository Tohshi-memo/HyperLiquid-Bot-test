# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T16:37:25.314730+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `2886`

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

- `news_risk_high->unknown_1h` score `3277.1869` n `31` status `ready` deltaP `1.6322` edge `273.1056` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3179.8457` n `31` status `ready` deltaP `3.3291` edge `264.9706` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `16.1406` n `31` status `ready` deltaP `25.8681` edge `1.1726` maxDD `0.0`
- `news_risk_high->equity_24h` score `13.297` n `31` status `ready` deltaP `24.1319` edge `0.9472` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `11.7848` n `31` status `ready` deltaP `25.0` edge `0.8154` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `7.7913` n `31` status `ready` deltaP `20.2055` edge `0.6016` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.6541` n `31` status `ready` deltaP `30.3649` edge `0.3168` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `4.8316` n `31` status `ready` deltaP `13.1196` edge `0.6737` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.637` n `31` status `ready` deltaP `38.5865` edge `0.142` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.9172` n `31` status `ready` deltaP `12.2424` edge `0.2723` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.462` n `31` status `ready` deltaP `29.9076` edge `0.0318` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.3868` n `31` status `ready` deltaP `25.6944` edge `0.0276` maxDD `0.0`
- `news_risk_high->equity_1h` score `2.3066` n `31` status `ready` deltaP `15.3467` edge `0.1086` maxDD `-0.1621`
- `news_risk_high->index_1h` score `2.3008` n `31` status `ready` deltaP `28.1003` edge `0.0129` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `1.8741` n `31` status `ready` deltaP `5.819` edge `0.2476` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.6626` n `31` status `ready` deltaP `8.6633` edge `0.1911` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1987` n `31` status `ready` deltaP `25.6905` edge `0.0103` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.3412` n `31` status `ready` deltaP `11.2903` edge `0.0242` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.258` n `31` status `ready` deltaP `8.8267` edge `0.014` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.4358` n `31` status `ready` deltaP `-2.8105` edge `0.0086` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
