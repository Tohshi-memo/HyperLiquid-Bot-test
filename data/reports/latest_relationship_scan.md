# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-20T01:52:28.153517+00:00`
- Price records: `672`
- Market context records: `4162`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10038`

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

- `risk_on_high->unknown_4h` score `144.6704` n `40` status `ready` deltaP `-10.1829` edge `12.3056` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `144.6704` n `40` status `ready` deltaP `-10.1829` edge `12.3056` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `35.3787` n `202` status `ready` deltaP `1.0909` edge `3.0989` maxDD `-9.6361`
- `market_context_high->unknown_24h` score `9.7074` n `198` status `ready` deltaP `-13.5573` edge `1.3027` maxDD `-24.2693`
- `market_context_high->unknown_4h` score `9.6713` n `202` status `ready` deltaP `-4.8116` edge `1.381` maxDD `-35.7719`
- `risk_on_high->equity_4h` score `2.2232` n `40` status `ready` deltaP `33.628` edge `-0.0342` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `2.2232` n `40` status `ready` deltaP `33.628` edge `-0.0342` maxDD `-0.044`
- `risk_on_high->commodity_24h` score `1.1854` n `40` status `ready` deltaP `1.1453` edge `0.3193` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `1.1854` n `40` status `ready` deltaP `1.1453` edge `0.3193` maxDD `-12.9187`
- `risk_on_high->crypto_major_4h` score `0.8566` n `40` status `ready` deltaP `15.3354` edge `0.0357` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.8566` n `40` status `ready` deltaP `15.3354` edge `0.0357` maxDD `-2.6576`
- `risk_on_high->equity_1h` score `0.1069` n `40` status `ready` deltaP `10.015` edge `-0.0189` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.1069` n `40` status `ready` deltaP `10.015` edge `-0.0189` maxDD `-0.7834`
- `risk_on_high->fx_4h` score `0.0944` n `40` status `ready` deltaP `10.0915` edge `0.0039` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.0944` n `40` status `ready` deltaP `10.0915` edge `0.0039` maxDD `-0.3925`
- `risk_on_high->metal_4h` score `0.0902` n `40` status `ready` deltaP `8.6585` edge `-0.0126` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.0902` n `40` status `ready` deltaP `8.6585` edge `-0.0126` maxDD `-1.3516`
- `risk_on_high->crypto_major_1h` score `0.0566` n `40` status `ready` deltaP `9.6108` edge `-0.0026` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.0566` n `40` status `ready` deltaP `9.6108` edge `-0.0026` maxDD `-2.3372`
- `risk_on_high->fx_1h` score `0.0482` n `40` status `ready` deltaP `4.2515` edge `0.0008` maxDD `-0.1704`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
