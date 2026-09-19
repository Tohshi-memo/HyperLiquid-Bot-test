# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T16:22:30.556972+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8582`

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

- `news_risk_high->crypto_major_24h` score `51.9773` n `72` status `ready` deltaP `30.0347` edge `4.2204` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `45.6269` n `72` status `ready` deltaP `35.2431` edge `3.7052` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `42.7964` n `133` status `ready` deltaP `-3.0465` edge `3.61` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `16.9321` n `43` status `ready` deltaP `-12.6985` edge `1.5182` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `16.9321` n `43` status `ready` deltaP `-12.6985` edge `1.5182` maxDD `-0.4694`
- `news_risk_high->equity_24h` score `9.6775` n `72` status `ready` deltaP `39.5833` edge `0.5468` maxDD `-0.0053`
- `risk_on_high->commodity_24h` score `8.9709` n `43` status `ready` deltaP `47.3958` edge `0.4316` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.9709` n `43` status `ready` deltaP `47.3958` edge `0.4316` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.4547` n `133` status `ready` deltaP `39.877` edge `0.4079` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `5.8146` n `98` status `ready` deltaP `22.2281` edge `0.4573` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.3763` n `98` status `ready` deltaP `22.0756` edge `0.3433` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `3.3599` n `98` status `ready` deltaP `19.6719` edge `0.1954` maxDD `-2.058`
- `market_context_high->commodity_4h` score `2.5429` n `133` status `ready` deltaP `27.1387` edge `0.0728` maxDD `-0.345`
- `risk_on_high->commodity_4h` score `2.4599` n `43` status `ready` deltaP `28.7649` edge `0.0482` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.4599` n `43` status `ready` deltaP `28.7649` edge `0.0482` maxDD `-0.1313`
- `news_risk_high->crypto_major_1h` score `2.4462` n `98` status `ready` deltaP `20.5701` edge `0.119` maxDD `-2.8494`
- `news_risk_high->metal_24h` score `1.7261` n `72` status `ready` deltaP `22.5694` edge `0.0778` maxDD `-2.4203`
- `risk_on_high->commodity_1h` score `1.5884` n `43` status `ready` deltaP `19.6978` edge `0.0196` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `1.5884` n `43` status `ready` deltaP `19.6978` edge `0.0196` maxDD `-0.1507`
- `market_context_high->commodity_1h` score `1.5275` n `133` status `ready` deltaP `19.0334` edge `0.0256` maxDD `-0.3491`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
