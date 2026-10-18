# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T18:07:31.327770+00:00`
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

- `market_context_high->commodity_24h` score `2.026` n `118` status `ready` deltaP `18.7472` edge `0.129` maxDD `-1.8119`
- `risk_on_high->commodity_24h` score `1.9031` n `85` status `ready` deltaP `20.9207` edge `0.0989` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `1.9031` n `85` status `ready` deltaP `20.9207` edge `0.0989` maxDD `-1.7154`
- `market_context_high->crypto_major_4h` score `1.613` n `119` status `ready` deltaP `18.8922` edge `0.4213` maxDD `-15.2359`
- `risk_on_high->crypto_major_4h` score `1.2458` n `86` status `ready` deltaP `19.498` edge `0.2778` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `1.2458` n `86` status `ready` deltaP `19.498` edge `0.2778` maxDD `-11.1788`
- `market_context_high->crypto_major_1h` score `0.4182` n `119` status `ready` deltaP `5.6119` edge `0.1051` maxDD `-3.7781`
- `risk_on_high->index_1h` score `0.1769` n `86` status `ready` deltaP `7.0571` edge `0.0061` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.1769` n `86` status `ready` deltaP `7.0571` edge `0.0061` maxDD `-0.7394`
- `risk_on_high->equity_1h` score `-0.2922` n `86` status `ready` deltaP `10.961` edge `0.0322` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.2922` n `86` status `ready` deltaP `10.961` edge `0.0322` maxDD `-5.3696`
- `market_context_high->crypto_alt_1h` score `-0.3296` n `119` status `ready` deltaP `2.5399` edge `0.0908` maxDD `-7.3329`
- `risk_on_high->metal_1h` score `-0.5097` n `86` status `ready` deltaP `0.5535` edge `0.0041` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.5097` n `86` status `ready` deltaP `0.5535` edge `0.0041` maxDD `-0.8513`
- `risk_on_high->crypto_major_1h` score `-0.5548` n `86` status `ready` deltaP `0.1497` edge `0.0198` maxDD `-4.6876`
- `risk_on_and_context->crypto_major_1h` score `-0.5548` n `86` status `ready` deltaP `0.1497` edge `0.0198` maxDD `-4.6876`
- `risk_on_high->fx_1h` score `-0.5998` n `86` status `ready` deltaP `-1.313` edge `-0.0032` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.5998` n `86` status `ready` deltaP `-1.313` edge `-0.0032` maxDD `-0.376`
- `market_context_high->index_1h` score `-0.6107` n `119` status `ready` deltaP `3.2756` edge `0.0021` maxDD `-1.3195`
- `market_context_high->fx_1h` score `-0.6305` n `119` status `ready` deltaP `-3.9317` edge `-0.0025` maxDD `-0.503`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
