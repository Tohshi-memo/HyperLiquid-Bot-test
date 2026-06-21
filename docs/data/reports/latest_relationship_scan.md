# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-21T00:37:31.475158+00:00`
- Price records: `672`
- Market context records: `4263`
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

- `risk_on_high->unknown_4h` score `131.4746` n `44` status `ready` deltaP `-2.6608` edge `11.1558` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `131.4746` n `44` status `ready` deltaP `-2.6608` edge `11.1558` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `27.3944` n `234` status `ready` deltaP `2.1483` edge `2.4265` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `7.6536` n `222` status `ready` deltaP `-1.8622` edge `1.1932` maxDD `-35.7719`
- `market_context_high->unknown_24h` score `7.4907` n `200` status `ready` deltaP `-9.2569` edge `1.0893` maxDD `-24.2693`
- `risk_on_high->equity_4h` score `1.9209` n `44` status `ready` deltaP `31.8736` edge `-0.0477` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `1.9209` n `44` status `ready` deltaP `31.8736` edge `-0.0477` maxDD `-0.044`
- `risk_on_high->crypto_major_4h` score `0.6288` n `44` status `ready` deltaP `13.7334` edge `0.0274` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.6288` n `44` status `ready` deltaP `13.7334` edge `0.0274` maxDD `-2.6576`
- `risk_on_high->fx_1h` score `0.3608` n `44` status `ready` deltaP `7.4442` edge `0.0034` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.3608` n `44` status `ready` deltaP `7.4442` edge `0.0034` maxDD `-0.1704`
- `risk_on_high->crypto_major_1h` score `0.0357` n `44` status `ready` deltaP `7.1993` edge `0.0108` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.0357` n `44` status `ready` deltaP `7.1993` edge `0.0108` maxDD `-2.3372`
- `risk_on_high->metal_24h` score `0.0353` n `40` status `ready` deltaP `-25.2083` edge `0.234` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `0.0353` n `40` status `ready` deltaP `-25.2083` edge `0.234` maxDD `-1.9133`
- `risk_on_high->fx_4h` score `-0.0021` n `44` status `ready` deltaP `8.1763` edge `0.0043` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `-0.0021` n `44` status `ready` deltaP `8.1763` edge `0.0043` maxDD `-0.3925`
- `risk_on_high->commodity_24h` score `-0.0087` n `40` status `ready` deltaP `-1.7361` edge `0.239` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `-0.0087` n `40` status `ready` deltaP `-1.7361` edge `0.239` maxDD `-12.9187`
- `risk_on_high->equity_1h` score `-0.1161` n `44` status `ready` deltaP `6.6277` edge `-0.0149` maxDD `-0.7834`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
