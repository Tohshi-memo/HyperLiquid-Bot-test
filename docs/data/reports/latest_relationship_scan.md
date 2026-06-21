# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-21T11:22:25.894908+00:00`
- Price records: `672`
- Market context records: `4307`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10730`

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

- `risk_on_high->unknown_4h` score `130.6346` n `44` status `ready` deltaP `-1.7462` edge `11.0797` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `130.6346` n `44` status `ready` deltaP `-1.7462` edge `11.0797` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `27.9121` n `236` status `ready` deltaP `3.3544` edge `2.4616` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `8.9912` n `236` status `ready` deltaP `1.297` edge `1.2836` maxDD `-35.7719`
- `market_context_high->unknown_24h` score `5.283` n `207` status `ready` deltaP `-7.8879` edge `0.8962` maxDD `-24.2693`
- `risk_on_high->metal_24h` score `2.0491` n `40` status `ready` deltaP `-19.8264` edge `0.4563` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `2.0491` n `40` status `ready` deltaP `-19.8264` edge `0.4563` maxDD `-1.9133`
- `risk_on_high->equity_4h` score `1.9633` n `44` status `ready` deltaP `30.3493` edge `-0.034` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `1.9633` n `44` status `ready` deltaP `30.3493` edge `-0.034` maxDD `-0.044`
- `risk_on_high->equity_24h` score `1.6953` n `40` status `ready` deltaP `22.9167` edge `-0.0115` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.6953` n `40` status `ready` deltaP `22.9167` edge `-0.0115` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `1.1106` n `44` status `ready` deltaP `16.02` edge `0.0523` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.1106` n `44` status `ready` deltaP `16.02` edge `0.0523` maxDD `-2.6576`
- `risk_on_high->fx_1h` score `0.4434` n `44` status `ready` deltaP `8.4921` edge `0.0033` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.4434` n `44` status `ready` deltaP `8.4921` edge `0.0033` maxDD `-0.1704`
- `risk_on_high->crypto_major_1h` score `0.1752` n `44` status `ready` deltaP `8.3969` edge `0.0207` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.1752` n `44` status `ready` deltaP `8.3969` edge `0.0207` maxDD `-2.3372`
- `risk_on_high->fx_4h` score `0.0021` n `44` status `ready` deltaP `8.4811` edge `0.0028` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.0021` n `44` status `ready` deltaP `8.4811` edge `0.0028` maxDD `-0.3925`
- `risk_on_high->equity_1h` score `-0.0273` n `44` status `ready` deltaP `6.7774` edge `-0.0085` maxDD `-0.7834`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
