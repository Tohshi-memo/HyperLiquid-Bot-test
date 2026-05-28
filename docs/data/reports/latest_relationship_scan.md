# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T09:22:18.659351+00:00`
- Price records: `672`
- Market context records: `2128`
- Flow alert records: `8022`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9158`

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

- `market_context_high->crypto_alt_4h` score `13.3449` n `158` status `ready` deltaP `37.5309` edge `0.9555` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.9588` n `158` status `ready` deltaP `41.6795` edge `0.7717` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `6.1255` n `158` status `ready` deltaP `24.3555` edge `0.423` maxDD `-2.6599`
- `market_context_high->equity_4h` score `5.0891` n `158` status `ready` deltaP `27.082` edge `0.353` maxDD `-5.0894`
- `market_context_high->metal_4h` score `3.1609` n `158` status `ready` deltaP `22.0129` edge `0.2554` maxDD `-4.7664`
- `market_context_high->crypto_major_1h` score `3.1462` n `158` status `ready` deltaP `17.4354` edge `0.1981` maxDD `-2.1721`
- `market_context_high->index_24h` score `3.1409` n `157` status `ready` deltaP `13.1664` edge `0.2968` maxDD `-4.1604`
- `market_context_high->index_4h` score `3.1019` n `158` status `ready` deltaP `22.5224` edge `0.1767` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `2.9208` n `158` status `ready` deltaP `15.0402` edge `0.2295` maxDD `-4.9097`
- `news_risk_high->unknown_1h` score `2.6793` n `33` status `ready` deltaP `29.8721` edge `0.0544` maxDD `-1.7548`
- `market_context_high->equity_24h` score `2.2477` n `157` status `ready` deltaP `24.5928` edge `0.5132` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `1.8393` n `157` status `ready` deltaP `25.1273` edge `0.5178` maxDD `-35.8966`
- `market_context_high->crypto_major_24h` score `1.4208` n `157` status `ready` deltaP `20.9453` edge `0.9011` maxDD `-62.3533`
- `news_risk_high->commodity_1h` score `0.8666` n `33` status `ready` deltaP `8.3243` edge `0.0847` maxDD `-2.1052`
- `market_context_high->equity_1h` score `0.7004` n `158` status `ready` deltaP `9.2701` edge `0.0754` maxDD `-2.6402`
- `market_context_high->metal_1h` score `0.4816` n `158` status `ready` deltaP `8.1937` edge `0.0525` maxDD `-2.3594`
- `market_context_high->metal_24h` score `0.1444` n `157` status `ready` deltaP `11.0605` edge `0.3349` maxDD `-23.2095`
- `market_context_high->unknown_1h` score `0.0717` n `158` status `ready` deltaP `5.0159` edge `0.0445` maxDD `-3.0902`
- `market_context_high->fx_24h` score `-0.0526` n `157` status `ready` deltaP `15.0232` edge `0.0324` maxDD `-2.811`
- `market_context_high->index_1h` score `-0.0579` n `158` status `ready` deltaP `3.7368` edge `0.0293` maxDD `-1.3898`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
