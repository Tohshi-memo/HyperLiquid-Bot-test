# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-20T18:07:29.740153+00:00`
- Price records: `672`
- Market context records: `4233`
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

- `risk_on_high->unknown_4h` score `130.6572` n `44` status `ready` deltaP `-3.7279` edge `11.0948` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `130.6572` n `44` status `ready` deltaP `-3.7279` edge `11.0948` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `29.2941` n `219` status `ready` deltaP `0.5736` edge `2.5953` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `7.9493` n `216` status `ready` deltaP `-2.5915` edge `1.2227` maxDD `-35.7719`
- `market_context_high->unknown_24h` score `5.8163` n `200` status `ready` deltaP `-12.3819` edge `0.9706` maxDD `-24.2693`
- `risk_on_high->commodity_24h` score `1.8908` n `40` status `ready` deltaP `2.7778` edge `0.3672` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `1.8908` n `40` status `ready` deltaP `2.7778` edge `0.3672` maxDD `-12.9187`
- `risk_on_high->equity_4h` score `1.6045` n `44` status `ready` deltaP `31.2639` edge `-0.07` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `1.6045` n `44` status `ready` deltaP `31.2639` edge `-0.07` maxDD `-0.044`
- `risk_on_high->fx_1h` score `0.2602` n `44` status `ready` deltaP `6.2466` edge `0.003` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.2602` n `44` status `ready` deltaP `6.2466` edge `0.003` maxDD `-0.1704`
- `risk_on_high->crypto_major_4h` score `0.1197` n `44` status `ready` deltaP `12.5139` edge `-0.0069` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.1197` n `44` status `ready` deltaP `12.5139` edge `-0.0069` maxDD `-2.6576`
- `risk_on_high->crypto_major_1h` score `0.0232` n `44` status `ready` deltaP `7.1993` edge `0.0092` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.0232` n `44` status `ready` deltaP `7.1993` edge `0.0092` maxDD `-2.3372`
- `risk_on_high->fx_4h` score `-0.0533` n `44` status `ready` deltaP `7.5665` edge `0.0018` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `-0.0533` n `44` status `ready` deltaP `7.5665` edge `0.0018` maxDD `-0.3925`
- `risk_on_high->equity_1h` score `-0.0574` n `44` status `ready` deltaP `7.5259` edge `-0.016` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `-0.0574` n `44` status `ready` deltaP `7.5259` edge `-0.016` maxDD `-0.7834`
- `market_context_high->fx_1h` score `-0.4381` n `219` status `ready` deltaP `0.1237` edge `-0.0011` maxDD `-1.1377`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
