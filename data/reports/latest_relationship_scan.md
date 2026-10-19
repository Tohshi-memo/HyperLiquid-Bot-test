# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-19T07:37:31.552363+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8964`

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

- `risk_on_high->equity_24h` score `2.3331` n `43` status `ready` deltaP `-17.8929` edge `0.8246` maxDD `-28.5375`
- `risk_on_and_context->equity_24h` score `2.3331` n `43` status `ready` deltaP `-17.8929` edge `0.8246` maxDD `-28.5375`
- `market_context_high->commodity_24h` score `1.52` n `76` status `ready` deltaP `15.302` edge `0.1098` maxDD `-1.8119`
- `market_context_high->equity_24h` score `1.4888` n `76` status `ready` deltaP `1.4462` edge `1.0333` maxDD `-55.843`
- `market_context_high->crypto_major_24h` score `1.1619` n `76` status `ready` deltaP `3.3077` edge `0.7366` maxDD `-35.1086`
- `risk_on_high->equity_1h` score `0.75` n `43` status `ready` deltaP `14.9732` edge `0.0205` maxDD `-1.9591`
- `risk_on_and_context->equity_1h` score `0.75` n `43` status `ready` deltaP `14.9732` edge `0.0205` maxDD `-1.9591`
- `risk_on_high->index_1h` score `0.5443` n `43` status `ready` deltaP `11.2194` edge `0.0009` maxDD `-0.4273`
- `risk_on_and_context->index_1h` score `0.5443` n `43` status `ready` deltaP `11.2194` edge `0.0009` maxDD `-0.4273`
- `market_context_high->crypto_major_4h` score `0.4537` n `77` status `ready` deltaP `4.6068` edge `0.3679` maxDD `-15.2359`
- `market_context_high->crypto_major_1h` score `0.2741` n `77` status `ready` deltaP `4.1975` edge `0.0953` maxDD `-3.7178`
- `risk_on_high->equity_4h` score `0.0353` n `43` status `ready` deltaP `5.9917` edge `0.0983` maxDD `-4.824`
- `risk_on_and_context->equity_4h` score `0.0353` n `43` status `ready` deltaP `5.9917` edge `0.0983` maxDD `-4.824`
- `risk_on_high->fx_4h` score `0.0093` n `43` status `ready` deltaP `2.9977` edge `0.0072` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `0.0093` n `43` status `ready` deltaP `2.9977` edge `0.0072` maxDD `-0.1126`
- `risk_on_high->fx_1h` score `-0.2372` n `43` status `ready` deltaP `0.7123` edge `-0.0005` maxDD `-0.1065`
- `risk_on_and_context->fx_1h` score `-0.2372` n `43` status `ready` deltaP `0.7123` edge `-0.0005` maxDD `-0.1065`
- `risk_on_high->commodity_24h` score `-0.3308` n `43` status `ready` deltaP `10.6815` edge `-0.019` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `-0.3308` n `43` status `ready` deltaP `10.6815` edge `-0.019` maxDD `-1.7154`
- `market_context_high->metal_1h` score `-0.3493` n `77` status `ready` deltaP `-0.2528` edge `0.0076` maxDD `-0.4687`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
