# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-20T16:07:26.413077+00:00`
- Price records: `672`
- Market context records: `4224`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9808`

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

- `risk_on_high->unknown_4h` score `145.7159` n `40` status `ready` deltaP `-7.1341` edge `12.3724` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `145.7159` n `40` status `ready` deltaP `-7.1341` edge `12.3724` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `30.3484` n `216` status `ready` deltaP `1.2725` edge `2.6785` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `9.3262` n `208` status `ready` deltaP `-3.0956` edge `1.3408` maxDD `-35.7719`
- `market_context_high->unknown_24h` score `7.3805` n `196` status `ready` deltaP `-12.2094` edge `1.0998` maxDD `-24.2693`
- `risk_on_high->commodity_24h` score `2.3259` n `40` status `ready` deltaP `4.1667` edge `0.3942` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `2.3259` n `40` status `ready` deltaP `4.1667` edge `0.3942` maxDD `-12.9187`
- `risk_on_high->equity_4h` score `1.7865` n `40` status `ready` deltaP `31.7988` edge `-0.0584` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `1.7865` n `40` status `ready` deltaP `31.7988` edge `-0.0584` maxDD `-0.044`
- `risk_on_high->fx_1h` score `0.3212` n `44` status `ready` deltaP `6.9951` edge `0.0031` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.3212` n `44` status `ready` deltaP `6.9951` edge `0.0031` maxDD `-0.1704`
- `risk_on_high->crypto_major_4h` score `0.1779` n `40` status `ready` deltaP `12.8963` edge `-0.0046` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.1779` n `40` status `ready` deltaP `12.8963` edge `-0.0046` maxDD `-2.6576`
- `risk_on_high->crypto_major_1h` score `-0.0032` n `44` status `ready` deltaP `6.8999` edge `0.0078` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `-0.0032` n `44` status `ready` deltaP `6.8999` edge `0.0078` maxDD `-2.3372`
- `risk_on_high->equity_1h` score `-0.007` n `44` status `ready` deltaP `7.5259` edge `-0.0118` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `-0.007` n `44` status `ready` deltaP `7.5259` edge `-0.0118` maxDD `-0.7834`
- `risk_on_high->fx_4h` score `-0.1003` n `40` status `ready` deltaP `6.7378` edge `0.0013` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `-0.1003` n `40` status `ready` deltaP `6.7378` edge `0.0013` maxDD `-0.3925`
- `risk_on_high->metal_4h` score `-0.1447` n `40` status `ready` deltaP `7.5915` edge `-0.0356` maxDD `-1.3516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
