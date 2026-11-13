# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T01:52:31.011473+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11760`

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

- `market_context_high->unknown_24h` score `297.1093` n `84` status `ready` deltaP `6.2996` edge `24.7312` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `62.2562` n `94` status `ready` deltaP `7.8004` edge `5.1808` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `30.5905` n `53` status `ready` deltaP `26.3758` edge `2.444` maxDD `-3.6503`
- `market_context_high->equity_24h` score `22.5731` n `84` status `ready` deltaP `24.1071` edge `1.791` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `12.1707` n `53` status `ready` deltaP `38.7448` edge `1.4986` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `9.4633` n `53` status `ready` deltaP `32.7341` edge `0.6834` maxDD `-7.0416`
- `market_context_high->crypto_alt_24h` score `9.3001` n `84` status `ready` deltaP `44.8661` edge `1.3028` maxDD `-25.4331`
- `news_risk_high->commodity_24h` score `7.0691` n `53` status `ready` deltaP `43.2292` edge `0.3009` maxDD `0.0`
- `market_context_high->metal_24h` score `6.6253` n `84` status `ready` deltaP `40.4266` edge `0.3239` maxDD `-0.3044`
- `news_risk_high->metal_4h` score `4.4906` n `53` status `ready` deltaP `43.0425` edge `0.1249` maxDD `-1.0104`
- `market_context_high->index_24h` score `4.3466` n `84` status `ready` deltaP `24.6776` edge `0.2072` maxDD `-0.0934`
- `news_risk_high->index_24h` score `3.9383` n `53` status `ready` deltaP `22.8806` edge `0.206` maxDD `-0.4279`
- `news_risk_high->commodity_4h` score `3.0837` n `53` status `ready` deltaP `28.0833` edge `0.0951` maxDD `-0.3611`
- `news_risk_high->equity_1h` score `2.994` n `53` status `ready` deltaP `16.8173` edge `0.2004` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `2.6291` n `53` status `ready` deltaP `19.3713` edge `0.2387` maxDD `-9.2335`
- `news_risk_high->metal_1h` score `2.1019` n `53` status `ready` deltaP `24.9915` edge `0.034` maxDD `-0.3692`
- `news_risk_high->crypto_alt_24h` score `1.8625` n `53` status `ready` deltaP `14.9469` edge `0.5897` maxDD `-29.0448`
- `news_risk_high->index_4h` score `1.6895` n `53` status `ready` deltaP `18.0022` edge `0.0644` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.4086` n `53` status `ready` deltaP `24.5168` edge `0.181` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.0944` n `53` status `ready` deltaP `15.5293` edge `0.0178` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
