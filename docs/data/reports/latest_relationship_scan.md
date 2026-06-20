# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-20T12:22:25.609239+00:00`
- Price records: `672`
- Market context records: `4207`
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

- `risk_on_high->unknown_4h` score `145.5953` n `40` status `ready` deltaP `-7.5915` edge `12.3654` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `145.5953` n `40` status `ready` deltaP `-7.5915` edge `12.3654` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `32.693` n `209` status `ready` deltaP `1.7807` edge `2.8705` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `9.8734` n `205` status `ready` deltaP `-3.1403` edge `1.3867` maxDD `-35.7719`
- `market_context_high->unknown_24h` score `7.9174` n `198` status `ready` deltaP `-12.3673` edge `1.1456` maxDD `-24.2693`
- `risk_on_high->commodity_24h` score `2.4366` n `40` status `ready` deltaP `4.6954` edge `0.3999` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `2.4366` n `40` status `ready` deltaP `4.6954` edge `0.3999` maxDD `-12.9187`
- `risk_on_high->equity_4h` score `2.1845` n `40` status `ready` deltaP `32.4085` edge `-0.0293` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `2.1845` n `40` status `ready` deltaP `32.4085` edge `-0.0293` maxDD `-0.044`
- `risk_on_high->crypto_major_4h` score `0.6558` n `40` status `ready` deltaP `14.1159` edge `0.0271` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.6558` n `40` status `ready` deltaP `14.1159` edge `0.0271` maxDD `-2.6576`
- `risk_on_high->equity_1h` score `0.1382` n `40` status `ready` deltaP `9.5659` edge `-0.0133` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.1382` n `40` status `ready` deltaP `9.5659` edge `-0.0133` maxDD `-0.7834`
- `risk_on_high->metal_4h` score `0.1248` n `40` status `ready` deltaP `8.9634` edge `-0.0102` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.1248` n `40` status `ready` deltaP `8.9634` edge `-0.0102` maxDD `-1.3516`
- `risk_on_high->fx_4h` score `0.0192` n `40` status `ready` deltaP `8.7195` edge `0.0034` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.0192` n `40` status `ready` deltaP `8.7195` edge `0.0034` maxDD `-0.3925`
- `risk_on_high->crypto_major_1h` score `0.0013` n `40` status `ready` deltaP `8.7126` edge `-0.0037` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.0013` n `40` status `ready` deltaP `8.7126` edge `-0.0037` maxDD `-2.3372`
- `risk_on_high->fx_1h` score `0.0007` n `40` status `ready` deltaP `3.3533` edge `0.0007` maxDD `-0.1704`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
