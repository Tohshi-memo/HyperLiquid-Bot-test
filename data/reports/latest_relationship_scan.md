# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-16T01:52:30.612215+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11497`

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

- `news_risk_high->unknown_4h` score `366.061` n `83` status `ready` deltaP `-21.9678` edge `30.741` maxDD `-4.1571`
- `news_risk_high->unknown_24h` score `38.8212` n `78` status `ready` deltaP `21.1806` edge `3.0939` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `24.3567` n `78` status `ready` deltaP `47.7698` edge `1.7503` maxDD `-1.4564`
- `news_risk_high->crypto_major_24h` score `20.6437` n `78` status `ready` deltaP `39.7303` edge `1.6025` maxDD `-9.098`
- `news_risk_high->equity_24h` score `15.9833` n `78` status `ready` deltaP `49.8531` edge `1.177` maxDD `-6.5262`
- `news_risk_high->index_24h` score `8.3805` n `78` status `ready` deltaP `59.6821` edge `0.3181` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.8132` n `78` status `ready` deltaP `38.4882` edge `0.3566` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `5.8065` n `52` status `ready` deltaP `38.0208` edge `0.2304` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.8065` n `52` status `ready` deltaP `38.0208` edge `0.2304` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.5144` n `147` status `ready` deltaP `31.2181` edge `0.2206` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `2.5342` n `52` status `ready` deltaP `32.9727` edge `-0.0044` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.5342` n `52` status `ready` deltaP `32.9727` edge `-0.0044` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.363` n `147` status `ready` deltaP `30.1339` edge `0.0176` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.7492` n `52` status `ready` deltaP `24.1557` edge `0.0197` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.7492` n `52` status `ready` deltaP `24.1557` edge `0.0197` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.6489` n `149` status `ready` deltaP `20.658` edge `0.0415` maxDD `-0.345`
- `news_risk_high->index_4h` score `0.8269` n `83` status `ready` deltaP `19.3579` edge `0.0398` maxDD `-0.6935`
- `market_context_high->commodity_1h` score `0.7646` n `149` status `ready` deltaP `12.9175` edge `0.0153` maxDD `-0.3491`
- `risk_on_high->crypto_alt_4h` score `0.2919` n `52` status `ready` deltaP `9.3926` edge `0.1363` maxDD `-6.2526`
- `risk_on_and_context->crypto_alt_4h` score `0.2919` n `52` status `ready` deltaP `9.3926` edge `0.1363` maxDD `-6.2526`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
