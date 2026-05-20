# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T09:22:16.083374+00:00`
- Price records: `672`
- Market context records: `1307`
- Flow alert records: `5674`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8781`

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

- `market_context_high->crypto_major_24h` score `16.882` n `128` status `ready` deltaP `41.059` edge `1.2463` maxDD `-8.0553`
- `market_context_high->metal_24h` score `13.0607` n `128` status `ready` deltaP `11.8056` edge `1.1764` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.5892` n `128` status `ready` deltaP `28.3854` edge `0.8115` maxDD `-15.1306`
- `market_context_high->index_24h` score `6.0271` n `128` status `ready` deltaP `31.4236` edge `0.4014` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.9074` n `128` status `ready` deltaP `24.3056` edge `0.5716` maxDD `-14.2815`
- `market_context_high->equity_4h` score `2.6005` n `157` status `ready` deltaP `13.1107` edge `0.1998` maxDD `-3.6396`
- `market_context_high->unknown_24h` score `2.1731` n `128` status `ready` deltaP `0.1736` edge `0.4529` maxDD `-10.1706`
- `market_context_high->commodity_24h` score `0.8662` n `128` status `ready` deltaP `-15.2778` edge `0.3222` maxDD `-6.8535`
- `market_context_high->fx_24h` score `0.7491` n `128` status `ready` deltaP `9.4619` edge `0.0458` maxDD `-0.3831`
- `market_context_high->metal_4h` score `0.2085` n `157` status `ready` deltaP `13.5253` edge `0.0703` maxDD `-6.4478`
- `market_context_high->equity_1h` score `0.2008` n `157` status `ready` deltaP `3.6671` edge `0.035` maxDD `-1.7505`
- `market_context_high->index_4h` score `0.1951` n `157` status `ready` deltaP `5.9413` edge `0.0943` maxDD `-3.7119`
- `market_context_high->index_1h` score `0.0991` n `157` status `ready` deltaP `6.0624` edge `0.0177` maxDD `-1.6329`
- `market_context_high->metal_1h` score `-0.1014` n `157` status `ready` deltaP `8.6426` edge `0.0029` maxDD `-2.8509`
- `market_context_high->fx_1h` score `-0.4858` n `157` status `ready` deltaP `1.2577` edge `-0.0033` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.6013` n `157` status `ready` deltaP `0.8467` edge `0.0313` maxDD `-3.6309`
- `market_context_high->crypto_alt_4h` score `-0.8725` n `157` status `ready` deltaP `10.2969` edge `0.1906` maxDD `-19.5565`
- `market_context_high->crypto_major_1h` score `-0.8875` n `157` status `ready` deltaP `-1.067` edge `-0.0046` maxDD `-5.8323`
- `market_context_high->unknown_4h` score `-0.9435` n `157` status `ready` deltaP `3.5634` edge `0.0824` maxDD `-11.1695`
- `market_context_high->commodity_1h` score `-0.9868` n `157` status `ready` deltaP `-2.153` edge `-0.0064` maxDD `-2.252`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
