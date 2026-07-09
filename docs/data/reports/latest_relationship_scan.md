# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T12:08:19.640878+00:00`
- Price records: `672`
- Market context records: `6181`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11120`

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

- `news_risk_high->crypto_alt_24h` score `12.6746` n `32` status `ready` deltaP `42.3848` edge `0.7884` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `7.0961` n `32` status `ready` deltaP `62.2867` edge `0.1761` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.019` n `32` status `ready` deltaP `41.8371` edge `0.0606` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3332` n `32` status `ready` deltaP `28.1437` edge `0.0207` maxDD `-0.1113`
- `news_risk_high->crypto_major_24h` score `1.8942` n `32` status `ready` deltaP `15.7956` edge `0.2155` maxDD `-4.2368`
- `market_context_high->unknown_1h` score `1.8849` n `192` status `ready` deltaP `1.5126` edge `0.2478` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.3049` n `32` status `ready` deltaP `13.5292` edge `0.1238` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.6907` n `32` status `ready` deltaP `8.7762` edge `0.0762` maxDD `-1.6923`
- `market_context_high->unknown_4h` score `0.5314` n `192` status `ready` deltaP `-0.7481` edge `0.3025` maxDD `-11.925`
- `market_context_high->metal_24h` score `0.06` n `192` status `ready` deltaP `19.9997` edge `0.1312` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.1071` n `32` status `ready` deltaP `9.663` edge `0.009` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.1642` n `192` status `ready` deltaP `2.4053` edge `0.062` maxDD `-2.671`
- `market_context_high->fx_1h` score `-0.3003` n `192` status `ready` deltaP `1.0604` edge `-0.001` maxDD `-0.5659`
- `news_risk_high->commodity_24h` score `-0.3221` n `32` status `ready` deltaP `14.5798` edge `-0.1035` maxDD `-0.3101`
- `market_context_high->metal_4h` score `-0.6987` n `192` status `ready` deltaP `3.3997` edge `0.0065` maxDD `-3.4996`
- `news_risk_high->metal_1h` score `-0.8011` n `32` status `ready` deltaP `-3.4431` edge `-0.03` maxDD `-1.6464`
- `market_context_high->commodity_1h` score `-0.81` n `192` status `ready` deltaP `-2.6946` edge `-0.0049` maxDD `-0.5708`
- `market_context_high->metal_1h` score `-0.8916` n `192` status `ready` deltaP `1.7652` edge `-0.0062` maxDD `-2.0564`
- `market_context_high->crypto_alt_1h` score `-0.973` n `192` status `ready` deltaP `3.047` edge `0.0302` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.9947` n `192` status `ready` deltaP `3.6334` edge `0.025` maxDD `-9.807`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
