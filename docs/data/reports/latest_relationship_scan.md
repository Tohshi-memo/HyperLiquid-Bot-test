# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T10:52:18.101122+00:00`
- Price records: `672`
- Market context records: `1314`
- Flow alert records: `5693`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8782`

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

- `market_context_high->crypto_major_24h` score `16.5143` n `128` status `ready` deltaP `40.0173` edge `1.2226` maxDD `-8.0553`
- `market_context_high->metal_24h` score `13.2988` n `128` status `ready` deltaP `12.8472` edge `1.1893` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.6432` n `128` status `ready` deltaP `28.3854` edge `0.816` maxDD `-15.1306`
- `market_context_high->index_24h` score `5.8357` n `128` status `ready` deltaP `30.3819` edge `0.3924` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.6598` n `128` status `ready` deltaP `23.2639` edge `0.5468` maxDD `-14.2815`
- `market_context_high->equity_4h` score `2.5151` n `157` status `ready` deltaP `12.9583` edge `0.1937` maxDD `-3.6396`
- `market_context_high->unknown_24h` score `2.1172` n `128` status `ready` deltaP `0.0` edge `0.4494` maxDD `-10.1706`
- `market_context_high->commodity_24h` score `1.0407` n `128` status `ready` deltaP `-14.2361` edge `0.3298` maxDD `-6.8535`
- `market_context_high->fx_24h` score `0.8732` n `128` status `ready` deltaP `10.5035` edge `0.0492` maxDD `-0.3831`
- `market_context_high->equity_1h` score `0.2104` n `157` status `ready` deltaP `3.6671` edge `0.0358` maxDD `-1.7505`
- `market_context_high->metal_4h` score `0.1737` n `157` status `ready` deltaP `13.5253` edge `0.0674` maxDD `-6.4478`
- `market_context_high->index_4h` score `0.1715` n `157` status `ready` deltaP `5.7888` edge `0.0923` maxDD `-3.7119`
- `market_context_high->index_1h` score `0.1155` n `157` status `ready` deltaP `6.2121` edge `0.0188` maxDD `-1.6329`
- `market_context_high->metal_1h` score `-0.0811` n `157` status `ready` deltaP `8.7923` edge `0.0036` maxDD `-2.8509`
- `market_context_high->fx_1h` score `-0.523` n `157` status `ready` deltaP `0.8086` edge `-0.0034` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.6612` n `157` status `ready` deltaP `0.2479` edge `0.0303` maxDD `-3.6309`
- `market_context_high->crypto_alt_4h` score `-0.8617` n `157` status `ready` deltaP `10.2969` edge `0.1915` maxDD `-19.5565`
- `market_context_high->crypto_major_1h` score `-0.9194` n `157` status `ready` deltaP `-1.5161` edge `-0.0057` maxDD `-5.8323`
- `market_context_high->unknown_4h` score `-0.9364` n `157` status `ready` deltaP `3.7158` edge `0.0823` maxDD `-11.1695`
- `market_context_high->commodity_1h` score `-0.9964` n `157` status `ready` deltaP `-2.3027` edge `-0.0062` maxDD `-2.252`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
