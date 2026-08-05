# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T13:37:30.205318+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11661`

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

- `market_context_high->unknown_24h` score `13.8741` n `89` status `ready` deltaP `8.425` edge `1.1043` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `4.9116` n `96` status `ready` deltaP `1.9563` edge `0.4958` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.5981` n `96` status `ready` deltaP `16.5905` edge `0.1072` maxDD `-2.7703`
- `market_context_high->fx_24h` score `1.1076` n `89` status `ready` deltaP `26.6659` edge `0.0848` maxDD `-4.3126`
- `market_context_high->metal_24h` score `0.8713` n `89` status `ready` deltaP `1.6268` edge `0.2177` maxDD `-2.6802`
- `market_context_high->commodity_1h` score `0.5196` n `98` status `ready` deltaP `8.1908` edge `0.0303` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0851` n `98` status `ready` deltaP `6.7885` edge `-0.0032` maxDD `-0.7973`
- `market_context_high->fx_4h` score `-0.0172` n `96` status `ready` deltaP `11.5345` edge `0.0069` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.57` n `98` status `ready` deltaP `-2.0286` edge `-0.0101` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.7018` n `98` status `ready` deltaP `-2.5602` edge `-0.0195` maxDD `-1.6054`
- `market_context_high->crypto_alt_1h` score `-0.9448` n `98` status `ready` deltaP `-4.2863` edge `-0.0215` maxDD `-3.0178`
- `market_context_high->metal_4h` score `-0.9555` n `96` status `ready` deltaP `0.94` edge `-0.0053` maxDD `-3.211`
- `market_context_high->crypto_alt_24h` score `-1.4781` n `89` status `ready` deltaP `0.6768` edge `-0.0497` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-1.723` n `96` status `ready` deltaP `-2.312` edge `-0.0665` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.8221` n `98` status `ready` deltaP `2.3647` edge `-0.0958` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.0846` n `96` status `ready` deltaP `-12.0173` edge `-0.0617` maxDD `-4.7021`
- `market_context_high->index_24h` score `-2.5725` n `89` status `ready` deltaP `-11.8232` edge `-0.0315` maxDD `-7.8922`
- `market_context_high->unknown_1h` score `-3.0881` n `98` status `ready` deltaP `5.0471` edge `-0.2463` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.626` n `98` status `ready` deltaP `-13.2653` edge `-0.0764` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.0038` n `89` status `ready` deltaP `11.1716` edge `-0.0292` maxDD `-50.8663`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
