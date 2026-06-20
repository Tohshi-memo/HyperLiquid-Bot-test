# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-20T20:22:30.661825+00:00`
- Price records: `672`
- Market context records: `4243`
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

- `risk_on_high->unknown_4h` score `130.6692` n `44` status `ready` deltaP `-3.7279` edge `11.0958` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `130.6692` n `44` status `ready` deltaP `-3.7279` edge `11.0958` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `29.2076` n `219` status `ready` deltaP `1.0227` edge `2.5851` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `7.5945` n `218` status `ready` deltaP `-2.7062` edge `1.1939` maxDD `-35.7719`
- `market_context_high->unknown_24h` score `6.3237` n `200` status `ready` deltaP `-11.5139` edge `1.0071` maxDD `-24.2693`
- `risk_on_high->equity_4h` score `1.7589` n `44` status `ready` deltaP `31.8736` edge `-0.0612` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `1.7589` n `44` status `ready` deltaP `31.8736` edge `-0.0612` maxDD `-0.044`
- `risk_on_high->commodity_24h` score `1.2318` n `40` status `ready` deltaP `1.2153` edge `0.3227` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `1.2318` n `40` status `ready` deltaP `1.2153` edge `0.3227` maxDD `-12.9187`
- `risk_on_high->crypto_major_4h` score `0.4076` n `44` status `ready` deltaP `13.4285` edge `0.011` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.4076` n `44` status `ready` deltaP `13.4285` edge `0.011` maxDD `-2.6576`
- `risk_on_high->fx_1h` score `0.2697` n `44` status `ready` deltaP `6.3963` edge `0.0028` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.2697` n `44` status `ready` deltaP `6.3963` edge `0.0028` maxDD `-0.1704`
- `risk_on_high->fx_4h` score `-0.017` n `44` status `ready` deltaP `8.0238` edge `0.0034` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `-0.017` n `44` status `ready` deltaP `8.0238` edge `0.0034` maxDD `-0.3925`
- `risk_on_high->crypto_major_1h` score `-0.0181` n `44` status `ready` deltaP `6.8999` edge `0.0059` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `-0.0181` n `44` status `ready` deltaP `6.8999` edge `0.0059` maxDD `-2.3372`
- `risk_on_high->equity_1h` score `-0.1701` n `44` status `ready` deltaP `6.7774` edge `-0.0204` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `-0.1701` n `44` status `ready` deltaP `6.7774` edge `-0.0204` maxDD `-0.7834`
- `market_context_high->fx_1h` score `-0.4318` n `219` status `ready` deltaP `0.2734` edge `-0.0013` maxDD `-1.1377`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
