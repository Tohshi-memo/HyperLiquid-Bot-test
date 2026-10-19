# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-19T08:37:28.814127+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8614`

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

- `risk_on_high->equity_24h` score `1.7819` n `43` status `ready` deltaP `-18.5885` edge `0.7833` maxDD `-28.5375`
- `risk_on_and_context->equity_24h` score `1.7819` n `43` status `ready` deltaP `-18.5885` edge `0.7833` maxDD `-28.5375`
- `market_context_high->commodity_24h` score `1.644` n `76` status `ready` deltaP `15.9977` edge `0.1155` maxDD `-1.8119`
- `market_context_high->crypto_major_24h` score `0.9518` n `76` status `ready` deltaP `2.6133` edge `0.7143` maxDD `-35.1086`
- `market_context_high->equity_24h` score `0.9376` n `76` status `ready` deltaP `0.7506` edge `0.992` maxDD `-55.843`
- `risk_on_high->equity_1h` score `0.7308` n `43` status `ready` deltaP `14.9732` edge `0.0189` maxDD `-1.9591`
- `risk_on_and_context->equity_1h` score `0.7308` n `43` status `ready` deltaP `14.9732` edge `0.0189` maxDD `-1.9591`
- `risk_on_high->index_1h` score `0.5419` n `43` status `ready` deltaP `11.2194` edge `0.0007` maxDD `-0.4273`
- `risk_on_and_context->index_1h` score `0.5419` n `43` status `ready` deltaP `11.2194` edge `0.0007` maxDD `-0.4273`
- `market_context_high->crypto_major_4h` score `0.3697` n `77` status `ready` deltaP `3.997` edge `0.3612` maxDD `-15.2359`
- `market_context_high->crypto_major_1h` score `0.2679` n `77` status `ready` deltaP `4.1975` edge `0.0945` maxDD `-3.7178`
- `risk_on_high->fx_4h` score `0.0117` n `43` status `ready` deltaP `2.9977` edge `0.0074` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `0.0117` n `43` status `ready` deltaP `2.9977` edge `0.0074` maxDD `-0.1126`
- `risk_on_high->equity_4h` score `-0.0494` n `43` status `ready` deltaP `5.533` edge `0.0943` maxDD `-4.824`
- `risk_on_and_context->equity_4h` score `-0.0494` n `43` status `ready` deltaP `5.533` edge `0.0943` maxDD `-4.824`
- `risk_on_high->commodity_24h` score `-0.2067` n `43` status `ready` deltaP `11.3772` edge `-0.0133` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `-0.2067` n `43` status `ready` deltaP `11.3772` edge `-0.0133` maxDD `-1.7154`
- `risk_on_high->fx_1h` score `-0.2294` n `43` status `ready` deltaP `0.8625` edge `-0.0005` maxDD `-0.1065`
- `risk_on_and_context->fx_1h` score `-0.2294` n `43` status `ready` deltaP `0.8625` edge `-0.0005` maxDD `-0.1065`
- `market_context_high->metal_1h` score `-0.3374` n `77` status `ready` deltaP `-0.1031` edge `0.0076` maxDD `-0.4687`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
