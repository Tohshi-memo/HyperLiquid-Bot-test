# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T22:52:35.173538+00:00`
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

- `news_risk_high->crypto_major_24h` score `53.1336` n `39` status `ready` deltaP `32.2783` edge `4.3018` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `49.2745` n `39` status `ready` deltaP `33.7073` edge `4.0194` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `37.8736` n `149` status `ready` deltaP `-0.9208` edge `3.1856` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `11.7523` n `52` status `ready` deltaP `-8.1614` edge `1.0563` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `11.7523` n `52` status `ready` deltaP `-8.1614` edge `1.0563` maxDD `-0.4694`
- `news_risk_high->equity_24h` score `11.2698` n `39` status `ready` deltaP `40.1309` edge `0.7089` maxDD `-1.3163`
- `news_risk_high->crypto_alt_4h` score `9.0977` n `77` status `ready` deltaP `29.0921` edge `0.6768` maxDD `-7.675`
- `risk_on_high->commodity_24h` score `8.5829` n `52` status `ready` deltaP `47.9167` edge `0.3958` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.5829` n `52` status `ready` deltaP `47.9167` edge `0.3958` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.2838` n `149` status `ready` deltaP `41.2053` edge `0.3848` maxDD `-0.8682`
- `news_risk_high->crypto_major_4h` score `5.7277` n `77` status `ready` deltaP `24.4279` edge `0.4319` maxDD `-8.0625`
- `news_risk_high->metal_24h` score `3.7698` n `39` status `ready` deltaP `27.2303` edge `0.1484` maxDD `-0.2629`
- `news_risk_high->crypto_alt_1h` score `3.076` n `77` status `ready` deltaP `16.7393` edge `0.1913` maxDD `-2.058`
- `risk_on_high->commodity_4h` score `2.8417` n `52` status `ready` deltaP `32.9972` edge `0.0518` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.8417` n `52` status `ready` deltaP `32.9972` edge `0.0518` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.7414` n `149` status `ready` deltaP `29.4995` edge `0.0736` maxDD `-0.345`
- `news_risk_high->crypto_major_1h` score `2.6507` n `77` status `ready` deltaP `20.336` edge `0.1376` maxDD `-2.8494`
- `news_risk_high->equity_4h` score `1.6713` n `77` status `ready` deltaP `14.4105` edge `0.1332` maxDD `-4.1995`
- `news_risk_high->fx_4h` score `1.4112` n `77` status `ready` deltaP `15.6419` edge `0.0352` maxDD `-0.084`
- `news_risk_high->equity_1h` score `1.2185` n `77` status `ready` deltaP `14.2352` edge `0.0472` maxDD `-0.9112`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
