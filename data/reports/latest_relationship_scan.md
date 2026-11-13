# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T10:22:28.714723+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10854`

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

- `market_context_high->unknown_24h` score `350.1984` n `75` status `ready` deltaP `6.0139` edge `29.1572` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `61.8144` n `82` status `ready` deltaP `5.4878` edge `5.1594` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `32.649` n `53` status `ready` deltaP `31.9314` edge `2.5785` maxDD `-3.6503`
- `market_context_high->equity_24h` score `25.718` n `75` status `ready` deltaP `26.4722` edge `2.0587` maxDD `-4.361`
- `news_risk_high->crypto_major_24h` score `14.0372` n `53` status `ready` deltaP `42.3906` edge `1.7136` maxDD `-12.7247`
- `market_context_high->crypto_alt_24h` score `10.6498` n `75` status `ready` deltaP `49.1389` edge `1.4123` maxDD `-23.9622`
- `news_risk_high->equity_4h` score `10.543` n `53` status `ready` deltaP `35.3255` edge `0.7561` maxDD `-7.0416`
- `market_context_high->metal_24h` score `7.2762` n `75` status `ready` deltaP `45.1111` edge `0.358` maxDD `-1.1913`
- `news_risk_high->commodity_24h` score `6.0268` n `53` status `ready` deltaP `38.1944` edge `0.2476` maxDD `0.0`
- `news_risk_high->metal_4h` score `4.6156` n `53` status `ready` deltaP `44.1096` edge `0.1282` maxDD `-1.0104`
- `market_context_high->index_24h` score `4.5633` n `75` status `ready` deltaP `23.7639` edge `0.231` maxDD `-0.0653`
- `news_risk_high->index_24h` score `4.1677` n `53` status `ready` deltaP `24.4431` edge `0.2147` maxDD `-0.4279`
- `news_risk_high->equity_1h` score `3.325` n `53` status `ready` deltaP `17.8652` edge `0.221` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `3.3141` n `53` status `ready` deltaP `20.1335` edge `0.2907` maxDD `-9.2335`
- `news_risk_high->crypto_alt_24h` score `3.1064` n `53` status `ready` deltaP `19.9816` edge `0.7156` maxDD `-29.0448`
- `news_risk_high->commodity_4h` score `3.0925` n `53` status `ready` deltaP `28.3882` edge `0.0938` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.0924` n `53` status `ready` deltaP `24.6921` edge `0.0352` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.9648` n `53` status `ready` deltaP `20.2888` edge `0.0721` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.8657` n `53` status `ready` deltaP `26.4985` edge `0.2264` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.1987` n `53` status `ready` deltaP `16.4275` edge `0.0205` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
