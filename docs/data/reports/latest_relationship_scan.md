# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T22:41:05.701114+00:00`
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

- `news_risk_high->crypto_major_24h` score `50.9443` n `39` status `ready` deltaP `29.8878` edge `4.1353` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `47.6821` n `39` status `ready` deltaP `33.7073` edge `3.8867` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `37.7932` n `149` status `ready` deltaP `-0.9208` edge `3.1789` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `11.6719` n `52` status `ready` deltaP `-8.1614` edge `1.0496` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `11.6719` n `52` status `ready` deltaP `-8.1614` edge `1.0496` maxDD `-0.4694`
- `news_risk_high->equity_24h` score `10.5321` n `39` status `ready` deltaP `37.7404` edge `0.6707` maxDD `-1.5704`
- `news_risk_high->crypto_alt_4h` score `9.1072` n `78` status `ready` deltaP `29.2253` edge `0.6767` maxDD `-7.675`
- `risk_on_high->commodity_24h` score `8.5829` n `52` status `ready` deltaP `47.9167` edge `0.3958` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.5829` n `52` status `ready` deltaP `47.9167` edge `0.3958` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.2838` n `149` status `ready` deltaP `41.2053` edge `0.3848` maxDD `-0.8682`
- `news_risk_high->crypto_major_4h` score `5.5574` n `78` status `ready` deltaP `23.5147` edge `0.4238` maxDD `-8.0625`
- `news_risk_high->metal_24h` score `3.4597` n `39` status `ready` deltaP `24.8398` edge `0.1385` maxDD `-0.2629`
- `news_risk_high->crypto_alt_1h` score `2.9163` n `78` status `ready` deltaP `15.8069` edge `0.1842` maxDD `-2.058`
- `risk_on_high->commodity_4h` score `2.8429` n `52` status `ready` deltaP `32.9972` edge `0.0519` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.8429` n `52` status `ready` deltaP `32.9972` edge `0.0519` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.7426` n `149` status `ready` deltaP `29.4995` edge `0.0737` maxDD `-0.345`
- `news_risk_high->crypto_major_1h` score `2.4737` n `78` status `ready` deltaP `19.3536` edge `0.1294` maxDD `-2.8494`
- `news_risk_high->equity_4h` score `1.7033` n `78` status `ready` deltaP `14.8101` edge `0.1332` maxDD `-4.1995`
- `news_risk_high->fx_4h` score `1.3402` n `78` status `ready` deltaP `14.8452` edge `0.0346` maxDD `-0.084`
- `news_risk_high->equity_1h` score `1.1413` n `78` status `ready` deltaP `13.4193` edge `0.0462` maxDD `-0.9112`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
