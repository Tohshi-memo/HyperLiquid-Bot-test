# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-15T22:58:47.759713+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11333`

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

- `news_risk_high->unknown_4h` score `366.1204` n `83` status `ready` deltaP `-21.5105` edge `30.7429` maxDD `-4.1571`
- `news_risk_high->unknown_24h` score `38.7264` n `78` status `ready` deltaP `21.1806` edge `3.086` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `24.1839` n `78` status `ready` deltaP `47.7698` edge `1.7359` maxDD `-1.4564`
- `news_risk_high->crypto_major_24h` score `20.1733` n `78` status `ready` deltaP `39.7303` edge `1.5633` maxDD `-9.098`
- `news_risk_high->equity_24h` score `15.7865` n `78` status `ready` deltaP `49.8531` edge `1.1606` maxDD `-6.5262`
- `news_risk_high->index_24h` score `8.3853` n `78` status `ready` deltaP `59.6821` edge `0.3185` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.7316` n `78` status `ready` deltaP `38.4882` edge `0.3498` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `5.8924` n `52` status `ready` deltaP `38.1944` edge `0.2364` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.8924` n `52` status `ready` deltaP `38.1944` edge `0.2364` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.5954` n `137` status `ready` deltaP `30.8951` edge `0.2295` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `2.7149` n `52` status `ready` deltaP `34.3616` edge `0.0014` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.7149` n `52` status `ready` deltaP `34.3616` edge `0.0014` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.3179` n `137` status `ready` deltaP `31.1752` edge `0.0069` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.7382` n `52` status `ready` deltaP `24.0033` edge `0.0198` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.7382` n `52` status `ready` deltaP `24.0033` edge `0.0198` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.6379` n `149` status `ready` deltaP `20.5056` edge `0.0416` maxDD `-0.345`
- `news_risk_high->index_4h` score `0.8112` n `83` status `ready` deltaP `19.2055` edge `0.0388` maxDD `-0.6935`
- `market_context_high->commodity_1h` score `0.7622` n `149` status `ready` deltaP `12.9175` edge `0.0151` maxDD `-0.3491`
- `risk_on_high->crypto_alt_4h` score `0.2542` n `52` status `ready` deltaP `9.0877` edge `0.1335` maxDD `-6.2526`
- `risk_on_and_context->crypto_alt_4h` score `0.2542` n `52` status `ready` deltaP `9.0877` edge `0.1335` maxDD `-6.2526`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
