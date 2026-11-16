# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T22:22:28.612524+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4296`

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

- `market_context_high->unknown_24h` score `889.0169` n `41` status `ready` deltaP `3.6207` edge `74.0606` maxDD `0.0`
- `news_risk_high->equity_24h` score `53.9098` n `50` status `ready` deltaP `59.2069` edge `4.1684` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `20.1267` n `50` status `ready` deltaP `38.1724` edge `2.4402` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `14.6548` n `50` status `ready` deltaP `45.1429` edge `1.0333` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `13.1211` n `41` status `ready` deltaP `46.0261` edge `1.7024` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `12.3101` n `41` status `ready` deltaP `19.9117` edge `1.5999` maxDD `-8.6878`
- `news_risk_high->crypto_alt_24h` score `9.5113` n `50` status `ready` deltaP `22.4483` edge `1.5203` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.0651` n `50` status `ready` deltaP `50.2414` edge `0.3675` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.6103` n `50` status `ready` deltaP `42.069` edge `0.2704` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.4178` n `50` status `ready` deltaP `47.7021` edge `0.1711` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.5576` n `50` status `ready` deltaP `26.8146` edge `0.3446` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `4.5214` n `50` status `ready` deltaP `22.2455` edge `0.2915` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `4.3955` n `50` status `ready` deltaP `22.0304` edge `0.357` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `4.1274` n `50` status `ready` deltaP `37.3191` edge `0.1205` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.2348` n `50` status `ready` deltaP `30.2796` edge `0.1027` maxDD `-0.7999`
- `market_context_high->metal_24h` score `3.1599` n `41` status `ready` deltaP `29.1253` edge `0.1756` maxDD `-4.8486`
- `news_risk_high->metal_1h` score `2.324` n `50` status `ready` deltaP `25.8922` edge `0.0465` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.5766` n `50` status `ready` deltaP `20.0419` edge `0.0279` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.8792` n `50` status `ready` deltaP `18.3448` edge `0.2077` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.849` n `50` status `ready` deltaP `17.7425` edge `0.0885` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
