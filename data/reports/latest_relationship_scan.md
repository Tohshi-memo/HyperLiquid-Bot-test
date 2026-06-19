# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-19T17:52:28.968996+00:00`
- Price records: `672`
- Market context records: `4125`
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

- `risk_on_high->unknown_4h` score `145.2657` n `40` status `ready` deltaP `-9.1165` edge `12.3481` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `145.2657` n `40` status `ready` deltaP `-9.1165` edge `12.3481` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `38.8669` n `200` status `ready` deltaP `1.8234` edge `3.3847` maxDD `-9.6361`
- `market_context_high->unknown_24h` score `13.9686` n `198` status `ready` deltaP `-10.303` edge `1.6361` maxDD `-24.2693`
- `market_context_high->unknown_4h` score `11.2562` n `198` status `ready` deltaP `-2.4751` edge `1.4975` maxDD `-35.7719`
- `risk_on_high->equity_4h` score `2.7548` n `40` status `ready` deltaP `36.297` edge `-0.0077` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `2.7548` n `40` status `ready` deltaP `36.297` edge `-0.0077` maxDD `-0.044`
- `risk_on_high->crypto_major_4h` score `1.6173` n `40` status `ready` deltaP `18.2143` edge `0.0799` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.6173` n `40` status `ready` deltaP `18.2143` edge `0.0799` maxDD `-2.6576`
- `risk_on_high->metal_4h` score `0.4828` n `40` status `ready` deltaP `11.109` edge `0.0214` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.4828` n `40` status `ready` deltaP `11.109` edge `0.0214` maxDD `-1.3516`
- `risk_on_high->equity_1h` score `0.3299` n `40` status `ready` deltaP `11.3623` edge `-0.0093` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.3299` n `40` status `ready` deltaP `11.3623` edge `-0.0093` maxDD `-0.7834`
- `risk_on_high->crypto_major_1h` score `0.2483` n `40` status `ready` deltaP `11.2575` edge `0.011` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.2483` n `40` status `ready` deltaP `11.2575` edge `0.011` maxDD `-2.3372`
- `risk_on_high->metal_24h` score `0.109` n `40` status `ready` deltaP `-19.906` edge `0.2081` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `0.109` n `40` status `ready` deltaP `-19.906` edge `0.2081` maxDD `-1.9133`
- `risk_on_high->fx_4h` score `0.0629` n `40` status `ready` deltaP `9.6805` edge `0.0026` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.0629` n `40` status `ready` deltaP `9.6805` edge `0.0026` maxDD `-0.3925`
- `risk_on_high->fx_1h` score `0.0085` n `40` status `ready` deltaP `3.503` edge `0.0007` maxDD `-0.1704`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
