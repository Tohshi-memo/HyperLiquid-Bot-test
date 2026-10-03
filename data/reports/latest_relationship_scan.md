# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T03:52:35.208505+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4818`

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

- `market_context_high->unknown_1h` score `365.7153` n `50` status `ready` deltaP `11.1737` edge `30.4067` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `293.2923` n `50` status `ready` deltaP `10.5183` edge `24.3709` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `11.6277` n `70` status `ready` deltaP `22.8968` edge `0.932` maxDD `-6.2533`
- `market_context_high->crypto_alt_24h` score `11.2092` n `50` status `ready` deltaP `22.6111` edge `0.9537` maxDD `-11.6271`
- `news_risk_high->equity_24h` score `10.4414` n `70` status `ready` deltaP `33.7351` edge `0.6937` maxDD `-2.8784`
- `market_context_high->crypto_major_24h` score `8.9374` n `50` status `ready` deltaP `31.3056` edge `0.6777` maxDD `-9.3299`
- `news_risk_high->crypto_alt_4h` score `7.7566` n `94` status `ready` deltaP `32.0543` edge `0.5671` maxDD `-6.4195`
- `news_risk_high->crypto_major_4h` score `7.4362` n `94` status `ready` deltaP `28.4152` edge `0.4698` maxDD `-1.1644`
- `market_context_high->crypto_major_4h` score `7.2577` n `50` status `ready` deltaP `16.628` edge `0.5643` maxDD `-3.294`
- `news_risk_high->crypto_major_24h` score `6.4208` n `70` status `ready` deltaP `12.1627` edge `0.5776` maxDD `-6.8893`
- `market_context_high->crypto_alt_4h` score `5.7922` n `50` status `ready` deltaP `15.8841` edge `0.5057` maxDD `-7.6465`
- `news_risk_high->equity_4h` score `3.403` n `94` status `ready` deltaP `27.6369` edge `0.1606` maxDD `-2.9013`
- `news_risk_high->index_24h` score `3.336` n `70` status `ready` deltaP `29.2758` edge `0.0987` maxDD `-0.2696`
- `market_context_high->crypto_alt_1h` score `3.163` n `50` status `ready` deltaP `14.2036` edge `0.2352` maxDD `-3.6376`
- `market_context_high->crypto_major_1h` score `2.9881` n `50` status `ready` deltaP `13.4012` edge `0.2047` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.7665` n `50` status `ready` deltaP `30.8598` edge `0.0383` maxDD `-0.0791`
- `news_risk_high->crypto_major_1h` score `1.7487` n `94` status `ready` deltaP `8.9757` edge `0.1391` maxDD `-1.5904`
- `news_risk_high->crypto_alt_1h` score `1.6351` n `94` status `ready` deltaP `6.7142` edge `0.1434` maxDD `-2.4854`
- `market_context_high->fx_1h` score `1.4472` n `50` status `ready` deltaP `20.3413` edge `0.0114` maxDD `-0.113`
- `market_context_high->fx_24h` score `1.1957` n `50` status `ready` deltaP `23.4583` edge `0.0987` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
