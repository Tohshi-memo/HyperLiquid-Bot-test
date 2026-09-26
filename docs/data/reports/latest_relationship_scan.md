# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T00:37:31.891973+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11662`

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

- `news_risk_high->unknown_24h` score `1674.432` n `87` status `ready` deltaP `-0.8022` edge `139.5458` maxDD `-0.0226`
- `market_context_high->unknown_1h` score `71.3986` n `47` status `ready` deltaP `8.1698` edge `5.9025` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `49.9873` n `47` status `ready` deltaP `28.5128` edge `4.0148` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `31.4572` n `47` status `ready` deltaP `24.782` edge `2.4942` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.1091` n `47` status `ready` deltaP `32.1587` edge `1.9136` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.5734` n `47` status `ready` deltaP `34.242` edge `0.4158` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.7107` n `47` status `ready` deltaP `31.2389` edge `0.1248` maxDD `-0.2401`
- `market_context_high->equity_4h` score `2.7193` n `47` status `ready` deltaP `17.2969` edge `0.1531` maxDD `-1.3444`
- `market_context_high->index_4h` score `2.5116` n `47` status `ready` deltaP `28.9958` edge `0.0314` maxDD `-0.2323`
- `market_context_high->crypto_alt_4h` score `1.3629` n `47` status `ready` deltaP `11.2124` edge `0.1056` maxDD `-3.3417`
- `market_context_high->equity_1h` score `1.1164` n `47` status `ready` deltaP `12.8137` edge `0.0479` maxDD `-1.5564`
- `market_context_high->index_1h` score `0.8421` n `47` status `ready` deltaP `13.2628` edge `0.0096` maxDD `-0.2275`
- `news_risk_high->crypto_alt_1h` score `0.8319` n `116` status `ready` deltaP `9.7925` edge `0.0951` maxDD `-4.2849`
- `news_risk_high->metal_24h` score `0.7965` n `87` status `ready` deltaP `24.5869` edge `0.1043` maxDD `-6.9545`
- `market_context_high->fx_1h` score `0.5093` n `47` status `ready` deltaP `10.5586` edge `0.0077` maxDD `-0.1854`
- `market_context_high->crypto_major_4h` score `0.4238` n `47` status `ready` deltaP `4.6899` edge `0.0945` maxDD `-5.2359`
- `market_context_high->crypto_major_1h` score `0.2547` n `47` status `ready` deltaP `4.6025` edge `0.0723` maxDD `-4.5405`
- `market_context_high->fx_4h` score `0.0469` n `47` status `ready` deltaP `9.4739` edge `0.0075` maxDD `-0.6736`
- `market_context_high->metal_1h` score `0.004` n `47` status `ready` deltaP `3.2775` edge `0.0103` maxDD `-0.1976`
- `news_risk_high->index_1h` score `-0.0272` n `116` status `ready` deltaP `3.3399` edge `0.0053` maxDD `-0.3863`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
