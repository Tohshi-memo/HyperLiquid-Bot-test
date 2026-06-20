# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-20T17:22:29.162191+00:00`
- Price records: `672`
- Market context records: `4230`
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

- `risk_on_high->unknown_4h` score `141.6223` n `41` status `ready` deltaP `-6.5549` edge `12.0274` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `141.6223` n `41` status `ready` deltaP `-6.5549` edge `12.0274` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `29.6457` n `218` status `ready` deltaP `0.8584` edge `2.6227` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `8.405` n `213` status `ready` deltaP `-3.1197` edge `1.2642` maxDD `-35.7719`
- `market_context_high->unknown_24h` score `5.6409` n `200` status `ready` deltaP `-12.7292` edge `0.9583` maxDD `-24.2693`
- `risk_on_high->commodity_24h` score `2.0873` n `40` status `ready` deltaP `3.2986` edge `0.3801` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `2.0873` n `40` status `ready` deltaP `3.2986` edge `0.3801` maxDD `-12.9187`
- `risk_on_high->equity_4h` score `1.647` n `41` status `ready` deltaP `31.5549` edge `-0.0684` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `1.647` n `41` status `ready` deltaP `31.5549` edge `-0.0684` maxDD `-0.044`
- `risk_on_high->fx_1h` score `0.2709` n `44` status `ready` deltaP `6.3963` edge `0.0029` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.2709` n `44` status `ready` deltaP `6.3963` edge `0.0029` maxDD `-0.1704`
- `risk_on_high->crypto_major_4h` score `0.1231` n `41` status `ready` deltaP `13.2622` edge `-0.0116` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.1231` n `41` status `ready` deltaP `13.2622` edge `-0.0116` maxDD `-2.6576`
- `risk_on_high->crypto_major_1h` score `0.0248` n `44` status `ready` deltaP `7.1993` edge `0.0094` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.0248` n `44` status `ready` deltaP `7.1993` edge `0.0094` maxDD `-2.3372`
- `risk_on_high->equity_1h` score `-0.043` n `44` status `ready` deltaP `7.5259` edge `-0.0148` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `-0.043` n `44` status `ready` deltaP `7.5259` edge `-0.0148` maxDD `-0.7834`
- `risk_on_high->fx_4h` score `-0.0837` n `41` status `ready` deltaP `7.0122` edge `0.0016` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `-0.0837` n `41` status `ready` deltaP `7.0122` edge `0.0016` maxDD `-0.3925`
- `risk_on_high->metal_4h` score `-0.3123` n `41` status `ready` deltaP `5.7927` edge `-0.0451` maxDD `-1.3516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
