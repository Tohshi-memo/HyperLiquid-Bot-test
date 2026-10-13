# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-13T16:52:25.359310+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9582`

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

- `market_context_high->crypto_alt_4h` score `7.92` n `117` status `ready` deltaP `19.8132` edge `0.6728` maxDD `-9.2574`
- `market_context_high->crypto_major_4h` score `6.8911` n `117` status `ready` deltaP `23.559` edge `0.5731` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `6.5089` n `54` status `ready` deltaP `22.0924` edge `0.4399` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `6.5089` n `54` status `ready` deltaP `22.0924` edge `0.4399` maxDD `-1.9151`
- `risk_on_high->commodity_24h` score `6.2821` n `48` status `ready` deltaP `32.0557` edge `0.3098` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.2821` n `48` status `ready` deltaP `32.0557` edge `0.3098` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `5.019` n `54` status `ready` deltaP `36.6644` edge `0.4843` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `5.019` n `54` status `ready` deltaP `36.6644` edge `0.4843` maxDD `-4.1548`
- `market_context_high->unknown_4h` score `4.3218` n `117` status `ready` deltaP `-3.467` edge `0.4479` maxDD `-1.8373`
- `market_context_high->crypto_alt_1h` score `2.0853` n `117` status `ready` deltaP `14.9138` edge `0.1811` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.5391` n `117` status `ready` deltaP `7.9073` edge `0.1561` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.3298` n `117` status `ready` deltaP `14.2225` edge `0.0372` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.156` n `54` status `ready` deltaP `3.3489` edge `0.0299` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.156` n `54` status `ready` deltaP `3.3489` edge `0.0299` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.3167` n `117` status `ready` deltaP `1.3976` edge `0.0023` maxDD `-0.3742`
- `market_context_high->metal_1h` score `-0.335` n `117` status `ready` deltaP `7.7141` edge `0.0076` maxDD `-0.9556`
- `risk_on_high->crypto_alt_1h` score `-0.3778` n `54` status `ready` deltaP `4.6574` edge `0.0231` maxDD `-5.8734`
- `risk_on_and_context->crypto_alt_1h` score `-0.3778` n `54` status `ready` deltaP `4.6574` edge `0.0231` maxDD `-5.8734`
- `risk_on_high->metal_1h` score `-0.4321` n `54` status `ready` deltaP `2.301` edge `0.0024` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4321` n `54` status `ready` deltaP `2.301` edge `0.0024` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
