# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-19T09:07:29.713411+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8686`

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

- `market_context_high->commodity_24h` score `1.6911` n `76` status `ready` deltaP `16.3455` edge `0.1171` maxDD `-1.8119`
- `risk_on_high->equity_24h` score `1.5429` n `43` status `ready` deltaP `-18.9363` edge `0.7657` maxDD `-28.5375`
- `risk_on_and_context->equity_24h` score `1.5429` n `43` status `ready` deltaP `-18.9363` edge `0.7657` maxDD `-28.5375`
- `market_context_high->crypto_major_24h` score `0.8503` n `76` status `ready` deltaP `2.2661` edge `0.7036` maxDD `-35.1086`
- `risk_on_high->equity_1h` score `0.7452` n `43` status `ready` deltaP `15.1233` edge `0.0191` maxDD `-1.9591`
- `risk_on_and_context->equity_1h` score `0.7452` n `43` status `ready` deltaP `15.1233` edge `0.0191` maxDD `-1.9591`
- `market_context_high->equity_24h` score `0.6986` n `76` status `ready` deltaP `0.4028` edge `0.9744` maxDD `-55.843`
- `risk_on_high->index_1h` score `0.5407` n `43` status `ready` deltaP `11.2194` edge `0.0006` maxDD `-0.4273`
- `risk_on_and_context->index_1h` score `0.5407` n `43` status `ready` deltaP `11.2194` edge `0.0006` maxDD `-0.4273`
- `market_context_high->crypto_major_4h` score `0.3337` n `77` status `ready` deltaP `3.8446` edge `0.3576` maxDD `-15.2359`
- `market_context_high->crypto_major_1h` score `0.2437` n `77` status `ready` deltaP `3.8981` edge `0.0934` maxDD `-3.7178`
- `risk_on_high->fx_4h` score `0.0252` n `43` status `ready` deltaP `3.1506` edge `0.0075` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `0.0252` n `43` status `ready` deltaP `3.1506` edge `0.0075` maxDD `-0.1126`
- `risk_on_high->equity_4h` score `-0.0578` n `43` status `ready` deltaP `5.533` edge `0.0936` maxDD `-4.824`
- `risk_on_and_context->equity_4h` score `-0.0578` n `43` status `ready` deltaP `5.533` edge `0.0936` maxDD `-4.824`
- `risk_on_high->commodity_24h` score `-0.1597` n `43` status `ready` deltaP `11.725` edge `-0.0117` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `-0.1597` n `43` status `ready` deltaP `11.725` edge `-0.0117` maxDD `-1.7154`
- `risk_on_high->fx_1h` score `-0.2302` n `43` status `ready` deltaP `0.8625` edge `-0.0006` maxDD `-0.1065`
- `risk_on_and_context->fx_1h` score `-0.2302` n `43` status `ready` deltaP `0.8625` edge `-0.0006` maxDD `-0.1065`
- `market_context_high->metal_1h` score `-0.3242` n `77` status `ready` deltaP `0.0466` edge `0.0077` maxDD `-0.4687`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
