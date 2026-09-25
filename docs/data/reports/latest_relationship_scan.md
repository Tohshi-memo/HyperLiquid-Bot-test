# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T18:07:30.692180+00:00`
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

- `market_context_high->unknown_1h` score `64.0846` n `47` status `ready` deltaP `7.7207` edge `5.296` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `50.6221` n `47` status `ready` deltaP `30.9434` edge `4.0515` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `32.0944` n `47` status `ready` deltaP `24.782` edge `2.5473` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.3426` n `47` status `ready` deltaP `34.7628` edge `1.9157` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.7417` n `47` status `ready` deltaP `34.9364` edge `0.4252` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.1659` n `47` status `ready` deltaP `35.5792` edge `0.1338` maxDD `-0.2401`
- `market_context_high->equity_4h` score `2.7061` n `47` status `ready` deltaP `17.2969` edge `0.152` maxDD `-1.3444`
- `market_context_high->index_4h` score `2.6858` n `47` status `ready` deltaP `30.9776` edge `0.0327` maxDD `-0.2323`
- `news_risk_high->commodity_24h` score `1.6172` n `61` status `ready` deltaP `20.7594` edge `0.0546` maxDD `-3.3249`
- `market_context_high->crypto_alt_4h` score `1.4881` n `47` status `ready` deltaP `11.5172` edge `0.114` maxDD `-3.3417`
- `market_context_high->equity_1h` score `1.0122` n `47` status `ready` deltaP `12.0652` edge `0.0442` maxDD `-1.5564`
- `news_risk_high->crypto_alt_1h` score `0.9064` n `111` status `ready` deltaP `9.179` edge `0.1054` maxDD `-4.2849`
- `market_context_high->index_1h` score `0.884` n `47` status `ready` deltaP `13.8616` edge `0.0091` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.4698` n `47` status `ready` deltaP `10.1095` edge `0.0074` maxDD `-0.1854`
- `market_context_high->crypto_major_4h` score `0.4604` n `47` status `ready` deltaP `5.1472` edge `0.0945` maxDD `-5.2359`
- `market_context_high->crypto_major_1h` score `0.2967` n `47` status `ready` deltaP `5.0516` edge `0.0728` maxDD `-4.5405`
- `news_risk_high->crypto_major_1h` score `0.0759` n `111` status `ready` deltaP `4.3616` edge `0.0528` maxDD `-3.3776`
- `market_context_high->metal_1h` score `0.0406` n `47` status `ready` deltaP `3.8763` edge `0.011` maxDD `-0.1976`
- `news_risk_high->metal_1h` score `0.0399` n `111` status `ready` deltaP `8.9942` edge `0.0063` maxDD `-0.7016`
- `news_risk_high->index_1h` score `0.0089` n `111` status `ready` deltaP `3.7601` edge `0.0059` maxDD `-0.3863`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
