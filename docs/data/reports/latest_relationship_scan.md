# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T06:42:52.099299+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9897`

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

- `market_context_high->unknown_1h` score `66.2202` n `47` status `ready` deltaP `10.5651` edge `5.455` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `39.4126` n `46` status `ready` deltaP `26.7286` edge `3.1218` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `24.3177` n `46` status `ready` deltaP `21.7014` edge `1.8818` maxDD `0.0`
- `market_context_high->equity_24h` score `22.7852` n `46` status `ready` deltaP `24.1244` edge `1.748` maxDD `-0.1382`
- `market_context_high->index_24h` score `7.5841` n `46` status `ready` deltaP `33.1522` edge `0.4197` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `5.6715` n `103` status `ready` deltaP `-0.9624` edge `1.3833` maxDD `-63.6743`
- `news_risk_high->crypto_alt_4h` score `4.8711` n `103` status `ready` deltaP `14.6889` edge `0.4078` maxDD `-5.9838`
- `news_risk_high->crypto_major_4h` score `4.7905` n `103` status `ready` deltaP `18.6523` edge `0.3326` maxDD `-2.619`
- `market_context_high->metal_24h` score `2.7597` n `46` status `ready` deltaP `27.1287` edge `0.0725` maxDD `-0.2042`
- `market_context_high->index_4h` score `2.7081` n `47` status `ready` deltaP `31.5873` edge `0.0305` maxDD `-0.2323`
- `news_risk_high->crypto_alt_1h` score `2.3968` n `108` status `ready` deltaP `12.9408` edge `0.1625` maxDD `-1.5895`
- `news_risk_high->crypto_alt_24h` score `2.0556` n `103` status `ready` deltaP `-3.5413` edge `0.8962` maxDD `-49.7699`
- `news_risk_high->commodity_24h` score `2.0204` n `103` status `ready` deltaP `21.1434` edge `0.1453` maxDD `-2.431`
- `news_risk_high->crypto_major_1h` score `1.93` n `108` status `ready` deltaP `15.0366` edge `0.1041` maxDD `-1.8141`
- `market_context_high->equity_4h` score `1.9284` n `47` status `ready` deltaP `14.4006` edge `0.1065` maxDD `-1.3444`
- `news_risk_high->fx_4h` score `1.6038` n `103` status `ready` deltaP `23.3765` edge `0.0414` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.232` n `103` status `ready` deltaP `29.6639` edge `0.1233` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.8876` n `47` status `ready` deltaP `13.8616` edge `0.0094` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.7293` n `47` status `ready` deltaP `9.8197` edge `0.0356` maxDD `-1.5564`
- `news_risk_high->metal_1h` score `0.546` n `108` status `ready` deltaP `14.1051` edge `0.0108` maxDD `-0.7468`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
