# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T09:07:28.954329+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8502`

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

- `news_risk_high->crypto_major_24h` score `55.2097` n `72` status `ready` deltaP `35.0694` edge `4.4562` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `48.3106` n `72` status `ready` deltaP `39.5834` edge `3.8999` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `36.9997` n `144` status `ready` deltaP `-2.185` edge `3.1212` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `11.441` n `72` status `ready` deltaP `44.618` edge `0.6602` maxDD `-0.0053`
- `risk_on_high->unknown_4h` score `8.2471` n `52` status `ready` deltaP `-9.076` edge `0.7703` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `8.2471` n `52` status `ready` deltaP `-9.076` edge `0.7703` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.2352` n `52` status `ready` deltaP `44.9653` edge `0.3865` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.2352` n `52` status `ready` deltaP `44.9653` edge `0.3865` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.017` n `144` status `ready` deltaP `38.0209` edge `0.3838` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `6.7241` n `81` status `ready` deltaP `23.0974` edge `0.5273` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.6221` n `81` status `ready` deltaP `19.9883` edge `0.3777` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `3.3225` n `81` status `ready` deltaP `17.4503` edge `0.2071` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.7144` n `81` status `ready` deltaP `20.9673` edge `0.1387` maxDD `-2.8494`
- `risk_on_high->commodity_4h` score `2.6453` n `52` status `ready` deltaP `31.4728` edge `0.0456` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.6453` n `52` status `ready` deltaP `31.4728` edge `0.0456` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.4933` n `144` status `ready` deltaP `27.2527` edge `0.0679` maxDD `-0.345`
- `news_risk_high->metal_24h` score `1.8662` n `72` status `ready` deltaP `24.3056` edge `0.0779` maxDD `-2.4203`
- `news_risk_high->fx_4h` score `1.2704` n `81` status `ready` deltaP `14.3029` edge `0.0324` maxDD `-0.084`
- `market_context_high->commodity_1h` score `1.0261` n `144` status `ready` deltaP `15.2113` edge `0.0218` maxDD `-0.3491`
- `news_risk_high->equity_1h` score `0.7988` n `81` status `ready` deltaP `9.8581` edge `0.0414` maxDD `-0.9112`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
