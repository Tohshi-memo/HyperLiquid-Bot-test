# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-14T19:07:29.683510+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9656`

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

- `market_context_high->crypto_alt_4h` score `7.1639` n `117` status `ready` deltaP `19.051` edge `0.6144` maxDD `-9.2196`
- `risk_on_high->commodity_24h` score `6.5562` n `54` status `ready` deltaP `33.2174` edge `0.3249` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.5562` n `54` status `ready` deltaP `33.2174` edge `0.3249` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `6.2484` n `117` status `ready` deltaP `21.12` edge `0.5358` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `5.7592` n `54` status `ready` deltaP `21.3302` edge `0.3824` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `5.7592` n `54` status `ready` deltaP `21.3302` edge `0.3824` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `4.6012` n `54` status `ready` deltaP `34.2254` edge `0.447` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.6012` n `54` status `ready` deltaP `34.2254` edge `0.447` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.7916` n `117` status `ready` deltaP `13.7162` edge `0.1643` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `1.279` n `117` status `ready` deltaP `5.9612` edge `0.1474` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.3738` n `117` status `ready` deltaP `13.9176` edge `0.0429` maxDD `-1.6961`
- `market_context_high->metal_1h` score `-0.2751` n `117` status `ready` deltaP `8.3129` edge `0.0086` maxDD `-0.9556`
- `risk_on_high->crypto_major_1h` score `-0.3251` n `54` status `ready` deltaP `1.4028` edge `0.0212` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.3251` n `54` status `ready` deltaP `1.4028` edge `0.0212` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.3419` n `117` status `ready` deltaP `1.0973` edge `0.0022` maxDD `-0.3742`
- `risk_on_high->metal_1h` score `-0.3932` n `54` status `ready` deltaP `2.8998` edge `0.0034` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.3932` n `54` status `ready` deltaP `2.8998` edge `0.0034` maxDD `-0.8513`
- `risk_on_high->metal_4h` score `-0.538` n `54` status `ready` deltaP `1.5244` edge `0.0254` maxDD `-1.6961`
- `risk_on_and_context->metal_4h` score `-0.538` n `54` status `ready` deltaP `1.5244` edge `0.0254` maxDD `-1.6961`
- `market_context_high->index_1h` score `-0.561` n `117` status `ready` deltaP `0.4735` edge `-0.0003` maxDD `-1.3154`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
