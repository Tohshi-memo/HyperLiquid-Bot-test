# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T17:51:43.151390+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8296`

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

- `market_context_high->unknown_4h` score `39.5644` n `149` status `ready` deltaP `-0.9208` edge `3.3265` maxDD `-0.5326`
- `news_risk_high->crypto_alt_24h` score `22.6805` n `35` status `ready` deltaP `32.2421` edge `1.813` maxDD `-9.3661`
- `risk_on_high->unknown_4h` score `13.4431` n `52` status `ready` deltaP `-8.1614` edge `1.1972` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `13.4431` n `52` status `ready` deltaP `-8.1614` edge `1.1972` maxDD `-0.4694`
- `news_risk_high->crypto_major_24h` score `11.4923` n `35` status `ready` deltaP `2.1082` edge `1.5911` maxDD `-7.8757`
- `risk_on_high->commodity_24h` score `8.5949` n `52` status `ready` deltaP `47.9167` edge `0.3968` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.5949` n `52` status `ready` deltaP `47.9167` edge `0.3968` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.2958` n `149` status `ready` deltaP `41.2053` edge `0.3858` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `7.0604` n `90` status `ready` deltaP `23.9905` edge `0.5577` maxDD `-7.675`
- `risk_on_high->commodity_4h` score `2.7849` n `52` status `ready` deltaP `32.6923` edge `0.0491` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.7849` n `52` status `ready` deltaP `32.6923` edge `0.0491` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.6846` n `149` status `ready` deltaP `29.1946` edge `0.0709` maxDD `-0.345`
- `news_risk_high->equity_4h` score `1.5616` n `90` status `ready` deltaP `15.0339` edge `0.1199` maxDD `-4.1995`
- `news_risk_high->crypto_major_4h` score `1.5565` n `90` status `ready` deltaP `15.4709` edge `0.3148` maxDD `-13.1382`
- `market_context_high->commodity_1h` score `1.1277` n `149` status `ready` deltaP `16.3606` edge `0.0226` maxDD `-0.3491`
- `news_risk_high->equity_24h` score `0.6897` n `35` status `ready` deltaP `4.995` edge `0.1931` maxDD `-5.0382`
- `risk_on_high->commodity_1h` score `0.5044` n `52` status `ready` deltaP `9.4427` edge `0.0143` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.5044` n `52` status `ready` deltaP `9.4427` edge `0.0143` maxDD `-0.1507`
- `risk_on_high->fx_24h` score `0.4697` n `52` status `ready` deltaP `14.3963` edge `-0.0526` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `0.4697` n `52` status `ready` deltaP `14.3963` edge `-0.0526` maxDD `-0.0054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
