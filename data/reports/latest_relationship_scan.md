# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T16:07:27.442829+00:00`
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

- `news_risk_high->unknown_1h` score `3271.5253` n `31` status `ready` deltaP `1.4825` edge `272.6348` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3172.2713` n `31` status `ready` deltaP `3.3291` edge `264.3394` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `16.1706` n `31` status `ready` deltaP `25.8681` edge `1.1751` maxDD `0.0`
- `news_risk_high->equity_24h` score `13.4783` n `31` status `ready` deltaP `24.4792` edge `0.96` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `11.7908` n `31` status `ready` deltaP `25.0` edge `0.8159` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `7.7661` n `31` status `ready` deltaP `20.2055` edge `0.5995` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.7153` n `31` status `ready` deltaP `30.3649` edge `0.3219` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `4.8316` n `31` status `ready` deltaP `13.1196` edge `0.6737` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.6346` n `31` status `ready` deltaP `38.5865` edge `0.1418` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.9726` n `31` status `ready` deltaP `12.5896` edge `0.2746` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.4728` n `31` status `ready` deltaP `29.9076` edge `0.0327` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.4325` n `31` status `ready` deltaP `26.0417` edge `0.0291` maxDD `0.0`
- `news_risk_high->equity_1h` score `2.3882` n `31` status `ready` deltaP `15.6461` edge `0.1134` maxDD `-0.1621`
- `news_risk_high->index_1h` score `2.3307` n `31` status `ready` deltaP `28.3997` edge `0.0134` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `1.9186` n `31` status `ready` deltaP `6.1184` edge `0.2513` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.7015` n `31` status `ready` deltaP `8.9627` edge `0.1941` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.2018` n `31` status `ready` deltaP `25.6905` edge `0.0107` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.3373` n `31` status `ready` deltaP `11.2903` edge `0.0237` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.2195` n `31` status `ready` deltaP `8.5218` edge `0.0111` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.4718` n `31` status `ready` deltaP `-3.1099` edge `0.0076` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
