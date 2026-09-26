# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T16:37:32.548424+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11728`

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

- `news_risk_high->unknown_24h` score `4414.326` n `85` status `ready` deltaP `1.2153` edge `367.8524` maxDD `0.0`
- `market_context_high->unknown_1h` score `69.2374` n `47` status `ready` deltaP `8.3196` edge `5.7214` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `46.4832` n `47` status `ready` deltaP `21.2212` edge `3.7714` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `25.7147` n `47` status `ready` deltaP `15.5806` edge `2.077` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.4684` n `47` status `ready` deltaP `31.9851` edge `1.9447` maxDD `-2.1786`
- `market_context_high->index_24h` score `6.8068` n `47` status `ready` deltaP `26.4295` edge `0.404` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.2334` n `47` status `ready` deltaP `27.0723` edge `0.1128` maxDD `-0.2401`
- `market_context_high->index_4h` score `2.7711` n `47` status `ready` deltaP `32.0446` edge `0.0327` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.7351` n `47` status `ready` deltaP `17.4494` edge `0.1534` maxDD `-1.3444`
- `news_risk_high->index_24h` score `2.1015` n `85` status `ready` deltaP `24.5772` edge `0.0683` maxDD `-2.2287`
- `news_risk_high->crypto_alt_24h` score `1.4756` n `85` status `ready` deltaP `9.473` edge `0.455` maxDD `-29.2814`
- `news_risk_high->metal_24h` score `1.4056` n `85` status `ready` deltaP `30.2513` edge `0.1433` maxDD `-6.8481`
- `market_context_high->crypto_alt_4h` score `1.1036` n `47` status `ready` deltaP `10.1453` edge `0.0911` maxDD `-3.3417`
- `market_context_high->equity_1h` score `1.0086` n `47` status `ready` deltaP `11.6161` edge `0.0469` maxDD `-1.5564`
- `market_context_high->index_1h` score `0.8193` n `47` status `ready` deltaP `12.9634` edge `0.0097` maxDD `-0.2275`
- `market_context_high->crypto_major_4h` score `0.635` n `47` status `ready` deltaP `5.6045` edge `0.106` maxDD `-5.2359`
- `market_context_high->fx_1h` score `0.4698` n `47` status `ready` deltaP `10.1095` edge `0.0074` maxDD `-0.1854`
- `market_context_high->crypto_major_1h` score `0.4105` n `47` status `ready` deltaP `5.8001` edge `0.0773` maxDD `-4.5405`
- `market_context_high->metal_1h` score `0.0289` n `47` status `ready` deltaP `3.7266` edge `0.0105` maxDD `-0.1976`
- `news_risk_high->index_1h` score `-0.0591` n `139` status `ready` deltaP `3.1211` edge `0.0034` maxDD `-0.3305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
