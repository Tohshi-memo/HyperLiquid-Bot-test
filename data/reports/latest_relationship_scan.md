# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T12:07:27.367007+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11258`

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

- `market_context_high->unknown_1h` score `84.6142` n `47` status `ready` deltaP `8.1698` edge `7.0038` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `50.2573` n `47` status `ready` deltaP `30.9434` edge `4.0211` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `31.8448` n `47` status `ready` deltaP `24.782` edge `2.5265` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.3467` n `47` status `ready` deltaP `34.5892` edge `1.9172` maxDD `-2.1786`
- `news_risk_high->unknown_1h` score `11.2041` n `111` status `ready` deltaP `3.4161` edge `0.9248` maxDD `-0.4452`
- `market_context_high->index_24h` score `7.7849` n `47` status `ready` deltaP `34.9364` edge `0.4288` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.3967` n `47` status `ready` deltaP `37.4889` edge `0.1403` maxDD `-0.2401`
- `news_risk_high->commodity_24h` score `3.089` n `52` status `ready` deltaP `26.1351` edge `0.118` maxDD `-1.7857`
- `market_context_high->index_4h` score `2.5754` n `47` status `ready` deltaP `30.0629` edge `0.0296` maxDD `-0.2323`
- `market_context_high->equity_4h` score `1.9794` n `47` status `ready` deltaP `13.9433` edge `0.1138` maxDD `-1.3444`
- `market_context_high->crypto_alt_4h` score `0.8592` n `47` status `ready` deltaP `9.5355` edge `0.0748` maxDD `-3.3417`
- `market_context_high->index_1h` score `0.8481` n `47` status `ready` deltaP `13.4125` edge `0.0091` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.8096` n `47` status `ready` deltaP `10.5682` edge `0.0373` maxDD `-1.5564`
- `news_risk_high->crypto_alt_1h` score `0.6006` n `111` status `ready` deltaP `7.5323` edge `0.0909` maxDD `-4.2849`
- `market_context_high->fx_1h` score `0.4458` n `47` status `ready` deltaP `9.8101` edge `0.0074` maxDD `-0.1854`
- `market_context_high->metal_1h` score `-0.003` n `47` status `ready` deltaP `3.1278` edge `0.0104` maxDD `-0.1976`
- `news_risk_high->index_1h` score `-0.0145` n `111` status `ready` deltaP `3.311` edge `0.0059` maxDD `-0.3863`
- `news_risk_high->metal_1h` score `-0.0272` n `111` status `ready` deltaP `8.2457` edge `0.0057` maxDD `-0.7016`
- `news_risk_high->equity_1h` score `-0.1289` n `111` status `ready` deltaP `1.3676` edge `0.0251` maxDD `-2.0595`
- `market_context_high->crypto_major_1h` score `-0.177` n `47` status `ready` deltaP `2.9558` edge `0.0473` maxDD `-4.5405`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
