# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-21T01:52:25.285889+00:00`
- Price records: `672`
- Market context records: `4268`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10816`

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

- `risk_on_high->unknown_4h` score `131.4144` n `44` status `ready` deltaP `-2.8132` edge `11.1518` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `131.4144` n `44` status `ready` deltaP `-2.8132` edge `11.1518` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `27.8187` n `236` status `ready` deltaP `2.4562` edge `2.4598` maxDD `-9.6361`
- `market_context_high->unknown_24h` score `7.702` n `200` status `ready` deltaP `-8.9097` edge `1.1046` maxDD `-24.2693`
- `market_context_high->unknown_4h` score `7.0085` n `227` status `ready` deltaP `-1.1812` edge `1.1349` maxDD `-35.7719`
- `risk_on_high->equity_4h` score `1.9833` n `44` status `ready` deltaP `31.8736` edge `-0.0425` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `1.9833` n `44` status `ready` deltaP `31.8736` edge `-0.0425` maxDD `-0.044`
- `risk_on_high->crypto_major_4h` score `0.6492` n `44` status `ready` deltaP `13.7334` edge `0.0291` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.6492` n `44` status `ready` deltaP `13.7334` edge `0.0291` maxDD `-2.6576`
- `risk_on_high->fx_1h` score `0.3847` n `44` status `ready` deltaP `7.7436` edge `0.0034` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.3847` n `44` status `ready` deltaP `7.7436` edge `0.0034` maxDD `-0.1704`
- `risk_on_high->metal_24h` score `0.323` n `40` status `ready` deltaP `-24.3403` edge `0.2651` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `0.323` n `40` status `ready` deltaP `-24.3403` edge `0.2651` maxDD `-1.9133`
- `risk_on_high->crypto_major_1h` score `0.0778` n `44` status `ready` deltaP `7.4987` edge `0.0142` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.0778` n `44` status `ready` deltaP `7.4987` edge `0.0142` maxDD `-2.3372`
- `risk_on_high->fx_4h` score `0.0177` n `44` status `ready` deltaP `8.4811` edge `0.0048` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.0177` n `44` status `ready` deltaP `8.4811` edge `0.0048` maxDD `-0.3925`
- `risk_on_high->equity_1h` score `-0.0621` n `44` status `ready` deltaP `6.9271` edge `-0.0124` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `-0.0621` n `44` status `ready` deltaP `6.9271` edge `-0.0124` maxDD `-0.7834`
- `risk_on_high->equity_24h` score `-0.2139` n `40` status `ready` deltaP `22.9167` edge `-0.1706` maxDD `0.0`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
