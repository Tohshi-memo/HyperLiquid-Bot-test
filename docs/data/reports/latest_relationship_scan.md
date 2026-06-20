# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-20T13:07:28.273590+00:00`
- Price records: `672`
- Market context records: `4210`
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

- `risk_on_high->unknown_4h` score `145.6679` n `40` status `ready` deltaP `-7.1341` edge `12.3684` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `145.6679` n `40` status `ready` deltaP `-7.1341` edge `12.3684` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `32.3591` n `210` status `ready` deltaP `1.8064` edge `2.8425` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `9.2277` n `208` status `ready` deltaP `-3.5764` edge `1.3358` maxDD `-35.7719`
- `market_context_high->unknown_24h` score `7.6691` n `198` status `ready` deltaP `-12.2758` edge `1.1243` maxDD `-24.2693`
- `risk_on_high->commodity_24h` score `2.4451` n `40` status `ready` deltaP `4.5918` edge `0.4013` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `2.4451` n `40` status `ready` deltaP `4.5918` edge `0.4013` maxDD `-12.9187`
- `risk_on_high->equity_4h` score `2.1173` n `40` status `ready` deltaP `32.4085` edge `-0.0349` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `2.1173` n `40` status `ready` deltaP `32.4085` edge `-0.0349` maxDD `-0.044`
- `risk_on_high->crypto_major_4h` score `0.5388` n `40` status `ready` deltaP `13.6585` edge `0.0204` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.5388` n `40` status `ready` deltaP `13.6585` edge `0.0204` maxDD `-2.6576`
- `risk_on_high->equity_1h` score `0.0926` n `40` status `ready` deltaP `9.4162` edge `-0.0161` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.0926` n `40` status `ready` deltaP `9.4162` edge `-0.0161` maxDD `-0.7834`
- `risk_on_high->metal_4h` score `0.0784` n `40` status `ready` deltaP `8.5061` edge `-0.0131` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.0784` n `40` status `ready` deltaP `8.5061` edge `-0.0131` maxDD `-1.3516`
- `risk_on_high->crypto_major_1h` score `0.0543` n `40` status `ready` deltaP `9.1617` edge `0.0001` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.0543` n `40` status `ready` deltaP `9.1617` edge `0.0001` maxDD `-2.3372`
- `risk_on_high->fx_4h` score `-0.0093` n `40` status `ready` deltaP `8.2622` edge `0.0028` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `-0.0093` n `40` status `ready` deltaP `8.2622` edge `0.0028` maxDD `-0.3925`
- `risk_on_high->fx_1h` score `-0.0156` n `40` status `ready` deltaP `3.0539` edge `0.0006` maxDD `-0.1704`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
