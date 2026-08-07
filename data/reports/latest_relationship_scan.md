# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T06:22:28.543825+00:00`
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

- `market_context_high->commodity_4h` score `1.012` n `120` status `ready` deltaP `12.1138` edge `0.0882` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.6775` n `109` status `ready` deltaP `2.6987` edge `0.1553` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.5729` n `109` status `ready` deltaP `21.3184` edge `0.0519` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4559` n `120` status `ready` deltaP `7.6497` edge `0.0286` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0873` n `120` status `ready` deltaP `7.3503` edge `-0.0028` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.218` n `120` status `ready` deltaP `7.8963` edge `0.0054` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.6004` n `120` status `ready` deltaP `-2.8243` edge `-0.0087` maxDD `-1.6224`
- `market_context_high->crypto_alt_1h` score `-0.7715` n `120` status `ready` deltaP `-2.994` edge `-0.0079` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.9185` n `120` status `ready` deltaP `-1.7764` edge `-0.0113` maxDD `-1.6054`
- `market_context_high->index_24h` score `-1.0648` n `109` status `ready` deltaP `-0.3783` edge `0.0855` maxDD `-7.8922`
- `market_context_high->equity_1h` score `-1.2142` n `120` status `ready` deltaP `4.5459` edge `-0.0295` maxDD `-10.5179`
- `market_context_high->index_4h` score `-1.4706` n `120` status `ready` deltaP `-5.2338` edge `-0.0282` maxDD `-4.7021`
- `market_context_high->metal_4h` score `-1.631` n `120` status `ready` deltaP `-1.3415` edge `-0.0035` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-1.9203` n `120` status `ready` deltaP `1.8089` edge `-0.0331` maxDD `-5.7857`
- `market_context_high->crypto_major_1h` score `-2.5386` n `120` status `ready` deltaP `-6.003` edge `-0.0342` maxDD `-7.6533`
- `market_context_high->crypto_alt_24h` score `-3.7966` n `109` status `ready` deltaP `-9.986` edge `-0.1055` maxDD `-4.5445`
- `market_context_high->equity_4h` score `-5.8164` n `120` status `ready` deltaP `1.1077` edge `-0.2242` maxDD `-34.9766`
- `market_context_high->commodity_24h` score `-6.3275` n `109` status `ready` deltaP `9.8099` edge `-0.0001` maxDD `-52.7876`
- `market_context_high->crypto_major_4h` score `-7.2469` n `120` status `ready` deltaP `-5.7317` edge `-0.1445` maxDD `-27.3622`
- `market_context_high->crypto_major_24h` score `-8.4943` n `109` status `ready` deltaP `-10.1377` edge `-0.3483` maxDD `-40.8499`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
