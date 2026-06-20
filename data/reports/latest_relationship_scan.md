# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-20T15:52:28.447043+00:00`
- Price records: `672`
- Market context records: `4223`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9808`

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

- `risk_on_high->unknown_4h` score `145.7135` n `40` status `ready` deltaP `-7.1341` edge `12.3722` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `145.7135` n `40` status `ready` deltaP `-7.1341` edge `12.3722` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `30.3448` n `216` status `ready` deltaP `1.2725` edge `2.6782` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `9.5021` n `207` status `ready` deltaP `-3.2814` edge `1.3567` maxDD `-35.7719`
- `market_context_high->unknown_24h` score `7.4679` n `196` status `ready` deltaP `-12.2413` edge `1.1073` maxDD `-24.2693`
- `risk_on_high->commodity_24h` score `2.3504` n `40` status `ready` deltaP `4.2028` edge `0.396` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `2.3504` n `40` status `ready` deltaP `4.2028` edge `0.396` maxDD `-12.9187`
- `risk_on_high->equity_4h` score `1.8189` n `40` status `ready` deltaP `31.7988` edge `-0.0557` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `1.8189` n `40` status `ready` deltaP `31.7988` edge `-0.0557` maxDD `-0.044`
- `risk_on_high->fx_1h` score `0.3344` n `44` status `ready` deltaP `7.1448` edge `0.0032` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.3344` n `44` status `ready` deltaP `7.1448` edge `0.0032` maxDD `-0.1704`
- `risk_on_high->crypto_major_4h` score `0.2055` n `40` status `ready` deltaP `12.8963` edge `-0.0023` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.2055` n `40` status `ready` deltaP `12.8963` edge `-0.0023` maxDD `-2.6576`
- `risk_on_high->equity_1h` score `0.0217` n `44` status `ready` deltaP `7.6756` edge `-0.0104` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.0217` n `44` status `ready` deltaP `7.6756` edge `-0.0104` maxDD `-0.7834`
- `risk_on_high->crypto_major_1h` score `0.0123` n `44` status `ready` deltaP `7.0496` edge `0.0088` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.0123` n `44` status `ready` deltaP `7.0496` edge `0.0088` maxDD `-2.3372`
- `risk_on_high->fx_4h` score `-0.0908` n `40` status `ready` deltaP `6.8902` edge `0.0015` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `-0.0908` n `40` status `ready` deltaP `6.8902` edge `0.0015` maxDD `-0.3925`
- `risk_on_high->metal_4h` score `-0.1157` n `40` status `ready` deltaP `7.7439` edge `-0.0329` maxDD `-1.3516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
