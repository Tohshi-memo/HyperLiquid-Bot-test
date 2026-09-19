# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T04:22:26.008319+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8294`

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

- `news_risk_high->crypto_major_24h` score `61.2395` n `54` status `ready` deltaP `35.1273` edge `4.9583` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `55.365` n `54` status `ready` deltaP `37.2685` edge `4.5032` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `36.3107` n `149` status `ready` deltaP `-1.3781` edge `3.0584` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `14.6562` n `54` status `ready` deltaP `49.1319` edge `0.8938` maxDD `0.0`
- `risk_on_high->unknown_4h` score `10.1893` n `52` status `ready` deltaP `-8.6187` edge `0.9291` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `10.1893` n `52` status `ready` deltaP `-8.6187` edge `0.9291` maxDD `-0.4694`
- `news_risk_high->crypto_alt_4h` score `8.8528` n `72` status `ready` deltaP `28.3706` edge `0.6612` maxDD `-7.675`
- `risk_on_high->commodity_24h` score `8.276` n `52` status `ready` deltaP `44.9653` edge `0.3899` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.276` n `52` status `ready` deltaP `44.9653` edge `0.3899` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.9769` n `149` status `ready` deltaP `38.2539` edge `0.3789` maxDD `-0.8682`
- `news_risk_high->crypto_major_4h` score `6.0018` n `72` status `ready` deltaP `24.6443` edge `0.4533` maxDD `-8.0625`
- `news_risk_high->metal_24h` score `4.7446` n `54` status `ready` deltaP `37.6157` edge `0.1604` maxDD `-0.2629`
- `news_risk_high->crypto_alt_1h` score `3.2314` n `81` status `ready` deltaP `17.0012` edge `0.2025` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.6017` n `81` status `ready` deltaP `19.9194` edge `0.1363` maxDD `-2.8494`
- `risk_on_high->commodity_4h` score `2.5212` n `52` status `ready` deltaP `30.1008` edge `0.0444` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.5212` n `52` status `ready` deltaP `30.1008` edge `0.0444` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.4209` n `149` status `ready` deltaP `26.6031` edge `0.0662` maxDD `-0.345`
- `news_risk_high->fx_4h` score `1.5519` n `72` status `ready` deltaP `16.9207` edge `0.0384` maxDD `-0.084`
- `news_risk_high->equity_4h` score `1.5475` n `72` status `ready` deltaP `12.3984` edge `0.1363` maxDD `-4.1995`
- `news_risk_high->fx_24h` score `1.4466` n `54` status `ready` deltaP `7.5231` edge `0.0746` maxDD `-0.0029`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
