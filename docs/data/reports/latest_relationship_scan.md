# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-19T07:22:30.893226+00:00`
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

- `risk_on_high->equity_24h` score `2.4827` n `43` status `ready` deltaP `-17.719` edge `0.8359` maxDD `-28.5375`
- `risk_on_and_context->equity_24h` score `2.4827` n `43` status `ready` deltaP `-17.719` edge `0.8359` maxDD `-28.5375`
- `market_context_high->equity_24h` score `1.6384` n `76` status `ready` deltaP `1.6201` edge `1.0446` maxDD `-55.843`
- `market_context_high->commodity_24h` score `1.4881` n `76` status `ready` deltaP `15.1281` edge `0.1083` maxDD `-1.8119`
- `market_context_high->crypto_major_24h` score `1.224` n `76` status `ready` deltaP `3.4813` edge `0.7434` maxDD `-35.1086`
- `risk_on_high->equity_1h` score `0.7524` n `43` status `ready` deltaP `14.9732` edge `0.0207` maxDD `-1.9591`
- `risk_on_and_context->equity_1h` score `0.7524` n `43` status `ready` deltaP `14.9732` edge `0.0207` maxDD `-1.9591`
- `risk_on_high->index_1h` score `0.5443` n `43` status `ready` deltaP `11.2194` edge `0.0009` maxDD `-0.4273`
- `risk_on_and_context->index_1h` score `0.5443` n `43` status `ready` deltaP `11.2194` edge `0.0009` maxDD `-0.4273`
- `market_context_high->crypto_major_4h` score `0.478` n `77` status `ready` deltaP `4.7592` edge `0.37` maxDD `-15.2359`
- `market_context_high->crypto_major_1h` score `0.2905` n `77` status `ready` deltaP `4.3472` edge `0.0964` maxDD `-3.7178`
- `risk_on_high->equity_4h` score `0.0632` n `43` status `ready` deltaP `6.1446` edge `0.0996` maxDD `-4.824`
- `risk_on_and_context->equity_4h` score `0.0632` n `43` status `ready` deltaP `6.1446` edge `0.0996` maxDD `-4.824`
- `risk_on_high->fx_4h` score `0.0093` n `43` status `ready` deltaP `2.9977` edge `0.0072` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `0.0093` n `43` status `ready` deltaP `2.9977` edge `0.0072` maxDD `-0.1126`
- `risk_on_high->fx_1h` score `-0.2372` n `43` status `ready` deltaP `0.7123` edge `-0.0005` maxDD `-0.1065`
- `risk_on_and_context->fx_1h` score `-0.2372` n `43` status `ready` deltaP `0.7123` edge `-0.0005` maxDD `-0.1065`
- `market_context_high->metal_1h` score `-0.3362` n `77` status `ready` deltaP `-0.1031` edge `0.0077` maxDD `-0.4687`
- `risk_on_high->commodity_24h` score `-0.3627` n `43` status `ready` deltaP `10.5076` edge `-0.0205` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `-0.3627` n `43` status `ready` deltaP `10.5076` edge `-0.0205` maxDD `-1.7154`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
