# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T01:22:25.221160+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8652`

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

- `market_context_high->unknown_24h` score `1143.0309` n `37` status `ready` deltaP `3.9861` edge `95.226` maxDD `0.0`
- `news_risk_high->equity_24h` score `47.2641` n `50` status `ready` deltaP `50.565` edge `3.6722` maxDD `-3.6503`
- `market_context_high->unknown_4h` score `44.0851` n `64` status `ready` deltaP `8.9939` edge `3.6138` maxDD `0.0`
- `market_context_high->equity_24h` score `32.9262` n `37` status `ready` deltaP `35.538` edge `2.6611` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `30.0319` n `37` status `ready` deltaP `54.9815` edge `2.2438` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `21.619` n `50` status `ready` deltaP `43.0953` edge `2.5987` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `11.773` n `50` status `ready` deltaP `36.7805` edge `0.8489` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `11.2666` n `37` status `ready` deltaP `12.1223` edge `1.2934` maxDD `-30.1597`
- `news_risk_high->crypto_alt_24h` score `9.1197` n `50` status `ready` deltaP `20.6031` edge `1.4824` maxDD `-29.0448`
- `market_context_high->index_24h` score `6.9005` n `37` status `ready` deltaP `46.138` edge `0.2761` maxDD `-0.0251`
- `news_risk_high->index_24h` score `6.8123` n `50` status `ready` deltaP `42.2461` edge `0.3164` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.2608` n `50` status `ready` deltaP `41.0745` edge `0.2479` maxDD `0.0`
- `news_risk_high->metal_4h` score `4.9286` n `50` status `ready` deltaP `43.9268` edge `0.1555` maxDD `-1.0104`
- `market_context_high->metal_24h` score `4.3765` n `37` status `ready` deltaP `53.7356` edge `0.292` maxDD `-3.7989`
- `news_risk_high->crypto_major_4h` score `4.3638` n `50` status `ready` deltaP `20.689` edge `0.3633` maxDD `-9.0062`
- `news_risk_high->crypto_alt_4h` score `4.1564` n `50` status `ready` deltaP `25.7744` edge `0.3181` maxDD `-9.4848`
- `news_risk_high->commodity_4h` score `3.7614` n `50` status `ready` deltaP `34.439` edge `0.1092` maxDD `-0.3611`
- `news_risk_high->equity_1h` score `3.7466` n `50` status `ready` deltaP `19.8503` edge `0.2429` maxDD `-3.7082`
- `news_risk_high->index_4h` score `2.4248` n `50` status `ready` deltaP `23.2744` edge `0.0819` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.1802` n `50` status `ready` deltaP `24.8443` edge `0.0415` maxDD `-0.3692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
