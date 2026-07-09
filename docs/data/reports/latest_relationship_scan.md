# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T18:22:25.950749+00:00`
- Price records: `672`
- Market context records: `6205`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11110`

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

- `news_risk_high->crypto_alt_24h` score `12.893` n `32` status `ready` deltaP `42.2194` edge `0.8077` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.6859` n `32` status `ready` deltaP `58.1633` edge `0.1694` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.0454` n `32` status `ready` deltaP `42.3018` edge `0.0597` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `2.2753` n `32` status `ready` deltaP `15.625` edge `0.2655` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.2721` n `32` status `ready` deltaP `27.3952` edge `0.0206` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.8693` n `192` status `ready` deltaP `1.5126` edge `0.2465` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.3852` n `32` status `ready` deltaP `14.2777` edge `0.1291` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.7226` n `32` status `ready` deltaP `9.5247` edge `0.0753` maxDD `-1.6923`
- `news_risk_high->commodity_24h` score `0.7034` n `32` status `ready` deltaP `18.7287` edge `-0.0457` maxDD `-0.3101`
- `market_context_high->unknown_4h` score `0.2363` n `192` status `ready` deltaP `-2.7566` edge `0.2913` maxDD `-11.925`
- `market_context_high->metal_24h` score `-0.04` n `192` status `ready` deltaP `19.8023` edge `0.1197` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.2604` n `32` status `ready` deltaP `8.801` edge `-0.0049` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.34` n `192` status `ready` deltaP `0.3119` edge `-0.0011` maxDD `-0.5659`
- `market_context_high->commodity_1h` score `-0.6278` n `192` status `ready` deltaP `-1.3473` edge `0.0013` maxDD `-0.5708`
- `market_context_high->metal_4h` score `-0.778` n `192` status `ready` deltaP `1.9944` edge `0.0057` maxDD `-3.4996`
- `news_risk_high->metal_1h` score `-0.8073` n `32` status `ready` deltaP `-3.7425` edge `-0.0288` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.9012` n `192` status `ready` deltaP `1.4658` edge `-0.005` maxDD `-2.0564`
- `market_context_high->crypto_major_1h` score `-0.9145` n `192` status `ready` deltaP `4.3819` edge `0.0303` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-0.9411` n `192` status `ready` deltaP `3.7955` edge `0.0293` maxDD `-9.3536`
- `market_context_high->equity_1h` score `-1.1016` n `192` status `ready` deltaP `-3.0127` edge `-0.0096` maxDD `-4.2573`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
