# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-19T15:37:49.287804+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8252`

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

- `market_context_high->commodity_24h` score `2.0753` n `76` status `ready` deltaP `18.8687` edge `0.1323` maxDD `-1.8119`
- `risk_on_high->equity_1h` score `0.5127` n `43` status `ready` deltaP `14.0475` edge `0.0069` maxDD `-1.9591`
- `risk_on_and_context->equity_1h` score `0.5127` n `43` status `ready` deltaP `14.0475` edge `0.0069` maxDD `-1.9591`
- `risk_on_high->index_1h` score `0.4423` n `43` status `ready` deltaP `10.1553` edge `-0.0005` maxDD `-0.4273`
- `risk_on_and_context->index_1h` score `0.4423` n `43` status `ready` deltaP `10.1553` edge `-0.0005` maxDD `-0.4273`
- `risk_on_high->commodity_24h` score `0.2245` n `43` status `ready` deltaP `14.2482` edge `0.0035` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.2245` n `43` status `ready` deltaP `14.2482` edge `0.0035` maxDD `-1.7154`
- `market_context_high->crypto_major_4h` score `0.0701` n `77` status `ready` deltaP `2.9299` edge `0.3299` maxDD `-15.2359`
- `market_context_high->crypto_major_1h` score `-0.0724` n `87` status `ready` deltaP `3.1781` edge `0.0712` maxDD `-4.8007`
- `risk_on_high->fx_4h` score `-0.1397` n `43` status `ready` deltaP `1.3152` edge `0.006` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.1397` n `43` status `ready` deltaP `1.3152` edge `0.006` maxDD `-0.1126`
- `risk_on_high->fx_1h` score `-0.2559` n `43` status `ready` deltaP `0.4143` edge `-0.0009` maxDD `-0.1065`
- `risk_on_and_context->fx_1h` score `-0.2559` n `43` status `ready` deltaP `0.4143` edge `-0.0009` maxDD `-0.1065`
- `market_context_high->crypto_major_24h` score `-0.2899` n `76` status `ready` deltaP `-1.9006` edge `0.5852` maxDD `-35.1086`
- `market_context_high->index_1h` score `-0.3373` n `87` status `ready` deltaP `3.7666` edge `-0.0016` maxDD `-1.0073`
- `market_context_high->metal_1h` score `-0.4546` n `87` status `ready` deltaP `-3.3278` edge `0.0014` maxDD `-0.6669`
- `market_context_high->fx_4h` score `-0.5615` n `77` status `ready` deltaP `-1.7957` edge `0.0037` maxDD `-0.7635`
- `market_context_high->metal_4h` score `-0.5763` n `77` status `ready` deltaP `-0.3505` edge `0.0507` maxDD `-0.7797`
- `risk_on_high->index_4h` score `-0.6352` n `43` status `ready` deltaP `4.6299` edge `0.0029` maxDD `-0.9359`
- `risk_on_and_context->index_4h` score `-0.6352` n `43` status `ready` deltaP `4.6299` edge `0.0029` maxDD `-0.9359`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
