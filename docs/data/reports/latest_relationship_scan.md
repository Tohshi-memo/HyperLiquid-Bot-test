# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-20T09:52:25.871392+00:00`
- Price records: `672`
- Market context records: `4196`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10050`

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

- `risk_on_high->unknown_4h` score `145.123` n `40` status `ready` deltaP `-9.1159` edge `12.3362` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `145.123` n `40` status `ready` deltaP `-9.1159` edge `12.3362` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `33.2335` n `207` status `ready` deltaP `0.8259` edge `2.9219` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `10.1238` n `202` status `ready` deltaP `-3.7446` edge `1.4116` maxDD `-35.7719`
- `market_context_high->unknown_24h` score `8.4599` n `198` status `ready` deltaP `-12.6657` edge `1.1928` maxDD `-24.2693`
- `risk_on_high->commodity_24h` score `2.3277` n `40` status `ready` deltaP `4.5341` edge `0.3919` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `2.3277` n `40` status `ready` deltaP `4.5341` edge `0.3919` maxDD `-12.9187`
- `risk_on_high->equity_4h` score `2.0933` n `40` status `ready` deltaP `31.4939` edge `-0.0308` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `2.0933` n `40` status `ready` deltaP `31.4939` edge `-0.0308` maxDD `-0.044`
- `risk_on_high->crypto_major_4h` score `0.676` n `40` status `ready` deltaP `13.9634` edge `0.0298` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.676` n `40` status `ready` deltaP `13.9634` edge `0.0298` maxDD `-2.6576`
- `risk_on_high->metal_4h` score `0.1396` n `40` status `ready` deltaP `8.9634` edge `-0.0083` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.1396` n `40` status `ready` deltaP `8.9634` edge `-0.0083` maxDD `-1.3516`
- `risk_on_high->fx_4h` score `0.084` n `40` status `ready` deltaP `9.7866` edge `0.0046` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.084` n `40` status `ready` deltaP `9.7866` edge `0.0046` maxDD `-0.3925`
- `risk_on_high->fx_1h` score `0.0552` n `40` status `ready` deltaP `4.2515` edge `0.0017` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.0552` n `40` status `ready` deltaP `4.2515` edge `0.0017` maxDD `-0.1704`
- `risk_on_high->equity_1h` score `-0.0093` n `40` status `ready` deltaP `8.9671` edge `-0.0216` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `-0.0093` n `40` status `ready` deltaP `8.9671` edge `-0.0216` maxDD `-0.7834`
- `risk_on_high->crypto_major_1h` score `-0.0533` n `40` status `ready` deltaP `8.5629` edge `-0.0097` maxDD `-2.3372`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
