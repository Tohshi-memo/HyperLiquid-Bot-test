# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-20T13:22:32.774312+00:00`
- Price records: `672`
- Market context records: `4212`
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

- `risk_on_high->unknown_4h` score `145.6933` n `40` status `ready` deltaP `-6.9817` edge `12.3695` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `145.6933` n `40` status `ready` deltaP `-6.9817` edge `12.3695` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `31.9931` n `211` status `ready` deltaP `1.656` edge `2.813` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `9.0137` n `209` status `ready` deltaP `-3.7161` edge `1.3189` maxDD `-35.7719`
- `market_context_high->unknown_24h` score `7.5948` n `198` status `ready` deltaP `-12.2451` edge `1.1179` maxDD `-24.2693`
- `risk_on_high->commodity_24h` score `2.4508` n `40` status `ready` deltaP `4.5571` edge `0.402` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `2.4508` n `40` status `ready` deltaP `4.5571` edge `0.402` maxDD `-12.9187`
- `risk_on_high->equity_4h` score `2.1005` n `40` status `ready` deltaP `32.4085` edge `-0.0363` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `2.1005` n `40` status `ready` deltaP `32.4085` edge `-0.0363` maxDD `-0.044`
- `risk_on_high->crypto_major_4h` score `0.5076` n `40` status `ready` deltaP `13.6585` edge `0.0178` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.5076` n `40` status `ready` deltaP `13.6585` edge `0.0178` maxDD `-2.6576`
- `risk_on_high->equity_1h` score `0.113` n `40` status `ready` deltaP `9.5659` edge `-0.0154` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.113` n `40` status `ready` deltaP `9.5659` edge `-0.0154` maxDD `-0.7834`
- `risk_on_high->metal_4h` score `0.0682` n `40` status `ready` deltaP `8.5061` edge `-0.0144` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.0682` n `40` status `ready` deltaP `8.5061` edge `-0.0144` maxDD `-1.3516`
- `risk_on_high->crypto_major_1h` score `0.0582` n `40` status `ready` deltaP `9.1617` edge `0.0006` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.0582` n `40` status `ready` deltaP `9.1617` edge `0.0006` maxDD `-2.3372`
- `risk_on_high->fx_1h` score `-0.0156` n `40` status `ready` deltaP `3.0539` edge `0.0006` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `-0.0156` n `40` status `ready` deltaP `3.0539` edge `0.0006` maxDD `-0.1704`
- `risk_on_high->fx_4h` score `-0.0211` n `40` status `ready` deltaP `8.1098` edge `0.0023` maxDD `-0.3925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
