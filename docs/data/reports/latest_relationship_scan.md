# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T09:52:18.097950+00:00`
- Price records: `672`
- Market context records: `2445`
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

- `news_risk_high->crypto_alt_24h` score `19.2206` n `43` status `ready` deltaP `43.0919` edge `1.3733` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `19.0437` n `43` status `ready` deltaP `53.7508` edge `1.2726` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.7643` n `43` status `ready` deltaP `29.7925` edge `1.0632` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `9.4414` n `43` status `ready` deltaP `16.6424` edge `0.7339` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `7.0067` n `43` status `ready` deltaP `23.4738` edge `0.45` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `5.8931` n `107` status `ready` deltaP `22.5175` edge `0.3738` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `5.03` n `124` status `ready` deltaP `23.215` edge `0.4454` maxDD `-10.1468`
- `news_risk_high->index_24h` score `4.9615` n `43` status `ready` deltaP `8.9309` edge `0.3958` maxDD `-1.3507`
- `market_context_high->crypto_alt_4h` score `4.841` n `124` status `ready` deltaP `23.3428` edge `0.5157` maxDD `-15.4319`
- `news_risk_high->commodity_4h` score `3.1807` n `43` status `ready` deltaP `28.6514` edge `0.2839` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.1686` n `43` status `ready` deltaP `33.0629` edge `0.0621` maxDD `-0.1442`
- `market_context_high->unknown_4h` score `2.6342` n `124` status `ready` deltaP `13.2278` edge `0.1923` maxDD `-1.8773`
- `market_context_high->crypto_major_24h` score `2.4935` n `107` status `ready` deltaP `11.361` edge `0.6332` maxDD `-25.1408`
- `news_risk_high->fx_4h` score `2.1098` n `43` status `ready` deltaP `26.8221` edge `0.0154` maxDD `-0.1382`
- `market_context_high->index_24h` score `1.7343` n `107` status `ready` deltaP `8.3658` edge `0.1192` maxDD `-0.436`
- `news_risk_high->unknown_4h` score `1.7045` n `43` status `ready` deltaP `15.5346` edge `0.1108` maxDD `-2.7857`
- `news_risk_high->unknown_1h` score `1.0809` n `43` status `ready` deltaP `20.2966` edge `0.0017` maxDD `-1.7548`
- `market_context_high->crypto_major_1h` score `0.8918` n `134` status `ready` deltaP `9.5451` edge `0.1301` maxDD `-4.2199`
- `market_context_high->crypto_alt_1h` score `0.8023` n `134` status `ready` deltaP `8.2045` edge `0.1309` maxDD `-6.1656`
- `market_context_high->index_4h` score `0.5927` n `124` status `ready` deltaP `13.0606` edge `0.0449` maxDD `-2.2732`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
