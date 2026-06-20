# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-20T19:52:28.863199+00:00`
- Price records: `672`
- Market context records: `4241`
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

- `risk_on_high->unknown_4h` score `130.6244` n `44` status `ready` deltaP `-4.0327` edge `11.0941` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `130.6244` n `44` status `ready` deltaP `-4.0327` edge `11.0941` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `29.2784` n `219` status `ready` deltaP `1.0227` edge `2.591` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `7.7563` n `217` status `ready` deltaP `-2.7235` edge `1.2075` maxDD `-35.7719`
- `market_context_high->unknown_24h` score `6.1927` n `200` status `ready` deltaP `-11.8611` edge `0.9985` maxDD `-24.2693`
- `risk_on_high->equity_4h` score `1.7397` n `44` status `ready` deltaP `31.8736` edge `-0.0628` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `1.7397` n `44` status `ready` deltaP `31.8736` edge `-0.0628` maxDD `-0.044`
- `risk_on_high->commodity_24h` score `1.3892` n `40` status `ready` deltaP `1.5625` edge `0.3335` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `1.3892` n `40` status `ready` deltaP `1.5625` edge `0.3335` maxDD `-12.9187`
- `risk_on_high->crypto_major_4h` score `0.3208` n `44` status `ready` deltaP `13.1236` edge `0.0058` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.3208` n `44` status `ready` deltaP `13.1236` edge `0.0058` maxDD `-2.6576`
- `risk_on_high->fx_1h` score `0.2566` n `44` status `ready` deltaP `6.2466` edge `0.0027` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.2566` n `44` status `ready` deltaP `6.2466` edge `0.0027` maxDD `-0.1704`
- `risk_on_high->crypto_major_1h` score `-0.0251` n `44` status `ready` deltaP `6.8999` edge `0.005` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `-0.0251` n `44` status `ready` deltaP `6.8999` edge `0.005` maxDD `-2.3372`
- `risk_on_high->fx_4h` score `-0.0375` n `44` status `ready` deltaP `7.7189` edge `0.0028` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `-0.0375` n `44` status `ready` deltaP `7.7189` edge `0.0028` maxDD `-0.3925`
- `risk_on_high->equity_1h` score `-0.133` n `44` status `ready` deltaP `7.0768` edge `-0.0193` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `-0.133` n `44` status `ready` deltaP `7.0768` edge `-0.0193` maxDD `-0.7834`
- `market_context_high->fx_1h` score `-0.4404` n `219` status `ready` deltaP `0.1237` edge `-0.0014` maxDD `-1.1377`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
