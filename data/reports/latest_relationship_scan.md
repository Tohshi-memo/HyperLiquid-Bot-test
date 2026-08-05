# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T10:37:29.248491+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11648`

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

- `market_context_high->unknown_24h` score `14.0621` n `89` status `ready` deltaP `10.1611` edge `1.1084` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.4275` n `92` status `ready` deltaP `2.2402` edge `0.5369` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.7179` n `92` status `ready` deltaP `18.1336` edge `0.1069` maxDD `-2.7703`
- `market_context_high->fx_24h` score `1.2142` n `89` status `ready` deltaP `28.402` edge `0.0869` maxDD `-4.3126`
- `market_context_high->metal_24h` score `0.9252` n `89` status `ready` deltaP `1.6268` edge `0.2246` maxDD `-2.6802`
- `market_context_high->commodity_1h` score `0.4465` n `96` status `ready` deltaP `7.5911` edge `0.0282` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.1358` n `96` status `ready` deltaP `7.4227` edge `-0.0032` maxDD `-0.7973`
- `market_context_high->fx_4h` score `0.0843` n `92` status `ready` deltaP `13.4411` edge `0.0072` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.551` n `96` status `ready` deltaP `-1.8151` edge `-0.0091` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.6321` n `96` status `ready` deltaP `-1.3847` edge `-0.0184` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.8974` n `92` status `ready` deltaP `1.7431` edge `-0.0032` maxDD `-3.211`
- `market_context_high->crypto_alt_1h` score `-0.9236` n `96` status `ready` deltaP `-4.1791` edge `-0.0195` maxDD `-3.0178`
- `market_context_high->crypto_alt_24h` score `-1.3417` n `89` status `ready` deltaP `1.5449` edge `-0.038` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-1.5366` n `92` status `ready` deltaP `-0.7224` edge `-0.0532` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.7364` n `96` status `ready` deltaP `3.0689` edge `-0.0895` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.1281` n `92` status `ready` deltaP `-13.1694` edge `-0.0596` maxDD `-4.7021`
- `market_context_high->index_24h` score `-2.3409` n `89` status `ready` deltaP `-9.7398` edge `-0.0157` maxDD `-7.8922`
- `market_context_high->unknown_1h` score `-3.2447` n `96` status `ready` deltaP `3.4057` edge `-0.2484` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.5204` n `96` status `ready` deltaP `-12.3503` edge `-0.0737` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.1813` n `89` status `ready` deltaP `9.7827` edge `-0.0427` maxDD `-50.8663`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
