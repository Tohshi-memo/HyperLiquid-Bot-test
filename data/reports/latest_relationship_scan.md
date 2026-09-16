# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-16T03:07:36.393023+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11549`

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

- `news_risk_high->unknown_4h` score `365.933` n `83` status `ready` deltaP `-21.6629` edge `30.7283` maxDD `-4.1571`
- `news_risk_high->unknown_24h` score `38.8356` n `78` status `ready` deltaP `21.1806` edge `3.0951` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `24.4131` n `78` status `ready` deltaP `47.7698` edge `1.755` maxDD `-1.4564`
- `news_risk_high->crypto_major_24h` score `20.7901` n `78` status `ready` deltaP `39.7303` edge `1.6147` maxDD `-9.098`
- `news_risk_high->equity_24h` score `15.9821` n `78` status `ready` deltaP `49.8531` edge `1.1769` maxDD `-6.5262`
- `news_risk_high->index_24h` score `8.3649` n `78` status `ready` deltaP `59.6821` edge `0.3168` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.836` n `78` status `ready` deltaP `38.4882` edge `0.3585` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `5.7674` n `52` status `ready` deltaP `37.8472` edge `0.2283` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.7674` n `52` status `ready` deltaP `37.8472` edge `0.2283` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.4682` n `149` status `ready` deltaP `31.1358` edge `0.2173` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `2.4685` n `52` status `ready` deltaP `32.4519` edge `-0.0064` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.4685` n `52` status `ready` deltaP `32.4519` edge `-0.0064` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.3337` n `149` status `ready` deltaP `29.677` edge `0.0182` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.7456` n `52` status `ready` deltaP `24.1557` edge `0.0194` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.7456` n `52` status `ready` deltaP `24.1557` edge `0.0194` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.6453` n `149` status `ready` deltaP `20.658` edge `0.0412` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.7934` n `149` status `ready` deltaP `13.2169` edge `0.0157` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.7913` n `83` status `ready` deltaP `18.7482` edge `0.0393` maxDD `-0.6935`
- `risk_on_high->crypto_alt_4h` score `0.3524` n `52` status `ready` deltaP `9.8499` edge `0.141` maxDD `-6.2526`
- `risk_on_and_context->crypto_alt_4h` score `0.3524` n `52` status `ready` deltaP `9.8499` edge `0.141` maxDD `-6.2526`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
