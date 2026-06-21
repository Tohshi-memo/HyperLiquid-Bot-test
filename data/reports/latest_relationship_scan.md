# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-21T00:22:28.330177+00:00`
- Price records: `672`
- Market context records: `4262`
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
- `market_context_high->unknown_1h` score `27.6508` n `233` status `ready` deltaP `1.9924` edge `2.4489` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `7.8055` n `221` status `ready` deltaP `-2.0334` edge `1.207` maxDD `-35.7719`
- `market_context_high->unknown_24h` score `7.4228` n `200` status `ready` deltaP `-9.4306` edge `1.0848` maxDD `-24.2693`
- `risk_on_high->equity_4h` score `1.9077` n `44` status `ready` deltaP `31.8736` edge `-0.0488` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `1.9077` n `44` status `ready` deltaP `31.8736` edge `-0.0488` maxDD `-0.044`
- `risk_on_high->crypto_major_4h` score `0.6192` n `44` status `ready` deltaP `13.7334` edge `0.0266` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.6192` n `44` status `ready` deltaP `13.7334` edge `0.0266` maxDD `-2.6576`
- `risk_on_high->fx_1h` score `0.362` n `44` status `ready` deltaP `7.4442` edge `0.0035` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.362` n `44` status `ready` deltaP `7.4442` edge `0.0035` maxDD `-0.1704`
- `risk_on_high->commodity_24h` score `0.0604` n `40` status `ready` deltaP `-1.5625` edge `0.2436` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `0.0604` n `40` status `ready` deltaP `-1.5625` edge `0.2436` maxDD `-12.9187`
- `risk_on_high->crypto_major_1h` score `0.0178` n `44` status `ready` deltaP `7.0496` edge `0.0095` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.0178` n `44` status `ready` deltaP `7.0496` edge `0.0095` maxDD `-2.3372`
- `risk_on_high->fx_4h` score `-0.0021` n `44` status `ready` deltaP `8.1763` edge `0.0043` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `-0.0021` n `44` status `ready` deltaP `8.1763` edge `0.0043` maxDD `-0.3925`
- `risk_on_high->metal_24h` score `-0.0244` n `40` status `ready` deltaP `-25.3819` edge `0.2275` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `-0.0244` n `40` status `ready` deltaP `-25.3819` edge `0.2275` maxDD `-1.9133`
- `risk_on_high->equity_1h` score `-0.1377` n `44` status `ready` deltaP `6.478` edge `-0.0157` maxDD `-0.7834`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
