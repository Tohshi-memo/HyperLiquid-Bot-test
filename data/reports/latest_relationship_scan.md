# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T18:22:31.086628+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10026`

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

- `market_context_high->unknown_24h` score `535.9706` n `64` status `ready` deltaP `3.8128` edge `44.6388` maxDD `0.0`
- `news_risk_high->equity_24h` score `45.5085` n `50` status `ready` deltaP `50.565` edge `3.5259` maxDD `-3.6503`
- `market_context_high->equity_24h` score `40.8259` n `64` status `ready` deltaP `46.94` edge `3.2434` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `33.8153` n `64` status `ready` deltaP `63.0633` edge `2.5052` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `23.2796` n `50` status `ready` deltaP `46.2149` edge `2.7908` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `12.2777` n `50` status `ready` deltaP `39.2195` edge `0.8747` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `9.3644` n `50` status `ready` deltaP `19.5633` edge `1.5207` maxDD `-29.0448`
- `market_context_high->index_24h` score `8.1701` n `64` status `ready` deltaP `49.5586` edge `0.3591` maxDD `-0.0251`
- `market_context_high->metal_24h` score `6.7404` n `64` status `ready` deltaP `63.7511` edge `0.5283` maxDD `-3.7989`
- `news_risk_high->commodity_24h` score `6.6271` n `50` status `ready` deltaP `43.6742` edge `0.2611` maxDD `0.0`
- `news_risk_high->index_24h` score `6.5759` n `50` status `ready` deltaP `42.2461` edge `0.2967` maxDD `-0.4279`
- `news_risk_high->crypto_major_4h` score `5.3891` n `50` status `ready` deltaP `22.9756` edge `0.4335` maxDD `-9.0062`
- `news_risk_high->metal_4h` score `4.9478` n `50` status `ready` deltaP `44.8415` edge `0.151` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.7118` n `50` status `ready` deltaP `27.4512` edge `0.3532` maxDD `-9.4848`
- `market_context_high->crypto_major_24h` score `4.5147` n `64` status `ready` deltaP `13.2149` edge `1.2219` maxDD `-69.0352`
- `news_risk_high->equity_1h` score `3.9948` n `50` status `ready` deltaP `21.3473` edge `0.2536` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.7064` n `50` status `ready` deltaP `34.5915` edge `0.1036` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.6085` n `50` status `ready` deltaP `25.2561` edge `0.084` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.1861` n `50` status `ready` deltaP `24.994` edge `0.041` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.2819` n `50` status `ready` deltaP `17.0479` edge `0.0233` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
