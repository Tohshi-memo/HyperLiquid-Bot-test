# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T16:37:31.097387+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11296`

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

- `market_context_high->unknown_1h` score `63.3131` n `47` status `ready` deltaP `7.4213` edge `5.2337` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `50.5117` n `47` status `ready` deltaP `30.9434` edge `4.0423` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `31.954` n `47` status `ready` deltaP `24.782` edge `2.5356` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.2807` n `47` status `ready` deltaP `34.5892` edge `1.9117` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.7477` n `47` status `ready` deltaP `34.9364` edge `0.4257` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.2841` n `47` status `ready` deltaP `36.6209` edge `0.1367` maxDD `-0.2401`
- `market_context_high->index_4h` score `2.6762` n `47` status `ready` deltaP `30.9776` edge `0.0319` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.5335` n `47` status `ready` deltaP `16.5347` edge `0.1427` maxDD `-1.3444`
- `news_risk_high->commodity_24h` score `1.9685` n `60` status `ready` deltaP `22.1528` edge `0.0609` maxDD `-2.5637`
- `market_context_high->crypto_alt_4h` score `1.3025` n `47` status `ready` deltaP `10.9075` edge `0.1026` maxDD `-3.3417`
- `market_context_high->equity_1h` score `0.9511` n `47` status `ready` deltaP `11.4664` edge `0.0431` maxDD `-1.5564`
- `market_context_high->index_1h` score `0.8577` n `47` status `ready` deltaP `13.5622` edge `0.0089` maxDD `-0.2275`
- `news_risk_high->crypto_alt_1h` score `0.8489` n `111` status `ready` deltaP `8.7299` edge `0.1036` maxDD `-4.2849`
- `market_context_high->fx_1h` score `0.4218` n `47` status `ready` deltaP `9.5107` edge `0.0074` maxDD `-0.1854`
- `market_context_high->crypto_major_4h` score `0.2518` n `47` status `ready` deltaP `4.385` edge `0.0822` maxDD `-5.2359`
- `market_context_high->crypto_major_1h` score `0.1984` n `47` status `ready` deltaP `4.3031` edge `0.0696` maxDD `-4.5405`
- `market_context_high->metal_1h` score `0.0328` n `47` status `ready` deltaP `3.7266` edge `0.011` maxDD `-0.1976`
- `news_risk_high->metal_1h` score `0.0279` n `111` status `ready` deltaP `8.8445` edge `0.0063` maxDD `-0.7016`
- `news_risk_high->index_1h` score `-0.0082` n `111` status `ready` deltaP `3.4607` edge `0.0057` maxDD `-0.3863`
- `news_risk_high->crypto_major_1h` score `-0.0224` n `111` status `ready` deltaP `3.6131` edge `0.0496` maxDD `-3.3776`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
