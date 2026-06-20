# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-20T17:52:27.501108+00:00`
- Price records: `672`
- Market context records: `4232`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9984`

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

- `risk_on_high->unknown_4h` score `134.0522` n `43` status `ready` deltaP `-4.6264` edge `11.3837` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `134.0522` n `43` status `ready` deltaP `-4.6264` edge `11.3837` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `29.2929` n `219` status `ready` deltaP `0.5736` edge `2.5952` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `8.0877` n `215` status `ready` deltaP `-2.7659` edge `1.2354` maxDD `-35.7719`
- `market_context_high->unknown_24h` score `5.7719` n `200` status `ready` deltaP `-12.3819` edge `0.9669` maxDD `-24.2693`
- `risk_on_high->commodity_24h` score `1.9587` n `40` status `ready` deltaP `2.9514` edge `0.3717` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `1.9587` n `40` status `ready` deltaP `2.9514` edge `0.3717` maxDD `-12.9187`
- `risk_on_high->equity_4h` score `1.5909` n `43` status `ready` deltaP `31.3634` edge `-0.0718` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `1.5909` n `43` status `ready` deltaP `31.3634` edge `-0.0718` maxDD `-0.044`
- `risk_on_high->fx_1h` score `0.2721` n `44` status `ready` deltaP `6.3963` edge `0.003` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.2721` n `44` status `ready` deltaP `6.3963` edge `0.003` maxDD `-0.1704`
- `risk_on_high->crypto_major_1h` score `0.0271` n `44` status `ready` deltaP `7.1993` edge `0.0097` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.0271` n `44` status `ready` deltaP `7.1993` edge `0.0097` maxDD `-2.3372`
- `risk_on_high->equity_1h` score `-0.0526` n `44` status `ready` deltaP `7.5259` edge `-0.0156` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `-0.0526` n `44` status `ready` deltaP `7.5259` edge `-0.0156` maxDD `-0.7834`
- `risk_on_high->crypto_major_4h` score `-0.0581` n `43` status `ready` deltaP `12.032` edge `-0.0185` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `-0.0581` n `43` status `ready` deltaP `12.032` edge `-0.0185` maxDD `-2.6576`
- `risk_on_high->fx_4h` score `-0.1113` n `43` status `ready` deltaP `6.6151` edge `0.0007` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `-0.1113` n `43` status `ready` deltaP `6.6151` edge `0.0007` maxDD `-0.3925`
- `market_context_high->fx_1h` score `-0.4303` n `219` status `ready` deltaP `0.2734` edge `-0.0011` maxDD `-1.1377`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
