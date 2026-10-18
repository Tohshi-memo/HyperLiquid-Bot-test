# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T18:52:27.076807+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9294`

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

- `market_context_high->commodity_24h` score `1.9976` n `115` status `ready` deltaP `18.7826` edge `0.1264` maxDD `-1.8119`
- `market_context_high->crypto_major_4h` score `1.8261` n `116` status `ready` deltaP `20.5004` edge `0.4379` maxDD `-15.2359`
- `risk_on_high->commodity_24h` score `1.8259` n `82` status `ready` deltaP `20.8398` edge `0.093` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `1.8259` n `82` status `ready` deltaP `20.8398` edge `0.093` maxDD `-1.7154`
- `risk_on_high->crypto_major_4h` score `1.505` n `83` status `ready` deltaP `21.7675` edge `0.2959` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `1.505` n `83` status `ready` deltaP `21.7675` edge `0.2959` maxDD `-11.1788`
- `market_context_high->crypto_major_1h` score `0.5428` n `116` status `ready` deltaP `6.8966` edge `0.1125` maxDD `-3.7781`
- `risk_on_high->index_1h` score `0.3214` n `83` status `ready` deltaP `8.8643` edge `0.0061` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.3214` n `83` status `ready` deltaP `8.8643` edge `0.0061` maxDD `-0.7394`
- `risk_on_high->equity_1h` score `-0.1668` n `83` status `ready` deltaP `12.618` edge `0.0316` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.1668` n `83` status `ready` deltaP `12.618` edge `0.0316` maxDD `-5.3696`
- `market_context_high->crypto_alt_1h` score `-0.3206` n `116` status `ready` deltaP `2.3539` edge `0.0932` maxDD `-7.3329`
- `risk_on_high->crypto_major_1h` score `-0.4093` n `83` status `ready` deltaP `1.8072` edge `0.0274` maxDD `-4.6876`
- `risk_on_and_context->crypto_major_1h` score `-0.4093` n `83` status `ready` deltaP `1.8072` edge `0.0274` maxDD `-4.6876`
- `market_context_high->metal_1h` score `-0.5007` n `116` status `ready` deltaP `2.1681` edge `0.0083` maxDD `-0.9556`
- `market_context_high->index_1h` score `-0.5151` n `116` status `ready` deltaP `4.4709` edge `0.0021` maxDD `-1.3195`
- `risk_on_high->fx_1h` score `-0.6646` n `83` status `ready` deltaP `-2.1075` edge `-0.0033` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.6646` n `83` status `ready` deltaP `-2.1075` edge `-0.0033` maxDD `-0.376`
- `market_context_high->fx_1h` score `-0.6658` n `116` status `ready` deltaP `-4.6106` edge `-0.0025` maxDD `-0.503`
- `market_context_high->metal_4h` score `-0.8273` n `116` status `ready` deltaP `2.6493` edge `0.0471` maxDD `-1.6961`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
