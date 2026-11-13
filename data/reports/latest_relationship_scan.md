# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T18:37:23.451648+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10554`

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

- `market_context_high->unknown_24h` score `370.4036` n `75` status `ready` deltaP `2.8889` edge `30.8618` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `33.7701` n `53` status `ready` deltaP `32.6258` edge `2.6673` maxDD `-3.6503`
- `market_context_high->equity_24h` score `25.5365` n `75` status `ready` deltaP `27.1666` edge `2.1011` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `17.3682` n `75` status `ready` deltaP `48.7986` edge `1.3735` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `14.4061` n `53` status `ready` deltaP `42.0434` edge `1.7632` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `10.956` n `53` status `ready` deltaP `34.5633` edge `0.7956` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `5.666` n `53` status `ready` deltaP `36.8056` edge `0.2268` maxDD `0.0`
- `market_context_high->index_24h` score `4.8706` n `75` status `ready` deltaP `25.9098` edge `0.2423` maxDD `-0.0653`
- `news_risk_high->metal_4h` score `4.767` n `53` status `ready` deltaP `45.1766` edge `0.1337` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.1896` n `53` status `ready` deltaP `23.9223` edge `0.22` maxDD `-0.4279`
- `market_context_high->metal_24h` score `3.9682` n `75` status `ready` deltaP `39.9445` edge `0.3316` maxDD `-3.7989`
- `news_risk_high->equity_1h` score `3.3707` n `53` status `ready` deltaP `17.2664` edge `0.2288` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.1919` n `53` status `ready` deltaP `29.1504` edge `0.097` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `3.1681` n `53` status `ready` deltaP `19.5237` edge `0.2826` maxDD `-9.2335`
- `news_risk_high->metal_1h` score `2.1966` n `53` status `ready` deltaP `25.74` edge `0.0369` maxDD `-0.3692`
- `news_risk_high->crypto_alt_24h` score `2.0835` n `53` status `ready` deltaP `15.6413` edge `0.6134` maxDD `-29.0448`
- `news_risk_high->index_4h` score `2.0212` n `53` status `ready` deltaP `20.2888` edge `0.0768` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.8101` n `53` status `ready` deltaP `26.1936` edge `0.2213` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.1867` n `53` status `ready` deltaP `16.1281` edge `0.0215` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.6167` n `53` status `ready` deltaP `16.9952` edge `0.0637` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
