# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T12:52:24.969306+00:00`
- Price records: `672`
- Market context records: `2143`
- Flow alert records: `8065`
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

- `market_context_high->crypto_alt_4h` score `13.1615` n `158` status `ready` deltaP `36.7687` edge `0.9453` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.731` n `158` status `ready` deltaP `40.9173` edge `0.7578` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `6.5924` n `158` status `ready` deltaP `25.4226` edge `0.4548` maxDD `-2.6599`
- `news_risk_high->commodity_4h` score `6.2142` n `33` status `ready` deltaP `28.1966` edge `0.397` maxDD `-3.0367`
- `market_context_high->equity_4h` score `4.9502` n `158` status `ready` deltaP `26.3198` edge `0.3465` maxDD `-5.0894`
- `market_context_high->index_24h` score `3.7931` n `157` status `ready` deltaP `15.3795` edge `0.3364` maxDD `-4.1604`
- `market_context_high->equity_24h` score `3.2278` n `157` status `ready` deltaP `26.8389` edge `0.5799` maxDD `-33.1875`
- `market_context_high->crypto_major_1h` score `3.1391` n `158` status `ready` deltaP `17.136` edge `0.1995` maxDD `-2.1721`
- `market_context_high->metal_4h` score `3.0495` n `158` status `ready` deltaP `21.2507` edge `0.2512` maxDD `-4.7664`
- `market_context_high->crypto_alt_1h` score `2.9927` n `158` status `ready` deltaP `15.639` edge `0.2315` maxDD `-4.9097`
- `market_context_high->index_4h` score `2.9845` n `158` status `ready` deltaP `21.7602` edge `0.172` maxDD `-1.8022`
- `market_context_high->unknown_24h` score `2.8941` n `157` status `ready` deltaP `27.362` edge `0.5908` maxDD `-35.8966`
- `news_risk_high->fx_4h` score `2.4163` n `33` status `ready` deltaP `31.3424` edge `0.0108` maxDD `-0.1382`
- `market_context_high->crypto_major_24h` score `2.1271` n `157` status `ready` deltaP `22.199` edge `0.9833` maxDD `-62.3533`
- `news_risk_high->unknown_4h` score `1.4394` n `33` status `ready` deltaP `18.0387` edge `0.1366` maxDD `-2.7857`
- `news_risk_high->unknown_1h` score `1.0917` n `39` status `ready` deltaP `20.8967` edge `-0.0014` maxDD `-1.7548`
- `market_context_high->equity_1h` score `0.7435` n `158` status `ready` deltaP `9.7192` edge `0.076` maxDD `-2.6402`
- `news_risk_high->fx_1h` score `0.596` n `39` status `ready` deltaP `9.5732` edge `0.0115` maxDD `-0.0524`
- `market_context_high->metal_24h` score `0.5886` n `157` status `ready` deltaP `13.1679` edge `0.3778` maxDD `-23.2095`
- `market_context_high->metal_1h` score `0.5583` n `158` status `ready` deltaP `8.7925` edge `0.0549` maxDD `-2.3594`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
