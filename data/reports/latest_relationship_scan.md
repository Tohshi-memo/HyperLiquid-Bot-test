# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T11:52:30.055758+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11882`

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

- `news_risk_high->unknown_24h` score `4346.4367` n `87` status `ready` deltaP `0.1736` edge `362.2019` maxDD `0.0`
- `market_context_high->unknown_1h` score `69.5613` n `47` status `ready` deltaP `8.4693` edge `5.7474` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `47.3088` n `47` status `ready` deltaP `22.4364` edge `3.8321` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `27.781` n `47` status `ready` deltaP `18.8792` edge `2.2272` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.5927` n `47` status `ready` deltaP `33.3739` edge `1.9458` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.0535` n `47` status `ready` deltaP `29.0337` edge `0.4072` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.4324` n `47` status `ready` deltaP `29.1556` edge `0.1155` maxDD `-0.2401`
- `market_context_high->equity_4h` score `2.7521` n `47` status `ready` deltaP `17.6018` edge `0.1538` maxDD `-1.3444`
- `market_context_high->index_4h` score `2.6554` n `47` status `ready` deltaP `30.6727` edge `0.0322` maxDD `-0.2323`
- `news_risk_high->index_24h` score `2.1242` n `87` status `ready` deltaP `25.0719` edge `0.0669` maxDD `-2.2287`
- `news_risk_high->crypto_alt_24h` score `2.1228` n `87` status `ready` deltaP `10.6621` edge `0.501` maxDD `-29.2814`
- `news_risk_high->metal_24h` score `1.4247` n `87` status `ready` deltaP `30.5496` edge `0.144` maxDD `-6.867`
- `market_context_high->crypto_alt_4h` score `1.3387` n `47` status `ready` deltaP `11.0599` edge `0.1046` maxDD `-3.3417`
- `market_context_high->equity_1h` score `1.0362` n `47` status `ready` deltaP `11.9155` edge `0.0472` maxDD `-1.5564`
- `market_context_high->crypto_major_4h` score `0.8119` n `47` status `ready` deltaP `6.9765` edge `0.1116` maxDD `-5.2359`
- `market_context_high->index_1h` score `0.7942` n `47` status `ready` deltaP `12.664` edge `0.0096` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.4829` n `47` status `ready` deltaP `10.2592` edge `0.0075` maxDD `-0.1854`
- `market_context_high->crypto_major_1h` score `0.3806` n `47` status `ready` deltaP `5.5007` edge `0.0768` maxDD `-4.5405`
- `news_risk_high->index_1h` score `0.043` n `137` status `ready` deltaP `4.3708` edge `0.0036` maxDD `-0.3322`
- `market_context_high->metal_1h` score `0.0367` n `47` status `ready` deltaP `3.8763` edge `0.0105` maxDD `-0.1976`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
