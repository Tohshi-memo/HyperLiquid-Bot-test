# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T07:07:27.599338+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4007`

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

- `news_risk_high->unknown_4h` score `3230.7307` n `31` status `ready` deltaP `3.4815` edge `269.21` maxDD `-0.1191`
- `news_risk_high->unknown_1h` score `3220.7977` n `31` status `ready` deltaP `1.6322` edge `268.4065` maxDD `-0.7395`
- `market_context_high->unknown_1h` score `90.5058` n `31` status `ready` deltaP `1.6322` edge `7.5407` maxDD `-0.4209`
- `news_risk_high->equity_24h` score `40.542` n `31` status `ready` deltaP `46.875` edge `3.066` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `38.7958` n `31` status `ready` deltaP `47.7431` edge `2.9147` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `33.2035` n `31` status `ready` deltaP `47.0486` edge `2.4533` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `10.8947` n `31` status `ready` deltaP `26.9128` edge `0.8155` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.5084` n `31` status `ready` deltaP `38.1393` edge `0.6695` maxDD `-2.178`
- `news_risk_high->metal_24h` score `9.7697` n `31` status `ready` deltaP `33.423` edge `0.6188` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `6.8479` n `31` status `ready` deltaP `17.8452` edge `0.9007` maxDD `-7.6714`
- `news_risk_high->index_24h` score `6.6595` n `31` status `ready` deltaP `48.2639` edge `0.2332` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.3655` n `31` status `ready` deltaP `45.8782` edge `0.1541` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.771` n `31` status `ready` deltaP `20.5862` edge `0.1957` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.4444` n `31` status `ready` deltaP `37.0722` edge `0.0659` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7333` n `31` status `ready` deltaP `32.2919` edge `0.021` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.5086` n `31` status `ready` deltaP `10.31` edge `0.299` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.2853` n `31` status `ready` deltaP `13.1543` edge `0.241` maxDD `-1.5232`
- `market_context_high->fx_4h` score `2.1238` n `31` status `ready` deltaP `26.9621` edge `0.0257` maxDD `-0.2774`
- `news_risk_high->metal_1h` score `1.5181` n `31` status `ready` deltaP `29.5827` edge `0.0253` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.1054` n `31` status `ready` deltaP `16.7781` edge `0.0856` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
