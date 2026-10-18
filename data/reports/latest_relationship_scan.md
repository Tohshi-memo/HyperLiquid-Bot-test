# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T11:37:26.176097+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9246`

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

- `market_context_high->commodity_24h` score `2.3759` n `128` status `ready` deltaP `19.6565` edge `0.1521` maxDD `-1.8119`
- `market_context_high->crypto_major_4h` score `2.0756` n `142` status `ready` deltaP `17.4017` edge `0.3974` maxDD `-15.2359`
- `risk_on_high->commodity_24h` score `1.855` n `88` status `ready` deltaP `20.1536` edge `0.1` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `1.855` n `88` status `ready` deltaP `20.1536` edge `0.1` maxDD `-1.7154`
- `market_context_high->crypto_major_1h` score `0.6621` n `142` status `ready` deltaP `4.9907` edge `0.1108` maxDD `-3.7781`
- `risk_on_high->crypto_major_4h` score `0.2208` n `91` status `ready` deltaP `14.0663` edge `0.1826` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `0.2208` n `91` status `ready` deltaP `14.0663` edge `0.1826` maxDD `-11.1788`
- `market_context_high->crypto_alt_1h` score `0.1157` n `142` status `ready` deltaP `6.3654` edge `0.1172` maxDD `-7.3329`
- `risk_on_high->index_1h` score `-0.0425` n `91` status `ready` deltaP `4.4055` edge `0.0055` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.0425` n `91` status `ready` deltaP `4.4055` edge `0.0055` maxDD `-0.7394`
- `risk_on_high->fx_1h` score `-0.2242` n `91` status `ready` deltaP `1.7986` edge `-0.0027` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.2242` n `91` status `ready` deltaP `1.7986` edge `-0.0027` maxDD `-0.376`
- `market_context_high->metal_1h` score `-0.3533` n `142` status `ready` deltaP `4.957` edge `0.0086` maxDD `-0.9556`
- `market_context_high->index_1h` score `-0.3996` n `142` status `ready` deltaP `5.6592` edge `0.0038` maxDD `-1.3195`
- `risk_on_high->equity_1h` score `-0.4392` n `91` status `ready` deltaP `9.5585` edge `0.0293` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.4392` n `91` status `ready` deltaP `9.5585` edge `0.0293` maxDD `-5.3696`
- `risk_on_high->metal_1h` score `-0.5335` n `91` status `ready` deltaP `0.097` edge `0.0041` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.5335` n `91` status `ready` deltaP `0.097` edge `0.0041` maxDD `-0.8513`
- `market_context_high->metal_4h` score `-0.5354` n `142` status `ready` deltaP `6.6279` edge `0.0449` maxDD `-1.6961`
- `market_context_high->fx_1h` score `-0.6926` n `142` status `ready` deltaP `-0.554` edge `-0.0019` maxDD `-0.503`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
