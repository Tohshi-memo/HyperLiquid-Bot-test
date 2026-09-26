# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T13:52:29.309294+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11822`

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

- `news_risk_high->unknown_24h` score `4384.9375` n `85` status `ready` deltaP `0.1736` edge `365.4103` maxDD `0.0`
- `market_context_high->unknown_1h` score `69.301` n `47` status `ready` deltaP `8.1698` edge `5.7277` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `47.0688` n `47` status `ready` deltaP `22.4364` edge `3.8121` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `26.9931` n `47` status `ready` deltaP `17.4904` edge `2.1708` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.6623` n `47` status `ready` deltaP `33.3739` edge `1.9516` maxDD `-2.1786`
- `market_context_high->index_24h` score `6.9606` n `47` status `ready` deltaP `27.992` edge `0.4064` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.357` n `47` status `ready` deltaP `28.2875` edge `0.115` maxDD `-0.2401`
- `market_context_high->index_4h` score `2.7565` n `47` status `ready` deltaP `31.8922` edge `0.0325` maxDD `-0.2323`
- `news_risk_high->crypto_alt_24h` score `2.754` n `85` status `ready` deltaP `11.3828` edge `0.5488` maxDD `-29.2814`
- `market_context_high->equity_4h` score `2.7387` n `47` status `ready` deltaP `17.4494` edge `0.1537` maxDD `-1.3444`
- `news_risk_high->index_24h` score `2.2553` n `85` status `ready` deltaP `26.1397` edge `0.0707` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `1.486` n `85` status `ready` deltaP `31.4665` edge `0.1455` maxDD `-6.8481`
- `market_context_high->crypto_alt_4h` score `1.2965` n `47` status `ready` deltaP `10.9075` edge `0.1021` maxDD `-3.3417`
- `market_context_high->equity_1h` score `1.0625` n `47` status `ready` deltaP `12.2149` edge `0.0474` maxDD `-1.5564`
- `market_context_high->crypto_major_4h` score `0.8493` n `47` status `ready` deltaP `7.1289` edge `0.1137` maxDD `-5.2359`
- `market_context_high->index_1h` score `0.8193` n `47` status `ready` deltaP `12.9634` edge `0.0097` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.4817` n `47` status `ready` deltaP `10.2592` edge `0.0074` maxDD `-0.1854`
- `market_context_high->crypto_major_1h` score `0.4645` n `47` status `ready` deltaP `6.0995` edge `0.0798` maxDD `-4.5405`
- `market_context_high->metal_1h` score `0.0445` n `47` status `ready` deltaP `4.026` edge `0.0105` maxDD `-0.1976`
- `news_risk_high->index_1h` score `-0.0591` n `139` status `ready` deltaP `3.1211` edge `0.0034` maxDD `-0.3305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
