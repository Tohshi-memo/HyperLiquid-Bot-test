# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-14T21:22:25.261776+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9346`

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

- `market_context_high->crypto_alt_4h` score `7.3085` n `117` status `ready` deltaP `19.5083` edge `0.6234` maxDD `-9.2196`
- `risk_on_high->commodity_24h` score `6.8458` n `54` status `ready` deltaP `34.7826` edge `0.3386` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.8458` n `54` status `ready` deltaP `34.7826` edge `0.3386` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `6.3126` n `117` status `ready` deltaP `21.5773` edge `0.5381` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `5.9038` n `54` status `ready` deltaP `21.7875` edge `0.3914` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `5.9038` n `54` status `ready` deltaP `21.7875` edge `0.3914` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `4.6429` n `54` status `ready` deltaP `34.6827` edge `0.4493` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.6429` n `54` status `ready` deltaP `34.6827` edge `0.4493` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.8132` n `117` status `ready` deltaP `13.8659` edge `0.1651` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `1.243` n `117` status `ready` deltaP `5.6618` edge `0.1464` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.4432` n `117` status `ready` deltaP `14.6798` edge `0.0436` maxDD `-1.6961`
- `market_context_high->metal_1h` score `-0.2631` n `117` status `ready` deltaP `8.4626` edge `0.0086` maxDD `-0.9556`
- `market_context_high->fx_1h` score `-0.3179` n `117` status `ready` deltaP `1.3976` edge `0.0022` maxDD `-0.3742`
- `risk_on_high->crypto_major_1h` score `-0.3484` n `54` status `ready` deltaP `1.1034` edge `0.0202` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.3484` n `54` status `ready` deltaP `1.1034` edge `0.0202` maxDD `-3.7781`
- `risk_on_high->metal_1h` score `-0.3854` n `54` status `ready` deltaP `3.0495` edge `0.0034` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.3854` n `54` status `ready` deltaP `3.0495` edge `0.0034` maxDD `-0.8513`
- `risk_on_high->metal_4h` score `-0.4929` n `54` status `ready` deltaP `2.2866` edge `0.0261` maxDD `-1.6961`
- `risk_on_and_context->metal_4h` score `-0.4929` n `54` status `ready` deltaP `2.2866` edge `0.0261` maxDD `-1.6961`
- `market_context_high->index_1h` score `-0.536` n `117` status `ready` deltaP `0.924` edge `-0.0001` maxDD `-1.3154`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
