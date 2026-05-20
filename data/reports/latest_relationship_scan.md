# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T11:22:17.795194+00:00`
- Price records: `672`
- Market context records: `1316`
- Flow alert records: `5699`
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

- `market_context_high->crypto_major_24h` score `16.3785` n `128` status `ready` deltaP `39.6701` edge `1.2136` maxDD `-8.0553`
- `market_context_high->metal_24h` score `13.3475` n `128` status `ready` deltaP `13.0208` edge `1.1922` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.6564` n `128` status `ready` deltaP `28.3854` edge `0.8171` maxDD `-15.1306`
- `market_context_high->index_24h` score `5.7636` n `128` status `ready` deltaP `30.0347` edge `0.3887` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.5661` n `128` status `ready` deltaP `22.9167` edge `0.5371` maxDD `-14.2815`
- `market_context_high->equity_4h` score `2.5043` n `157` status `ready` deltaP `12.9583` edge `0.1928` maxDD `-3.6396`
- `market_context_high->unknown_24h` score `2.045` n `128` status `ready` deltaP `-0.3472` edge `0.4457` maxDD `-10.1706`
- `market_context_high->commodity_24h` score `1.1165` n `128` status `ready` deltaP `-13.8889` edge `0.3338` maxDD `-6.8535`
- `market_context_high->fx_24h` score `0.913` n `128` status `ready` deltaP `10.8507` edge `0.0502` maxDD `-0.3831`
- `market_context_high->equity_1h` score `0.2272` n `157` status `ready` deltaP `3.6671` edge `0.0372` maxDD `-1.7505`
- `market_context_high->index_4h` score `0.1566` n `157` status `ready` deltaP `5.6364` edge `0.0914` maxDD `-3.7119`
- `market_context_high->metal_4h` score `0.1495` n `157` status `ready` deltaP `13.3729` edge `0.0664` maxDD `-6.4478`
- `market_context_high->index_1h` score `0.1201` n `157` status `ready` deltaP `6.2121` edge `0.0194` maxDD `-1.6329`
- `market_context_high->metal_1h` score `-0.0811` n `157` status `ready` deltaP `8.7923` edge `0.0036` maxDD `-2.8509`
- `market_context_high->fx_1h` score `-0.523` n `157` status `ready` deltaP `0.8086` edge `-0.0034` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.6277` n `157` status `ready` deltaP `0.5473` edge `0.0311` maxDD `-3.6309`
- `market_context_high->crypto_alt_4h` score `-0.8677` n `157` status `ready` deltaP `10.2969` edge `0.191` maxDD `-19.5565`
- `market_context_high->crypto_major_1h` score `-0.9117` n `157` status `ready` deltaP `-1.3664` edge `-0.0057` maxDD `-5.8323`
- `market_context_high->unknown_4h` score `-0.9395` n `157` status `ready` deltaP `3.7158` edge `0.0819` maxDD `-11.1695`
- `market_context_high->commodity_1h` score `-0.9748` n `157` status `ready` deltaP `-2.153` edge `-0.0054` maxDD `-2.252`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
