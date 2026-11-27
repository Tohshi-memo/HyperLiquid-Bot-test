# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T17:07:38.019840+00:00`
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

- `news_risk_high->unknown_1h` score `3277.2049` n `31` status `ready` deltaP `1.6322` edge `273.1071` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3180.0833` n `31` status `ready` deltaP `3.3291` edge `264.9904` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `16.1478` n `31` status `ready` deltaP `25.8681` edge `1.1732` maxDD `0.0`
- `news_risk_high->equity_24h` score `13.1643` n `31` status `ready` deltaP `23.9583` edge `0.9373` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `11.804` n `31` status `ready` deltaP `25.0` edge `0.817` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `7.8189` n `31` status `ready` deltaP `20.2055` edge `0.6039` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.6265` n `31` status `ready` deltaP `30.3649` edge `0.3145` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `4.8285` n `31` status `ready` deltaP `13.1196` edge `0.6733` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.637` n `31` status `ready` deltaP `38.5865` edge `0.142` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.892` n `31` status `ready` deltaP `12.2424` edge `0.2702` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.4414` n `31` status `ready` deltaP `29.7551` edge `0.0311` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.3458` n `31` status `ready` deltaP `25.3472` edge `0.0265` maxDD `0.0`
- `news_risk_high->index_1h` score `2.2852` n `31` status `ready` deltaP `27.9506` edge `0.0126` maxDD `-0.0136`
- `news_risk_high->equity_1h` score `2.2814` n `31` status `ready` deltaP `15.197` edge `0.1075` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `1.8616` n `31` status `ready` deltaP `5.819` edge `0.246` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.6493` n `31` status `ready` deltaP `8.5136` edge `0.1904` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.18` n `31` status `ready` deltaP `25.3911` edge `0.0099` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.3466` n `31` status `ready` deltaP `11.2903` edge `0.0249` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.2941` n `31` status `ready` deltaP `9.1316` edge `0.0166` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.4191` n `31` status `ready` deltaP `-2.6608` edge `0.009` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
