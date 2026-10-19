# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-19T12:22:32.440371+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8566`

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

- `market_context_high->commodity_24h` score `1.7899` n `76` status `ready` deltaP `17.0411` edge `0.1207` maxDD `-1.8119`
- `risk_on_high->equity_1h` score `0.672` n `43` status `ready` deltaP `14.6729` edge `0.016` maxDD `-1.9591`
- `risk_on_and_context->equity_1h` score `0.672` n `43` status `ready` deltaP `14.6729` edge `0.016` maxDD `-1.9591`
- `risk_on_high->index_1h` score `0.5154` n `43` status `ready` deltaP `10.9191` edge `0.0005` maxDD `-0.4273`
- `risk_on_and_context->index_1h` score `0.5154` n `43` status `ready` deltaP `10.9191` edge `0.0005` maxDD `-0.4273`
- `market_context_high->crypto_major_24h` score `0.2588` n `76` status `ready` deltaP `0.3563` edge `0.6405` maxDD `-35.1086`
- `market_context_high->crypto_major_1h` score `0.1962` n `77` status `ready` deltaP `3.2993` edge `0.0913` maxDD `-3.7178`
- `market_context_high->crypto_major_4h` score `0.1851` n `77` status `ready` deltaP `3.3873` edge `0.3416` maxDD `-15.2359`
- `risk_on_high->fx_4h` score `0.0286` n `43` status `ready` deltaP `3.2239` edge `0.0073` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `0.0286` n `43` status `ready` deltaP `3.2239` edge `0.0073` maxDD `-0.1126`
- `risk_on_high->commodity_24h` score `-0.0609` n `43` status `ready` deltaP `12.4206` edge `-0.0081` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `-0.0609` n `43` status `ready` deltaP `12.4206` edge `-0.0081` maxDD `-1.7154`
- `risk_on_high->equity_24h` score `-0.0756` n `43` status `ready` deltaP `-21.1972` edge `0.6459` maxDD `-28.5375`
- `risk_on_and_context->equity_24h` score `-0.0756` n `43` status `ready` deltaP `-21.1972` edge `0.6459` maxDD `-28.5375`
- `risk_on_high->fx_1h` score `-0.2544` n `43` status `ready` deltaP `0.412` edge `-0.0007` maxDD `-0.1065`
- `risk_on_and_context->fx_1h` score `-0.2544` n `43` status `ready` deltaP `0.412` edge `-0.0007` maxDD `-0.1065`
- `market_context_high->metal_1h` score `-0.3757` n `77` status `ready` deltaP `-0.5522` edge `0.0074` maxDD `-0.4687`
- `risk_on_high->equity_4h` score `-0.4274` n `43` status `ready` deltaP `4.5269` edge `0.0695` maxDD `-4.824`
- `risk_on_and_context->equity_4h` score `-0.4274` n `43` status `ready` deltaP `4.5269` edge `0.0695` maxDD `-4.824`
- `market_context_high->fx_4h` score `-0.4521` n `77` status `ready` deltaP `0.113` edge `0.005` maxDD `-0.7635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
