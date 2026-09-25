# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T12:22:41.864748+00:00`
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

- `market_context_high->unknown_1h` score `84.5506` n `47` status `ready` deltaP `8.1698` edge `6.9985` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `50.2801` n `47` status `ready` deltaP `30.9434` edge `4.023` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `31.8364` n `47` status `ready` deltaP `24.782` edge `2.5258` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.3287` n `47` status `ready` deltaP `34.5892` edge `1.9157` maxDD `-2.1786`
- `news_risk_high->unknown_1h` score `11.1405` n `111` status `ready` deltaP `3.4161` edge `0.9195` maxDD `-0.4452`
- `market_context_high->index_24h` score `7.7801` n `47` status `ready` deltaP `34.9364` edge `0.4284` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.378` n `47` status `ready` deltaP `37.3153` edge `0.1399` maxDD `-0.2401`
- `news_risk_high->commodity_24h` score `3.0824` n `53` status `ready` deltaP `26.3528` edge `0.116` maxDD `-1.7857`
- `market_context_high->index_4h` score `2.5608` n `47` status `ready` deltaP `29.9105` edge `0.0294` maxDD `-0.2323`
- `market_context_high->equity_4h` score `1.9794` n `47` status `ready` deltaP `13.9433` edge `0.1138` maxDD `-1.3444`
- `market_context_high->crypto_alt_4h` score `0.8808` n `47` status `ready` deltaP `9.5355` edge `0.0766` maxDD `-3.3417`
- `market_context_high->index_1h` score `0.8613` n `47` status `ready` deltaP `13.5622` edge `0.0092` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.8264` n `47` status `ready` deltaP `10.7179` edge `0.0377` maxDD `-1.5564`
- `news_risk_high->crypto_alt_1h` score `0.6306` n `111` status `ready` deltaP `7.682` edge `0.0924` maxDD `-4.2849`
- `market_context_high->fx_1h` score `0.4338` n `47` status `ready` deltaP `9.6604` edge `0.0074` maxDD `-0.1854`
- `market_context_high->metal_1h` score `0.0048` n `47` status `ready` deltaP `3.2775` edge `0.0104` maxDD `-0.1976`
- `news_risk_high->index_1h` score `-0.0059` n `111` status `ready` deltaP `3.4607` edge `0.006` maxDD `-0.3863`
- `news_risk_high->metal_1h` score `-0.0152` n `111` status `ready` deltaP `8.3954` edge `0.0057` maxDD `-0.7016`
- `news_risk_high->equity_1h` score `-0.118` n `111` status `ready` deltaP `1.5173` edge `0.0255` maxDD `-2.0595`
- `market_context_high->crypto_major_1h` score `-0.1494` n `47` status `ready` deltaP `3.1055` edge `0.0486` maxDD `-4.5405`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
