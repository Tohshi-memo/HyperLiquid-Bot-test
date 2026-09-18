# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T22:22:31.040666+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8098`

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

- `news_risk_high->crypto_major_24h` score `48.6903` n `39` status `ready` deltaP `27.4973` edge `3.9634` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `45.9529` n `39` status `ready` deltaP `33.7073` edge `3.7426` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `37.7176` n `149` status `ready` deltaP `-0.9208` edge `3.1726` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `11.5963` n `52` status `ready` deltaP `-8.1614` edge `1.0433` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `11.5963` n `52` status `ready` deltaP `-8.1614` edge `1.0433` maxDD `-0.4694`
- `news_risk_high->equity_24h` score `9.7858` n `39` status `ready` deltaP `35.3499` edge `0.6319` maxDD `-1.8331`
- `news_risk_high->crypto_alt_4h` score `9.03` n `79` status `ready` deltaP `29.3551` edge `0.6694` maxDD `-7.675`
- `risk_on_high->commodity_24h` score `8.5829` n `52` status `ready` deltaP `47.9167` edge `0.3958` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.5829` n `52` status `ready` deltaP `47.9167` edge `0.3958` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.2838` n `149` status `ready` deltaP `41.2053` edge `0.3848` maxDD `-0.8682`
- `news_risk_high->crypto_major_4h` score `5.3425` n `79` status `ready` deltaP `22.6286` edge `0.4118` maxDD `-8.0625`
- `news_risk_high->metal_24h` score `3.1105` n `39` status `ready` deltaP `22.4493` edge `0.1295` maxDD `-0.2629`
- `risk_on_high->commodity_4h` score `2.8441` n `52` status `ready` deltaP `32.9972` edge `0.052` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.8441` n `52` status `ready` deltaP `32.9972` edge `0.052` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.7438` n `149` status `ready` deltaP `29.4995` edge `0.0738` maxDD `-0.345`
- `news_risk_high->crypto_alt_1h` score `2.6983` n `79` status `ready` deltaP `14.8981` edge `0.1721` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.2759` n `79` status `ready` deltaP `18.3961` edge `0.1193` maxDD `-2.8494`
- `news_risk_high->equity_4h` score `1.7356` n `79` status `ready` deltaP `15.1996` edge `0.1333` maxDD `-4.1995`
- `news_risk_high->fx_4h` score `1.3603` n `79` status `ready` deltaP `15.186` edge `0.034` maxDD `-0.084`
- `market_context_high->commodity_1h` score `1.1217` n `149` status `ready` deltaP `16.2109` edge `0.0231` maxDD `-0.3491`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
