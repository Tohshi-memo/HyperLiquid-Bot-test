# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T07:22:30.321351+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8464`

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

- `news_risk_high->crypto_major_24h` score `57.3857` n `66` status `ready` deltaP `35.7797` edge `4.6328` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `50.6216` n `66` status `ready` deltaP `38.952` edge `4.0967` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `36.0437` n `149` status `ready` deltaP `-1.8354` edge `3.0392` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `12.6895` n `66` status `ready` deltaP `47.0486` edge `0.7438` maxDD `0.0`
- `risk_on_high->unknown_4h` score `9.9223` n `52` status `ready` deltaP `-9.076` edge `0.9099` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `9.9223` n `52` status `ready` deltaP `-9.076` edge `0.9099` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.252` n `52` status `ready` deltaP `44.9653` edge `0.3879` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.252` n `52` status `ready` deltaP `44.9653` edge `0.3879` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.9529` n `149` status `ready` deltaP `38.2539` edge `0.3769` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `6.613` n `81` status `ready` deltaP `22.4876` edge `0.5221` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.5025` n `81` status `ready` deltaP `19.3786` edge `0.3718` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `3.3513` n `81` status `ready` deltaP `17.4503` edge `0.2095` maxDD `-2.058`
- `news_risk_high->metal_24h` score `3.224` n `66` status `ready` deltaP `29.9085` edge `0.11` maxDD `-0.9246`
- `news_risk_high->crypto_major_1h` score `2.6748` n `81` status `ready` deltaP `20.5182` edge `0.1384` maxDD `-2.8494`
- `risk_on_high->commodity_4h` score `2.576` n `52` status `ready` deltaP `30.7106` edge `0.0449` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.576` n `52` status `ready` deltaP `30.7106` edge `0.0449` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.4757` n `149` status `ready` deltaP `27.2129` edge `0.0667` maxDD `-0.345`
- `news_risk_high->fx_4h` score `1.2838` n `81` status `ready` deltaP `14.4554` edge `0.0325` maxDD `-0.084`
- `news_risk_high->fx_24h` score `1.04` n `66` status `ready` deltaP `5.9501` edge `0.0512` maxDD `-0.0029`
- `market_context_high->commodity_1h` score `1.0378` n `149` status `ready` deltaP `15.4624` edge `0.0211` maxDD `-0.3491`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
