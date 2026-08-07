# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T05:22:30.627944+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11768`

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

- `market_context_high->commodity_4h` score `1.0871` n `120` status `ready` deltaP `12.7235` edge `0.0904` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.7777` n `109` status `ready` deltaP `3.3665` edge `0.1592` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.5824` n `109` status `ready` deltaP `21.4854` edge `0.052` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4631` n `120` status `ready` deltaP `7.6497` edge `0.0292` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0584` n `120` status `ready` deltaP `6.9012` edge `-0.0035` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.2251` n `120` status `ready` deltaP `7.8963` edge `0.0045` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.556` n `120` status `ready` deltaP `-2.2255` edge `-0.007` maxDD `-1.6224`
- `market_context_high->crypto_alt_1h` score `-0.7567` n `120` status `ready` deltaP `-2.8443` edge `-0.007` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.9485` n `120` status `ready` deltaP `-1.9261` edge `-0.0128` maxDD `-1.6054`
- `market_context_high->index_24h` score `-1.064` n `109` status `ready` deltaP `-0.3783` edge `0.0856` maxDD `-7.8922`
- `market_context_high->equity_1h` score `-1.2423` n `120` status `ready` deltaP `4.5459` edge `-0.0331` maxDD `-10.5179`
- `market_context_high->index_4h` score `-1.4737` n `120` status `ready` deltaP `-5.2338` edge `-0.0286` maxDD `-4.7021`
- `market_context_high->metal_4h` score `-1.5498` n `120` status `ready` deltaP `-0.7317` edge `-0.0008` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-1.8732` n `120` status `ready` deltaP `2.1138` edge `-0.0312` maxDD `-5.7857`
- `market_context_high->crypto_major_1h` score `-2.5159` n `120` status `ready` deltaP `-5.8533` edge `-0.0333` maxDD `-7.6533`
- `market_context_high->crypto_alt_24h` score `-3.6735` n `109` status `ready` deltaP `-9.3182` edge `-0.0997` maxDD `-4.5445`
- `market_context_high->equity_4h` score `-5.8008` n `120` status `ready` deltaP `1.1077` edge `-0.2222` maxDD `-34.9766`
- `market_context_high->commodity_24h` score `-6.3345` n `109` status `ready` deltaP `9.8099` edge `-0.001` maxDD `-52.7876`
- `market_context_high->crypto_major_4h` score `-7.2229` n `120` status `ready` deltaP `-5.7317` edge `-0.1425` maxDD `-27.3622`
- `market_context_high->crypto_major_24h` score `-8.4381` n `109` status `ready` deltaP `-10.1377` edge `-0.3411` maxDD `-40.8499`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
