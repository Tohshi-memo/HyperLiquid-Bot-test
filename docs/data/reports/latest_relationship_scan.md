# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T10:52:20.265868+00:00`
- Price records: `672`
- Market context records: `2449`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9222`

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

- `news_risk_high->crypto_alt_24h` score `19.3085` n `43` status `ready` deltaP `43.7863` edge `1.376` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `19.1449` n `43` status `ready` deltaP `54.4452` edge `1.2764` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.7175` n `43` status `ready` deltaP `29.7925` edge `1.0593` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `9.3694` n `43` status `ready` deltaP `16.6424` edge `0.7279` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `6.9034` n `43` status `ready` deltaP `23.1266` edge `0.4437` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `5.9288` n `109` status `ready` deltaP `22.2732` edge `0.3784` maxDD `-1.626`
- `news_risk_high->index_24h` score `4.9591` n `43` status `ready` deltaP `8.9309` edge `0.3956` maxDD `-1.3507`
- `market_context_high->crypto_major_4h` score `4.8613` n `126` status `ready` deltaP `22.6215` edge `0.4353` maxDD `-10.1468`
- `market_context_high->crypto_alt_4h` score `4.6065` n `126` status `ready` deltaP `22.4957` edge `0.5018` maxDD `-15.4319`
- `news_risk_high->commodity_4h` score `3.1815` n `43` status `ready` deltaP `28.6514` edge `0.284` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.1396` n `43` status `ready` deltaP `32.7156` edge `0.062` maxDD `-0.1442`
- `market_context_high->crypto_major_24h` score `2.543` n `109` status `ready` deltaP `12.0126` edge `0.6352` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `2.4084` n `126` status `ready` deltaP `12.1153` edge `0.1809` maxDD `-1.8773`
- `news_risk_high->fx_4h` score `2.122` n `43` status `ready` deltaP `26.9746` edge `0.0154` maxDD `-0.1382`
- `news_risk_high->unknown_4h` score `1.6671` n `43` status `ready` deltaP `15.3822` edge `0.1087` maxDD `-2.7857`
- `market_context_high->index_24h` score `1.4035` n `109` status `ready` deltaP `6.9253` edge `0.1114` maxDD `-0.5824`
- `news_risk_high->unknown_1h` score `1.1924` n `43` status `ready` deltaP `20.7457` edge `0.008` maxDD `-1.7548`
- `market_context_high->crypto_major_1h` score `0.8561` n `136` status `ready` deltaP `9.233` edge `0.1292` maxDD `-4.2199`
- `market_context_high->crypto_alt_1h` score `0.7464` n `136` status `ready` deltaP `7.9253` edge `0.1281` maxDD `-6.1656`
- `news_risk_high->commodity_1h` score `0.5297` n `43` status `ready` deltaP `8.9681` edge `0.0761` maxDD `-2.1052`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
