# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T16:52:35.216613+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4244`

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

- `news_risk_high->equity_24h` score `53.3726` n `50` status `ready` deltaP `59.1073` edge `4.1243` maxDD `-3.6503`
- `market_context_high->unknown_24h` score `26.7171` n `30` status `ready` deltaP `3.9792` edge `2.1999` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `21.3431` n `50` status `ready` deltaP `41.391` edge `2.5747` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `18.6195` n `30` status `ready` deltaP `14.6482` edge `1.6084` maxDD `-8.6878`
- `news_risk_high->equity_4h` score `14.1433` n `50` status `ready` deltaP `43.0989` edge `1.0043` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `12.4787` n `30` status `ready` deltaP `43.391` edge `1.6376` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `10.3272` n `50` status `ready` deltaP `25.3149` edge `1.6058` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.0043` n `50` status `ready` deltaP `50.1107` edge `0.3633` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.1249` n `50` status `ready` deltaP `41.1765` edge `0.2359` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.1371` n `50` status `ready` deltaP `45.5129` edge `0.1623` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `5.128` n `50` status `ready` deltaP `29.3394` edge `0.3753` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.7484` n `50` status `ready` deltaP `23.1872` edge `0.3787` maxDD `-9.0062`
- `news_risk_high->equity_1h` score `4.4123` n `50` status `ready` deltaP `21.7964` edge `0.2854` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `4.0242` n `50` status `ready` deltaP `36.7945` edge `0.1154` maxDD `-0.3611`
- `market_context_high->metal_24h` score `3.8181` n `30` status `ready` deltaP `46.9435` edge `0.2657` maxDD `-3.7989`
- `news_risk_high->index_4h` score `2.951` n `50` status `ready` deltaP `27.4673` edge `0.0978` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.3204` n `50` status `ready` deltaP `26.0419` edge `0.0452` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.4125` n `50` status `ready` deltaP `18.2455` edge `0.0262` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.9814` n `50` status `ready` deltaP `18.7904` edge `0.0985` maxDD `-6.1688`
- `news_risk_high->metal_24h` score `0.9396` n `50` status `ready` deltaP `18.2768` edge `0.2159` maxDD `-7.3825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
