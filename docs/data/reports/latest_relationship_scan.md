# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-20T09:35:07.311974+00:00`
- Price records: `672`
- Market context records: `4194`
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

- `risk_on_high->unknown_4h` score `145.0784` n `40` status `ready` deltaP `-9.2683` edge `12.3335` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `145.0784` n `40` status `ready` deltaP `-9.2683` edge `12.3335` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `33.6083` n `206` status `ready` deltaP `0.9811` edge `2.9521` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `10.0793` n `202` status `ready` deltaP `-3.897` edge `1.4089` maxDD `-35.7719`
- `market_context_high->unknown_24h` score `8.4828` n `198` status `ready` deltaP `-12.695` edge `1.1949` maxDD `-24.2693`
- `risk_on_high->commodity_24h` score `2.3328` n `40` status `ready` deltaP `4.5681` edge `0.3921` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `2.3328` n `40` status `ready` deltaP `4.5681` edge `0.3921` maxDD `-12.9187`
- `risk_on_high->equity_4h` score `2.0535` n `40` status `ready` deltaP `31.3415` edge `-0.0331` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `2.0535` n `40` status `ready` deltaP `31.3415` edge `-0.0331` maxDD `-0.044`
- `risk_on_high->crypto_major_4h` score `0.6448` n `40` status `ready` deltaP `13.9634` edge `0.0272` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.6448` n `40` status `ready` deltaP `13.9634` edge `0.0272` maxDD `-2.6576`
- `risk_on_high->metal_4h` score `0.1357` n `40` status `ready` deltaP `8.9634` edge `-0.0088` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.1357` n `40` status `ready` deltaP `8.9634` edge `-0.0088` maxDD `-1.3516`
- `risk_on_high->fx_4h` score `0.0958` n `40` status `ready` deltaP `9.939` edge `0.0051` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.0958` n `40` status `ready` deltaP `9.939` edge `0.0051` maxDD `-0.3925`
- `risk_on_high->fx_1h` score `0.0661` n `40` status `ready` deltaP `4.4012` edge `0.0021` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.0661` n `40` status `ready` deltaP `4.4012` edge `0.0021` maxDD `-0.1704`
- `risk_on_high->equity_1h` score `-0.0309` n `40` status `ready` deltaP `8.9671` edge `-0.0234` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `-0.0309` n `40` status `ready` deltaP `8.9671` edge `-0.0234` maxDD `-0.7834`
- `risk_on_high->crypto_major_1h` score `-0.0572` n `40` status `ready` deltaP `8.5629` edge `-0.0102` maxDD `-2.3372`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
