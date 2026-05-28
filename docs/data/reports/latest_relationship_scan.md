# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T10:07:18.026568+00:00`
- Price records: `672`
- Market context records: `2131`
- Flow alert records: `8031`
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

- `market_context_high->crypto_alt_4h` score `13.2519` n `158` status `ready` deltaP `37.0735` edge `0.9508` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.902` n `158` status `ready` deltaP `41.3746` edge `0.769` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `6.2119` n `158` status `ready` deltaP `24.3555` edge `0.4302` maxDD `-2.6599`
- `market_context_high->equity_4h` score `5.0154` n `158` status `ready` deltaP `26.6247` edge `0.3499` maxDD `-5.0894`
- `market_context_high->index_24h` score `3.2952` n `157` status `ready` deltaP `13.6855` edge `0.3062` maxDD `-4.1604`
- `market_context_high->crypto_major_1h` score `3.1606` n `158` status `ready` deltaP `17.4354` edge `0.1993` maxDD `-2.1721`
- `market_context_high->metal_4h` score `3.1039` n `158` status `ready` deltaP `21.5556` edge `0.2537` maxDD `-4.7664`
- `market_context_high->index_4h` score `3.0449` n `158` status `ready` deltaP `22.0651` edge `0.175` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `2.9256` n `158` status `ready` deltaP `15.0402` edge `0.2299` maxDD `-4.9097`
- `news_risk_high->unknown_1h` score `2.7597` n `33` status `ready` deltaP `30.0218` edge `0.0601` maxDD `-1.7548`
- `market_context_high->equity_24h` score `2.4884` n `157` status `ready` deltaP `25.1118` edge `0.5298` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `2.1232` n `157` status `ready` deltaP `25.6463` edge `0.538` maxDD `-35.8966`
- `market_context_high->crypto_major_24h` score `1.5924` n `157` status `ready` deltaP `21.2913` edge `0.9208` maxDD `-62.3533`
- `news_risk_high->commodity_1h` score `0.8642` n `33` status `ready` deltaP `8.3243` edge `0.0845` maxDD `-2.1052`
- `market_context_high->equity_1h` score `0.7136` n `158` status `ready` deltaP `9.4198` edge `0.0755` maxDD `-2.6402`
- `market_context_high->metal_1h` score `0.4648` n `158` status `ready` deltaP `8.044` edge `0.0521` maxDD `-2.3594`
- `market_context_high->metal_24h` score `0.272` n `157` status `ready` deltaP `11.5795` edge `0.3478` maxDD `-23.2095`
- `market_context_high->unknown_1h` score `0.1521` n `158` status `ready` deltaP `5.1656` edge `0.0502` maxDD `-3.0902`
- `market_context_high->fx_24h` score `-0.0179` n `157` status `ready` deltaP `15.5423` edge `0.0334` maxDD `-2.811`
- `market_context_high->index_1h` score `-0.0316` n `158` status `ready` deltaP `4.0362` edge `0.0295` maxDD `-1.3898`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
