# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-20T21:52:30.740921+00:00`
- Price records: `672`
- Market context records: `4250`
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

- `risk_on_high->unknown_4h` score `130.7652` n `44` status `ready` deltaP `-3.7279` edge `11.1038` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `130.7652` n `44` status `ready` deltaP `-3.7279` edge `11.1038` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `27.9901` n `223` status `ready` deltaP `1.254` edge `2.4821` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `7.5291` n `219` status `ready` deltaP `-2.5344` edge `1.1873` maxDD `-35.7719`
- `market_context_high->unknown_24h` score `6.6587` n `200` status `ready` deltaP `-11.1667` edge `1.0327` maxDD `-24.2693`
- `risk_on_high->equity_4h` score `1.8621` n `44` status `ready` deltaP `31.8736` edge `-0.0526` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `1.8621` n `44` status `ready` deltaP `31.8736` edge `-0.0526` maxDD `-0.044`
- `risk_on_high->commodity_24h` score `0.7573` n `40` status `ready` deltaP `0.1736` edge `0.2901` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `0.7573` n `40` status `ready` deltaP `0.1736` edge `0.2901` maxDD `-12.9187`
- `risk_on_high->crypto_major_4h` score `0.5604` n `44` status `ready` deltaP `13.7334` edge `0.0217` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.5604` n `44` status `ready` deltaP `13.7334` edge `0.0217` maxDD `-2.6576`
- `risk_on_high->fx_1h` score `0.3332` n `44` status `ready` deltaP `7.1448` edge `0.0031` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.3332` n `44` status `ready` deltaP `7.1448` edge `0.0031` maxDD `-0.1704`
- `risk_on_high->fx_4h` score `0.0209` n `44` status `ready` deltaP `8.6336` edge `0.0042` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.0209` n `44` status `ready` deltaP `8.6336` edge `0.0042` maxDD `-0.3925`
- `risk_on_high->crypto_major_1h` score `0.0108` n `44` status `ready` deltaP `7.0496` edge `0.0086` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.0108` n `44` status `ready` deltaP `7.0496` edge `0.0086` maxDD `-2.3372`
- `risk_on_high->equity_1h` score `-0.1137` n `44` status `ready` deltaP `6.7774` edge `-0.0157` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `-0.1137` n `44` status `ready` deltaP `6.7774` edge `-0.0157` maxDD `-0.7834`
- `risk_on_high->metal_4h` score `-0.3592` n `44` status `ready` deltaP `3.4368` edge `-0.0354` maxDD `-1.3516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
