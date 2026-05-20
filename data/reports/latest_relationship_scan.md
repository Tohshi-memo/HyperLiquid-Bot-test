# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T06:52:14.438616+00:00`
- Price records: `672`
- Market context records: `1297`
- Flow alert records: `5644`
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

- `market_context_high->crypto_major_24h` score `17.3118` n `128` status `ready` deltaP `41.4062` edge `1.2798` maxDD `-8.0553`
- `market_context_high->metal_24h` score `12.4814` n `128` status `ready` deltaP `10.0694` edge `1.1397` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.5104` n `128` status `ready` deltaP `27.8645` edge `0.8084` maxDD `-15.1306`
- `market_context_high->index_24h` score `5.9314` n `128` status `ready` deltaP `30.9028` edge `0.3969` maxDD `-5.3574`
- `market_context_high->equity_24h` score `4.0443` n `128` status `ready` deltaP `25.3472` edge `0.5822` maxDD `-14.2815`
- `market_context_high->equity_4h` score `2.412` n `152` status `ready` deltaP `12.524` edge `0.188` maxDD `-3.6396`
- `market_context_high->unknown_24h` score `2.3423` n `128` status `ready` deltaP `1.3889` edge `0.4589` maxDD `-10.1706`
- `market_context_high->commodity_24h` score `0.8595` n `128` status `ready` deltaP `-15.4514` edge `0.3228` maxDD `-6.8535`
- `market_context_high->fx_24h` score `0.5442` n `128` status `ready` deltaP `7.7257` edge `0.0403` maxDD `-0.3831`
- `market_context_high->equity_1h` score `0.196` n `157` status `ready` deltaP `3.5174` edge `0.0356` maxDD `-1.7505`
- `market_context_high->index_1h` score `0.1131` n `157` status `ready` deltaP `6.2121` edge `0.0185` maxDD `-1.6329`
- `market_context_high->index_4h` score `0.0914` n `152` status `ready` deltaP `4.9984` edge `0.0873` maxDD `-3.7119`
- `market_context_high->metal_1h` score `0.0424` n `157` status `ready` deltaP `9.8402` edge `0.0069` maxDD `-2.8509`
- `market_context_high->metal_4h` score `-0.0067` n `152` status `ready` deltaP `12.7407` edge `0.0576` maxDD `-6.4478`
- `market_context_high->unknown_4h` score `-0.1268` n `152` status `ready` deltaP `3.2172` edge `0.1951` maxDD `-11.1695`
- `market_context_high->fx_1h` score `-0.499` n `157` status `ready` deltaP `1.108` edge `-0.0034` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.6073` n `157` status `ready` deltaP `0.697` edge `0.0318` maxDD `-3.6309`
- `market_context_high->crypto_major_1h` score `-0.8384` n `157` status `ready` deltaP `-0.4682` edge `-0.0023` maxDD `-5.8323`
- `market_context_high->crypto_major_4h` score `-0.8399` n `152` status `ready` deltaP `5.6402` edge `0.1256` maxDD `-13.3376`
- `market_context_high->crypto_alt_4h` score `-1.0298` n `152` status `ready` deltaP `10.1011` edge `0.1788` maxDD `-19.5565`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
