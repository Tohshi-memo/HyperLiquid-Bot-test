# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T07:07:29.361653+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8452`

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

- `news_risk_high->crypto_major_24h` score `57.7286` n `65` status `ready` deltaP `35.6865` edge `4.662` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `51.0299` n `65` status `ready` deltaP `38.8355` edge `4.1315` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `36.0353` n `149` status `ready` deltaP `-1.8354` edge `3.0385` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `12.8762` n `65` status `ready` deltaP `47.2222` edge `0.7582` maxDD `0.0`
- `risk_on_high->unknown_4h` score `9.9139` n `52` status `ready` deltaP `-9.076` edge `0.9092` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `9.9139` n `52` status `ready` deltaP `-9.076` edge `0.9092` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.2556` n `52` status `ready` deltaP `44.9653` edge `0.3882` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.2556` n `52` status `ready` deltaP `44.9653` edge `0.3882` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.9565` n `149` status `ready` deltaP `38.2539` edge `0.3772` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `6.5744` n `81` status `ready` deltaP `22.3352` edge `0.5199` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.4735` n `81` status `ready` deltaP `19.2261` edge `0.3704` maxDD `-8.0625`
- `news_risk_high->metal_24h` score `3.4542` n `65` status `ready` deltaP `30.9936` edge `0.1153` maxDD `-0.726`
- `news_risk_high->crypto_alt_1h` score `3.3537` n `81` status `ready` deltaP `17.4503` edge `0.2097` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.6736` n `81` status `ready` deltaP `20.5182` edge `0.1383` maxDD `-2.8494`
- `risk_on_high->commodity_4h` score `2.5614` n `52` status `ready` deltaP `30.5582` edge `0.0447` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.5614` n `52` status `ready` deltaP `30.5582` edge `0.0447` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.4611` n `149` status `ready` deltaP `27.0605` edge `0.0665` maxDD `-0.345`
- `news_risk_high->fx_4h` score `1.2838` n `81` status `ready` deltaP `14.4554` edge `0.0325` maxDD `-0.084`
- `news_risk_high->fx_24h` score `1.0676` n `65` status `ready` deltaP `6.1004` edge `0.0525` maxDD `-0.0029`
- `market_context_high->commodity_1h` score `1.0378` n `149` status `ready` deltaP `15.4624` edge `0.0211` maxDD `-0.3491`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
