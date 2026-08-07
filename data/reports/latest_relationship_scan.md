# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T07:22:28.655947+00:00`
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

- `market_context_high->commodity_4h` score `0.955` n `120` status `ready` deltaP `11.6565` edge `0.0865` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.5724` n `109` status `ready` deltaP `2.0309` edge `0.151` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.5713` n `109` status `ready` deltaP `21.3184` edge `0.0517` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.42` n `120` status `ready` deltaP `7.3503` edge `0.0276` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.1052` n `120` status `ready` deltaP `7.6497` edge `-0.0025` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.1904` n `120` status `ready` deltaP `8.3537` edge `0.0059` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.6417` n `120` status `ready` deltaP `-3.4231` edge `-0.01` maxDD `-1.6224`
- `market_context_high->crypto_alt_1h` score `-0.7832` n `120` status `ready` deltaP `-2.994` edge `-0.0094` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.9772` n `120` status `ready` deltaP `-2.3752` edge `-0.0122` maxDD `-1.6054`
- `market_context_high->index_24h` score `-1.0827` n `109` status `ready` deltaP `-0.3783` edge `0.0832` maxDD `-7.8922`
- `market_context_high->equity_1h` score `-1.2695` n `120` status `ready` deltaP `4.0968` edge `-0.0336` maxDD `-10.5179`
- `market_context_high->index_4h` score `-1.5077` n `120` status `ready` deltaP `-5.8435` edge `-0.0289` maxDD `-4.7021`
- `market_context_high->metal_4h` score `-1.6952` n `120` status `ready` deltaP `-1.7988` edge `-0.0058` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-1.9805` n `120` status `ready` deltaP `1.6565` edge `-0.0371` maxDD `-5.7857`
- `market_context_high->crypto_major_1h` score `-2.5974` n `120` status `ready` deltaP `-6.3024` edge `-0.0371` maxDD `-7.6533`
- `market_context_high->crypto_alt_24h` score `-3.8956` n `109` status `ready` deltaP `-10.6538` edge `-0.1093` maxDD `-4.5445`
- `market_context_high->equity_4h` score `-5.8612` n `120` status `ready` deltaP `0.6504` edge `-0.2269` maxDD `-34.9766`
- `market_context_high->commodity_24h` score `-6.3134` n `109` status `ready` deltaP `9.8099` edge `0.0017` maxDD `-52.7876`
- `market_context_high->crypto_major_4h` score `-7.2975` n `120` status `ready` deltaP `-5.8841` edge `-0.1477` maxDD `-27.3622`
- `market_context_high->unknown_1h` score `-8.4348` n `120` status `ready` deltaP `1.7715` edge `-0.67` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
