# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-20T21:22:25.135149+00:00`
- Price records: `672`
- Market context records: `4247`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10368`

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

- `risk_on_high->unknown_4h` score `130.7052` n `44` status `ready` deltaP `-3.7279` edge `11.0988` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `130.7052` n `44` status `ready` deltaP `-3.7279` edge `11.0988` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `28.5748` n `221` status `ready` deltaP `0.9132` edge `2.5331` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `7.4691` n `219` status `ready` deltaP `-2.5344` edge `1.1823` maxDD `-35.7719`
- `market_context_high->unknown_24h` score `6.5519` n `200` status `ready` deltaP `-11.1667` edge `1.0238` maxDD `-24.2693`
- `risk_on_high->equity_4h` score `1.8237` n `44` status `ready` deltaP `31.8736` edge `-0.0558` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `1.8237` n `44` status `ready` deltaP `31.8736` edge `-0.0558` maxDD `-0.044`
- `risk_on_high->commodity_24h` score `0.9087` n `40` status `ready` deltaP `0.5208` edge `0.3004` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `0.9087` n `40` status `ready` deltaP `0.5208` edge `0.3004` maxDD `-12.9187`
- `risk_on_high->crypto_major_4h` score `0.5232` n `44` status `ready` deltaP `13.7334` edge `0.0186` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.5232` n `44` status `ready` deltaP `13.7334` edge `0.0186` maxDD `-2.6576`
- `risk_on_high->fx_1h` score `0.3069` n `44` status `ready` deltaP `6.8454` edge `0.0029` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.3069` n `44` status `ready` deltaP `6.8454` edge `0.0029` maxDD `-0.1704`
- `risk_on_high->fx_4h` score `0.013` n `44` status `ready` deltaP `8.4811` edge `0.0042` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.013` n `44` status `ready` deltaP `8.4811` edge `0.0042` maxDD `-0.3925`
- `risk_on_high->crypto_major_1h` score `0.0069` n `44` status `ready` deltaP `7.0496` edge `0.0081` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.0069` n `44` status `ready` deltaP `7.0496` edge `0.0081` maxDD `-2.3372`
- `risk_on_high->equity_1h` score `-0.1473` n `44` status `ready` deltaP `6.7774` edge `-0.0185` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `-0.1473` n `44` status `ready` deltaP `6.7774` edge `-0.0185` maxDD `-0.7834`
- `risk_on_high->metal_4h` score `-0.3977` n `44` status `ready` deltaP `3.1319` edge `-0.0383` maxDD `-1.3516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
