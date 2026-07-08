# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T19:37:31.686171+00:00`
- Price records: `672`
- Market context records: `6117`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11131`

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

- `news_risk_high->crypto_alt_24h` score `9.4293` n `30` status `ready` deltaP `37.0833` edge `0.5533` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `7.9441` n `30` status `ready` deltaP `70.4861` edge `0.1921` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.2275` n `32` status `ready` deltaP `43.9787` edge `0.0637` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3668` n `32` status `ready` deltaP `28.4431` edge `0.0215` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.2332` n `32` status `ready` deltaP `13.5292` edge `0.1146` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.8175` n `195` status `ready` deltaP `6.0366` edge `0.1196` maxDD `-2.671`
- `news_risk_high->crypto_alt_1h` score `0.6011` n `32` status `ready` deltaP `8.3271` edge `0.0677` maxDD `-1.6923`
- `news_risk_high->index_24h` score `-0.0234` n `30` status `ready` deltaP `8.8889` edge `0.0249` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.2918` n `195` status `ready` deltaP `1.1354` edge `-0.0004` maxDD `-0.5659`
- `news_risk_high->commodity_24h` score `-0.4783` n `30` status `ready` deltaP `14.0973` edge `-0.1133` maxDD `-0.3101`
- `market_context_high->metal_4h` score `-0.6996` n `195` status `ready` deltaP `2.9323` edge `0.0095` maxDD `-3.4996`
- `market_context_high->commodity_1h` score `-0.7236` n `195` status `ready` deltaP `-1.8394` edge `-0.0034` maxDD `-0.5708`
- `market_context_high->equity_1h` score `-0.7604` n `195` status `ready` deltaP `-0.1098` edge `0.0148` maxDD `-4.2573`
- `news_risk_high->metal_1h` score `-0.8096` n `32` status `ready` deltaP `-3.4431` edge `-0.0311` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.8799` n `195` status `ready` deltaP `1.9415` edge `-0.0064` maxDD `-2.0564`
- `market_context_high->index_4h` score `-0.946` n `195` status `ready` deltaP `0.9365` edge `0.0189` maxDD `-1.381`
- `market_context_high->crypto_major_1h` score `-0.9648` n `195` status `ready` deltaP `4.3145` edge `0.0243` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-0.9748` n `195` status `ready` deltaP `3.3111` edge `0.0282` maxDD `-9.3536`
- `news_risk_high->index_1h` score `-1.1622` n `32` status `ready` deltaP `-10.7223` edge `-0.0212` maxDD `-1.1725`
- `market_context_high->index_1h` score `-1.315` n `195` status `ready` deltaP `-3.655` edge `0.0017` maxDD `-0.9531`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
