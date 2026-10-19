# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-19T06:07:36.062960+00:00`
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

- `risk_on_high->equity_24h` score `3.2218` n `43` status `ready` deltaP `-16.8494` edge `0.8917` maxDD `-28.5375`
- `risk_on_and_context->equity_24h` score `3.2218` n `43` status `ready` deltaP `-16.8494` edge `0.8917` maxDD `-28.5375`
- `market_context_high->equity_24h` score `2.3775` n `76` status `ready` deltaP `2.4897` edge `1.1004` maxDD `-55.843`
- `market_context_high->crypto_major_24h` score `1.4961` n `76` status `ready` deltaP `4.3494` edge `0.7725` maxDD `-35.1086`
- `market_context_high->commodity_24h` score `1.3285` n `76` status `ready` deltaP `14.2585` edge `0.1008` maxDD `-1.8119`
- `risk_on_high->equity_1h` score `0.7632` n `43` status `ready` deltaP `14.9732` edge `0.0216` maxDD `-1.9591`
- `risk_on_and_context->equity_1h` score `0.7632` n `43` status `ready` deltaP `14.9732` edge `0.0216` maxDD `-1.9591`
- `market_context_high->crypto_major_4h` score `0.566` n `77` status `ready` deltaP `5.5214` edge `0.3762` maxDD `-15.2359`
- `risk_on_high->index_1h` score `0.5322` n `43` status `ready` deltaP `11.0693` edge `0.0009` maxDD `-0.4273`
- `risk_on_and_context->index_1h` score `0.5322` n `43` status `ready` deltaP `11.0693` edge `0.0009` maxDD `-0.4273`
- `market_context_high->crypto_major_1h` score `0.2975` n `77` status `ready` deltaP `4.4969` edge `0.0963` maxDD `-3.7178`
- `risk_on_high->equity_4h` score `0.2059` n `43` status `ready` deltaP `6.9092` edge `0.1064` maxDD `-4.824`
- `risk_on_and_context->equity_4h` score `0.2059` n `43` status `ready` deltaP `6.9092` edge `0.1064` maxDD `-4.824`
- `risk_on_high->fx_4h` score `0.0362` n `43` status `ready` deltaP `3.3035` edge `0.0074` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `0.0362` n `43` status `ready` deltaP `3.3035` edge `0.0074` maxDD `-0.1126`
- `risk_on_high->fx_1h` score `-0.2279` n `43` status `ready` deltaP `0.8625` edge `-0.0003` maxDD `-0.1065`
- `risk_on_and_context->fx_1h` score `-0.2279` n `43` status `ready` deltaP `0.8625` edge `-0.0003` maxDD `-0.1065`
- `risk_on_high->index_4h` score `-0.3452` n `43` status `ready` deltaP `7.3999` edge `0.0086` maxDD `-0.9359`
- `risk_on_and_context->index_4h` score `-0.3452` n `43` status `ready` deltaP `7.3999` edge `0.0086` maxDD `-0.9359`
- `market_context_high->metal_1h` score `-0.3637` n `77` status `ready` deltaP `-0.4025` edge `0.0074` maxDD `-0.4687`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
