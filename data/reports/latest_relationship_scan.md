# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T20:07:32.886718+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6816`

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

- `market_context_high->unknown_24h` score `1617.0643` n `134` status `ready` deltaP `-1.7491` edge `134.81` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `62.8662` n `134` status `ready` deltaP `5.7517` edge `5.2138` maxDD `-0.3966`
- `market_context_high->index_24h` score `2.238` n `134` status `ready` deltaP `27.4513` edge `0.0218` maxDD `-0.1315`
- `market_context_high->metal_1h` score `0.2863` n `134` status `ready` deltaP `9.706` edge `0.0099` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.1005` n `134` status `ready` deltaP `13.3919` edge `0.0132` maxDD `-1.8344`
- `market_context_high->commodity_4h` score `0.0927` n `134` status `ready` deltaP `11.9562` edge `0.0499` maxDD `-1.0837`
- `market_context_high->fx_1h` score `-0.1018` n `134` status `ready` deltaP `3.5794` edge `-0.0011` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.3834` n `134` status `ready` deltaP `0.896` edge `0.0135` maxDD `-0.4475`
- `market_context_high->crypto_major_1h` score `-0.4209` n `134` status `ready` deltaP `5.3691` edge `0.0319` maxDD `-5.2213`
- `market_context_high->equity_1h` score `-0.4301` n `134` status `ready` deltaP `1.7875` edge `0.0398` maxDD `-2.3383`
- `market_context_high->fx_4h` score `-0.4949` n `134` status `ready` deltaP `-0.0159` edge `-0.0035` maxDD `-0.4545`
- `market_context_high->index_1h` score `-0.9972` n `134` status `ready` deltaP `-3.7425` edge `-0.0023` maxDD `-1.1344`
- `market_context_high->fx_24h` score `-1.0458` n `134` status `ready` deltaP `5.014` edge `0.0125` maxDD `-0.9792`
- `market_context_high->crypto_alt_1h` score `-1.1487` n `134` status `ready` deltaP `2.1003` edge `0.0252` maxDD `-8.251`
- `market_context_high->equity_4h` score `-1.5307` n `134` status `ready` deltaP `-2.7917` edge `-0.0192` maxDD `-6.008`
- `market_context_high->metal_24h` score `-1.667` n `134` status `ready` deltaP `3.9257` edge `0.0248` maxDD `-10.5088`
- `market_context_high->index_4h` score `-2.4456` n `134` status `ready` deltaP `-7.1965` edge `-0.0238` maxDD `-3.5621`
- `market_context_high->equity_24h` score `-2.6483` n `134` status `ready` deltaP `9.8881` edge `-0.0109` maxDD `-14.0571`
- `market_context_high->crypto_major_4h` score `-2.7204` n `134` status `ready` deltaP `4.6551` edge `-0.0503` maxDD `-19.0267`
- `market_context_high->commodity_24h` score `-4.4391` n `134` status `ready` deltaP `1.4252` edge `-0.0196` maxDD `-24.0547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
