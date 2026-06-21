# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-21T12:00:28.808942+00:00`
- Price records: `672`
- Market context records: `4310`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10730`

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

- `risk_on_high->unknown_4h` score `130.683` n `44` status `ready` deltaP `-1.4413` edge `11.0817` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `130.683` n `44` status `ready` deltaP `-1.4413` edge `11.0817` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `27.9649` n `236` status `ready` deltaP `3.8035` edge `2.463` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `9.0396` n `236` status `ready` deltaP `1.6019` edge `1.2856` maxDD `-35.7719`
- `market_context_high->unknown_24h` score `5.7958` n `208` status `ready` deltaP `-7.7323` edge `0.9379` maxDD `-24.2693`
- `risk_on_high->metal_24h` score `2.1706` n `40` status `ready` deltaP `-19.3056` edge `0.4684` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `2.1706` n `40` status `ready` deltaP `-19.3056` edge `0.4684` maxDD `-1.9133`
- `risk_on_high->equity_4h` score `2.0551` n `44` status `ready` deltaP `30.8066` edge `-0.0294` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `2.0551` n `44` status `ready` deltaP `30.8066` edge `-0.0294` maxDD `-0.044`
- `risk_on_high->equity_24h` score `1.7805` n `40` status `ready` deltaP `22.9167` edge `-0.0044` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.7805` n `40` status `ready` deltaP `22.9167` edge `-0.0044` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `1.2431` n `44` status `ready` deltaP `16.4773` edge `0.0603` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.2431` n `44` status `ready` deltaP `16.4773` edge `0.0603` maxDD `-2.6576`
- `risk_on_high->fx_1h` score `0.4027` n `44` status `ready` deltaP `8.043` edge `0.0029` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.4027` n `44` status `ready` deltaP `8.043` edge `0.0029` maxDD `-0.1704`
- `risk_on_high->crypto_major_1h` score `0.197` n `44` status `ready` deltaP `8.5466` edge `0.0225` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.197` n `44` status `ready` deltaP `8.5466` edge `0.0225` maxDD `-2.3372`
- `risk_on_high->fx_4h` score `-0.0161` n `44` status `ready` deltaP `8.1763` edge `0.0025` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `-0.0161` n `44` status `ready` deltaP `8.1763` edge `0.0025` maxDD `-0.3925`
- `risk_on_high->equity_1h` score `-0.0297` n `44` status `ready` deltaP `6.9271` edge `-0.0097` maxDD `-0.7834`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
