# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T07:07:19.702096+00:00`
- Price records: `672`
- Market context records: `1298`
- Flow alert records: `5647`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8780`

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

- `market_context_high->crypto_major_24h` score `17.277` n `128` status `ready` deltaP `41.4062` edge `1.2769` maxDD `-8.0553`
- `market_context_high->metal_24h` score `12.5589` n `128` status `ready` deltaP `10.2431` edge `1.145` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.5363` n `128` status `ready` deltaP `28.0381` edge `0.8094` maxDD `-15.1306`
- `market_context_high->index_24h` score `5.9645` n `128` status `ready` deltaP `31.0764` edge `0.3985` maxDD `-5.3574`
- `market_context_high->equity_24h` score `4.0497` n `128` status `ready` deltaP `25.3472` edge `0.5829` maxDD `-14.2815`
- `market_context_high->equity_4h` score `2.4072` n `152` status `ready` deltaP `12.524` edge `0.1876` maxDD `-3.6396`
- `market_context_high->unknown_24h` score `2.3248` n `128` status `ready` deltaP `1.2153` edge `0.4586` maxDD `-10.1706`
- `market_context_high->commodity_24h` score `0.8439` n `128` status `ready` deltaP `-15.4514` edge `0.3215` maxDD `-6.8535`
- `market_context_high->fx_24h` score `0.5641` n `128` status `ready` deltaP `7.8994` edge `0.0408` maxDD `-0.3831`
- `market_context_high->equity_1h` score `0.1936` n `157` status `ready` deltaP `3.5174` edge `0.0354` maxDD `-1.7505`
- `market_context_high->index_1h` score `0.1123` n `157` status `ready` deltaP `6.2121` edge `0.0184` maxDD `-1.6329`
- `market_context_high->index_4h` score `0.0914` n `152` status `ready` deltaP `4.9984` edge `0.0873` maxDD `-3.7119`
- `market_context_high->metal_1h` score `0.0184` n `157` status `ready` deltaP `9.6905` edge `0.0059` maxDD `-2.8509`
- `market_context_high->metal_4h` score `-0.0417` n `152` status `ready` deltaP `12.5883` edge `0.0557` maxDD `-6.4478`
- `market_context_high->unknown_4h` score `-0.1498` n `152` status `ready` deltaP `3.0648` edge `0.1942` maxDD `-11.1695`
- `market_context_high->fx_1h` score `-0.4858` n `157` status `ready` deltaP `1.2577` edge `-0.0033` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.6001` n `157` status `ready` deltaP `0.697` edge `0.0324` maxDD `-3.6309`
- `market_context_high->crypto_major_1h` score `-0.8384` n `157` status `ready` deltaP `-0.4682` edge `-0.0023` maxDD `-5.8323`
- `market_context_high->crypto_major_4h` score `-0.8611` n `152` status `ready` deltaP `5.4878` edge `0.1239` maxDD `-13.3376`
- `market_context_high->commodity_1h` score `-1.0372` n `157` status `ready` deltaP `-2.4524` edge `-0.0086` maxDD `-2.252`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
