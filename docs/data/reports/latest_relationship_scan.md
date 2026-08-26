# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T03:07:24.517119+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14808`

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

- `news_risk_high->unknown_24h` score `46.1862` n `51` status `ready` deltaP `11.6319` edge `3.7713` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.5808` n `53` status `ready` deltaP `24.0652` edge `0.8979` maxDD `-0.1281`
- `news_risk_high->equity_24h` score `6.9861` n `51` status `ready` deltaP `29.9939` edge `0.4753` maxDD `-4.7801`
- `news_risk_high->crypto_alt_24h` score `5.4134` n `51` status `ready` deltaP `28.4722` edge `0.2613` maxDD `0.0`
- `news_risk_high->index_24h` score `3.9944` n `51` status `ready` deltaP `40.2676` edge `0.0796` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.2882` n `53` status `ready` deltaP `15.8626` edge `0.2038` maxDD `-0.8426`
- `news_risk_high->fx_4h` score `2.8315` n `53` status `ready` deltaP `34.0486` edge `0.0224` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.6222` n `133` status `ready` deltaP `22.2068` edge `0.1113` maxDD `-0.5994`
- `news_risk_high->equity_4h` score `1.5703` n `53` status `ready` deltaP `19.1268` edge `0.0804` maxDD `-2.164`
- `news_risk_high->metal_24h` score `1.1505` n `51` status `ready` deltaP `29.1156` edge `-0.094` maxDD `-0.0053`
- `news_risk_high->fx_1h` score `1.0578` n `53` status `ready` deltaP `14.8712` edge `0.006` maxDD `-0.0257`
- `news_risk_high->commodity_1h` score `0.4943` n `53` status `ready` deltaP `11.4253` edge `-0.0037` maxDD `-0.5024`
- `news_risk_high->equity_1h` score `0.4248` n `53` status `ready` deltaP `13.0748` edge `0.0037` maxDD `-0.9128`
- `market_context_high->unknown_1h` score `0.317` n `134` status `ready` deltaP `11.5962` edge `-0.006` maxDD `-1.5916`
- `news_risk_high->index_4h` score `0.0089` n `53` status `ready` deltaP `5.4418` edge `0.0042` maxDD `-0.1788`
- `news_risk_high->index_1h` score `-0.0861` n `53` status `ready` deltaP `3.7002` edge `-0.0004` maxDD `-0.1583`
- `market_context_high->fx_1h` score `-0.4843` n `134` status `ready` deltaP `1.7763` edge `-0.0007` maxDD `-0.8587`
- `news_risk_high->metal_1h` score `-0.5708` n `53` status `ready` deltaP `-1.8105` edge `-0.0129` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.7795` n `53` status `ready` deltaP `2.5282` edge `-0.0287` maxDD `-0.249`
- `news_risk_high->commodity_4h` score `-1.0521` n `53` status `ready` deltaP `-2.1255` edge `0.0026` maxDD `-1.1986`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
