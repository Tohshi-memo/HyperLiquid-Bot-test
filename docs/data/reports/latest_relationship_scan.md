# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T10:07:26.794515+00:00`
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

- `market_context_high->unknown_24h` score `14.3865` n `88` status `ready` deltaP `10.4955` edge `1.1332` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.4347` n `92` status `ready` deltaP `2.2402` edge `0.5375` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.7131` n `92` status `ready` deltaP `18.1336` edge `0.1065` maxDD `-2.7703`
- `market_context_high->fx_24h` score `1.1883` n `88` status `ready` deltaP `27.904` edge `0.0869` maxDD `-4.3126`
- `market_context_high->metal_24h` score `0.864` n `88` status `ready` deltaP `1.231` edge `0.2194` maxDD `-2.6802`
- `market_context_high->commodity_1h` score `0.3666` n `94` status `ready` deltaP `6.6824` edge `0.0276` maxDD `-1.3282`
- `market_context_high->fx_4h` score `0.0851` n `92` status `ready` deltaP `13.4411` edge `0.0073` maxDD `-1.8797`
- `market_context_high->fx_1h` score `0.0612` n `94` status `ready` deltaP `6.5805` edge `-0.0038` maxDD `-0.7973`
- `market_context_high->metal_1h` score `-0.4907` n `94` status `ready` deltaP `-0.8345` edge `-0.0079` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.5293` n `94` status `ready` deltaP `0.5765` edge `-0.0183` maxDD `-1.6054`
- `market_context_high->crypto_alt_1h` score `-0.8465` n `94` status `ready` deltaP `-3.1596` edge `-0.0164` maxDD `-3.0178`
- `market_context_high->metal_4h` score `-0.899` n `92` status `ready` deltaP `1.7431` edge `-0.0034` maxDD `-3.211`
- `market_context_high->crypto_alt_24h` score `-1.3604` n `88` status `ready` deltaP `1.4836` edge `-0.04` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-1.5296` n `92` status `ready` deltaP `-0.7224` edge `-0.0523` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.6641` n `94` status `ready` deltaP `4.3987` edge `-0.0891` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.1266` n `92` status `ready` deltaP `-13.1694` edge `-0.0594` maxDD `-4.7021`
- `market_context_high->index_24h` score `-2.3433` n `88` status `ready` deltaP `-9.8011` edge `-0.0156` maxDD `-7.8922`
- `market_context_high->unknown_1h` score `-3.1932` n `94` status `ready` deltaP `3.389` edge `-0.244` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.4038` n `94` status `ready` deltaP `-11.5524` edge `-0.0693` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-5.9963` n `88` status `ready` deltaP `9.959` edge `-0.039` maxDD `-49.6923`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
