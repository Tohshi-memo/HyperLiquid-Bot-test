# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T10:22:31.106319+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8522`

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

- `news_risk_high->crypto_major_24h` score `54.6314` n `72` status `ready` deltaP `34.2013` edge `4.4138` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `47.8727` n `72` status `ready` deltaP `38.7153` edge `3.8692` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `36.9481` n `144` status `ready` deltaP `-2.185` edge `3.1169` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `11.1928` n `72` status `ready` deltaP `43.75` edge `0.6453` maxDD `-0.0053`
- `risk_on_high->commodity_24h` score `8.2316` n `52` status `ready` deltaP `44.9653` edge `0.3862` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.2316` n `52` status `ready` deltaP `44.9653` edge `0.3862` maxDD `0.0`
- `risk_on_high->unknown_4h` score `8.1955` n `52` status `ready` deltaP `-9.076` edge `0.766` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `8.1955` n `52` status `ready` deltaP `-9.076` edge `0.766` maxDD `-0.4694`
- `market_context_high->commodity_24h` score `7.0134` n `144` status `ready` deltaP `38.0209` edge `0.3835` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `6.6581` n `81` status `ready` deltaP `23.0974` edge `0.5218` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.6923` n `81` status `ready` deltaP `20.4456` edge `0.3805` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `3.3445` n `86` status `ready` deltaP `18.5803` edge `0.2014` maxDD `-2.058`
- `risk_on_high->commodity_4h` score `2.7001` n `52` status `ready` deltaP `32.0825` edge `0.0461` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.7001` n `52` status `ready` deltaP `32.0825` edge `0.0461` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.548` n `144` status `ready` deltaP `27.8624` edge `0.0684` maxDD `-0.345`
- `news_risk_high->crypto_major_1h` score `2.283` n `86` status `ready` deltaP `18.3505` edge `0.1202` maxDD `-2.8494`
- `news_risk_high->metal_24h` score `1.8981` n `72` status `ready` deltaP `24.4792` edge `0.0794` maxDD `-2.4203`
- `news_risk_high->fx_4h` score `1.2205` n `81` status `ready` deltaP `13.6932` edge `0.0323` maxDD `-0.084`
- `market_context_high->commodity_1h` score `1.0908` n `144` status `ready` deltaP `15.9598` edge `0.0222` maxDD `-0.3491`
- `news_risk_high->equity_1h` score `0.684` n `86` status `ready` deltaP `8.888` edge `0.0383` maxDD `-0.9112`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
