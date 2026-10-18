# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T13:52:33.556872+00:00`
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

- `market_context_high->commodity_24h` score `2.292` n `131` status `ready` deltaP `20.0322` edge `0.1426` maxDD `-1.8119`
- `risk_on_high->commodity_24h` score `1.8317` n `90` status `ready` deltaP `20.5071` edge `0.0957` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `1.8317` n `90` status `ready` deltaP `20.5071` edge `0.0957` maxDD `-1.7154`
- `market_context_high->crypto_major_4h` score `1.7298` n `136` status `ready` deltaP `16.3648` edge `0.3755` maxDD `-15.2359`
- `market_context_high->crypto_major_1h` score `0.8717` n `136` status `ready` deltaP `6.4547` edge `0.1185` maxDD `-3.7781`
- `risk_on_high->crypto_major_4h` score `0.3898` n `91` status `ready` deltaP `14.6761` edge `0.2002` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `0.3898` n `91` status `ready` deltaP `14.6761` edge `0.2002` maxDD `-11.1788`
- `risk_on_high->index_1h` score `0.0212` n `91` status `ready` deltaP `5.1562` edge `0.0058` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.0212` n `91` status `ready` deltaP `5.1562` edge `0.0058` maxDD `-0.7394`
- `market_context_high->crypto_alt_1h` score `-0.0354` n `136` status `ready` deltaP `4.764` edge `0.1137` maxDD `-7.3329`
- `risk_on_high->fx_1h` score `-0.2484` n `91` status `ready` deltaP `1.3481` edge `-0.0028` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.2484` n `91` status `ready` deltaP `1.3481` edge `-0.0028` maxDD `-0.376`
- `risk_on_high->equity_1h` score `-0.4091` n `91` status `ready` deltaP `9.7087` edge `0.0308` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.4091` n `91` status `ready` deltaP `9.7087` edge `0.0308` maxDD `-5.3696`
- `market_context_high->metal_1h` score `-0.4243` n `136` status `ready` deltaP `3.5928` edge `0.0086` maxDD `-0.9556`
- `market_context_high->index_1h` score `-0.4571` n `136` status `ready` deltaP `4.9704` edge `0.0036` maxDD `-1.3195`
- `risk_on_high->metal_1h` score `-0.4938` n `91` status `ready` deltaP `0.8455` edge `0.0042` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4938` n `91` status `ready` deltaP `0.8455` edge `0.0042` maxDD `-0.8513`
- `market_context_high->metal_4h` score `-0.6775` n `136` status `ready` deltaP `4.8512` edge `0.0449` maxDD `-1.6961`
- `market_context_high->fx_1h` score `-0.7299` n `136` status `ready` deltaP `-1.0356` edge `-0.0018` maxDD `-0.503`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
