# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-14T11:52:31.774780+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `9354`

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

- `market_context_high->unknown_24h` score `560.7575` n `67` status `ready` deltaP `4.5139` edge `46.6997` maxDD `0.0`
- `news_risk_high->equity_24h` score `38.4696` n `53` status `ready` deltaP `37.8342` edge `3.0242` maxDD `-3.6503`
- `market_context_high->equity_24h` score `34.2012` n `67` status `ready` deltaP `33.1313` edge `2.7834` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `22.3029` n `67` status `ready` deltaP `56.4988` edge `1.5896` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `16.1353` n `53` status `ready` deltaP `42.0434` edge `1.9849` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.2304` n `53` status `ready` deltaP `36.0877` edge `0.8083` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `6.9364` n `53` status `ready` deltaP `47.5694` edge `0.2609` maxDD `0.0`
- `market_context_high->index_24h` score `6.8129` n `67` status `ready` deltaP `39.2387` edge `0.3153` maxDD `-0.0653`
- `news_risk_high->index_24h` score `5.5095` n `53` status `ready` deltaP `35.3806` edge `0.2536` maxDD `-0.4279`
- `market_context_high->metal_24h` score `5.0843` n `67` status `ready` deltaP `50.2488` edge `0.406` maxDD `-3.7989`
- `news_risk_high->metal_4h` score `4.8953` n `53` status `ready` deltaP `46.0913` edge `0.1383` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.0616` n `53` status `ready` deltaP `21.0481` edge `0.3469` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.5768` n `53` status `ready` deltaP `18.7634` edge `0.236` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.2199` n `53` status `ready` deltaP `29.4553` edge `0.0973` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.1823` n `53` status `ready` deltaP `25.4406` edge `0.0377` maxDD `-0.3692`
- `news_risk_high->crypto_alt_4h` score `2.1692` n `53` status `ready` deltaP `26.4985` edge `0.2653` maxDD `-10.1088`
- `news_risk_high->index_4h` score `2.1687` n `53` status `ready` deltaP `22.118` edge `0.0769` maxDD `-0.8235`
- `news_risk_high->crypto_alt_24h` score `1.8978` n `53` status `ready` deltaP `14.4261` edge `0.5977` maxDD `-29.0448`
- `news_risk_high->index_1h` score `1.2382` n `53` status `ready` deltaP `16.7269` edge `0.0218` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.7367` n `53` status `ready` deltaP `17.594` edge `0.0751` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
