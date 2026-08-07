# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T09:27:39.169489+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11739`

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

- `market_context_high->commodity_4h` score `0.9952` n `120` status `ready` deltaP `12.1138` edge `0.0868` maxDD `-2.7703`
- `market_context_high->fx_24h` score `0.569` n `109` status `ready` deltaP `21.3184` edge `0.0514` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4763` n `120` status `ready` deltaP `7.9491` edge `0.0283` maxDD `-1.3282`
- `market_context_high->metal_24h` score `0.3792` n `109` status `ready` deltaP `0.6954` edge `0.1438` maxDD `-2.6802`
- `market_context_high->fx_1h` score `0.1145` n `120` status `ready` deltaP `7.7994` edge `-0.0023` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.1761` n `120` status `ready` deltaP `8.6585` edge `0.0057` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.6736` n `120` status `ready` deltaP `-3.8722` edge `-0.0111` maxDD `-1.6224`
- `market_context_high->crypto_alt_1h` score `-0.8183` n `120` status `ready` deltaP `-3.2934` edge `-0.0119` maxDD `-3.0178`
- `market_context_high->index_1h` score `-1.0431` n `120` status `ready` deltaP `-3.1237` edge `-0.0127` maxDD `-1.6054`
- `market_context_high->index_24h` score `-1.1676` n `109` status `ready` deltaP `-1.5469` edge `0.0801` maxDD `-7.8922`
- `market_context_high->equity_1h` score `-1.3225` n `120` status `ready` deltaP `3.6477` edge `-0.0374` maxDD `-10.5179`
- `market_context_high->index_4h` score `-1.5077` n `120` status `ready` deltaP `-5.8435` edge `-0.0289` maxDD `-4.7021`
- `market_context_high->metal_4h` score `-1.7747` n `120` status `ready` deltaP `-2.1037` edge `-0.0104` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-2.0929` n `120` status `ready` deltaP `1.0467` edge `-0.0424` maxDD `-5.7857`
- `market_context_high->crypto_major_1h` score `-2.6765` n `120` status `ready` deltaP `-6.6018` edge `-0.0417` maxDD `-7.6533`
- `market_context_high->crypto_alt_24h` score `-3.9512` n `109` status `ready` deltaP `-11.1546` edge `-0.1106` maxDD `-4.5445`
- `market_context_high->equity_4h` score `-5.9058` n `120` status `ready` deltaP `0.4979` edge `-0.2316` maxDD `-34.9766`
- `market_context_high->commodity_24h` score `-6.2705` n `109` status `ready` deltaP `9.8099` edge `0.0072` maxDD `-52.7876`
- `market_context_high->crypto_major_4h` score `-7.4013` n `120` status `ready` deltaP `-6.3415` edge `-0.1533` maxDD `-27.3622`
- `market_context_high->unknown_1h` score `-8.3028` n `120` status `ready` deltaP `1.7715` edge `-0.659` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
