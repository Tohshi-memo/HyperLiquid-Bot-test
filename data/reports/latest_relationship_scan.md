# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T20:22:31.933465+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8260`

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

- `market_context_high->unknown_24h` score `639.7233` n `57` status `ready` deltaP `3.9861` edge `53.2837` maxDD `0.0`
- `news_risk_high->equity_24h` score `46.0137` n `50` status `ready` deltaP `50.565` edge `3.568` maxDD `-3.6503`
- `market_context_high->equity_24h` score `41.012` n `57` status `ready` deltaP `45.0211` edge `3.2717` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `34.3936` n `57` status `ready` deltaP `62.568` edge `2.5567` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `22.9807` n `50` status `ready` deltaP `45.5217` edge `2.7571` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `11.9942` n `50` status `ready` deltaP `38.0` edge `0.8592` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `9.5175` n `50` status `ready` deltaP `20.6031` edge `1.5334` maxDD `-29.0448`
- `market_context_high->crypto_major_24h` score `9.5041` n `57` status `ready` deltaP `15.5919` edge `1.379` maxDD `-50.6085`
- `market_context_high->index_24h` score `8.1565` n `57` status `ready` deltaP `48.9829` edge `0.3618` maxDD `-0.0251`
- `news_risk_high->index_24h` score `6.6371` n `50` status `ready` deltaP `42.2461` edge `0.3018` maxDD `-0.4279`
- `market_context_high->metal_24h` score `6.6113` n `57` status `ready` deltaP `63.2187` edge `0.5153` maxDD `-3.7989`
- `news_risk_high->commodity_24h` score `6.4778` n `50` status `ready` deltaP `42.2877` edge `0.2579` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `4.9955` n `50` status `ready` deltaP `22.061` edge `0.4068` maxDD `-9.0062`
- `news_risk_high->metal_4h` score `4.87` n `50` status `ready` deltaP `44.0793` edge `0.1496` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.4048` n `50` status `ready` deltaP `26.689` edge `0.3327` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `3.9816` n `50` status `ready` deltaP `21.3473` edge `0.2525` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.6734` n `50` status `ready` deltaP `34.1341` edge `0.1039` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.4905` n `50` status `ready` deltaP `24.0366` edge `0.0823` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.1718` n `50` status `ready` deltaP `24.8443` edge `0.0408` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.2915` n `50` status `ready` deltaP `17.1976` edge `0.0231` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
