# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T21:52:29.710380+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4308`

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

- `market_context_high->unknown_24h` score `744.2513` n `39` status `ready` deltaP `3.6207` edge `61.9968` maxDD `0.0`
- `news_risk_high->equity_24h` score `53.8498` n `50` status `ready` deltaP `59.2069` edge `4.1634` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `20.2335` n `50` status `ready` deltaP `38.5172` edge `2.4516` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `14.6476` n `50` status `ready` deltaP `45.1429` edge `1.0327` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `12.8249` n `39` status `ready` deltaP `44.6198` edge `1.6738` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `12.1321` n `39` status `ready` deltaP `17.2546` edge `1.5948` maxDD `-8.6878`
- `news_risk_high->crypto_alt_24h` score `9.583` n `50` status `ready` deltaP `22.7931` edge `1.5272` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.0603` n `50` status `ready` deltaP `50.2414` edge `0.3671` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.5263` n `50` status `ready` deltaP `41.7241` edge `0.2657` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.4481` n `50` status `ready` deltaP `48.0061` edge `0.1716` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.6336` n `50` status `ready` deltaP `27.1185` edge `0.3489` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `4.5598` n `50` status `ready` deltaP `22.5449` edge `0.2927` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `4.4654` n `50` status `ready` deltaP `22.3343` edge `0.3608` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `4.1044` n `50` status `ready` deltaP `37.1672` edge `0.1196` maxDD `-0.3611`
- `market_context_high->metal_24h` score `3.6654` n `39` status `ready` deltaP `31.6269` edge `0.1883` maxDD `-4.1625`
- `news_risk_high->index_4h` score `3.2348` n `50` status `ready` deltaP `30.2796` edge `0.1027` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.3515` n `50` status `ready` deltaP `26.1916` edge `0.0468` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.5766` n `50` status `ready` deltaP `20.0419` edge `0.0279` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.8878` n `50` status `ready` deltaP `18.3448` edge `0.2088` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.8848` n `50` status `ready` deltaP `18.0419` edge `0.0911` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
