# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T08:07:26.170763+00:00`
- Price records: `672`
- Market context records: `6797`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11656`

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

- `market_context_high->unknown_24h` score `0.8504` n `176` status `ready` deltaP `-1.3731` edge `0.4934` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `0.2035` n `176` status `ready` deltaP `9.012` edge `0.1437` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.2503` n `185` status `ready` deltaP `6.4986` edge `0.0218` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.3997` n `185` status `ready` deltaP `3.6462` edge `0.0188` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.427` n `185` status `ready` deltaP `-0.9354` edge `0.0` maxDD `-0.5468`
- `market_context_high->index_1h` score `-0.6603` n `185` status `ready` deltaP `-1.8587` edge `-0.0007` maxDD `-0.7249`
- `market_context_high->metal_1h` score `-0.7031` n `185` status `ready` deltaP `-5.1432` edge `-0.003` maxDD `-1.2285`
- `market_context_high->commodity_1h` score `-0.7065` n `185` status `ready` deltaP `-1.8255` edge `-0.0101` maxDD `-2.1314`
- `market_context_high->equity_1h` score `-1.2954` n `185` status `ready` deltaP `2.2326` edge `-0.0184` maxDD `-4.0213`
- `market_context_high->fx_4h` score `-1.4001` n `182` status `ready` deltaP `4.4207` edge `-0.0026` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.4606` n `182` status `ready` deltaP `-2.7405` edge `-0.02` maxDD `-5.5853`
- `market_context_high->index_4h` score `-1.5178` n `182` status `ready` deltaP `2.8176` edge `-0.0216` maxDD `-6.0089`
- `market_context_high->unknown_1h` score `-1.5359` n `185` status `ready` deltaP `-4.9935` edge `-0.0046` maxDD `-3.2083`
- `market_context_high->metal_4h` score `-2.6754` n `182` status `ready` deltaP `-5.5967` edge `-0.008` maxDD `-5.4819`
- `market_context_high->crypto_major_4h` score `-3.0828` n `182` status `ready` deltaP `0.7086` edge `-0.0685` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-3.2061` n `182` status `ready` deltaP `-0.1776` edge `-0.0591` maxDD `-20.0604`
- `market_context_high->unknown_4h` score `-3.3514` n `182` status `ready` deltaP `-13.6542` edge `0.0483` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.502` n `176` status `ready` deltaP `-9.7853` edge `-0.0063` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-4.5919` n `182` status `ready` deltaP `0.2513` edge `-0.1544` maxDD `-27.8787`
- `market_context_high->metal_24h` score `-9.3258` n `176` status `ready` deltaP `-19.3656` edge `-0.218` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
