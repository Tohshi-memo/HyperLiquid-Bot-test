# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T19:37:28.706654+00:00`
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

- `market_context_high->unknown_1h` score `75.5542` n `47` status `ready` deltaP `7.8704` edge `6.2508` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `50.6269` n `47` status `ready` deltaP `30.9434` edge `4.0519` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `32.0716` n `47` status `ready` deltaP `24.782` edge `2.5454` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.3877` n `47` status `ready` deltaP `34.9364` edge `1.9183` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.7273` n `47` status `ready` deltaP `34.9364` edge `0.424` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.0538` n `47` status `ready` deltaP `34.5375` edge `0.1314` maxDD `-0.2401`
- `market_context_high->equity_4h` score `2.7229` n `47` status `ready` deltaP `17.2969` edge `0.1534` maxDD `-1.3444`
- `market_context_high->index_4h` score `2.681` n `47` status `ready` deltaP `30.9776` edge `0.0323` maxDD `-0.2323`
- `news_risk_high->unknown_1h` score `2.1442` n `111` status `ready` deltaP `3.1167` edge `0.1718` maxDD `-0.4452`
- `market_context_high->crypto_alt_4h` score `1.4653` n `47` status `ready` deltaP `11.5172` edge `0.1121` maxDD `-3.3417`
- `market_context_high->equity_1h` score `1.1104` n `47` status `ready` deltaP `12.8137` edge `0.0474` maxDD `-1.5564`
- `market_context_high->index_1h` score `0.902` n `47` status `ready` deltaP `14.0113` edge `0.0096` maxDD `-0.2275`
- `news_risk_high->crypto_alt_1h` score `0.9004` n `111` status `ready` deltaP `9.179` edge `0.1049` maxDD `-4.2849`
- `market_context_high->fx_1h` score `0.4949` n `47` status `ready` deltaP `10.4089` edge `0.0075` maxDD `-0.1854`
- `market_context_high->crypto_major_4h` score `0.4434` n `47` status `ready` deltaP `4.9948` edge `0.0941` maxDD `-5.2359`
- `market_context_high->crypto_major_1h` score `0.3039` n `47` status `ready` deltaP `5.0516` edge `0.0734` maxDD `-4.5405`
- `news_risk_high->metal_24h` score `0.1448` n `67` status `ready` deltaP `18.2784` edge `0.0628` maxDD `-6.9545`
- `news_risk_high->crypto_major_1h` score `0.0831` n `111` status `ready` deltaP `4.3616` edge `0.0534` maxDD `-3.3776`
- `news_risk_high->equity_1h` score `0.0666` n `111` status `ready` deltaP `3.6131` edge `0.0352` maxDD `-2.0595`
- `news_risk_high->index_1h` score `0.0206` n `111` status `ready` deltaP `3.9098` edge `0.0064` maxDD `-0.3863`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
