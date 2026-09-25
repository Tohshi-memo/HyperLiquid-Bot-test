# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T14:22:36.489198+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11076`

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

- `market_context_high->unknown_1h` score `63.9898` n `47` status `ready` deltaP `7.8704` edge `5.2871` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `50.4109` n `47` status `ready` deltaP `30.9434` edge `4.0339` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `31.7956` n `47` status `ready` deltaP `24.782` edge `2.5224` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.2495` n `47` status `ready` deltaP `34.5892` edge `1.9091` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.7585` n `47` status `ready` deltaP `34.9364` edge `0.4266` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.3382` n `47` status `ready` deltaP `36.9681` edge `0.1389` maxDD `-0.2401`
- `news_risk_high->commodity_24h` score `2.9951` n `57` status `ready` deltaP `26.6265` edge `0.1069` maxDD `-1.7857`
- `market_context_high->index_4h` score `2.573` n `47` status `ready` deltaP `30.0629` edge `0.0294` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.1754` n `47` status `ready` deltaP `15.1628` edge `0.122` maxDD `-1.3444`
- `market_context_high->crypto_alt_4h` score `0.9892` n `47` status `ready` deltaP `9.8404` edge `0.0836` maxDD `-3.3417`
- `market_context_high->equity_1h` score `0.9355` n `47` status `ready` deltaP `11.3167` edge `0.0428` maxDD `-1.5564`
- `market_context_high->index_1h` score `0.8864` n `47` status `ready` deltaP `13.8616` edge `0.0093` maxDD `-0.2275`
- `news_risk_high->crypto_alt_1h` score `0.8369` n `111` status `ready` deltaP `8.5802` edge `0.1036` maxDD `-4.2849`
- `market_context_high->fx_1h` score `0.447` n `47` status `ready` deltaP `9.8101` edge `0.0075` maxDD `-0.1854`
- `market_context_high->crypto_major_1h` score `0.1648` n `47` status `ready` deltaP `4.0037` edge `0.0688` maxDD `-4.5405`
- `market_context_high->metal_1h` score `0.0258` n `47` status `ready` deltaP `3.5769` edge `0.0111` maxDD `-0.1976`
- `news_risk_high->metal_1h` score `0.0171` n `111` status `ready` deltaP `8.6948` edge `0.0064` maxDD `-0.7016`
- `news_risk_high->index_1h` score `0.0104` n `111` status `ready` deltaP `3.7601` edge `0.0061` maxDD `-0.3863`
- `news_risk_high->equity_1h` score `-0.0471` n `111` status `ready` deltaP `2.1161` edge `0.0306` maxDD `-2.0595`
- `news_risk_high->crypto_major_1h` score `-0.0559` n `111` status `ready` deltaP `3.3137` edge `0.0488` maxDD `-3.3776`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
