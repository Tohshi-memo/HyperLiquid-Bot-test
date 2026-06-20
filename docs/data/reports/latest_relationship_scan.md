# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-20T19:22:26.845241+00:00`
- Price records: `672`
- Market context records: `4239`
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

- `risk_on_high->unknown_4h` score `130.5932` n `44` status `ready` deltaP `-4.0327` edge `11.0915` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `130.5932` n `44` status `ready` deltaP `-4.0327` edge `11.0915` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `29.3588` n `219` status `ready` deltaP `1.0227` edge `2.5977` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `7.8853` n `216` status `ready` deltaP `-2.8963` edge `1.2194` maxDD `-35.7719`
- `market_context_high->unknown_24h` score `6.078` n `200` status `ready` deltaP `-12.0347` edge `0.9901` maxDD `-24.2693`
- `risk_on_high->equity_4h` score `1.6769` n `44` status `ready` deltaP `31.5688` edge `-0.066` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `1.6769` n `44` status `ready` deltaP `31.5688` edge `-0.066` maxDD `-0.044`
- `risk_on_high->commodity_24h` score `1.543` n `40` status `ready` deltaP `1.9097` edge `0.344` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `1.543` n `40` status `ready` deltaP `1.9097` edge `0.344` maxDD `-12.9187`
- `risk_on_high->fx_1h` score `0.2542` n `44` status `ready` deltaP `6.2466` edge `0.0025` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.2542` n `44` status `ready` deltaP `6.2466` edge `0.0025` maxDD `-0.1704`
- `risk_on_high->crypto_major_4h` score `0.2029` n `44` status `ready` deltaP `12.8188` edge `-0.002` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.2029` n `44` status `ready` deltaP `12.8188` edge `-0.002` maxDD `-2.6576`
- `risk_on_high->crypto_major_1h` score `-0.0313` n `44` status `ready` deltaP `6.8999` edge `0.0042` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `-0.0313` n `44` status `ready` deltaP `6.8999` edge `0.0042` maxDD `-2.3372`
- `risk_on_high->fx_4h` score `-0.0502` n `44` status `ready` deltaP `7.5665` edge `0.0022` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `-0.0502` n `44` status `ready` deltaP `7.5665` edge `0.0022` maxDD `-0.3925`
- `risk_on_high->equity_1h` score `-0.0934` n `44` status `ready` deltaP `7.3762` edge `-0.018` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `-0.0934` n `44` status `ready` deltaP `7.3762` edge `-0.018` maxDD `-0.7834`
- `market_context_high->fx_1h` score `-0.442` n `219` status `ready` deltaP `0.1237` edge `-0.0016` maxDD `-1.1377`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
