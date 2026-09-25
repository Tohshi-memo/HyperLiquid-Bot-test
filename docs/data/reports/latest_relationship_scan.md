# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T09:07:34.909441+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11206`

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

- `market_context_high->unknown_1h` score `84.8481` n `47` status `ready` deltaP `8.4693` edge `7.0213` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `50.1853` n `47` status `ready` deltaP `30.9434` edge `4.0151` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `32.2768` n `47` status `ready` deltaP `24.782` edge `2.5625` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.7571` n `47` status `ready` deltaP `34.5892` edge `1.9514` maxDD `-2.1786`
- `news_risk_high->unknown_1h` score `11.4381` n `111` status `ready` deltaP `3.7156` edge `0.9423` maxDD `-0.4452`
- `market_context_high->index_24h` score `7.9764` n `47` status `ready` deltaP `36.3253` edge `0.4355` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.6774` n `47` status `ready` deltaP `39.5723` edge `0.1498` maxDD `-0.2401`
- `news_risk_high->commodity_24h` score `3.6406` n `47` status `ready` deltaP `30.0753` edge `0.1377` maxDD `-1.7857`
- `market_context_high->index_4h` score `2.7637` n `47` status `ready` deltaP `31.8922` edge `0.0331` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.2695` n `47` status `ready` deltaP `15.6201` edge `0.1268` maxDD `-1.3444`
- `market_context_high->crypto_alt_4h` score `1.0608` n `47` status `ready` deltaP `9.5355` edge `0.0916` maxDD `-3.3417`
- `market_context_high->equity_1h` score `0.9127` n `47` status `ready` deltaP `11.3167` edge `0.0409` maxDD `-1.5564`
- `market_context_high->index_1h` score `0.9044` n `47` status `ready` deltaP `14.0113` edge `0.0098` maxDD `-0.2275`
- `news_risk_high->crypto_alt_1h` score `0.7326` n `111` status `ready` deltaP `7.9814` edge `0.0989` maxDD `-4.2849`
- `market_context_high->fx_1h` score `0.4709` n `47` status `ready` deltaP `10.1095` edge `0.0075` maxDD `-0.1854`
- `market_context_high->metal_1h` score `0.0321` n `47` status `ready` deltaP `3.5769` edge `0.0119` maxDD `-0.1976`
- `news_risk_high->metal_1h` score `0.0267` n `111` status `ready` deltaP `8.6948` edge `0.0072` maxDD `-0.7016`
- `news_risk_high->index_1h` score `0.0221` n `111` status `ready` deltaP `3.9098` edge `0.0066` maxDD `-0.3863`
- `market_context_high->crypto_major_1h` score `-0.0523` n `47` status `ready` deltaP `3.2552` edge `0.0557` maxDD `-4.5405`
- `news_risk_high->equity_1h` score `-0.0619` n `111` status `ready` deltaP `2.1161` edge `0.0287` maxDD `-2.0595`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
