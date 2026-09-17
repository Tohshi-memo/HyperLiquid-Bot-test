# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T01:52:29.793449+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10533`

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

- `news_risk_high->unknown_4h` score `377.4864` n `83` status `ready` deltaP `-20.9007` edge `31.686` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `16.9698` n `83` status `ready` deltaP `39.2194` edge `1.2906` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `15.5193` n `83` status `ready` deltaP `31.2855` edge `1.2842` maxDD `-13.2931`
- `news_risk_high->equity_24h` score `11.7073` n `83` status `ready` deltaP `40.5184` edge `0.8829` maxDD `-6.5262`
- `risk_on_high->commodity_24h` score `7.4809` n `52` status `ready` deltaP `42.3611` edge `0.341` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.4809` n `52` status `ready` deltaP `42.3611` edge `0.341` maxDD `0.0`
- `news_risk_high->index_24h` score `6.6026` n `83` status `ready` deltaP `45.9484` edge `0.2615` maxDD `-0.075`
- `market_context_high->commodity_24h` score `6.1817` n `149` status `ready` deltaP `35.6497` edge `0.33` maxDD `-0.8682`
- `news_risk_high->metal_24h` score `4.7946` n `83` status `ready` deltaP `31.9905` edge `0.2317` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `2.5349` n `52` status `ready` deltaP `33.1463` edge `-0.0055` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.5349` n `52` status `ready` deltaP `33.1463` edge `-0.0055` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.4` n `149` status `ready` deltaP `30.3714` edge `0.0191` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.3012` n `52` status `ready` deltaP `28.8813` edge `0.0342` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.3012` n `52` status `ready` deltaP `28.8813` edge `0.0342` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.2009` n `149` status `ready` deltaP `25.3836` edge `0.056` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.9743` n `149` status `ready` deltaP `15.0133` edge `0.0188` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.3627` n `83` status `ready` deltaP `11.736` edge `0.0311` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.351` n `52` status `ready` deltaP `8.0954` edge `0.0105` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.351` n `52` status `ready` deltaP `8.0954` edge `0.0105` maxDD `-0.1507`
- `risk_on_high->metal_1h` score `0.1326` n `52` status `ready` deltaP `6.1147` edge `0.0068` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
