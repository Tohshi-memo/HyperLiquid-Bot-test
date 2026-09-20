# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T04:52:34.347915+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9268`

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

- `news_risk_high->crypto_major_24h` score `40.6166` n `81` status `ready` deltaP `16.2423` edge `3.4432` maxDD `-10.3413`
- `news_risk_high->crypto_alt_24h` score `37.4939` n `81` status `ready` deltaP `29.2052` edge `3.0677` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `19.21` n `86` status `ready` deltaP `-0.1169` edge `1.6166` maxDD `-0.5326`
- `market_context_high->commodity_24h` score `7.3424` n `83` status `ready` deltaP `37.2574` edge `0.416` maxDD `-0.8682`
- `news_risk_high->equity_24h` score `6.376` n `81` status `ready` deltaP `33.2755` edge `0.3231` maxDD `-0.4217`
- `news_risk_high->crypto_alt_4h` score `6.217` n `98` status `ready` deltaP `23.4476` edge `0.4827` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.8648` n `98` status `ready` deltaP `23.1427` edge `0.3769` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `3.8623` n `86` status `ready` deltaP `34.827` edge `0.103` maxDD `-0.0659`
- `news_risk_high->crypto_alt_1h` score `3.4032` n `98` status `ready` deltaP `18.9234` edge `0.204` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.6285` n `98` status `ready` deltaP `21.1689` edge `0.1302` maxDD `-2.8494`
- `market_context_high->fx_4h` score `2.0304` n `86` status `ready` deltaP `27.2617` edge `0.0048` maxDD `-0.0543`
- `market_context_high->commodity_1h` score `1.8613` n `86` status `ready` deltaP `21.1252` edge `0.0353` maxDD `-0.3491`
- `news_risk_high->metal_24h` score `1.4755` n `81` status `ready` deltaP `22.3765` edge `0.0582` maxDD `-2.4203`
- `news_risk_high->metal_4h` score `0.8978` n `98` status `ready` deltaP `20.0441` edge `0.0466` maxDD `-2.0994`
- `market_context_high->fx_24h` score `0.8785` n `83` status `ready` deltaP `13.7258` edge `-0.0141` maxDD `-0.0027`
- `news_risk_high->metal_1h` score `0.7446` n `98` status `ready` deltaP `15.9049` edge `0.0162` maxDD `-0.8144`
- `news_risk_high->equity_1h` score `0.3719` n `98` status `ready` deltaP `5.9178` edge `0.0321` maxDD `-0.9112`
- `market_context_high->fx_1h` score `0.3678` n `86` status `ready` deltaP `8.0003` edge `0.0031` maxDD `-0.063`
- `news_risk_high->commodity_24h` score `0.3036` n `81` status `ready` deltaP `17.2068` edge `0.0548` maxDD `-3.4467`
- `news_risk_high->fx_4h` score `-0.1305` n `98` status `ready` deltaP `4.6229` edge `0.0219` maxDD `-0.421`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
