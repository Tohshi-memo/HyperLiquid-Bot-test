# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T04:37:34.687121+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11820`

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

- `market_context_high->unknown_24h` score `283.3909` n `84` status `ready` deltaP `6.2996` edge `23.588` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `55.733` n `94` status `ready` deltaP `6.8857` edge `4.6433` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `31.2833` n `53` status `ready` deltaP `28.2856` edge `2.489` maxDD `-3.6503`
- `market_context_high->equity_24h` score `23.2659` n `84` status `ready` deltaP `26.0169` edge `1.836` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `12.6949` n `53` status `ready` deltaP `39.092` edge `1.5635` maxDD `-12.7247`
- `market_context_high->crypto_alt_24h` score `9.8277` n `84` status `ready` deltaP `46.7758` edge `1.3577` maxDD `-25.4331`
- `news_risk_high->equity_4h` score `9.5173` n `53` status `ready` deltaP `32.7341` edge `0.6879` maxDD `-7.0416`
- `market_context_high->metal_24h` score `6.8956` n `84` status `ready` deltaP `42.3363` edge `0.3337` maxDD `-0.3044`
- `news_risk_high->commodity_24h` score `6.7185` n `53` status `ready` deltaP `41.6667` edge `0.2821` maxDD `0.0`
- `market_context_high->index_24h` score `4.4508` n `84` status `ready` deltaP `25.5456` edge `0.2101` maxDD `-0.0934`
- `news_risk_high->metal_4h` score `4.2871` n `53` status `ready` deltaP `41.5181` edge `0.1181` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.0425` n `53` status `ready` deltaP `23.7486` edge `0.2089` maxDD `-0.4279`
- `news_risk_high->commodity_4h` score `3.2271` n `53` status `ready` deltaP `29.4553` edge `0.0979` maxDD `-0.3611`
- `news_risk_high->equity_1h` score `3.2002` n `53` status `ready` deltaP `17.5658` edge `0.2126` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `2.8619` n `53` status `ready` deltaP `19.3713` edge `0.2581` maxDD `-9.2335`
- `news_risk_high->crypto_alt_24h` score `2.3901` n `53` status `ready` deltaP `16.8566` edge `0.6446` maxDD `-29.0448`
- `news_risk_high->metal_1h` score `2.0516` n `53` status `ready` deltaP `24.5424` edge `0.0328` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.6615` n `53` status `ready` deltaP `17.6973` edge `0.0641` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.6487` n `53` status `ready` deltaP `25.2789` edge `0.2067` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.1735` n `53` status `ready` deltaP `16.2778` edge `0.0194` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
