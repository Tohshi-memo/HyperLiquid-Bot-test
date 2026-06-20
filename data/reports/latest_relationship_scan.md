# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-20T13:37:25.252023+00:00`
- Price records: `672`
- Market context records: `4213`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9632`

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

- `risk_on_high->unknown_4h` score `145.7199` n `40` status `ready` deltaP `-6.8293` edge `12.3707` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `145.7199` n `40` status `ready` deltaP `-6.8293` edge `12.3707` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `31.6698` n `212` status `ready` deltaP `1.8303` edge `2.7849` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `9.0403` n `209` status `ready` deltaP `-3.5637` edge `1.3201` maxDD `-35.7719`
- `market_context_high->unknown_24h` score `7.5193` n `198` status `ready` deltaP `-12.2143` edge `1.1114` maxDD `-24.2693`
- `risk_on_high->commodity_24h` score `2.4588` n `40` status `ready` deltaP `4.5222` edge `0.4029` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `2.4588` n `40` status `ready` deltaP `4.5222` edge `0.4029` maxDD `-12.9187`
- `risk_on_high->equity_4h` score `2.0921` n `40` status `ready` deltaP `32.4085` edge `-0.037` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `2.0921` n `40` status `ready` deltaP `32.4085` edge `-0.037` maxDD `-0.044`
- `risk_on_high->crypto_major_4h` score `0.4884` n `40` status `ready` deltaP `13.6585` edge `0.0162` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.4884` n `40` status `ready` deltaP `13.6585` edge `0.0162` maxDD `-2.6576`
- `risk_on_high->equity_1h` score `0.1345` n `40` status `ready` deltaP `9.7156` edge `-0.0146` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.1345` n `40` status `ready` deltaP `9.7156` edge `-0.0146` maxDD `-0.7834`
- `risk_on_high->crypto_major_1h` score `0.059` n `40` status `ready` deltaP `9.1617` edge `0.0007` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.059` n `40` status `ready` deltaP `9.1617` edge `0.0007` maxDD `-2.3372`
- `risk_on_high->metal_4h` score `0.0565` n `40` status `ready` deltaP `8.5061` edge `-0.0159` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.0565` n `40` status `ready` deltaP `8.5061` edge `-0.0159` maxDD `-1.3516`
- `risk_on_high->fx_1h` score `-0.0149` n `40` status `ready` deltaP `3.0539` edge `0.0007` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `-0.0149` n `40` status `ready` deltaP `3.0539` edge `0.0007` maxDD `-0.1704`
- `risk_on_high->fx_4h` score `-0.029` n `40` status `ready` deltaP `7.9573` edge `0.0023` maxDD `-0.3925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
