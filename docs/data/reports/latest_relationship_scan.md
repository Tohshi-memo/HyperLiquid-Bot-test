# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T17:22:24.895861+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11744`

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

- `news_risk_high->unknown_24h` score `4424.4024` n `85` status `ready` deltaP `1.2153` edge `368.6921` maxDD `0.0`
- `market_context_high->unknown_1h` score `69.2614` n `47` status `ready` deltaP `8.3196` edge `5.7234` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `46.4033` n `47` status `ready` deltaP `21.0476` edge `3.7659` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `25.4822` n `47` status `ready` deltaP `15.0598` edge `2.0611` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.4744` n `47` status `ready` deltaP `31.9851` edge `1.9452` maxDD `-2.1786`
- `market_context_high->index_24h` score `6.7778` n `47` status `ready` deltaP `26.0823` edge `0.4039` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.2623` n `47` status `ready` deltaP `27.4195` edge `0.1129` maxDD `-0.2401`
- `market_context_high->index_4h` score `2.7577` n `47` status `ready` deltaP `31.8922` edge `0.0326` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.7363` n `47` status `ready` deltaP `17.4494` edge `0.1535` maxDD `-1.3444`
- `news_risk_high->index_24h` score `2.0725` n `85` status `ready` deltaP `24.23` edge `0.0682` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `1.4245` n `85` status `ready` deltaP `30.5985` edge `0.1434` maxDD `-6.8481`
- `news_risk_high->crypto_alt_24h` score `1.2432` n `85` status `ready` deltaP `8.9522` edge `0.4391` maxDD `-29.2814`
- `market_context_high->equity_1h` score `1.0086` n `47` status `ready` deltaP `11.6161` edge `0.0469` maxDD `-1.5564`
- `market_context_high->crypto_alt_4h` score `0.9662` n `47` status `ready` deltaP `9.688` edge `0.0827` maxDD `-3.3417`
- `market_context_high->index_1h` score `0.8074` n `47` status `ready` deltaP `12.8137` edge `0.0097` maxDD `-0.2275`
- `market_context_high->crypto_major_4h` score `0.5494` n `47` status `ready` deltaP `5.2997` edge `0.1009` maxDD `-5.2359`
- `market_context_high->fx_1h` score `0.4578` n `47` status `ready` deltaP `9.9598` edge `0.0074` maxDD `-0.1854`
- `market_context_high->crypto_major_1h` score `0.3997` n `47` status `ready` deltaP `5.8001` edge `0.0764` maxDD `-4.5405`
- `market_context_high->metal_1h` score `0.0289` n `47` status `ready` deltaP `3.7266` edge `0.0105` maxDD `-0.1976`
- `news_risk_high->index_1h` score `-0.0711` n `139` status `ready` deltaP `2.9714` edge `0.0034` maxDD `-0.3305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
