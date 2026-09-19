# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T11:07:30.046509+00:00`
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

- `news_risk_high->crypto_major_24h` score `54.2754` n `72` status `ready` deltaP `33.6805` edge `4.3876` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `47.5814` n `72` status `ready` deltaP `38.1945` edge `3.8484` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `36.9505` n `144` status `ready` deltaP `-2.185` edge `3.1171` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `11.0395` n `72` status `ready` deltaP `43.2292` edge `0.636` maxDD `-0.0053`
- `risk_on_high->commodity_24h` score `8.2256` n `52` status `ready` deltaP `44.9653` edge `0.3857` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.2256` n `52` status `ready` deltaP `44.9653` edge `0.3857` maxDD `0.0`
- `risk_on_high->unknown_4h` score `8.1979` n `52` status `ready` deltaP `-9.076` edge `0.7662` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `8.1979` n `52` status `ready` deltaP `-9.076` edge `0.7662` maxDD `-0.4694`
- `market_context_high->commodity_24h` score `7.0074` n `144` status `ready` deltaP `38.0209` edge `0.383` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `6.5921` n `81` status `ready` deltaP `23.0974` edge `0.5163` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.6935` n `81` status `ready` deltaP `20.4456` edge `0.3806` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `3.4723` n `89` status `ready` deltaP `19.4426` edge `0.2063` maxDD `-2.058`
- `risk_on_high->commodity_4h` score `2.7001` n `52` status `ready` deltaP `32.0825` edge `0.0461` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.7001` n `52` status `ready` deltaP `32.0825` edge `0.0461` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.548` n `144` status `ready` deltaP `27.8624` edge `0.0684` maxDD `-0.345`
- `news_risk_high->crypto_major_1h` score `2.3679` n `89` status `ready` deltaP `19.1415` edge `0.122` maxDD `-2.8494`
- `news_risk_high->metal_24h` score `1.9077` n `72` status `ready` deltaP `24.4792` edge `0.0802` maxDD `-2.4203`
- `news_risk_high->fx_4h` score `1.1949` n `81` status `ready` deltaP `13.3883` edge `0.0322` maxDD `-0.084`
- `market_context_high->commodity_1h` score `1.0776` n `144` status `ready` deltaP `15.8101` edge `0.0221` maxDD `-0.3491`
- `news_risk_high->metal_1h` score `0.645` n `89` status `ready` deltaP `14.494` edge `0.0173` maxDD `-0.8144`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
