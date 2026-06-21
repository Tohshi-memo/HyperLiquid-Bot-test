# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-21T02:07:25.882653+00:00`
- Price records: `672`
- Market context records: `4269`
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

- `risk_on_high->unknown_4h` score `131.3964` n `44` status `ready` deltaP `-2.8132` edge `11.1503` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `131.3964` n `44` status `ready` deltaP `-2.8132` edge `11.1503` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `27.8043` n `236` status `ready` deltaP `2.3065` edge `2.4596` maxDD `-9.6361`
- `market_context_high->unknown_24h` score `7.7164` n `200` status `ready` deltaP `-8.9097` edge `1.1058` maxDD `-24.2693`
- `market_context_high->unknown_4h` score `6.9015` n `228` status `ready` deltaP `-1.0189` edge `1.1249` maxDD `-35.7719`
- `risk_on_high->equity_4h` score `1.9977` n `44` status `ready` deltaP `31.8736` edge `-0.0413` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `1.9977` n `44` status `ready` deltaP `31.8736` edge `-0.0413` maxDD `-0.044`
- `risk_on_high->crypto_major_4h` score `0.6552` n `44` status `ready` deltaP `13.7334` edge `0.0296` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.6552` n `44` status `ready` deltaP `13.7334` edge `0.0296` maxDD `-2.6576`
- `risk_on_high->fx_1h` score `0.3967` n `44` status `ready` deltaP `7.8933` edge `0.0034` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.3967` n `44` status `ready` deltaP `7.8933` edge `0.0034` maxDD `-0.1704`
- `risk_on_high->metal_24h` score `0.3742` n `40` status `ready` deltaP `-24.1667` edge `0.2705` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `0.3742` n `40` status `ready` deltaP `-24.1667` edge `0.2705` maxDD `-1.9133`
- `risk_on_high->crypto_major_1h` score `0.0786` n `44` status `ready` deltaP `7.4987` edge `0.0143` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.0786` n `44` status `ready` deltaP `7.4987` edge `0.0143` maxDD `-2.3372`
- `risk_on_high->fx_4h` score `0.0264` n `44` status `ready` deltaP `8.6336` edge `0.0049` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.0264` n `44` status `ready` deltaP `8.6336` edge `0.0049` maxDD `-0.3925`
- `risk_on_high->equity_1h` score `-0.0597` n `44` status `ready` deltaP `6.9271` edge `-0.0122` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `-0.0597` n `44` status `ready` deltaP `6.9271` edge `-0.0122` maxDD `-0.7834`
- `risk_on_high->equity_24h` score `-0.1479` n `40` status `ready` deltaP `22.9167` edge `-0.1651` maxDD `0.0`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
