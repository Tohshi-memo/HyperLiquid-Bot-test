# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T20:07:26.747889+00:00`
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

- `market_context_high->unknown_24h` score `624.0441` n `58` status `ready` deltaP `3.9861` edge `51.9771` maxDD `0.0`
- `news_risk_high->equity_24h` score `45.9609` n `50` status `ready` deltaP `50.565` edge `3.5636` maxDD `-3.6503`
- `market_context_high->equity_24h` score `40.9582` n `58` status `ready` deltaP `45.3236` edge `3.2652` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `34.347` n `58` status `ready` deltaP `62.81` edge `2.5512` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `23.0318` n `50` status `ready` deltaP `45.695` edge `2.7625` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `12.0268` n `50` status `ready` deltaP `38.1524` edge `0.8609` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `9.5206` n `50` status `ready` deltaP `20.6031` edge `1.5338` maxDD `-29.0448`
- `market_context_high->crypto_major_24h` score `8.8017` n `58` status `ready` deltaP `15.2812` edge `1.355` maxDD `-53.205`
- `market_context_high->index_24h` score `8.1541` n `58` status `ready` deltaP `49.0737` edge `0.361` maxDD `-0.0251`
- `market_context_high->metal_24h` score `6.636` n `58` status `ready` deltaP `63.3479` edge `0.5176` maxDD `-3.7989`
- `news_risk_high->index_24h` score `6.6311` n `50` status `ready` deltaP `42.2461` edge `0.3013` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.4953` n `50` status `ready` deltaP `42.461` edge `0.2582` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `5.0401` n `50` status `ready` deltaP `22.2134` edge `0.4095` maxDD `-9.0062`
- `news_risk_high->metal_4h` score `4.87` n `50` status `ready` deltaP `44.0793` edge `0.1496` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.4386` n `50` status `ready` deltaP `26.8415` edge `0.3345` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `3.9864` n `50` status `ready` deltaP `21.3473` edge `0.2529` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.688` n `50` status `ready` deltaP `34.2866` edge `0.1041` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.5039` n `50` status `ready` deltaP `24.189` edge `0.0824` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.1849` n `50` status `ready` deltaP `24.994` edge `0.0409` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.2927` n `50` status `ready` deltaP `17.1976` edge `0.0232` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
