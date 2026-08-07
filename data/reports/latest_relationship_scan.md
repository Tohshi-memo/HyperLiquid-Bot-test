# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T06:37:28.581033+00:00`
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

- `market_context_high->commodity_4h` score `0.9914` n `120` status `ready` deltaP `11.9613` edge `0.0875` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.6497` n `109` status `ready` deltaP `2.5318` edge `0.1541` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.5729` n `109` status `ready` deltaP `21.3184` edge `0.0519` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4511` n `120` status `ready` deltaP `7.6497` edge `0.0282` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0958` n `120` status `ready` deltaP `7.5` edge `-0.0027` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.2086` n `120` status `ready` deltaP `8.0488` edge `0.0056` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.6121` n `120` status `ready` deltaP `-2.974` edge `-0.0092` maxDD `-1.6224`
- `market_context_high->crypto_alt_1h` score `-0.7723` n `120` status `ready` deltaP `-2.994` edge `-0.008` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.9305` n `120` status `ready` deltaP `-1.9261` edge `-0.0113` maxDD `-1.6054`
- `market_context_high->index_24h` score `-1.0687` n `109` status `ready` deltaP `-0.3783` edge `0.085` maxDD `-7.8922`
- `market_context_high->equity_1h` score `-1.2173` n `120` status `ready` deltaP `4.5459` edge `-0.0299` maxDD `-10.5179`
- `market_context_high->index_4h` score `-1.4793` n `120` status `ready` deltaP `-5.3862` edge `-0.0283` maxDD `-4.7021`
- `market_context_high->metal_4h` score `-1.6516` n `120` status `ready` deltaP `-1.4939` edge `-0.0042` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-1.9275` n `120` status `ready` deltaP `1.8089` edge `-0.0337` maxDD `-5.7857`
- `market_context_high->crypto_major_1h` score `-2.5458` n `120` status `ready` deltaP `-6.003` edge `-0.0348` maxDD `-7.6533`
- `market_context_high->crypto_alt_24h` score `-3.8207` n `109` status `ready` deltaP `-10.153` edge `-0.1064` maxDD `-4.5445`
- `market_context_high->equity_4h` score `-5.8226` n `120` status `ready` deltaP `1.1077` edge `-0.225` maxDD `-34.9766`
- `market_context_high->commodity_24h` score `-6.3251` n `109` status `ready` deltaP `9.8099` edge `0.0002` maxDD `-52.7876`
- `market_context_high->crypto_major_4h` score `-7.2711` n `120` status `ready` deltaP `-5.8841` edge `-0.1455` maxDD `-27.3622`
- `market_context_high->crypto_major_24h` score `-8.5099` n `109` status `ready` deltaP `-10.1377` edge `-0.3503` maxDD `-40.8499`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
