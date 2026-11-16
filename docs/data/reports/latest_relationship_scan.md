# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T23:52:23.502841+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4392`

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

- `market_context_high->unknown_24h` score `1429.5239` n `47` status `ready` deltaP `3.4483` edge `119.104` maxDD `0.0`
- `news_risk_high->equity_24h` score `54.2638` n `50` status `ready` deltaP `59.2069` edge `4.1979` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `19.9157` n `50` status `ready` deltaP `37.6552` edge `2.4166` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `17.6707` n `47` status `ready` deltaP `14.6185` edge `1.5411` maxDD `-9.6132`
- `news_risk_high->equity_4h` score `14.6671` n `50` status `ready` deltaP `45.0122` edge `1.0352` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `12.9399` n `47` status `ready` deltaP `43.485` edge `1.6961` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `9.445` n `50` status `ready` deltaP `22.4483` edge `1.5118` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.0975` n `50` status `ready` deltaP `50.2414` edge `0.3702` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.8113` n `50` status `ready` deltaP `42.931` edge `0.2814` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.4195` n `50` status `ready` deltaP `47.7378` edge `0.171` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `4.6053` n `50` status `ready` deltaP `22.8443` edge `0.2945` maxDD `-3.7082`
- `news_risk_high->crypto_alt_4h` score `4.4776` n `50` status `ready` deltaP `26.3841` edge `0.3408` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.3376` n `50` status `ready` deltaP `21.7561` edge `0.354` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `4.1141` n `50` status `ready` deltaP `37.1829` edge `0.1203` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.2171` n `50` status `ready` deltaP `30.1341` edge `0.1022` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.324` n `50` status `ready` deltaP `25.8922` edge `0.0465` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.5898` n `50` status `ready` deltaP `20.1916` edge `0.028` maxDD `-0.4103`
- `market_context_high->metal_24h` score `1.1962` n `47` status `ready` deltaP `22.898` edge `0.1196` maxDD `-8.1391`
- `news_risk_high->metal_24h` score `0.8706` n `50` status `ready` deltaP `18.3448` edge `0.2066` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.8646` n `50` status `ready` deltaP `17.7425` edge `0.0905` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
