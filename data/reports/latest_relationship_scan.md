# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-16T00:52:30.055516+00:00`
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

- `news_risk_high->unknown_4h` score `366.0672` n `83` status `ready` deltaP `-21.8153` edge `30.7405` maxDD `-4.1571`
- `news_risk_high->unknown_24h` score `38.7792` n `78` status `ready` deltaP `21.1806` edge `3.0904` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `24.2835` n `78` status `ready` deltaP `47.7698` edge `1.7442` maxDD `-1.4564`
- `news_risk_high->crypto_major_24h` score `20.4925` n `78` status `ready` deltaP `39.7303` edge `1.5899` maxDD `-9.098`
- `news_risk_high->equity_24h` score `15.9137` n `78` status `ready` deltaP `49.8531` edge `1.1712` maxDD `-6.5262`
- `news_risk_high->index_24h` score `8.3793` n `78` status `ready` deltaP `59.6821` edge `0.318` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.7856` n `78` status `ready` deltaP `38.4882` edge `0.3543` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `5.8492` n `52` status `ready` deltaP `38.1944` edge `0.2328` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.8492` n `52` status `ready` deltaP `38.1944` edge `0.2328` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.5563` n `143` status `ready` deltaP `31.2014` edge `0.2242` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `2.5872` n `52` status `ready` deltaP `33.32` edge `-0.0023` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.5872` n `52` status `ready` deltaP `33.32` edge `-0.0023` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.3213` n `143` status `ready` deltaP `30.348` edge `0.0127` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.7528` n `52` status `ready` deltaP `24.1557` edge `0.02` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.7528` n `52` status `ready` deltaP `24.1557` edge `0.02` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.6525` n `149` status `ready` deltaP `20.658` edge `0.0418` maxDD `-0.345`
- `news_risk_high->index_4h` score `0.8174` n `83` status `ready` deltaP `19.2055` edge `0.0396` maxDD `-0.6935`
- `market_context_high->commodity_1h` score `0.8042` n `149` status `ready` deltaP `13.3666` edge `0.0156` maxDD `-0.3491`
- `risk_on_high->crypto_alt_4h` score `0.2574` n `52` status `ready` deltaP `9.0877` edge `0.1339` maxDD `-6.2526`
- `risk_on_and_context->crypto_alt_4h` score `0.2574` n `52` status `ready` deltaP `9.0877` edge `0.1339` maxDD `-6.2526`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
