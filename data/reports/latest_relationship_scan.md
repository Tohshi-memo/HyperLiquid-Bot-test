# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-20T16:22:31.171510+00:00`
- Price records: `672`
- Market context records: `4225`
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
- `market_context_high->unknown_4h` score `9.1058` n `209` status `ready` deltaP `-3.3901` edge `1.3244` maxDD `-35.7719`
- `market_context_high->unknown_24h` score `6.9198` n `197` status `ready` deltaP `-12.3881` edge `1.0626` maxDD `-24.2693`
- `risk_on_high->commodity_24h` score `2.2904` n `40` status `ready` deltaP `3.9931` edge `0.3924` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `2.2904` n `40` status `ready` deltaP `3.9931` edge `0.3924` maxDD `-12.9187`
- `risk_on_high->equity_4h` score `1.7479` n `40` status `ready` deltaP `31.6463` edge `-0.0606` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `1.7479` n `40` status `ready` deltaP `31.6463` edge `-0.0606` maxDD `-0.044`
- `risk_on_high->fx_1h` score `0.3093` n `44` status `ready` deltaP `6.8454` edge `0.0031` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.3093` n `44` status `ready` deltaP `6.8454` edge `0.0031` maxDD `-0.1704`
- `risk_on_high->crypto_major_4h` score `0.1623` n `40` status `ready` deltaP `12.8963` edge `-0.0059` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.1623` n `40` status `ready` deltaP `12.8963` edge `-0.0059` maxDD `-2.6576`
- `risk_on_high->crypto_major_1h` score `0.01` n `44` status `ready` deltaP `7.0496` edge `0.0085` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.01` n `44` status `ready` deltaP `7.0496` edge `0.0085` maxDD `-2.3372`
- `risk_on_high->equity_1h` score `-0.0106` n `44` status `ready` deltaP `7.5259` edge `-0.0121` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `-0.0106` n `44` status `ready` deltaP `7.5259` edge `-0.0121` maxDD `-0.7834`
- `risk_on_high->fx_4h` score `-0.1097` n `40` status `ready` deltaP `6.5854` edge `0.0011` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `-0.1097` n `40` status `ready` deltaP `6.5854` edge `0.0011` maxDD `-0.3925`
- `risk_on_high->metal_4h` score `-0.1675` n `40` status `ready` deltaP `7.439` edge `-0.0375` maxDD `-1.3516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
