# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-20T22:54:46.664390+00:00`
- Price records: `672`
- Market context records: `4255`
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

- `risk_on_high->unknown_4h` score `131.0202` n `44` status `ready` deltaP `-3.2705` edge `11.122` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `131.0202` n `44` status `ready` deltaP `-3.2705` edge `11.122` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `26.8996` n `227` status `ready` deltaP `1.9178` edge `2.3868` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `7.7841` n `219` status `ready` deltaP `-2.077` edge `1.2055` maxDD `-35.7719`
- `market_context_high->unknown_24h` score `6.977` n `200` status `ready` deltaP `-10.4722` edge `1.0546` maxDD `-24.2693`
- `risk_on_high->equity_4h` score `1.8933` n `44` status `ready` deltaP `31.8736` edge `-0.05` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `1.8933` n `44` status `ready` deltaP `31.8736` edge `-0.05` maxDD `-0.044`
- `risk_on_high->crypto_major_4h` score `0.6024` n `44` status `ready` deltaP `13.7334` edge `0.0252` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.6024` n `44` status `ready` deltaP `13.7334` edge `0.0252` maxDD `-2.6576`
- `risk_on_high->commodity_24h` score `0.4713` n `40` status `ready` deltaP `-0.5208` edge `0.2709` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `0.4713` n `40` status `ready` deltaP `-0.5208` edge `0.2709` maxDD `-12.9187`
- `risk_on_high->fx_1h` score `0.3368` n `44` status `ready` deltaP `7.1448` edge `0.0034` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.3368` n `44` status `ready` deltaP `7.1448` edge `0.0034` maxDD `-0.1704`
- `risk_on_high->fx_4h` score `0.0312` n `44` status `ready` deltaP `8.786` edge `0.0045` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.0312` n `44` status `ready` deltaP `8.786` edge `0.0045` maxDD `-0.3925`
- `risk_on_high->crypto_major_1h` score `0.0225` n `44` status `ready` deltaP `7.0496` edge `0.0101` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.0225` n `44` status `ready` deltaP `7.0496` edge `0.0101` maxDD `-2.3372`
- `risk_on_high->equity_1h` score `-0.0897` n `44` status `ready` deltaP `6.6277` edge `-0.0127` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `-0.0897` n `44` status `ready` deltaP `6.6277` edge `-0.0127` maxDD `-0.7834`
- `risk_on_high->metal_24h` score `-0.304` n `40` status `ready` deltaP `-26.4236` edge `0.1986` maxDD `-1.9133`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
