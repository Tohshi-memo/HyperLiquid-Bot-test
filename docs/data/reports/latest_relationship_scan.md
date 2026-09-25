# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T18:52:37.773835+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11312`

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

- `market_context_high->unknown_1h` score `66.6382` n `47` status `ready` deltaP `7.7207` edge `5.5088` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `50.6317` n `47` status `ready` deltaP `30.9434` edge `4.0523` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `32.0848` n `47` status `ready` deltaP `24.782` edge `2.5465` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.3769` n `47` status `ready` deltaP `34.9364` edge `1.9174` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.7357` n `47` status `ready` deltaP `34.9364` edge `0.4247` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.1087` n `47` status `ready` deltaP `35.0584` edge `0.1325` maxDD `-0.2401`
- `market_context_high->equity_4h` score `2.7121` n `47` status `ready` deltaP `17.2969` edge `0.1525` maxDD `-1.3444`
- `market_context_high->index_4h` score `2.6834` n `47` status `ready` deltaP `30.9776` edge `0.0325` maxDD `-0.2323`
- `market_context_high->crypto_alt_4h` score `1.4833` n `47` status `ready` deltaP `11.5172` edge `0.1136` maxDD `-3.3417`
- `market_context_high->equity_1h` score `1.0661` n `47` status `ready` deltaP `12.5143` edge `0.0457` maxDD `-1.5564`
- `news_risk_high->crypto_alt_1h` score `0.9028` n `111` status `ready` deltaP `9.179` edge `0.1051` maxDD `-4.2849`
- `market_context_high->index_1h` score `0.8864` n `47` status `ready` deltaP `13.8616` edge `0.0093` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.4829` n `47` status `ready` deltaP `10.2592` edge `0.0075` maxDD `-0.1854`
- `market_context_high->crypto_major_4h` score `0.4676` n `47` status `ready` deltaP `5.1472` edge `0.0951` maxDD `-5.2359`
- `news_risk_high->commodity_24h` score `0.3423` n `64` status `ready` deltaP `17.1875` edge `0.015` maxDD `-5.7513`
- `market_context_high->crypto_major_1h` score `0.3015` n `47` status `ready` deltaP `5.0516` edge `0.0732` maxDD `-4.5405`
- `news_risk_high->crypto_major_1h` score `0.0807` n `111` status `ready` deltaP `4.3616` edge `0.0532` maxDD `-3.3776`
- `news_risk_high->equity_1h` score `0.0378` n `111` status `ready` deltaP `3.3137` edge `0.0335` maxDD `-2.0595`
- `market_context_high->metal_1h` score `0.0211` n `47` status `ready` deltaP `3.5769` edge `0.0105` maxDD `-0.1976`
- `news_risk_high->index_1h` score `0.0104` n `111` status `ready` deltaP `3.7601` edge `0.0061` maxDD `-0.3863`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
