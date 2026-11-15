# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T03:07:42.005462+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `9372`

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

- `market_context_high->unknown_24h` score `558.7788` n `66` status `ready` deltaP `2.4306` edge `46.5487` maxDD `0.0`
- `news_risk_high->equity_24h` score `41.3283` n `53` status `ready` deltaP `45.4731` edge `3.2115` maxDD `-3.6503`
- `market_context_high->equity_24h` score `37.5746` n `66` status `ready` deltaP `40.4988` edge `3.0154` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `29.1962` n `66` status `ready` deltaP `57.7652` edge `2.1556` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `21.0122` n `53` status `ready` deltaP `43.0851` edge `2.6032` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.8355` n `53` status `ready` deltaP `39.1365` edge `0.8384` maxDD `-7.0416`
- `market_context_high->index_24h` score `7.2988` n `66` status `ready` deltaP `42.5978` edge `0.3334` maxDD `-0.0653`
- `news_risk_high->commodity_24h` score `7.2292` n `53` status `ready` deltaP `50.0` edge `0.2691` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `6.1364` n `53` status `ready` deltaP `14.4261` edge `1.1411` maxDD `-29.0448`
- `news_risk_high->index_24h` score `5.9408` n `53` status `ready` deltaP `38.8528` edge `0.2664` maxDD `-0.4279`
- `news_risk_high->crypto_major_4h` score `5.9092` n `53` status `ready` deltaP `22.5725` edge `0.4907` maxDD `-9.2335`
- `market_context_high->metal_24h` score `5.6568` n `66` status `ready` deltaP `53.7721` edge `0.4559` maxDD `-3.7989`
- `news_risk_high->metal_4h` score `5.0273` n `53` status `ready` deltaP `46.0913` edge `0.1493` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `3.759` n `53` status `ready` deltaP `20.2604` edge `0.2412` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.3746` n `53` status `ready` deltaP `31.2845` edge `0.098` maxDD `-0.3611`
- `news_risk_high->crypto_alt_4h` score `3.2134` n `53` status `ready` deltaP `27.2607` edge `0.3941` maxDD `-10.1088`
- `news_risk_high->index_4h` score `2.4706` n `53` status `ready` deltaP `25.4717` edge `0.0797` maxDD `-0.8235`
- `market_context_high->crypto_major_24h` score `2.3269` n `66` status `ready` deltaP `12.6105` edge `1.1424` maxDD `-76.2717`
- `news_risk_high->metal_1h` score `2.2374` n `53` status `ready` deltaP `25.74` edge `0.0403` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3771` n `53` status `ready` deltaP `18.3736` edge `0.0224` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
