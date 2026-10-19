# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-19T05:52:27.111113+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8928`

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

- `risk_on_high->equity_24h` score `3.3713` n `43` status `ready` deltaP `-16.6755` edge `0.903` maxDD `-28.5375`
- `risk_on_and_context->equity_24h` score `3.3713` n `43` status `ready` deltaP `-16.6755` edge `0.903` maxDD `-28.5375`
- `market_context_high->equity_24h` score `2.527` n `76` status `ready` deltaP `2.6636` edge `1.1117` maxDD `-55.843`
- `market_context_high->crypto_major_24h` score `1.5527` n `76` status `ready` deltaP `4.523` edge `0.7786` maxDD `-35.1086`
- `market_context_high->commodity_24h` score `1.2954` n `76` status `ready` deltaP `14.0846` edge `0.0992` maxDD `-1.8119`
- `risk_on_high->equity_1h` score `0.7836` n `43` status `ready` deltaP `15.1233` edge `0.0223` maxDD `-1.9591`
- `risk_on_and_context->equity_1h` score `0.7836` n `43` status `ready` deltaP `15.1233` edge `0.0223` maxDD `-1.9591`
- `market_context_high->crypto_major_4h` score `0.584` n `77` status `ready` deltaP `5.6739` edge `0.3775` maxDD `-15.2359`
- `risk_on_high->index_1h` score `0.5455` n `43` status `ready` deltaP `11.2194` edge `0.001` maxDD `-0.4273`
- `risk_on_and_context->index_1h` score `0.5455` n `43` status `ready` deltaP `11.2194` edge `0.001` maxDD `-0.4273`
- `market_context_high->crypto_major_1h` score `0.3084` n `77` status `ready` deltaP `4.6466` edge `0.0967` maxDD `-3.7178`
- `risk_on_high->equity_4h` score `0.2434` n `43` status `ready` deltaP `7.0621` edge `0.1085` maxDD `-4.824`
- `risk_on_and_context->equity_4h` score `0.2434` n `43` status `ready` deltaP `7.0621` edge `0.1085` maxDD `-4.824`
- `risk_on_high->fx_4h` score `0.0374` n `43` status `ready` deltaP `3.3035` edge `0.0075` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `0.0374` n `43` status `ready` deltaP `3.3035` edge `0.0075` maxDD `-0.1126`
- `risk_on_high->fx_1h` score `-0.2279` n `43` status `ready` deltaP `0.8625` edge `-0.0003` maxDD `-0.1065`
- `risk_on_and_context->fx_1h` score `-0.2279` n `43` status `ready` deltaP `0.8625` edge `-0.0003` maxDD `-0.1065`
- `risk_on_high->index_4h` score `-0.3294` n `43` status `ready` deltaP `7.5528` edge `0.0089` maxDD `-0.9359`
- `risk_on_and_context->index_4h` score `-0.3294` n `43` status `ready` deltaP `7.5528` edge `0.0089` maxDD `-0.9359`
- `market_context_high->metal_1h` score `-0.3517` n `77` status `ready` deltaP `-0.2528` edge `0.0074` maxDD `-0.4687`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
