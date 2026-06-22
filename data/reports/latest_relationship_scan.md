# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-22T02:52:26.813424+00:00`
- Price records: `672`
- Market context records: `4376`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11143`

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

- `risk_on_high->unknown_4h` score `132.6232` n `44` status `ready` deltaP `-1.5937` edge `11.2444` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `132.6232` n `44` status `ready` deltaP `-1.5937` edge `11.2444` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `35.1592` n `213` status `ready` deltaP `3.3229` edge `3.0574` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `11.2202` n `213` status `ready` deltaP `3.2399` edge `1.4564` maxDD `-35.7719`
- `risk_on_high->equity_4h` score `3.2202` n `44` status `ready` deltaP `35.3797` edge `0.0372` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `3.2202` n `44` status `ready` deltaP `35.3797` edge `0.0372` maxDD `-0.044`
- `risk_on_high->metal_24h` score `2.9232` n `44` status `ready` deltaP `-15.183` edge `0.5374` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `2.9232` n `44` status `ready` deltaP `-15.183` edge `0.5374` maxDD `-1.9133`
- `risk_on_high->equity_24h` score `1.6474` n `44` status `ready` deltaP `19.6181` edge `0.0065` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.6474` n `44` status `ready` deltaP `19.6181` edge `0.0065` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `1.6377` n `44` status `ready` deltaP `17.2395` edge `0.0881` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.6377` n `44` status `ready` deltaP `17.2395` edge `0.0881` maxDD `-2.6576`
- `risk_on_high->index_24h` score `0.917` n `44` status `ready` deltaP `21.5278` edge `-0.0671` maxDD `0.0`
- `risk_on_and_context->index_24h` score `0.917` n `44` status `ready` deltaP `21.5278` edge `-0.0671` maxDD `0.0`
- `risk_on_high->fx_1h` score `0.4901` n `44` status `ready` deltaP `9.0909` edge `0.0032` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.4901` n `44` status `ready` deltaP `9.0909` edge `0.0032` maxDD `-0.1704`
- `risk_on_high->equity_1h` score `0.3779` n `44` status `ready` deltaP `9.3223` edge `0.0083` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.3779` n `44` status `ready` deltaP `9.3223` edge `0.0083` maxDD `-0.7834`
- `risk_on_high->metal_4h` score `0.3264` n `44` status `ready` deltaP `6.1807` edge `0.0342` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.3264` n `44` status `ready` deltaP `6.1807` edge `0.0342` maxDD `-1.3516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
