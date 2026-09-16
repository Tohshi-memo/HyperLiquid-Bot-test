# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-16T00:07:24.718279+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11489`

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

- `news_risk_high->unknown_4h` score `366.1` n `83` status `ready` deltaP `-21.5105` edge `30.7412` maxDD `-4.1571`
- `news_risk_high->unknown_24h` score `38.7516` n `78` status `ready` deltaP `21.1806` edge `3.0881` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `24.2247` n `78` status `ready` deltaP `47.7698` edge `1.7393` maxDD `-1.4564`
- `news_risk_high->crypto_major_24h` score `20.3689` n `78` status `ready` deltaP `39.7303` edge `1.5796` maxDD `-9.098`
- `news_risk_high->equity_24h` score `15.8585` n `78` status `ready` deltaP `49.8531` edge `1.1666` maxDD `-6.5262`
- `news_risk_high->index_24h` score `8.3793` n `78` status `ready` deltaP `59.6821` edge `0.318` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.7676` n `78` status `ready` deltaP `38.4882` edge `0.3528` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `5.86` n `52` status `ready` deltaP `38.1944` edge `0.2337` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.86` n `52` status `ready` deltaP `38.1944` edge `0.2337` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.5851` n `140` status `ready` deltaP `31.0515` edge `0.2276` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `2.6179` n `52` status `ready` deltaP `33.4936` edge `-0.0009` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.6179` n `52` status `ready` deltaP `33.4936` edge `-0.0009` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.2836` n `140` status `ready` deltaP `30.4167` edge `0.0091` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.7394` n `52` status `ready` deltaP `24.0033` edge `0.0199` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.7394` n `52` status `ready` deltaP `24.0033` edge `0.0199` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.6391` n `149` status `ready` deltaP `20.5056` edge `0.0417` maxDD `-0.345`
- `news_risk_high->index_4h` score `0.8151` n `83` status `ready` deltaP `19.2055` edge `0.0393` maxDD `-0.6935`
- `market_context_high->commodity_1h` score `0.7742` n `149` status `ready` deltaP `13.0672` edge `0.0151` maxDD `-0.3491`
- `risk_on_high->crypto_alt_4h` score `0.2714` n `52` status `ready` deltaP `9.0877` edge `0.1357` maxDD `-6.2526`
- `risk_on_and_context->crypto_alt_4h` score `0.2714` n `52` status `ready` deltaP `9.0877` edge `0.1357` maxDD `-6.2526`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
