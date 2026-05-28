# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T08:22:16.167028+00:00`
- Price records: `672`
- Market context records: `2123`
- Flow alert records: `8009`
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

- `market_context_high->crypto_alt_4h` score `13.2831` n `158` status `ready` deltaP `37.0735` edge `0.9534` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.92` n `158` status `ready` deltaP `41.3746` edge `0.7705` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `6.0243` n `158` status `ready` deltaP `24.0506` edge `0.4166` maxDD `-2.6599`
- `market_context_high->equity_4h` score `5.1708` n `158` status `ready` deltaP `27.082` edge `0.3598` maxDD `-5.0894`
- `market_context_high->metal_4h` score `3.2125` n `158` status `ready` deltaP `22.0129` edge `0.2597` maxDD `-4.7664`
- `market_context_high->index_4h` score `3.1477` n `158` status `ready` deltaP `22.6748` edge `0.1795` maxDD `-1.8022`
- `market_context_high->crypto_major_1h` score `3.1306` n `158` status `ready` deltaP `17.4354` edge `0.1968` maxDD `-2.1721`
- `market_context_high->index_24h` score `2.9475` n `157` status `ready` deltaP `12.4744` edge `0.2853` maxDD `-4.1604`
- `market_context_high->crypto_alt_1h` score `2.8668` n `158` status `ready` deltaP `14.7408` edge `0.227` maxDD `-4.9097`
- `news_risk_high->unknown_1h` score `2.6662` n `33` status `ready` deltaP `29.7224` edge `0.0543` maxDD `-1.7548`
- `market_context_high->equity_24h` score `1.9631` n `157` status `ready` deltaP `23.9008` edge `0.4941` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `1.4239` n `157` status `ready` deltaP `24.4353` edge `0.4878` maxDD `-35.8966`
- `market_context_high->crypto_major_24h` score `1.1609` n `157` status `ready` deltaP `20.2532` edge `0.8724` maxDD `-62.3533`
- `news_risk_high->commodity_1h` score `0.7911` n `33` status `ready` deltaP `7.7255` edge `0.0824` maxDD `-2.1052`
- `market_context_high->equity_1h` score `0.7639` n `158` status `ready` deltaP `9.7192` edge `0.0777` maxDD `-2.6402`
- `market_context_high->metal_1h` score `0.5092` n `158` status `ready` deltaP `8.3434` edge `0.0538` maxDD `-2.3594`
- `market_context_high->unknown_1h` score `0.0586` n `158` status `ready` deltaP `4.8662` edge `0.0444` maxDD `-3.0902`
- `market_context_high->index_1h` score `-0.0208` n `158` status `ready` deltaP `4.0362` edge `0.0304` maxDD `-1.3898`
- `market_context_high->metal_24h` score `-0.021` n `157` status `ready` deltaP `10.3685` edge `0.3183` maxDD `-23.2095`
- `news_risk_high->equity_1h` score `-0.0633` n `33` status `ready` deltaP `3.8696` edge `0.0211` maxDD `-1.8406`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
