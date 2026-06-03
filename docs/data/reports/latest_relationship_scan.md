# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T15:07:34.497760+00:00`
- Price records: `672`
- Market context records: `2774`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9237`

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

- `market_context_high->unknown_24h` score `3.9226` n `137` status `ready` deltaP `8.0773` edge `0.3195` maxDD `-1.7175`
- `market_context_high->crypto_alt_24h` score `2.3085` n `137` status `ready` deltaP `4.2947` edge `0.659` maxDD `-22.6673`
- `market_context_high->unknown_4h` score `0.9688` n `142` status `ready` deltaP `6.4904` edge `0.1428` maxDD `-3.7602`
- `market_context_high->commodity_24h` score `0.221` n `137` status `ready` deltaP `9.9325` edge `0.2715` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.107` n `142` status `ready` deltaP `11.3192` edge `0.0224` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.0289` n `142` status `ready` deltaP `4.0314` edge `0.0438` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.1615` n `142` status `ready` deltaP `3.2998` edge `0.0067` maxDD `-1.2855`
- `market_context_high->commodity_1h` score `-0.5875` n `142` status `ready` deltaP `0.3163` edge `-0.0021` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.5993` n `142` status `ready` deltaP `-1.2861` edge `0.003` maxDD `-0.2164`
- `market_context_high->crypto_alt_1h` score `-0.6913` n `142` status `ready` deltaP `5.2459` edge `0.0524` maxDD `-10.747`
- `market_context_high->metal_1h` score `-0.7004` n `142` status `ready` deltaP `-0.1666` edge `-0.0041` maxDD `-3.0996`
- `market_context_high->crypto_major_1h` score `-0.9225` n `142` status `ready` deltaP `3.926` edge `0.0425` maxDD `-9.622`
- `market_context_high->fx_4h` score `-1.1739` n `142` status `ready` deltaP `-4.0579` edge `0.0071` maxDD `-0.5631`
- `market_context_high->equity_1h` score `-1.1856` n `142` status `ready` deltaP `-4.0967` edge `0.0118` maxDD `-2.6634`
- `market_context_high->crypto_alt_4h` score `-1.3851` n `142` status `ready` deltaP `14.0329` edge `0.2251` maxDD `-28.7261`
- `market_context_high->fx_24h` score `-1.4161` n `137` status `ready` deltaP `-1.5182` edge `-0.0207` maxDD `-0.6418`
- `market_context_high->commodity_4h` score `-1.5502` n `142` status `ready` deltaP `0.161` edge `-0.0078` maxDD `-10.0279`
- `market_context_high->equity_4h` score `-1.9019` n `142` status `ready` deltaP `-0.0193` edge `-0.0204` maxDD `-5.7037`
- `market_context_high->metal_4h` score `-2.3613` n `142` status `ready` deltaP `-2.1427` edge `-0.0334` maxDD `-11.4038`
- `market_context_high->crypto_major_4h` score `-2.6061` n `142` status `ready` deltaP `5.1249` edge `0.1223` maxDD `-32.2466`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
