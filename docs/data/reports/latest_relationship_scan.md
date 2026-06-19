# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-19T17:07:29.577509+00:00`
- Price records: `672`
- Market context records: `4121`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10016`

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

- `risk_on_high->unknown_4h` score `145.4061` n `40` status `ready` deltaP `-8.8174` edge `12.3578` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `145.4061` n `40` status `ready` deltaP `-8.8174` edge `12.3578` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `39.5994` n `198` status `ready` deltaP `1.4547` edge `3.4482` maxDD `-9.6361`
- `market_context_high->unknown_24h` score `14.3441` n `198` status `ready` deltaP `-9.9437` edge `1.665` maxDD `-24.2693`
- `market_context_high->unknown_4h` score `11.3965` n `198` status `ready` deltaP `-2.176` edge `1.5072` maxDD `-35.7719`
- `risk_on_high->equity_4h` score `2.796` n `40` status `ready` deltaP `36.5719` edge `-0.0061` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `2.796` n `40` status `ready` deltaP `36.5719` edge `-0.0061` maxDD `-0.044`
- `risk_on_high->crypto_major_4h` score `1.6764` n `40` status `ready` deltaP `18.4581` edge `0.0832` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.6764` n `40` status `ready` deltaP `18.4581` edge `0.0832` maxDD `-2.6576`
- `risk_on_high->metal_4h` score `0.5147` n `40` status `ready` deltaP `11.3623` edge `0.0238` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.5147` n `40` status `ready` deltaP `11.3623` edge `0.0238` maxDD `-1.3516`
- `risk_on_high->equity_1h` score `0.2639` n `40` status `ready` deltaP `10.9132` edge `-0.0118` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.2639` n `40` status `ready` deltaP `10.9132` edge `-0.0118` maxDD `-0.7834`
- `risk_on_high->crypto_major_1h` score `0.221` n `40` status `ready` deltaP `10.9581` edge `0.0095` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.221` n `40` status `ready` deltaP `10.9581` edge `0.0095` maxDD `-2.3372`
- `risk_on_high->metal_24h` score `0.2039` n `40` status `ready` deltaP `-19.6257` edge `0.2184` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `0.2039` n `40` status `ready` deltaP `-19.6257` edge `0.2184` maxDD `-1.9133`
- `risk_on_high->fx_4h` score `0.0756` n `40` status `ready` deltaP `9.8952` edge `0.0028` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.0756` n `40` status `ready` deltaP `9.8952` edge `0.0028` maxDD `-0.3925`
- `risk_on_high->fx_1h` score `0.035` n `40` status `ready` deltaP `3.9521` edge `0.0011` maxDD `-0.1704`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
