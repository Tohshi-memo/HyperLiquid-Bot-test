# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T14:52:25.326605+00:00`
- Price records: `672`
- Market context records: `1330`
- Flow alert records: `5742`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8783`

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

- `market_context_high->crypto_major_24h` score `15.3333` n `128` status `ready` deltaP `37.2395` edge `1.1427` maxDD `-8.0553`
- `market_context_high->metal_24h` score `13.3398` n `128` status `ready` deltaP `13.1944` edge `1.1904` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.6648` n `128` status `ready` deltaP `28.3854` edge `0.8178` maxDD `-15.1306`
- `market_context_high->index_24h` score `5.1143` n `128` status `ready` deltaP `27.6042` edge `0.3508` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.8259` n `128` status `ready` deltaP `20.4861` edge `0.4584` maxDD `-14.2815`
- `market_context_high->equity_4h` score `2.3581` n `157` status `ready` deltaP `12.1961` edge `0.1857` maxDD `-3.6396`
- `market_context_high->commodity_24h` score `1.7477` n `128` status `ready` deltaP `-11.4583` edge `0.3702` maxDD `-6.8535`
- `market_context_high->unknown_24h` score `1.3946` n `128` status `ready` deltaP `-2.7778` edge `0.4077` maxDD `-10.1706`
- `market_context_high->fx_24h` score `1.1782` n `128` status `ready` deltaP `13.2813` edge `0.0561` maxDD `-0.3831`
- `market_context_high->metal_4h` score `0.1967` n `157` status `ready` deltaP `13.6778` edge `0.0683` maxDD `-6.4478`
- `market_context_high->equity_1h` score `0.1804` n `157` status `ready` deltaP `3.3677` edge `0.0353` maxDD `-1.7505`
- `market_context_high->index_4h` score `0.0764` n `157` status `ready` deltaP `4.8742` edge `0.0862` maxDD `-3.7119`
- `market_context_high->index_1h` score `0.036` n `157` status `ready` deltaP `5.1642` edge `0.0156` maxDD `-1.6329`
- `market_context_high->metal_1h` score `-0.0547` n `157` status `ready` deltaP `9.2414` edge `0.0028` maxDD `-2.8509`
- `market_context_high->fx_1h` score `-0.5002` n `157` status `ready` deltaP `1.108` edge `-0.0035` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.6756` n `157` status `ready` deltaP `0.3976` edge `0.0281` maxDD `-3.6309`
- `market_context_high->commodity_1h` score `-0.8825` n `157` status `ready` deltaP `-1.7039` edge `-0.0007` maxDD `-2.252`
- `market_context_high->crypto_major_1h` score `-0.9763` n `157` status `ready` deltaP `-1.9652` edge `-0.01` maxDD `-5.8323`
- `market_context_high->crypto_alt_4h` score `-1.1159` n `157` status `ready` deltaP `9.5347` edge `0.1754` maxDD `-19.5565`
- `market_context_high->unknown_4h` score `-1.1225` n `157` status `ready` deltaP `3.1061` edge `0.0625` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
