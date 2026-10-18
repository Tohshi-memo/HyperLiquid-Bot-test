# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T11:07:25.633300+00:00`
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

- `market_context_high->commodity_24h` score `2.4095` n `127` status `ready` deltaP `19.7015` edge `0.1546` maxDD `-1.8119`
- `market_context_high->crypto_major_4h` score `2.106` n `143` status `ready` deltaP `17.6627` edge `0.3982` maxDD `-15.2359`
- `risk_on_high->commodity_24h` score `1.9173` n `86` status `ready` deltaP `19.9578` edge `0.1065` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `1.9173` n `86` status `ready` deltaP `19.9578` edge `0.1065` maxDD `-1.7154`
- `market_context_high->crypto_major_1h` score `0.6722` n `143` status `ready` deltaP `5.1464` edge `0.1106` maxDD `-3.7781`
- `risk_on_high->crypto_major_4h` score `0.2216` n `91` status `ready` deltaP `14.0663` edge `0.1827` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `0.2216` n `91` status `ready` deltaP `14.0663` edge `0.1827` maxDD `-11.1788`
- `market_context_high->crypto_alt_1h` score `0.1237` n `143` status `ready` deltaP `6.5408` edge `0.1167` maxDD `-7.3329`
- `risk_on_high->index_1h` score `-0.0665` n `91` status `ready` deltaP `4.1052` edge `0.0055` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.0665` n `91` status `ready` deltaP `4.1052` edge `0.0055` maxDD `-0.7394`
- `risk_on_high->fx_1h` score `-0.2242` n `91` status `ready` deltaP `1.7986` edge `-0.0027` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.2242` n `91` status `ready` deltaP `1.7986` edge `-0.0027` maxDD `-0.376`
- `market_context_high->metal_1h` score `-0.3359` n `143` status `ready` deltaP `5.2919` edge `0.0086` maxDD `-0.9556`
- `market_context_high->index_1h` score `-0.3948` n `143` status `ready` deltaP `5.7037` edge `0.0039` maxDD `-1.3195`
- `risk_on_high->equity_1h` score `-0.468` n `91` status `ready` deltaP `9.2582` edge `0.0289` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.468` n `91` status `ready` deltaP `9.2582` edge `0.0289` maxDD `-5.3696`
- `market_context_high->metal_4h` score `-0.509` n `143` status `ready` deltaP `6.9579` edge `0.0449` maxDD `-1.6961`
- `risk_on_high->metal_1h` score `-0.5335` n `91` status `ready` deltaP `0.097` edge `0.0041` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.5335` n `91` status `ready` deltaP `0.097` edge `0.0041` maxDD `-0.8513`
- `market_context_high->fx_1h` score `-0.663` n `143` status `ready` deltaP `-0.1995` edge `-0.0018` maxDD `-0.503`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
