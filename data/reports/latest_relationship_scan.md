# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T09:22:31.884249+00:00`
- Price records: `672`
- Market context records: `2548`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9252`

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

- `market_context_high->unknown_24h` score `5.6131` n `120` status `ready` deltaP `19.6181` edge `0.3698` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `5.5274` n `151` status `ready` deltaP `24.1671` edge `0.5674` maxDD `-15.4319`
- `market_context_high->crypto_major_24h` score `4.5785` n `120` status `ready` deltaP `11.1111` edge `0.5728` maxDD `-15.2264`
- `market_context_high->crypto_major_4h` score `3.8722` n `151` status `ready` deltaP `17.2923` edge `0.3884` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `1.9325` n `151` status `ready` deltaP `10.8171` edge `0.1939` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `1.1982` n `151` status `ready` deltaP `9.9427` edge `0.1523` maxDD `-6.1656`
- `market_context_high->equity_24h` score `0.8355` n `120` status `ready` deltaP `17.5` edge `0.0143` maxDD `-2.2408`
- `market_context_high->index_24h` score `0.7562` n `120` status `ready` deltaP `7.0486` edge `0.1141` maxDD `-2.5127`
- `market_context_high->crypto_major_1h` score `0.7181` n `151` status `ready` deltaP `8.3188` edge `0.1238` maxDD `-4.2199`
- `market_context_high->crypto_alt_24h` score `-0.0804` n `120` status `ready` deltaP `-1.7361` edge `0.6587` maxDD `-40.5944`
- `market_context_high->index_4h` score `-0.0891` n `151` status `ready` deltaP `6.2591` edge `0.035` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.1113` n `151` status `ready` deltaP `3.3202` edge `0.0376` maxDD `-2.8543`
- `market_context_high->index_1h` score `-0.2273` n `151` status `ready` deltaP `3.0386` edge `0.0102` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.3319` n `151` status `ready` deltaP `0.9934` edge `0.0043` maxDD `-0.278`
- `market_context_high->commodity_1h` score `-0.3969` n `151` status `ready` deltaP `3.5333` edge `0.0134` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.4149` n `151` status `ready` deltaP `1.5287` edge `0.0114` maxDD `-2.9823`
- `market_context_high->equity_1h` score `-0.8002` n `151` status `ready` deltaP `-0.2141` edge `0.0186` maxDD `-2.7085`
- `market_context_high->metal_4h` score `-0.8044` n `151` status `ready` deltaP `3.9321` edge `0.0455` maxDD `-4.7664`
- `market_context_high->fx_24h` score `-0.861` n `120` status `ready` deltaP `0.7986` edge `0.0031` maxDD `-2.1715`
- `market_context_high->fx_4h` score `-0.8623` n `151` status `ready` deltaP `0.2261` edge `0.0126` maxDD `-0.8774`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
