# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T08:52:19.321291+00:00`
- Price records: `672`
- Market context records: `2126`
- Flow alert records: `8016`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9149`

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

- `market_context_high->crypto_alt_4h` score `13.3291` n `158` status `ready` deltaP `37.3784` edge `0.9552` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.9466` n `158` status `ready` deltaP `41.5271` edge `0.7717` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `6.0979` n `158` status `ready` deltaP `24.3555` edge `0.4207` maxDD `-2.6599`
- `market_context_high->equity_4h` score `5.1311` n `158` status `ready` deltaP `27.082` edge `0.3565` maxDD `-5.0894`
- `market_context_high->metal_4h` score `3.1945` n `158` status `ready` deltaP `22.0129` edge `0.2582` maxDD `-4.7664`
- `market_context_high->crypto_major_1h` score `3.139` n `158` status `ready` deltaP `17.4354` edge `0.1975` maxDD `-2.1721`
- `market_context_high->index_4h` score `3.1297` n `158` status `ready` deltaP `22.6748` edge `0.178` maxDD `-1.8022`
- `market_context_high->index_24h` score `3.0472` n `157` status `ready` deltaP `12.8204` edge `0.2913` maxDD `-4.1604`
- `market_context_high->crypto_alt_1h` score `2.8932` n `158` status `ready` deltaP `14.8905` edge `0.2282` maxDD `-4.9097`
- `news_risk_high->unknown_1h` score `2.6877` n `33` status `ready` deltaP `29.8721` edge `0.0551` maxDD `-1.7548`
- `market_context_high->equity_24h` score `2.1108` n `157` status `ready` deltaP `24.2468` edge `0.5041` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `1.6424` n `157` status `ready` deltaP `24.7813` edge `0.5037` maxDD `-35.8966`
- `market_context_high->crypto_major_24h` score `1.2959` n `157` status `ready` deltaP `20.5992` edge `0.8874` maxDD `-62.3533`
- `news_risk_high->commodity_1h` score `0.8258` n `33` status `ready` deltaP `8.0249` edge `0.0833` maxDD `-2.1052`
- `market_context_high->equity_1h` score `0.7292` n `158` status `ready` deltaP `9.4198` edge `0.0768` maxDD `-2.6402`
- `market_context_high->metal_1h` score `0.5056` n `158` status `ready` deltaP `8.3434` edge `0.0535` maxDD `-2.3594`
- `market_context_high->unknown_1h` score `0.0801` n `158` status `ready` deltaP `5.0159` edge `0.0452` maxDD `-3.0902`
- `market_context_high->metal_24h` score `0.0695` n `157` status `ready` deltaP `10.7145` edge `0.3276` maxDD `-23.2095`
- `market_context_high->index_1h` score `-0.0519` n `158` status `ready` deltaP `3.7368` edge `0.0298` maxDD `-1.3898`
- `market_context_high->fx_24h` score `-0.0761` n `157` status `ready` deltaP `14.6772` edge `0.0317` maxDD `-2.811`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
