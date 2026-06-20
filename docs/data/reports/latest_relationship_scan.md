# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-20T14:52:29.745119+00:00`
- Price records: `672`
- Market context records: `4218`
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

- `risk_on_high->unknown_4h` score `145.8293` n `40` status `ready` deltaP `-6.6768` edge `12.3788` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `145.8293` n `40` status `ready` deltaP `-6.6768` edge `12.3788` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `30.3401` n `216` status `ready` deltaP `1.1089` edge `2.6789` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `9.3711` n `208` status `ready` deltaP `-3.1191` edge `1.3447` maxDD `-35.7719`
- `market_context_high->unknown_24h` score `7.499` n `197` status `ready` deltaP `-12.2125` edge `1.1097` maxDD `-24.2693`
- `risk_on_high->commodity_24h` score `2.4471` n `40` status `ready` deltaP `4.346` edge `0.4031` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `2.4471` n `40` status `ready` deltaP `4.346` edge `0.4031` maxDD `-12.9187`
- `risk_on_high->equity_4h` score `1.9781` n `40` status `ready` deltaP `32.4085` edge `-0.0465` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `1.9781` n `40` status `ready` deltaP `32.4085` edge `-0.0465` maxDD `-0.044`
- `risk_on_high->crypto_major_4h` score `0.3706` n `40` status `ready` deltaP `13.5061` edge `0.0074` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.3706` n `40` status `ready` deltaP `13.5061` edge `0.0074` maxDD `-2.6576`
- `risk_on_high->fx_1h` score `0.2391` n `43` status `ready` deltaP `6.0437` edge `0.0026` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.2391` n `43` status `ready` deltaP `6.0437` edge `0.0026` maxDD `-0.1704`
- `risk_on_high->metal_4h` score `-0.0271` n `40` status `ready` deltaP `8.3537` edge `-0.0256` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `-0.0271` n `40` status `ready` deltaP `8.3537` edge `-0.0256` maxDD `-1.3516`
- `risk_on_high->equity_1h` score `-0.0586` n `43` status `ready` deltaP `7.3319` edge `-0.0148` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `-0.0586` n `43` status `ready` deltaP `7.3319` edge `-0.0148` maxDD `-0.7834`
- `risk_on_high->fx_4h` score `-0.0639` n `40` status `ready` deltaP `7.3476` edge `0.0019` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `-0.0639` n `40` status `ready` deltaP `7.3476` edge `0.0019` maxDD `-0.3925`
- `risk_on_high->crypto_major_1h` score `-0.1261` n `43` status `ready` deltaP `6.8027` edge `-0.0073` maxDD `-2.3372`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
