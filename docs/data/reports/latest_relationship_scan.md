# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-19T18:37:30.322704+00:00`
- Price records: `672`
- Market context records: `4128`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10016`

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

- `risk_on_high->unknown_4h` score `145.112` n `40` status `ready` deltaP `-9.4184` edge `12.3373` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `145.112` n `40` status `ready` deltaP `-9.4184` edge `12.3373` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `38.0774` n `202` status `ready` deltaP `1.54` edge `3.3208` maxDD `-9.6361`
- `market_context_high->unknown_24h` score `13.5688` n `198` status `ready` deltaP `-10.6655` edge `1.6052` maxDD `-24.2693`
- `market_context_high->unknown_4h` score `11.1025` n `198` status `ready` deltaP `-2.777` edge `1.4867` maxDD `-35.7719`
- `risk_on_high->equity_4h` score `2.7291` n `40` status `ready` deltaP `36.1707` edge `-0.009` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `2.7291` n `40` status `ready` deltaP `36.1707` edge `-0.009` maxDD `-0.044`
- `risk_on_high->crypto_major_4h` score `1.5544` n `40` status `ready` deltaP `17.9683` edge `0.0763` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.5544` n `40` status `ready` deltaP `17.9683` edge `0.0763` maxDD `-2.6576`
- `risk_on_high->metal_4h` score `0.4453` n `40` status `ready` deltaP `10.8535` edge `0.0183` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.4453` n `40` status `ready` deltaP `10.8535` edge `0.0183` maxDD `-1.3516`
- `risk_on_high->equity_1h` score `0.2939` n `40` status `ready` deltaP `11.0629` edge `-0.0103` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.2939` n `40` status `ready` deltaP `11.0629` edge `-0.0103` maxDD `-0.7834`
- `risk_on_high->crypto_major_1h` score `0.2203` n `40` status `ready` deltaP `10.9581` edge `0.0094` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.2203` n `40` status `ready` deltaP `10.9581` edge `0.0094` maxDD `-2.3372`
- `risk_on_high->fx_4h` score `0.0493` n `40` status `ready` deltaP `9.4637` edge `0.0023` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.0493` n `40` status `ready` deltaP `9.4637` edge `0.0023` maxDD `-0.3925`
- `risk_on_high->fx_1h` score `0.0007` n `40` status `ready` deltaP `3.3533` edge `0.0007` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.0007` n `40` status `ready` deltaP `3.3533` edge `0.0007` maxDD `-0.1704`
- `risk_on_high->metal_24h` score `0.0007` n `40` status `ready` deltaP `-20.1888` edge `0.1961` maxDD `-1.9133`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
