# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T18:52:33.850362+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11734`

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

- `market_context_high->unknown_24h` score `305.3683` n `84` status `ready` deltaP `6.4425` edge `25.4185` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `83.4654` n `94` status `ready` deltaP `8.1053` edge `6.9462` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `28.2183` n `53` status `ready` deltaP `22.4326` edge `2.2726` maxDD `-3.6503`
- `market_context_high->equity_24h` score `20.2009` n `84` status `ready` deltaP `20.1639` edge `1.6196` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `11.3192` n `53` status `ready` deltaP `37.0699` edge `1.4006` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `9.2757` n `53` status `ready` deltaP `32.4292` edge `0.6698` maxDD `-7.0416`
- `market_context_high->crypto_alt_24h` score `7.9478` n `84` status `ready` deltaP `40.1137` edge `1.1611` maxDD `-25.4331`
- `news_risk_high->commodity_24h` score `7.4826` n `53` status `ready` deltaP `43.2526` edge `0.3352` maxDD `0.0`
- `market_context_high->metal_24h` score `6.1823` n `84` status `ready` deltaP `38.8491` edge `0.2975` maxDD `-0.3044`
- `news_risk_high->metal_4h` score `4.7232` n `53` status `ready` deltaP `44.7193` edge `0.1331` maxDD `-1.0104`
- `market_context_high->index_24h` score `3.9634` n `84` status `ready` deltaP `22.1371` edge `0.1922` maxDD `-0.0934`
- `news_risk_high->index_24h` score `3.555` n `53` status `ready` deltaP `20.3401` edge `0.191` maxDD `-0.4279`
- `news_risk_high->commodity_4h` score `3.0195` n `53` status `ready` deltaP `26.7114` edge `0.0989` maxDD `-0.3611`
- `news_risk_high->equity_1h` score `3.0` n `53` status `ready` deltaP `16.8173` edge `0.2009` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `2.9876` n `53` status `ready` deltaP `21.0481` edge `0.2574` maxDD `-9.2335`
- `news_risk_high->metal_1h` score `2.217` n `53` status `ready` deltaP `26.0394` edge `0.0366` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.6773` n `53` status `ready` deltaP `17.8497` edge `0.0644` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.61` n `53` status `ready` deltaP `25.7363` edge `0.1987` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.1819` n `53` status `ready` deltaP `16.4275` edge `0.0191` maxDD `-0.4103`
- `market_context_high->fx_24h` score `0.5729` n `84` status `ready` deltaP `23.896` edge `0.0484` maxDD `-3.4642`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
