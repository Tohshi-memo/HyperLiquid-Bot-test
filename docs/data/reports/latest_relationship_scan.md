# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T17:07:27.755666+00:00`
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

- `news_risk_high->unknown_24h` score `4420.9836` n `85` status `ready` deltaP `1.2153` edge `368.4072` maxDD `0.0`
- `market_context_high->unknown_1h` score `69.4594` n `47` status `ready` deltaP `8.3196` edge `5.7399` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `46.4261` n `47` status `ready` deltaP `21.0476` edge `3.7678` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `25.5585` n `47` status `ready` deltaP `15.2334` edge `2.0663` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.472` n `47` status `ready` deltaP `31.9851` edge `1.945` maxDD `-2.1786`
- `market_context_high->index_24h` score `6.7778` n `47` status `ready` deltaP `26.0823` edge `0.4039` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.2485` n `47` status `ready` deltaP `27.2459` edge `0.1129` maxDD `-0.2401`
- `market_context_high->index_4h` score `2.7577` n `47` status `ready` deltaP `31.8922` edge `0.0326` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.7363` n `47` status `ready` deltaP `17.4494` edge `0.1535` maxDD `-1.3444`
- `news_risk_high->index_24h` score `2.0725` n `85` status `ready` deltaP `24.23` edge `0.0682` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `1.4154` n `85` status `ready` deltaP `30.4249` edge `0.1434` maxDD `-6.8481`
- `news_risk_high->crypto_alt_24h` score `1.3195` n `85` status `ready` deltaP `9.1258` edge `0.4443` maxDD `-29.2814`
- `market_context_high->crypto_alt_4h` score `1.018` n `47` status `ready` deltaP `9.8404` edge `0.086` maxDD `-3.3417`
- `market_context_high->equity_1h` score `0.9955` n `47` status `ready` deltaP `11.4664` edge `0.0468` maxDD `-1.5564`
- `market_context_high->index_1h` score `0.8074` n `47` status `ready` deltaP `12.8137` edge `0.0097` maxDD `-0.2275`
- `market_context_high->crypto_major_4h` score `0.5856` n `47` status `ready` deltaP `5.4521` edge `0.1029` maxDD `-5.2359`
- `market_context_high->fx_1h` score `0.4578` n `47` status `ready` deltaP `9.9598` edge `0.0074` maxDD `-0.1854`
- `market_context_high->crypto_major_1h` score `0.4045` n `47` status `ready` deltaP `5.8001` edge `0.0768` maxDD `-4.5405`
- `market_context_high->metal_1h` score `0.0289` n `47` status `ready` deltaP `3.7266` edge `0.0105` maxDD `-0.1976`
- `news_risk_high->index_1h` score `-0.0711` n `139` status `ready` deltaP `2.9714` edge `0.0034` maxDD `-0.3305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
