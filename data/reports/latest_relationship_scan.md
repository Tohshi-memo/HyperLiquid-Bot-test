# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-06T09:52:25.680159+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11781`

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

- `market_context_high->unknown_24h` score `12.7512` n `97` status `ready` deltaP `4.0038` edge `1.0402` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `3.7446` n `109` status `ready` deltaP `-0.7356` edge `0.4165` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.0408` n `109` status `ready` deltaP `12.6846` edge `0.0868` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.9841` n `97` status `ready` deltaP `4.4995` edge `0.213` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.5391` n `97` status `ready` deltaP `21.2843` edge `0.0478` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4084` n `109` status `ready` deltaP `7.61` edge `0.0249` maxDD `-1.3282`
- `market_context_high->fx_1h` score `-0.0003` n `109` status `ready` deltaP `5.6831` edge `-0.0029` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.2679` n `109` status `ready` deltaP `7.0276` edge `0.0048` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5331` n `109` status `ready` deltaP `-1.7099` edge `-0.0075` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.7074` n `109` status `ready` deltaP `-2.7578` edge `-0.0189` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.75` n `109` status `ready` deltaP `3.2418` edge `0.0057` maxDD `-3.211`
- `market_context_high->index_24h` score `-1.4327` n `97` status `ready` deltaP `-4.9631` edge `0.0689` maxDD `-7.8922`
- `market_context_high->crypto_alt_1h` score `-1.4642` n `109` status `ready` deltaP `-4.8385` edge `-0.0187` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.7598` n `109` status `ready` deltaP `1.8679` edge `-0.0845` maxDD `-10.619`
- `market_context_high->index_4h` score `-1.9972` n `109` status `ready` deltaP `-11.2959` edge `-0.0553` maxDD `-4.7021`
- `market_context_high->crypto_alt_4h` score `-2.1707` n `109` status `ready` deltaP `1.0796` edge `-0.0491` maxDD `-5.7857`
- `market_context_high->crypto_alt_24h` score `-2.2317` n `97` status `ready` deltaP `-1.3603` edge `-0.0326` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-2.572` n `109` status `ready` deltaP `1.1344` edge `-0.1772` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.2156` n `109` status `ready` deltaP `-10.8499` edge `-0.0583` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.7698` n `97` status `ready` deltaP `5.1152` edge `-0.0335` maxDD `-52.482`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
