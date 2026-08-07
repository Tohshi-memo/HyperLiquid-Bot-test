# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T06:07:28.969950+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11736`

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

- `market_context_high->commodity_4h` score `1.0302` n `120` status `ready` deltaP `12.2662` edge `0.0887` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.7052` n `109` status `ready` deltaP `2.8657` edge `0.1565` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.5729` n `109` status `ready` deltaP `21.3184` edge `0.0519` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4583` n `120` status `ready` deltaP `7.6497` edge `0.0288` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0787` n `120` status `ready` deltaP `7.2006` edge `-0.0029` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.2188` n `120` status `ready` deltaP `7.8963` edge `0.0053` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5872` n `120` status `ready` deltaP `-2.6746` edge `-0.008` maxDD `-1.6224`
- `market_context_high->crypto_alt_1h` score `-0.7739` n `120` status `ready` deltaP `-2.994` edge `-0.0082` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.9341` n `120` status `ready` deltaP `-1.9261` edge `-0.0116` maxDD `-1.6054`
- `market_context_high->index_24h` score `-1.0632` n `109` status `ready` deltaP `-0.3783` edge `0.0857` maxDD `-7.8922`
- `market_context_high->equity_1h` score `-1.222` n `120` status `ready` deltaP `4.5459` edge `-0.0305` maxDD `-10.5179`
- `market_context_high->index_4h` score `-1.4706` n `120` status `ready` deltaP `-5.2338` edge `-0.0282` maxDD `-4.7021`
- `market_context_high->metal_4h` score `-1.6104` n `120` status `ready` deltaP `-1.189` edge `-0.0028` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-1.8998` n `120` status `ready` deltaP `1.9613` edge `-0.0324` maxDD `-5.7857`
- `market_context_high->crypto_major_1h` score `-2.5374` n `120` status `ready` deltaP `-6.003` edge `-0.0341` maxDD `-7.6533`
- `market_context_high->crypto_alt_24h` score `-3.7688` n `109` status `ready` deltaP `-9.8191` edge `-0.1043` maxDD `-4.5445`
- `market_context_high->equity_4h` score `-5.814` n `120` status `ready` deltaP `1.1077` edge `-0.2239` maxDD `-34.9766`
- `market_context_high->commodity_24h` score `-6.3306` n `109` status `ready` deltaP `9.8099` edge `-0.0005` maxDD `-52.7876`
- `market_context_high->crypto_major_4h` score `-7.2349` n `120` status `ready` deltaP `-5.7317` edge `-0.1435` maxDD `-27.3622`
- `market_context_high->crypto_major_24h` score `-8.4779` n `109` status `ready` deltaP `-10.1377` edge `-0.3462` maxDD `-40.8499`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
