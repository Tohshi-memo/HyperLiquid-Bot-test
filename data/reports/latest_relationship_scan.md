# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-19T06:37:29.873043+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8936`

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

- `risk_on_high->equity_24h` score `2.9204` n `43` status `ready` deltaP `-17.1972` edge `0.8689` maxDD `-28.5375`
- `risk_on_and_context->equity_24h` score `2.9204` n `43` status `ready` deltaP `-17.1972` edge `0.8689` maxDD `-28.5375`
- `market_context_high->equity_24h` score `2.0761` n `76` status `ready` deltaP `2.1419` edge `1.0776` maxDD `-55.843`
- `market_context_high->commodity_24h` score `1.3935` n `76` status `ready` deltaP `14.6064` edge `0.1039` maxDD `-1.8119`
- `market_context_high->crypto_major_24h` score `1.3914` n `76` status `ready` deltaP `4.0022` edge `0.7614` maxDD `-35.1086`
- `risk_on_high->equity_1h` score `0.7356` n `43` status `ready` deltaP `14.823` edge `0.0203` maxDD `-1.9591`
- `risk_on_and_context->equity_1h` score `0.7356` n `43` status `ready` deltaP `14.823` edge `0.0203` maxDD `-1.9591`
- `market_context_high->crypto_major_4h` score `0.533` n `77` status `ready` deltaP `5.2165` edge `0.374` maxDD `-15.2359`
- `risk_on_high->index_1h` score `0.5178` n `43` status `ready` deltaP `10.9191` edge `0.0007` maxDD `-0.4273`
- `risk_on_and_context->index_1h` score `0.5178` n `43` status `ready` deltaP `10.9191` edge `0.0007` maxDD `-0.4273`
- `market_context_high->crypto_major_1h` score `0.303` n `77` status `ready` deltaP `4.4969` edge `0.097` maxDD `-3.7178`
- `risk_on_high->equity_4h` score `0.1383` n `43` status `ready` deltaP `6.6033` edge `0.1028` maxDD `-4.824`
- `risk_on_and_context->equity_4h` score `0.1383` n `43` status `ready` deltaP `6.6033` edge `0.1028` maxDD `-4.824`
- `risk_on_high->fx_4h` score `0.0093` n `43` status `ready` deltaP `2.9977` edge `0.0072` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `0.0093` n `43` status `ready` deltaP `2.9977` edge `0.0072` maxDD `-0.1126`
- `risk_on_high->fx_1h` score `-0.2287` n `43` status `ready` deltaP `0.8625` edge `-0.0004` maxDD `-0.1065`
- `risk_on_and_context->fx_1h` score `-0.2287` n `43` status `ready` deltaP `0.8625` edge `-0.0004` maxDD `-0.1065`
- `market_context_high->metal_1h` score `-0.3505` n `77` status `ready` deltaP `-0.2528` edge `0.0075` maxDD `-0.4687`
- `risk_on_high->index_4h` score `-0.3769` n `43` status `ready` deltaP `7.0941` edge `0.008` maxDD `-0.9359`
- `risk_on_and_context->index_4h` score `-0.3769` n `43` status `ready` deltaP `7.0941` edge `0.008` maxDD `-0.9359`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
