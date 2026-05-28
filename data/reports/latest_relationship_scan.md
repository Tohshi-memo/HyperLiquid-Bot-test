# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T09:07:21.446074+00:00`
- Price records: `672`
- Market context records: `2127`
- Flow alert records: `8019`
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

- `market_context_high->crypto_alt_4h` score `13.3497` n `158` status `ready` deltaP `37.5309` edge `0.9559` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.9624` n `158` status `ready` deltaP `41.6795` edge `0.772` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `6.1135` n `158` status `ready` deltaP `24.3555` edge `0.422` maxDD `-2.6599`
- `market_context_high->equity_4h` score `5.1071` n `158` status `ready` deltaP `27.082` edge `0.3545` maxDD `-5.0894`
- `market_context_high->metal_4h` score `3.1777` n `158` status `ready` deltaP `22.0129` edge `0.2568` maxDD `-4.7664`
- `market_context_high->crypto_major_1h` score `3.1462` n `158` status `ready` deltaP `17.4354` edge `0.1981` maxDD `-2.1721`
- `market_context_high->index_4h` score `3.1079` n `158` status `ready` deltaP `22.5224` edge `0.1772` maxDD `-1.8022`
- `market_context_high->index_24h` score `3.0934` n `157` status `ready` deltaP `12.9934` edge `0.294` maxDD `-4.1604`
- `market_context_high->crypto_alt_1h` score `2.9196` n `158` status `ready` deltaP `15.0402` edge `0.2294` maxDD `-4.9097`
- `news_risk_high->unknown_1h` score `2.6841` n `33` status `ready` deltaP `29.8721` edge `0.0548` maxDD `-1.7548`
- `market_context_high->equity_24h` score `2.1775` n `157` status `ready` deltaP `24.4198` edge `0.5085` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `1.7427` n `157` status `ready` deltaP `24.9543` edge `0.5109` maxDD `-35.8966`
- `market_context_high->crypto_major_24h` score `1.358` n `157` status `ready` deltaP `20.7723` edge `0.8942` maxDD `-62.3533`
- `news_risk_high->commodity_1h` score `0.8474` n `33` status `ready` deltaP `8.1746` edge `0.0841` maxDD `-2.1052`
- `market_context_high->equity_1h` score `0.7088` n `158` status `ready` deltaP `9.2701` edge `0.0761` maxDD `-2.6402`
- `market_context_high->metal_1h` score `0.502` n `158` status `ready` deltaP `8.3434` edge `0.0532` maxDD `-2.3594`
- `market_context_high->metal_24h` score `0.1074` n `157` status `ready` deltaP `10.8875` edge `0.3313` maxDD `-23.2095`
- `market_context_high->unknown_1h` score `0.0765` n `158` status `ready` deltaP `5.0159` edge `0.0449` maxDD `-3.0902`
- `market_context_high->index_1h` score `-0.0543` n `158` status `ready` deltaP `3.7368` edge `0.0296` maxDD `-1.3898`
- `market_context_high->fx_24h` score `-0.064` n `157` status `ready` deltaP `14.8502` edge `0.0321` maxDD `-2.811`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
