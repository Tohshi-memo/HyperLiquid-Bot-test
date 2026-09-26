# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T05:22:29.824095+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11768`

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

- `news_risk_high->unknown_24h` score `3271.5011` n `97` status `ready` deltaP `-0.6837` edge `272.6341` maxDD `-0.0226`
- `market_context_high->unknown_1h` score `69.8422` n `47` status `ready` deltaP `8.0201` edge `5.7738` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `48.7178` n `47` status `ready` deltaP `25.2142` edge `3.931` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `30.0996` n `47` status `ready` deltaP `22.8723` edge `2.3938` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.2963` n `47` status `ready` deltaP `33.3739` edge `1.9211` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.3431` n `47` status `ready` deltaP `32.1587` edge `0.4105` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.4998` n `47` status `ready` deltaP `29.5028` edge `0.1188` maxDD `-0.2401`
- `market_context_high->equity_4h` score `2.6875` n `47` status `ready` deltaP `16.8396` edge `0.1535` maxDD `-1.3444`
- `market_context_high->index_4h` score `2.503` n `47` status `ready` deltaP `28.8434` edge `0.0317` maxDD `-0.2323`
- `market_context_high->crypto_alt_4h` score `1.1609` n `47` status `ready` deltaP `10.9075` edge `0.0908` maxDD `-3.3417`
- `news_risk_high->metal_24h` score `1.1414` n `97` status `ready` deltaP `27.1996` edge `0.1311` maxDD `-6.9545`
- `market_context_high->equity_1h` score `1.0506` n `47` status `ready` deltaP `12.0652` edge `0.0474` maxDD `-1.5564`
- `market_context_high->index_1h` score `0.7571` n `47` status `ready` deltaP `12.2149` edge `0.0095` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.5213` n `47` status `ready` deltaP `10.7083` edge `0.0077` maxDD `-0.1854`
- `news_risk_high->index_24h` score `0.4184` n `97` status `ready` deltaP `13.7994` edge `0.043` maxDD `-2.344`
- `market_context_high->crypto_major_4h` score `0.3684` n `47` status `ready` deltaP `4.5375` edge `0.0909` maxDD `-5.2359`
- `market_context_high->crypto_major_1h` score `0.335` n `47` status `ready` deltaP `5.2013` edge `0.075` maxDD `-4.5405`
- `news_risk_high->index_1h` score `0.1632` n `126` status `ready` deltaP `5.7813` edge `0.0043` maxDD `-0.3395`
- `market_context_high->metal_1h` score `0.0196` n `47` status `ready` deltaP `3.5769` edge `0.0103` maxDD `-0.1976`
- `market_context_high->fx_4h` score `0.0103` n `47` status `ready` deltaP `9.0166` edge `0.0075` maxDD `-0.6736`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
