# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T12:07:33.325212+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11822`

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

- `news_risk_high->unknown_24h` score `4434.4171` n `86` status `ready` deltaP `0.1736` edge `369.5336` maxDD `0.0`
- `market_context_high->unknown_1h` score `69.5061` n `47` status `ready` deltaP `8.4693` edge `5.7428` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `47.2896` n `47` status `ready` deltaP `22.4364` edge `3.8305` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `27.6879` n `47` status `ready` deltaP `18.7056` edge `2.2206` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.6059` n `47` status `ready` deltaP `33.3739` edge `1.9469` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.0523` n `47` status `ready` deltaP `29.0337` edge `0.4071` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.4336` n `47` status `ready` deltaP `29.1556` edge `0.1156` maxDD `-0.2401`
- `market_context_high->equity_4h` score `2.7521` n `47` status `ready` deltaP `17.6018` edge `0.1538` maxDD `-1.3444`
- `news_risk_high->crypto_alt_24h` score `2.7263` n `86` status `ready` deltaP `11.531` edge `0.5455` maxDD `-29.2814`
- `market_context_high->index_4h` score `2.6676` n `47` status `ready` deltaP `30.8251` edge `0.0322` maxDD `-0.2323`
- `news_risk_high->index_24h` score `2.234` n `86` status `ready` deltaP `26.1144` edge `0.0691` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `1.4818` n `86` status `ready` deltaP `31.4317` edge `0.1452` maxDD `-6.8481`
- `market_context_high->crypto_alt_4h` score `1.3097` n `47` status `ready` deltaP `10.9075` edge `0.1032` maxDD `-3.3417`
- `market_context_high->equity_1h` score `1.0242` n `47` status `ready` deltaP `11.7658` edge `0.0472` maxDD `-1.5564`
- `market_context_high->crypto_major_4h` score `0.8107` n `47` status `ready` deltaP `6.9765` edge `0.1115` maxDD `-5.2359`
- `market_context_high->index_1h` score `0.8074` n `47` status `ready` deltaP `12.8137` edge `0.0097` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.4698` n `47` status `ready` deltaP `10.1095` edge `0.0074` maxDD `-0.1854`
- `market_context_high->crypto_major_1h` score `0.3806` n `47` status `ready` deltaP `5.5007` edge `0.0768` maxDD `-4.5405`
- `market_context_high->metal_1h` score `0.0367` n `47` status `ready` deltaP `3.8763` edge `0.0105` maxDD `-0.1976`
- `news_risk_high->index_1h` score `-0.0022` n `137` status `ready` deltaP `3.7906` edge `0.0037` maxDD `-0.3322`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
