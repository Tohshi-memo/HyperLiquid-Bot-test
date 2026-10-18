# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T14:22:28.586743+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9222`

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

- `market_context_high->commodity_24h` score `2.1945` n `131` status `ready` deltaP `19.443` edge `0.1384` maxDD `-1.8119`
- `risk_on_high->commodity_24h` score `1.86` n `90` status `ready` deltaP `20.6813` edge `0.0969` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `1.86` n `90` status `ready` deltaP `20.6813` edge `0.0969` maxDD `-1.7154`
- `market_context_high->crypto_major_4h` score `1.0273` n `134` status `ready` deltaP `16.088` edge `0.3649` maxDD `-15.2359`
- `market_context_high->crypto_major_1h` score `0.8531` n `134` status `ready` deltaP `6.1176` edge `0.1192` maxDD `-3.7781`
- `risk_on_high->crypto_major_4h` score `0.468` n `91` status `ready` deltaP `14.9809` edge `0.2082` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `0.468` n `91` status `ready` deltaP `14.9809` edge `0.2082` maxDD `-11.1788`
- `risk_on_high->index_1h` score `0.0356` n `91` status `ready` deltaP `5.3064` edge `0.006` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.0356` n `91` status `ready` deltaP `5.3064` edge `0.006` maxDD `-0.7394`
- `market_context_high->crypto_alt_1h` score `-0.0894` n `134` status `ready` deltaP `4.3391` edge `0.1096` maxDD `-7.3329`
- `risk_on_high->fx_1h` score `-0.2484` n `91` status `ready` deltaP `1.3481` edge `-0.0028` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.2484` n `91` status `ready` deltaP `1.3481` edge `-0.0028` maxDD `-0.376`
- `risk_on_high->equity_1h` score `-0.3731` n `91` status `ready` deltaP `10.009` edge `0.0318` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.3731` n `91` status `ready` deltaP `10.009` edge `0.0318` maxDD `-5.3696`
- `market_context_high->metal_1h` score `-0.4149` n `134` status `ready` deltaP `3.7425` edge `0.0088` maxDD `-0.9556`
- `market_context_high->index_1h` score `-0.4448` n `134` status `ready` deltaP `5.1096` edge `0.0037` maxDD `-1.3195`
- `risk_on_high->metal_1h` score `-0.4844` n `91` status `ready` deltaP `0.9952` edge `0.0044` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4844` n `91` status `ready` deltaP `0.9952` edge `0.0044` maxDD `-0.8513`
- `market_context_high->metal_4h` score `-0.7156` n `134` status `ready` deltaP `4.4207` edge `0.0446` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.7307` n `91` status `ready` deltaP `-1.1483` edge `0.0059` maxDD `-4.6876`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
