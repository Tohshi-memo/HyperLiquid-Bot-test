# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T09:37:22.849107+00:00`
- Price records: `672`
- Market context records: `2129`
- Flow alert records: `8025`
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

- `market_context_high->crypto_alt_4h` score `13.3219` n `158` status `ready` deltaP `37.3784` edge `0.9546` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.9528` n `158` status `ready` deltaP `41.6795` edge `0.7712` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `6.1459` n `158` status `ready` deltaP `24.3555` edge `0.4247` maxDD `-2.6599`
- `market_context_high->equity_4h` score `5.0638` n `158` status `ready` deltaP `26.9296` edge `0.3519` maxDD `-5.0894`
- `market_context_high->index_24h` score `3.1907` n `157` status `ready` deltaP `13.3395` edge `0.2998` maxDD `-4.1604`
- `market_context_high->crypto_major_1h` score `3.1462` n `158` status `ready` deltaP `17.4354` edge `0.1981` maxDD `-2.1721`
- `market_context_high->metal_4h` score `3.1403` n `158` status `ready` deltaP `21.8605` edge `0.2547` maxDD `-4.7664`
- `market_context_high->index_4h` score `3.0837` n `158` status `ready` deltaP `22.37` edge `0.1762` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `2.9244` n `158` status `ready` deltaP `15.0402` edge `0.2298` maxDD `-4.9097`
- `news_risk_high->unknown_1h` score `2.6829` n `33` status `ready` deltaP `29.8721` edge `0.0547` maxDD `-1.7548`
- `market_context_high->equity_24h` score `2.3239` n `157` status `ready` deltaP `24.7658` edge `0.5184` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `1.9323` n `157` status `ready` deltaP `25.3003` edge `0.5244` maxDD `-35.8966`
- `market_context_high->crypto_major_24h` score `1.4836` n `157` status `ready` deltaP `21.1183` edge `0.908` maxDD `-62.3533`
- `news_risk_high->commodity_1h` score `0.8809` n `33` status `ready` deltaP `8.474` edge `0.0849` maxDD `-2.1052`
- `market_context_high->equity_1h` score `0.6956` n `158` status `ready` deltaP `9.2701` edge `0.075` maxDD `-2.6402`
- `market_context_high->metal_1h` score `0.466` n `158` status `ready` deltaP `8.044` edge `0.0522` maxDD `-2.3594`
- `market_context_high->metal_24h` score `0.187` n `157` status `ready` deltaP `11.2335` edge `0.3392` maxDD `-23.2095`
- `market_context_high->unknown_1h` score `0.0753` n `158` status `ready` deltaP `5.0159` edge `0.0448` maxDD `-3.0902`
- `market_context_high->fx_24h` score `-0.0413` n `157` status `ready` deltaP `15.1963` edge `0.0327` maxDD `-2.811`
- `market_context_high->index_1h` score `-0.0603` n `158` status `ready` deltaP `3.7368` edge `0.0291` maxDD `-1.3898`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
