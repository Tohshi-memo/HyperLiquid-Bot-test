# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-20T09:22:27.748280+00:00`
- Price records: `672`
- Market context records: `4193`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10042`

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

- `risk_on_high->unknown_4h` score `145.035` n `40` status `ready` deltaP `-9.4207` edge `12.3309` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `145.035` n `40` status `ready` deltaP `-9.4207` edge `12.3309` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `33.9881` n `205` status `ready` deltaP `1.1392` edge `2.9827` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `10.0359` n `202` status `ready` deltaP `-4.0494` edge `1.4063` maxDD `-35.7719`
- `market_context_high->unknown_24h` score `8.5069` n `198` status `ready` deltaP `-12.7242` edge `1.1971` maxDD `-24.2693`
- `risk_on_high->commodity_24h` score `2.3404` n `40` status `ready` deltaP `4.602` edge `0.3925` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `2.3404` n `40` status `ready` deltaP `4.602` edge `0.3925` maxDD `-12.9187`
- `risk_on_high->equity_4h` score `2.0137` n `40` status `ready` deltaP `31.189` edge `-0.0354` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `2.0137` n `40` status `ready` deltaP `31.189` edge `-0.0354` maxDD `-0.044`
- `risk_on_high->crypto_major_4h` score `0.6076` n `40` status `ready` deltaP `13.9634` edge `0.0241` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.6076` n `40` status `ready` deltaP `13.9634` edge `0.0241` maxDD `-2.6576`
- `risk_on_high->metal_4h` score `0.1239` n `40` status `ready` deltaP `8.811` edge `-0.0093` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.1239` n `40` status `ready` deltaP `8.811` edge `-0.0093` maxDD `-1.3516`
- `risk_on_high->fx_4h` score `0.1038` n `40` status `ready` deltaP `10.0915` edge `0.0051` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.1038` n `40` status `ready` deltaP `10.0915` edge `0.0051` maxDD `-0.3925`
- `risk_on_high->fx_1h` score `0.063` n `40` status `ready` deltaP `4.4012` edge `0.0017` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.063` n `40` status `ready` deltaP `4.4012` edge `0.0017` maxDD `-0.1704`
- `risk_on_high->crypto_major_1h` score `-0.0704` n `40` status `ready` deltaP `8.5629` edge `-0.0119` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `-0.0704` n `40` status `ready` deltaP `8.5629` edge `-0.0119` maxDD `-2.3372`
- `risk_on_high->equity_1h` score `-0.0717` n `40` status `ready` deltaP `8.8174` edge `-0.0258` maxDD `-0.7834`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
