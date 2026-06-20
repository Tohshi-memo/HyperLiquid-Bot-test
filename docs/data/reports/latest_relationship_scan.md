# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-20T17:37:29.670163+00:00`
- Price records: `672`
- Market context records: `4231`
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

- `risk_on_high->unknown_4h` score `137.7448` n `42` status `ready` deltaP `-5.5677` edge `11.6977` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `137.7448` n `42` status `ready` deltaP `-5.5677` edge `11.6977` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `29.2917` n `219` status `ready` deltaP `0.5736` edge `2.5951` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `8.2453` n `214` status `ready` deltaP `-2.942` edge `1.2497` maxDD `-35.7719`
- `market_context_high->unknown_24h` score `5.7076` n `200` status `ready` deltaP `-12.5556` edge `0.9627` maxDD `-24.2693`
- `risk_on_high->commodity_24h` score `2.0254` n `40` status `ready` deltaP `3.125` edge `0.3761` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `2.0254` n `40` status `ready` deltaP `3.125` edge `0.3761` maxDD `-12.9187`
- `risk_on_high->equity_4h` score `1.6142` n `42` status `ready` deltaP `31.4605` edge `-0.0705` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `1.6142` n `42` status `ready` deltaP `31.4605` edge `-0.0705` maxDD `-0.044`
- `risk_on_high->fx_1h` score `0.2721` n `44` status `ready` deltaP `6.3963` edge `0.003` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.2721` n `44` status `ready` deltaP `6.3963` edge `0.003` maxDD `-0.1704`
- `risk_on_high->crypto_major_1h` score `0.0271` n `44` status `ready` deltaP `7.1993` edge `0.0097` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.0271` n `44` status `ready` deltaP `7.1993` edge `0.0097` maxDD `-2.3372`
- `risk_on_high->equity_1h` score `-0.0526` n `44` status `ready` deltaP `7.5259` edge `-0.0156` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `-0.0526` n `44` status `ready` deltaP `7.5259` edge `-0.0156` maxDD `-0.7834`
- `risk_on_high->crypto_major_4h` score `-0.075` n `42` status `ready` deltaP `11.5201` edge `-0.0165` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `-0.075` n `42` status `ready` deltaP `11.5201` edge `-0.0165` maxDD `-2.6576`
- `risk_on_high->fx_4h` score `-0.1725` n `42` status `ready` deltaP `5.6185` edge `-0.0005` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `-0.1725` n `42` status `ready` deltaP `5.6185` edge `-0.0005` maxDD `-0.3925`
- `risk_on_high->metal_4h` score `-0.4142` n `42` status `ready` deltaP `4.2247` edge `-0.0477` maxDD `-1.3516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
