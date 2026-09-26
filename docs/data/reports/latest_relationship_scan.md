# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T20:22:33.197719+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11754`

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

- `news_risk_high->unknown_24h` score `4436.5296` n `85` status `ready` deltaP `1.2153` edge `369.7027` maxDD `0.0`
- `market_context_high->unknown_1h` score `66.0094` n `47` status `ready` deltaP `8.3196` edge `5.4524` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `46.3479` n `47` status `ready` deltaP `20.7003` edge `3.7636` maxDD `-2.4756`
- `market_context_high->equity_24h` score `25.4382` n `47` status `ready` deltaP `31.6378` edge `1.9445` maxDD `-2.1786`
- `market_context_high->crypto_alt_24h` score `25.0879` n `47` status `ready` deltaP `14.8862` edge `2.0294` maxDD `-2.7051`
- `market_context_high->index_24h` score `6.7603` n `47` status `ready` deltaP `25.9087` edge `0.4036` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.2485` n `47` status `ready` deltaP `27.2459` edge `0.1129` maxDD `-0.2401`
- `market_context_high->index_4h` score `2.8711` n `47` status `ready` deltaP `33.2641` edge `0.0329` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.8349` n `47` status `ready` deltaP `18.5164` edge `0.1546` maxDD `-1.3444`
- `news_risk_high->index_24h` score `2.055` n `85` status `ready` deltaP `24.0564` edge `0.0679` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `1.4154` n `85` status `ready` deltaP `30.4249` edge `0.1434` maxDD `-6.8481`
- `market_context_high->equity_1h` score `1.1164` n `47` status `ready` deltaP `12.8137` edge `0.0479` maxDD `-1.5564`
- `market_context_high->crypto_alt_4h` score `0.8752` n `47` status `ready` deltaP `8.9258` edge `0.0802` maxDD `-3.3417`
- `news_risk_high->crypto_alt_24h` score `0.8489` n `85` status `ready` deltaP `8.7786` edge `0.4074` maxDD `-29.2814`
- `market_context_high->index_1h` score `0.8205` n `47` status `ready` deltaP `12.9634` edge `0.0098` maxDD `-0.2275`
- `market_context_high->crypto_major_1h` score `0.4321` n `47` status `ready` deltaP `6.0995` edge `0.0771` maxDD `-4.5405`
- `market_context_high->crypto_major_4h` score `0.4192` n `47` status `ready` deltaP `4.8423` edge `0.0931` maxDD `-5.2359`
- `market_context_high->fx_1h` score `0.3823` n `47` status `ready` deltaP `9.0616` edge `0.0071` maxDD `-0.1854`
- `market_context_high->metal_1h` score `0.0367` n `47` status `ready` deltaP `3.8763` edge `0.0105` maxDD `-0.1976`
- `news_risk_high->index_1h` score `-0.0579` n `139` status `ready` deltaP `3.1211` edge `0.0035` maxDD `-0.3305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
