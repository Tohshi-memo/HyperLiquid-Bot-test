# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-20T00:07:26.238960+00:00`
- Price records: `672`
- Market context records: `4154`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9992`

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

- `risk_on_high->unknown_4h` score `144.698` n `40` status `ready` deltaP `-10.1829` edge `12.3079` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `144.698` n `40` status `ready` deltaP `-10.1829` edge `12.3079` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `36.2271` n `202` status `ready` deltaP `1.0909` edge `3.1696` maxDD `-9.6361`
- `market_context_high->unknown_24h` score `10.5919` n `198` status `ready` deltaP `-13.2718` edge `1.3745` maxDD `-24.2693`
- `market_context_high->unknown_4h` score `9.6989` n `202` status `ready` deltaP `-4.8116` edge `1.3833` maxDD `-35.7719`
- `risk_on_high->equity_4h` score `2.3214` n `40` status `ready` deltaP `34.3902` edge `-0.0311` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `2.3214` n `40` status `ready` deltaP `34.3902` edge `-0.0311` maxDD `-0.044`
- `risk_on_high->crypto_major_4h` score `0.9884` n `40` status `ready` deltaP `16.0976` edge `0.0416` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.9884` n `40` status `ready` deltaP `16.0976` edge `0.0416` maxDD `-2.6576`
- `risk_on_high->commodity_24h` score `0.8416` n `40` status `ready` deltaP `0.3125` edge `0.2962` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `0.8416` n `40` status `ready` deltaP `0.3125` edge `0.2962` maxDD `-12.9187`
- `risk_on_high->equity_1h` score `0.1668` n `40` status `ready` deltaP `10.3144` edge `-0.0159` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.1668` n `40` status `ready` deltaP `10.3144` edge `-0.0159` maxDD `-0.7834`
- `risk_on_high->fx_4h` score `0.0928` n `40` status `ready` deltaP `10.0915` edge `0.0037` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.0928` n `40` status `ready` deltaP `10.0915` edge `0.0037` maxDD `-0.3925`
- `risk_on_high->crypto_major_1h` score `0.0737` n `40` status `ready` deltaP `9.7605` edge `-0.0014` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.0737` n `40` status `ready` deltaP `9.7605` edge `-0.0014` maxDD `-2.3372`
- `risk_on_high->fx_1h` score `0.0326` n `40` status `ready` deltaP `3.9521` edge `0.0008` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.0326` n `40` status `ready` deltaP `3.9521` edge `0.0008` maxDD `-0.1704`
- `risk_on_high->metal_4h` score `0.0195` n `40` status `ready` deltaP `8.0488` edge `-0.0176` maxDD `-1.3516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
