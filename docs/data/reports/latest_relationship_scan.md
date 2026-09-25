# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T14:52:31.990342+00:00`
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

- `market_context_high->unknown_1h` score `63.4787` n `47` status `ready` deltaP `7.571` edge `5.2465` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `50.4193` n `47` status `ready` deltaP `30.9434` edge `4.0346` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `31.8304` n `47` status `ready` deltaP `24.782` edge `2.5253` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.2699` n `47` status `ready` deltaP `34.5892` edge `1.9108` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.7585` n `47` status `ready` deltaP `34.9364` edge `0.4266` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.3394` n `47` status `ready` deltaP `36.9681` edge `0.139` maxDD `-0.2401`
- `news_risk_high->commodity_24h` score `2.9999` n `57` status `ready` deltaP `26.6265` edge `0.1073` maxDD `-1.7857`
- `market_context_high->index_4h` score `2.6034` n `47` status `ready` deltaP `30.3678` edge `0.0299` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.2526` n `47` status `ready` deltaP `15.4677` edge `0.1264` maxDD `-1.3444`
- `market_context_high->crypto_alt_4h` score `1.0314` n `47` status `ready` deltaP `9.9928` edge `0.0861` maxDD `-3.3417`
- `market_context_high->equity_1h` score `0.9727` n `47` status `ready` deltaP `11.4664` edge `0.0449` maxDD `-1.5564`
- `market_context_high->index_1h` score `0.89` n `47` status `ready` deltaP `13.8616` edge `0.0096` maxDD `-0.2275`
- `news_risk_high->crypto_alt_1h` score `0.8752` n `111` status `ready` deltaP `8.8796` edge `0.1048` maxDD `-4.2849`
- `market_context_high->fx_1h` score `0.4326` n `47` status `ready` deltaP `9.6604` edge `0.0073` maxDD `-0.1854`
- `market_context_high->crypto_major_1h` score `0.1816` n `47` status `ready` deltaP `4.1534` edge `0.0692` maxDD `-4.5405`
- `market_context_high->metal_1h` score `0.0359` n `47` status `ready` deltaP `3.7266` edge `0.0114` maxDD `-0.1976`
- `news_risk_high->metal_1h` score `0.0327` n `111` status `ready` deltaP `8.8445` edge `0.0067` maxDD `-0.7016`
- `news_risk_high->index_1h` score `0.0128` n `111` status `ready` deltaP `3.7601` edge `0.0064` maxDD `-0.3863`
- `news_risk_high->equity_1h` score `-0.0229` n `111` status `ready` deltaP `2.2658` edge `0.0327` maxDD `-2.0595`
- `news_risk_high->crypto_major_1h` score `-0.0392` n `111` status `ready` deltaP `3.4634` edge `0.0492` maxDD `-3.3776`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
