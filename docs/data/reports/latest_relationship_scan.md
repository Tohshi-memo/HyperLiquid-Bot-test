# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-19T18:22:31.344312+00:00`
- Price records: `672`
- Market context records: `4127`
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

- `risk_on_high->unknown_4h` score `145.1645` n `40` status `ready` deltaP `-9.3175` edge `12.341` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `145.1645` n `40` status `ready` deltaP `-9.3175` edge `12.341` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `38.0942` n `202` status `ready` deltaP `1.6897` edge `3.3212` maxDD `-9.6361`
- `market_context_high->unknown_24h` score `13.7021` n `198` status `ready` deltaP `-10.5443` edge `1.6155` maxDD `-24.2693`
- `market_context_high->unknown_4h` score `11.1549` n `198` status `ready` deltaP `-2.6761` edge `1.4904` maxDD `-35.7719`
- `risk_on_high->equity_4h` score `2.7473` n `40` status `ready` deltaP `36.2632` edge `-0.0081` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `2.7473` n `40` status `ready` deltaP `36.2632` edge `-0.0081` maxDD `-0.044`
- `risk_on_high->crypto_major_4h` score `1.5838` n `40` status `ready` deltaP `18.0505` edge `0.0782` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.5838` n `40` status `ready` deltaP `18.0505` edge `0.0782` maxDD `-2.6576`
- `risk_on_high->metal_4h` score `0.463` n `40` status `ready` deltaP `10.9389` edge `0.02` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.463` n `40` status `ready` deltaP `10.9389` edge `0.02` maxDD `-1.3516`
- `risk_on_high->equity_1h` score `0.3011` n `40` status `ready` deltaP `11.0629` edge `-0.0097` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.3011` n `40` status `ready` deltaP `11.0629` edge `-0.0097` maxDD `-0.7834`
- `risk_on_high->crypto_major_1h` score `0.2327` n `40` status `ready` deltaP `11.1078` edge `0.01` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.2327` n `40` status `ready` deltaP `11.1078` edge `0.01` maxDD `-2.3372`
- `risk_on_high->fx_4h` score `0.0538` n `40` status `ready` deltaP `9.5362` edge `0.0024` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.0538` n `40` status `ready` deltaP `9.5362` edge `0.0024` maxDD `-0.3925`
- `risk_on_high->metal_24h` score `0.0368` n `40` status `ready` deltaP `-20.0943` edge `0.2001` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `0.0368` n `40` status `ready` deltaP `-20.0943` edge `0.2001` maxDD `-1.9133`
- `risk_on_high->fx_1h` score `0.0093` n `40` status `ready` deltaP `3.503` edge `0.0008` maxDD `-0.1704`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
