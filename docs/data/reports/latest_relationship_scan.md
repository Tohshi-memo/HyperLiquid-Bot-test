# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T00:07:23.477186+00:00`
- Price records: `672`
- Market context records: `3019`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6987`

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

- `market_context_high->crypto_alt_24h` score `21.1678` n `99` status `ready` deltaP `9.2487` edge `2.094` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `12.5285` n `99` status `ready` deltaP `42.3769` edge `0.7856` maxDD `-1.2589`
- `market_context_high->unknown_24h` score `12.3958` n `99` status `ready` deltaP `21.0227` edge `0.9393` maxDD `-1.7175`
- `market_context_high->equity_24h` score `6.7126` n `99` status `ready` deltaP `19.9022` edge `1.0031` maxDD `-18.3486`
- `market_context_high->index_24h` score `6.5976` n `99` status `ready` deltaP `19.4918` edge `0.5454` maxDD `-4.7103`
- `market_context_high->commodity_4h` score `2.4834` n `110` status `ready` deltaP `18.459` edge `0.1486` maxDD `-2.8438`
- `market_context_high->equity_4h` score `0.5333` n `110` status `ready` deltaP `13.4673` edge `0.1695` maxDD `-12.9393`
- `market_context_high->crypto_alt_4h` score `0.3777` n `110` status `ready` deltaP `24.0023` edge `0.4432` maxDD `-38.7172`
- `market_context_high->index_4h` score `0.1141` n `110` status `ready` deltaP `16.3803` edge `0.0952` maxDD `-10.8483`
- `market_context_high->commodity_1h` score `0.0049` n `122` status `ready` deltaP `2.5302` edge `0.0258` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.4068` n `122` status `ready` deltaP `4.0272` edge `0.0224` maxDD `-4.1126`
- `market_context_high->equity_1h` score `-0.4339` n `122` status `ready` deltaP `2.8934` edge `0.0347` maxDD `-5.7692`
- `market_context_high->fx_1h` score `-0.4484` n `122` status `ready` deltaP `-3.2075` edge `0.0005` maxDD `-0.2615`
- `market_context_high->crypto_alt_1h` score `-0.7752` n `122` status `ready` deltaP `5.5168` edge `0.0768` maxDD `-14.7034`
- `market_context_high->unknown_1h` score `-0.904` n `122` status `ready` deltaP `3.7131` edge `-0.027` maxDD `-3.1801`
- `market_context_high->fx_4h` score `-1.0723` n `110` status `ready` deltaP `-8.6391` edge `-0.0009` maxDD `-0.6521`
- `market_context_high->unknown_4h` score `-1.2045` n `110` status `ready` deltaP `-1.5355` edge `0.0152` maxDD `-3.7602`
- `market_context_high->metal_1h` score `-1.2336` n `122` status `ready` deltaP `-3.0357` edge `-0.0061` maxDD `-6.8783`
- `market_context_high->crypto_major_1h` score `-1.235` n `122` status `ready` deltaP `3.2934` edge `0.046` maxDD `-15.1032`
- `market_context_high->fx_24h` score `-1.7577` n `99` status `ready` deltaP `-5.0978` edge `-0.0253` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
