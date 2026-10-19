# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-19T06:22:23.744518+00:00`
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

- `risk_on_high->equity_24h` score `3.0687` n `43` status `ready` deltaP `-17.0233` edge `0.8801` maxDD `-28.5375`
- `risk_on_and_context->equity_24h` score `3.0687` n `43` status `ready` deltaP `-17.0233` edge `0.8801` maxDD `-28.5375`
- `market_context_high->equity_24h` score `2.2244` n `76` status `ready` deltaP `2.3158` edge `1.0888` maxDD `-55.843`
- `market_context_high->crypto_major_24h` score `1.441` n `76` status `ready` deltaP `4.1758` edge `0.7666` maxDD `-35.1086`
- `market_context_high->commodity_24h` score `1.3628` n `76` status `ready` deltaP `14.4325` edge `0.1025` maxDD `-1.8119`
- `risk_on_high->equity_1h` score `0.7416` n `43` status `ready` deltaP `14.823` edge `0.0208` maxDD `-1.9591`
- `risk_on_and_context->equity_1h` score `0.7416` n `43` status `ready` deltaP `14.823` edge `0.0208` maxDD `-1.9591`
- `market_context_high->crypto_major_4h` score `0.5495` n `77` status `ready` deltaP `5.369` edge `0.3751` maxDD `-15.2359`
- `risk_on_high->index_1h` score `0.519` n `43` status `ready` deltaP `10.9191` edge `0.0008` maxDD `-0.4273`
- `risk_on_and_context->index_1h` score `0.519` n `43` status `ready` deltaP `10.9191` edge `0.0008` maxDD `-0.4273`
- `market_context_high->crypto_major_1h` score `0.2991` n `77` status `ready` deltaP `4.4969` edge `0.0965` maxDD `-3.7178`
- `risk_on_high->equity_4h` score `0.1697` n `43` status `ready` deltaP `6.7562` edge `0.1044` maxDD `-4.824`
- `risk_on_and_context->equity_4h` score `0.1697` n `43` status `ready` deltaP `6.7562` edge `0.1044` maxDD `-4.824`
- `risk_on_high->fx_4h` score `0.0228` n `43` status `ready` deltaP `3.1506` edge `0.0073` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `0.0228` n `43` status `ready` deltaP `3.1506` edge `0.0073` maxDD `-0.1126`
- `risk_on_high->fx_1h` score `-0.2279` n `43` status `ready` deltaP `0.8625` edge `-0.0003` maxDD `-0.1065`
- `risk_on_and_context->fx_1h` score `-0.2279` n `43` status `ready` deltaP `0.8625` edge `-0.0003` maxDD `-0.1065`
- `risk_on_high->index_4h` score `-0.361` n `43` status `ready` deltaP `7.247` edge `0.0083` maxDD `-0.9359`
- `risk_on_and_context->index_4h` score `-0.361` n `43` status `ready` deltaP `7.247` edge `0.0083` maxDD `-0.9359`
- `market_context_high->metal_1h` score `-0.3637` n `77` status `ready` deltaP `-0.4025` edge `0.0074` maxDD `-0.4687`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
