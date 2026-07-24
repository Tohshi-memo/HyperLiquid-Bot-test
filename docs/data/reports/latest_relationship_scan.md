# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T02:52:24.410147+00:00`
- Price records: `672`
- Market context records: `7734`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14676`

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

- `market_context_high->equity_24h` score `3.9617` n `132` status `ready` deltaP `19.7444` edge `0.3327` maxDD `-6.0681`
- `market_context_high->crypto_major_1h` score `1.0118` n `133` status `ready` deltaP `13.0082` edge `0.0417` maxDD `-1.5286`
- `market_context_high->crypto_major_4h` score `0.9187` n `133` status `ready` deltaP `14.4989` edge `0.1517` maxDD `-6.7444`
- `market_context_high->crypto_alt_4h` score `0.6529` n `133` status `ready` deltaP `8.8093` edge `0.1074` maxDD `-3.9374`
- `market_context_high->equity_1h` score `0.5402` n `133` status `ready` deltaP `8.3463` edge `0.0753` maxDD `-4.2072`
- `market_context_high->equity_4h` score `0.4118` n `133` status `ready` deltaP `1.6636` edge `0.233` maxDD `-6.9701`
- `market_context_high->index_1h` score `0.3974` n `133` status `ready` deltaP `9.0949` edge `0.0155` maxDD `-0.7743`
- `market_context_high->fx_24h` score `0.227` n `132` status `ready` deltaP `16.2998` edge `0.0292` maxDD `-3.0343`
- `market_context_high->crypto_alt_1h` score `0.0777` n `133` status `ready` deltaP `3.6795` edge `0.0252` maxDD `-1.4603`
- `market_context_high->metal_24h` score `0.0664` n `133` status `ready` deltaP `5.8062` edge `0.1759` maxDD `-2.3927`
- `market_context_high->commodity_1h` score `-0.2133` n `133` status `ready` deltaP `3.2446` edge `0.0065` maxDD `-0.6722`
- `market_context_high->commodity_4h` score `-0.2445` n `133` status `ready` deltaP `3.7168` edge `0.0142` maxDD `-1.0817`
- `market_context_high->index_4h` score `-0.2655` n `133` status `ready` deltaP `10.5585` edge `0.0414` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.4639` n `133` status `ready` deltaP `0.0734` edge `-0.0004` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.7812` n `133` status `ready` deltaP `2.3153` edge `0.0198` maxDD `-0.6936`
- `market_context_high->metal_4h` score `-1.5219` n `133` status `ready` deltaP `0.6808` edge `0.0741` maxDD `-1.4368`
- `market_context_high->fx_4h` score `-1.5522` n `133` status `ready` deltaP `-5.0792` edge `-0.0023` maxDD `-1.6936`
- `market_context_high->commodity_24h` score `-1.7213` n `132` status `ready` deltaP `5.6858` edge `-0.023` maxDD `-7.0012`
- `market_context_high->unknown_1h` score `-2.1073` n `133` status `ready` deltaP `-0.825` edge `-0.1111` maxDD `-1.054`
- `market_context_high->index_24h` score `-2.5482` n `132` status `ready` deltaP `-18.4537` edge `0.0066` maxDD `-2.1544`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
