# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T13:22:32.137818+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9102`

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

- `market_context_high->unknown_4h` score `31.7965` n `58` status `ready` deltaP `1.23` edge `2.6565` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `20.1966` n `101` status `ready` deltaP `7.797` edge `2.3169` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `14.3142` n `101` status `ready` deltaP `8.182` edge `1.6264` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `3.3496` n `101` status `ready` deltaP `16.48` edge `0.2902` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.0749` n `101` status `ready` deltaP `19.8337` edge `0.2498` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.3745` n `101` status `ready` deltaP `14.7344` edge `0.1462` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `1.7751` n `101` status `ready` deltaP `16.5308` edge `0.09` maxDD `-2.8494`
- `news_risk_high->commodity_24h` score `1.3353` n `101` status `ready` deltaP `23.8913` edge `0.1425` maxDD `-3.4467`
- `market_context_high->equity_1h` score `0.766` n `58` status `ready` deltaP `5.5596` edge `0.0521` maxDD `-0.36`
- `market_context_high->index_1h` score `0.6322` n `58` status `ready` deltaP `9.6789` edge `0.0137` maxDD `-0.0435`
- `news_risk_high->metal_1h` score `0.4555` n `101` status `ready` deltaP `13.101` edge `0.0108` maxDD `-0.8144`
- `market_context_high->fx_1h` score `0.4097` n `58` status `ready` deltaP `9.5241` edge `0.0063` maxDD `-0.1854`
- `news_risk_high->fx_4h` score `0.3269` n `101` status `ready` deltaP `9.8602` edge `0.0251` maxDD `-0.421`
- `news_risk_high->metal_4h` score `0.2799` n `101` status `ready` deltaP `14.6598` edge `0.031` maxDD `-2.0994`
- `market_context_high->index_4h` score `0.2537` n `58` status `ready` deltaP `13.5618` edge `0.0058` maxDD `-1.0949`
- `market_context_high->metal_1h` score `0.1776` n `58` status `ready` deltaP `4.6511` edge `0.0146` maxDD `-0.1314`
- `news_risk_high->fx_1h` score `-0.1393` n `101` status `ready` deltaP `3.8907` edge `0.0068` maxDD `-0.2147`
- `news_risk_high->equity_1h` score `-0.3089` n `101` status `ready` deltaP `1.1724` edge `0.007` maxDD `-0.9112`
- `market_context_high->fx_4h` score `-0.4235` n `58` status `ready` deltaP `1.6663` edge `-0.003` maxDD `-0.6588`
- `news_risk_high->metal_24h` score `-0.4819` n `101` status `ready` deltaP `8.7355` edge `-0.0356` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
