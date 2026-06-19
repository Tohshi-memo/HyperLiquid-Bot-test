# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-19T19:37:30.998615+00:00`
- Price records: `672`
- Market context records: `4133`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10024`

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

- `risk_on_high->unknown_4h` score `144.8958` n `40` status `ready` deltaP `-9.8252` edge `12.322` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `144.8958` n `40` status `ready` deltaP `-9.8252` edge `12.322` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `38.0462` n `202` status `ready` deltaP `1.2406` edge `3.3202` maxDD `-9.6361`
- `market_context_high->unknown_24h` score `13.0281` n `198` status `ready` deltaP `-11.1541` edge `1.5634` maxDD `-24.2693`
- `market_context_high->unknown_4h` score `10.8863` n `198` status `ready` deltaP `-3.1838` edge `1.4714` maxDD `-35.7719`
- `risk_on_high->equity_4h` score `2.685` n `40` status `ready` deltaP `35.9498` edge `-0.0112` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `2.685` n `40` status `ready` deltaP `35.9498` edge `-0.0112` maxDD `-0.044`
- `risk_on_high->crypto_major_4h` score `1.4523` n `40` status `ready` deltaP `17.6368` edge `0.07` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.4523` n `40` status `ready` deltaP `17.6368` edge `0.07` maxDD `-2.6576`
- `risk_on_high->metal_4h` score `0.3752` n `40` status `ready` deltaP `10.5091` edge `0.0116` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.3752` n `40` status `ready` deltaP `10.5091` edge `0.0116` maxDD `-1.3516`
- `risk_on_high->equity_1h` score `0.2771` n `40` status `ready` deltaP `11.0629` edge `-0.0117` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.2771` n `40` status `ready` deltaP `11.0629` edge `-0.0117` maxDD `-0.7834`
- `risk_on_high->crypto_major_1h` score `0.2015` n `40` status `ready` deltaP `10.9581` edge `0.007` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.2015` n `40` status `ready` deltaP `10.9581` edge `0.007` maxDD `-2.3372`
- `risk_on_high->fx_4h` score `0.0397` n `40` status `ready` deltaP `9.3237` edge `0.002` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.0397` n `40` status `ready` deltaP `9.3237` edge `0.002` maxDD `-0.3925`
- `risk_on_high->fx_1h` score `0.0093` n `40` status `ready` deltaP `3.503` edge `0.0008` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.0093` n `40` status `ready` deltaP `3.503` edge `0.0008` maxDD `-0.1704`
- `risk_on_high->commodity_24h` score `-0.0072` n `40` status `ready` deltaP `-1.7477` edge `0.2392` maxDD `-12.9187`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
