# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-14T14:52:37.953699+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `9384`

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

- `market_context_high->unknown_24h` score `574.1411` n `66` status `ready` deltaP `4.5139` edge `47.815` maxDD `0.0`
- `news_risk_high->equity_24h` score `39.4163` n `53` status `ready` deltaP `39.9175` edge `3.0892` maxDD `-3.6503`
- `market_context_high->equity_24h` score `35.6626` n `66` status `ready` deltaP `34.9432` edge `2.8931` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `23.4782` n `66` status `ready` deltaP `57.7652` edge `1.6791` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `16.8842` n `53` status `ready` deltaP `42.3906` edge `2.0786` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.2118` n `53` status `ready` deltaP `35.6304` edge `0.8098` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `7.1846` n `53` status `ready` deltaP `49.6528` edge `0.2677` maxDD `0.0`
- `market_context_high->index_24h` score `7.1025` n `66` status `ready` deltaP `41.2089` edge `0.3263` maxDD `-0.0653`
- `news_risk_high->index_24h` score `5.7445` n `53` status `ready` deltaP `37.4639` edge `0.2593` maxDD `-0.4279`
- `market_context_high->metal_24h` score `5.2376` n `66` status `ready` deltaP `51.5152` edge `0.4172` maxDD `-3.7989`
- `news_risk_high->metal_4h` score `4.8454` n `53` status `ready` deltaP `45.4815` edge `0.1382` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.1414` n `53` status `ready` deltaP `20.5908` edge `0.3566` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.6679` n `53` status `ready` deltaP `19.5119` edge `0.2386` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.3342` n `53` status `ready` deltaP `30.6748` edge `0.0987` maxDD `-0.3611`
- `news_risk_high->crypto_alt_24h` score `2.4197` n `53` status `ready` deltaP `14.4261` edge `0.6646` maxDD `-29.0448`
- `news_risk_high->index_4h` score `2.3235` n `53` status `ready` deltaP `23.9473` edge `0.0776` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `2.2776` n `53` status `ready` deltaP `26.4985` edge `0.2792` maxDD `-10.1088`
- `news_risk_high->metal_1h` score `2.2469` n `53` status `ready` deltaP `26.1891` edge `0.0381` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3244` n `53` status `ready` deltaP `17.7748` edge `0.022` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.856` n `53` status `ready` deltaP `18.1928` edge `0.0864` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
