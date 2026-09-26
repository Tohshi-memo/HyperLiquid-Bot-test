# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T16:52:26.997952+00:00`
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

- `news_risk_high->unknown_24h` score `4417.5024` n `85` status `ready` deltaP `1.2153` edge `368.1171` maxDD `0.0`
- `market_context_high->unknown_1h` score `69.487` n `47` status `ready` deltaP `8.3196` edge `5.7422` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `46.4489` n `47` status `ready` deltaP `21.0476` edge `3.7697` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `25.6348` n `47` status `ready` deltaP `15.407` edge `2.0715` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.4696` n `47` status `ready` deltaP `31.9851` edge `1.9448` maxDD `-2.1786`
- `market_context_high->index_24h` score `6.7917` n `47` status `ready` deltaP `26.2559` edge `0.4039` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.2473` n `47` status `ready` deltaP `27.2459` edge `0.1128` maxDD `-0.2401`
- `market_context_high->index_4h` score `2.7577` n `47` status `ready` deltaP `31.8922` edge `0.0326` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.7351` n `47` status `ready` deltaP `17.4494` edge `0.1534` maxDD `-1.3444`
- `news_risk_high->index_24h` score `2.0864` n `85` status `ready` deltaP `24.4036` edge `0.0682` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `1.4146` n `85` status `ready` deltaP `30.4249` edge `0.1433` maxDD `-6.8481`
- `news_risk_high->crypto_alt_24h` score `1.3957` n `85` status `ready` deltaP `9.2994` edge `0.4495` maxDD `-29.2814`
- `market_context_high->crypto_alt_4h` score `1.0602` n `47` status `ready` deltaP `9.9928` edge `0.0885` maxDD `-3.3417`
- `market_context_high->equity_1h` score `1.0086` n `47` status `ready` deltaP `11.6161` edge `0.0469` maxDD `-1.5564`
- `market_context_high->index_1h` score `0.8074` n `47` status `ready` deltaP `12.8137` edge `0.0097` maxDD `-0.2275`
- `market_context_high->crypto_major_4h` score `0.6048` n `47` status `ready` deltaP `5.4521` edge `0.1045` maxDD `-5.2359`
- `market_context_high->fx_1h` score `0.4578` n `47` status `ready` deltaP `9.9598` edge `0.0074` maxDD `-0.1854`
- `market_context_high->crypto_major_1h` score `0.4093` n `47` status `ready` deltaP `5.8001` edge `0.0772` maxDD `-4.5405`
- `market_context_high->metal_1h` score `0.0289` n `47` status `ready` deltaP `3.7266` edge `0.0105` maxDD `-0.1976`
- `news_risk_high->index_1h` score `-0.0711` n `139` status `ready` deltaP `2.9714` edge `0.0034` maxDD `-0.3305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
