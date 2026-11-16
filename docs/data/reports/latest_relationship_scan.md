# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T15:52:26.472346+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4202`

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

- `news_risk_high->equity_24h` score `53.0833` n `50` status `ready` deltaP `58.4152` edge `4.1048` maxDD `-3.6503`
- `market_context_high->unknown_24h` score `48.7191` n `30` status `ready` deltaP `3.9792` edge `4.0334` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `21.4653` n `50` status `ready` deltaP `41.91` edge `2.5869` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `18.6381` n `30` status `ready` deltaP `14.8212` edge `1.6088` maxDD `-8.6878`
- `news_risk_high->equity_4h` score `13.9854` n `50` status `ready` deltaP `42.4901` edge `0.9952` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `12.6008` n `30` status `ready` deltaP `43.91` edge `1.6498` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `10.3394` n `50` status `ready` deltaP `25.4879` edge `1.6062` maxDD `-29.0448`
- `news_risk_high->index_24h` score `7.9285` n `50` status `ready` deltaP `49.4187` edge `0.3616` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.1057` n `50` status `ready` deltaP `41.1765` edge `0.2343` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `5.2426` n `50` status `ready` deltaP `29.796` edge `0.3818` maxDD `-9.4848`
- `news_risk_high->metal_4h` score `5.0935` n `50` status `ready` deltaP `45.2085` edge `0.1607` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.8726` n `50` status `ready` deltaP `23.6438` edge `0.386` maxDD `-9.0062`
- `news_risk_high->equity_1h` score `4.3523` n `50` status `ready` deltaP `21.7964` edge `0.2804` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.9407` n `50` status `ready` deltaP `36.1857` edge `0.1125` maxDD `-0.3611`
- `market_context_high->metal_24h` score `3.8259` n `30` status `ready` deltaP `46.9435` edge `0.2667` maxDD `-3.7989`
- `news_risk_high->index_4h` score `2.9316` n `50` status `ready` deltaP `27.3151` edge `0.0972` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.276` n `50` status `ready` deltaP `25.5928` edge `0.0445` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3993` n `50` status `ready` deltaP `18.0958` edge `0.0261` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.9861` n `50` status `ready` deltaP `18.9401` edge `0.0981` maxDD `-6.1688`
- `news_risk_high->metal_24h` score `0.9474` n `50` status `ready` deltaP `18.2768` edge `0.2169` maxDD `-7.3825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
