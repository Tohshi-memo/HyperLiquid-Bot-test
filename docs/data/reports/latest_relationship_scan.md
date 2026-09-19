# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T05:52:29.986726+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8406`

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

- `news_risk_high->crypto_major_24h` score `59.328` n `60` status `ready` deltaP `35.1736` edge `4.7987` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `53.1026` n `60` status `ready` deltaP `38.1945` edge `4.3085` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `35.9693` n `149` status `ready` deltaP `-1.8354` edge `3.033` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `13.7976` n `60` status `ready` deltaP `48.0903` edge `0.8292` maxDD `0.0`
- `risk_on_high->unknown_4h` score `9.8479` n `52` status `ready` deltaP `-9.076` edge `0.9037` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `9.8479` n `52` status `ready` deltaP `-9.076` edge `0.9037` maxDD `-0.4694`
- `news_risk_high->crypto_alt_4h` score `8.2974` n `76` status `ready` deltaP `26.9336` edge `0.6245` maxDD `-7.675`
- `risk_on_high->commodity_24h` score `8.2664` n `52` status `ready` deltaP `44.9653` edge `0.3891` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.2664` n `52` status `ready` deltaP `44.9653` edge `0.3891` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.9673` n `149` status `ready` deltaP `38.2539` edge `0.3781` maxDD `-0.8682`
- `news_risk_high->crypto_major_4h` score `5.6354` n `76` status `ready` deltaP `23.4996` edge `0.4304` maxDD `-8.0625`
- `news_risk_high->metal_24h` score `4.4593` n `60` status `ready` deltaP `37.0486` edge `0.1404` maxDD `-0.2629`
- `news_risk_high->crypto_alt_1h` score `3.2842` n `81` status `ready` deltaP `17.1509` edge `0.2059` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.5934` n `81` status `ready` deltaP `19.7697` edge `0.1366` maxDD `-2.8494`
- `risk_on_high->commodity_4h` score `2.52` n `52` status `ready` deltaP `30.1008` edge `0.0443` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.52` n `52` status `ready` deltaP `30.1008` edge `0.0443` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.4197` n `149` status `ready` deltaP `26.6031` edge `0.0661` maxDD `-0.345`
- `news_risk_high->fx_4h` score `1.4829` n `76` status `ready` deltaP `16.4634` edge `0.0357` maxDD `-0.084`
- `news_risk_high->fx_24h` score `1.2144` n `60` status `ready` deltaP `6.8402` edge `0.0598` maxDD `-0.0029`
- `market_context_high->commodity_1h` score `1.0283` n `149` status `ready` deltaP `15.3127` edge `0.0213` maxDD `-0.3491`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
