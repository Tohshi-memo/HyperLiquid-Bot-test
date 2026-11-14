# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-14T22:22:22.428174+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `9210`

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

- `market_context_high->unknown_24h` score `576.3054` n `66` status `ready` deltaP `3.4722` edge `48.0023` maxDD `0.0`
- `news_risk_high->equity_24h` score `40.881` n `53` status `ready` deltaP `44.9522` edge `3.1777` maxDD `-3.6503`
- `market_context_high->equity_24h` score `37.1274` n `66` status `ready` deltaP `39.9779` edge `2.9816` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `27.041` n `66` status `ready` deltaP `57.7652` edge `1.976` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `19.5809` n `53` status `ready` deltaP `43.0851` edge `2.4197` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.7167` n `53` status `ready` deltaP `38.2219` edge `0.8346` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `7.3643` n `53` status `ready` deltaP `51.3889` edge `0.2711` maxDD `0.0`
- `market_context_high->index_24h` score `7.2332` n `66` status `ready` deltaP `42.077` edge `0.3314` maxDD `-0.0653`
- `news_risk_high->index_24h` score `5.8752` n `53` status `ready` deltaP `38.332` edge `0.2644` maxDD `-0.4279`
- `news_risk_high->crypto_major_4h` score `5.4972` n `53` status `ready` deltaP `22.2676` edge `0.4584` maxDD `-9.2335`
- `market_context_high->metal_24h` score `5.3686` n `66` status `ready` deltaP `51.5152` edge `0.434` maxDD `-3.7989`
- `news_risk_high->metal_4h` score `5.0377` n `53` status `ready` deltaP `46.701` edge `0.1461` maxDD `-1.0104`
- `news_risk_high->crypto_alt_24h` score `4.7355` n `53` status `ready` deltaP `14.4261` edge `0.9615` maxDD `-29.0448`
- `news_risk_high->equity_1h` score `3.7734` n `53` status `ready` deltaP `20.1107` edge `0.2434` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.5593` n `53` status `ready` deltaP `33.1138` edge `0.1012` maxDD `-0.3611`
- `news_risk_high->crypto_alt_4h` score `3.218` n `53` status `ready` deltaP `28.0229` edge `0.3896` maxDD `-10.1088`
- `news_risk_high->index_4h` score `2.5218` n `53` status `ready` deltaP `26.0815` edge `0.0799` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `2.2901` n `53` status `ready` deltaP `26.3388` edge `0.0407` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3903` n `53` status `ready` deltaP `18.5233` edge `0.0225` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `1.1507` n `53` status `ready` deltaP `19.6898` edge `0.1142` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
