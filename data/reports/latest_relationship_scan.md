# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-19T19:07:33.964110+00:00`
- Price records: `672`
- Market context records: `4130`
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

- `risk_on_high->unknown_4h` score `145.0046` n `40` status `ready` deltaP `-9.6212` edge `12.3297` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `145.0046` n `40` status `ready` deltaP `-9.6212` edge `12.3297` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `38.045` n `202` status `ready` deltaP `1.2406` edge `3.3201` maxDD `-9.6361`
- `market_context_high->unknown_24h` score `13.2985` n `198` status `ready` deltaP `-10.9091` edge `1.5843` maxDD `-24.2693`
- `market_context_high->unknown_4h` score `10.995` n `198` status `ready` deltaP `-2.9798` edge `1.4791` maxDD `-35.7719`
- `risk_on_high->equity_4h` score `2.6926` n `40` status `ready` deltaP `35.9848` edge `-0.0108` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `2.6926` n `40` status `ready` deltaP `35.9848` edge `-0.0108` maxDD `-0.044`
- `risk_on_high->crypto_major_4h` score `1.4944` n `40` status `ready` deltaP `17.803` edge `0.0724` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.4944` n `40` status `ready` deltaP `17.803` edge `0.0724` maxDD `-2.6576`
- `risk_on_high->metal_4h` score `0.4076` n `40` status `ready` deltaP `10.6818` edge `0.0146` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.4076` n `40` status `ready` deltaP `10.6818` edge `0.0146` maxDD `-1.3516`
- `risk_on_high->equity_1h` score `0.2807` n `40` status `ready` deltaP `11.0629` edge `-0.0114` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.2807` n `40` status `ready` deltaP `11.0629` edge `-0.0114` maxDD `-0.7834`
- `risk_on_high->crypto_major_1h` score `0.2031` n `40` status `ready` deltaP `10.9581` edge `0.0072` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.2031` n `40` status `ready` deltaP `10.9581` edge `0.0072` maxDD `-2.3372`
- `risk_on_high->fx_4h` score `0.0402` n `40` status `ready` deltaP `9.3182` edge `0.0021` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.0402` n `40` status `ready` deltaP `9.3182` edge `0.0021` maxDD `-0.3925`
- `risk_on_high->fx_1h` score `-0.0001` n `40` status `ready` deltaP `3.3533` edge `0.0006` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `-0.0001` n `40` status `ready` deltaP `3.3533` edge `0.0006` maxDD `-0.1704`
- `risk_on_high->metal_24h` score `-0.0762` n `40` status `ready` deltaP `-20.3788` edge `0.1875` maxDD `-1.9133`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
