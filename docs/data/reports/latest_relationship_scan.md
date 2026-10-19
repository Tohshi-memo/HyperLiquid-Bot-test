# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-19T15:22:31.601685+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8228`

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

- `market_context_high->commodity_24h` score `2.0482` n `76` status `ready` deltaP `18.6951` edge `0.1312` maxDD `-1.8119`
- `risk_on_high->equity_1h` score `0.5235` n `43` status `ready` deltaP `14.0475` edge `0.0078` maxDD `-1.9591`
- `risk_on_and_context->equity_1h` score `0.5235` n `43` status `ready` deltaP `14.0475` edge `0.0078` maxDD `-1.9591`
- `risk_on_high->index_1h` score `0.4435` n `43` status `ready` deltaP `10.1553` edge `-0.0004` maxDD `-0.4273`
- `risk_on_and_context->index_1h` score `0.4435` n `43` status `ready` deltaP `10.1553` edge `-0.0004` maxDD `-0.4273`
- `risk_on_high->commodity_24h` score `0.1975` n `43` status `ready` deltaP `14.0746` edge `0.0024` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.1975` n `43` status `ready` deltaP `14.0746` edge `0.0024` maxDD `-1.7154`
- `market_context_high->crypto_major_4h` score `0.0866` n `77` status `ready` deltaP `3.0824` edge `0.331` maxDD `-15.2359`
- `market_context_high->crypto_major_1h` score `-0.1262` n `86` status `ready` deltaP `2.6703` edge `0.0677` maxDD `-4.8007`
- `risk_on_high->fx_4h` score `-0.1275` n `43` status `ready` deltaP `1.4677` edge `0.006` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.1275` n `43` status `ready` deltaP `1.4677` edge `0.006` maxDD `-0.1126`
- `risk_on_high->fx_1h` score `-0.2481` n `43` status `ready` deltaP `0.564` edge `-0.0009` maxDD `-0.1065`
- `risk_on_and_context->fx_1h` score `-0.2481` n `43` status `ready` deltaP `0.564` edge `-0.0009` maxDD `-0.1065`
- `market_context_high->crypto_major_24h` score `-0.2496` n `76` status `ready` deltaP `-1.727` edge `0.5892` maxDD `-35.1086`
- `market_context_high->index_1h` score `-0.3804` n `86` status `ready` deltaP `3.1785` edge `-0.0032` maxDD `-1.0073`
- `market_context_high->metal_1h` score `-0.4942` n `86` status `ready` deltaP `-3.9827` edge `0.0007` maxDD `-0.6669`
- `market_context_high->fx_4h` score `-0.5535` n `77` status `ready` deltaP `-1.6432` edge `0.0037` maxDD `-0.7635`
- `market_context_high->metal_4h` score `-0.5778` n `77` status `ready` deltaP `-0.3505` edge `0.0505` maxDD `-0.7797`
- `risk_on_high->index_4h` score `-0.6194` n `43` status `ready` deltaP `4.7823` edge `0.0032` maxDD `-0.9359`
- `risk_on_and_context->index_4h` score `-0.6194` n `43` status `ready` deltaP `4.7823` edge `0.0032` maxDD `-0.9359`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
