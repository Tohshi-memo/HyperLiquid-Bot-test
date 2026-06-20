# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-20T23:52:30.238281+00:00`
- Price records: `672`
- Market context records: `4259`
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

- `risk_on_high->unknown_4h` score `131.3686` n `44` status `ready` deltaP `-2.9657` edge `11.149` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `131.3686` n `44` status `ready` deltaP `-2.9657` edge `11.149` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `28.1739` n `231` status `ready` deltaP `1.6766` edge `2.4946` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `8.1324` n `219` status `ready` deltaP `-1.7722` edge `1.2325` maxDD `-35.7719`
- `market_context_high->unknown_24h` score `7.2726` n `200` status `ready` deltaP `-9.7778` edge `1.0746` maxDD `-24.2693`
- `risk_on_high->equity_4h` score `1.8789` n `44` status `ready` deltaP `31.8736` edge `-0.0512` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `1.8789` n `44` status `ready` deltaP `31.8736` edge `-0.0512` maxDD `-0.044`
- `risk_on_high->crypto_major_4h` score `0.5868` n `44` status `ready` deltaP `13.7334` edge `0.0239` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.5868` n `44` status `ready` deltaP `13.7334` edge `0.0239` maxDD `-2.6576`
- `risk_on_high->fx_1h` score `0.3608` n `44` status `ready` deltaP `7.4442` edge `0.0034` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.3608` n `44` status `ready` deltaP `7.4442` edge `0.0034` maxDD `-0.1704`
- `risk_on_high->commodity_24h` score `0.1974` n `40` status `ready` deltaP `-1.2153` edge `0.2527` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `0.1974` n `40` status `ready` deltaP `-1.2153` edge `0.2527` maxDD `-12.9187`
- `risk_on_high->fx_4h` score `-0.0036` n `44` status `ready` deltaP `8.1763` edge `0.0041` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `-0.0036` n `44` status `ready` deltaP `8.1763` edge `0.0041` maxDD `-0.3925`
- `risk_on_high->crypto_major_1h` score `-0.0095` n `44` status `ready` deltaP `6.7502` edge `0.008` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `-0.0095` n `44` status `ready` deltaP `6.7502` edge `0.008` maxDD `-2.3372`
- `risk_on_high->metal_24h` score `-0.1298` n `40` status `ready` deltaP `-25.7292` edge `0.2163` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `-0.1298` n `40` status `ready` deltaP `-25.7292` edge `0.2163` maxDD `-1.9133`
- `risk_on_high->equity_1h` score `-0.1712` n `44` status `ready` deltaP `6.1786` edge `-0.0165` maxDD `-0.7834`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
