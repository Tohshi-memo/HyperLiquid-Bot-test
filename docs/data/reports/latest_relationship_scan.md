# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T01:22:31.526736+00:00`
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

- `market_context_high->unknown_24h` score `1832.9111` n `53` status `ready` deltaP `3.4483` edge `152.7196` maxDD `0.0`
- `news_risk_high->equity_24h` score `54.607` n `50` status `ready` deltaP `59.2069` edge `4.2265` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `19.6825` n `50` status `ready` deltaP `37.3103` edge `2.389` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `16.6699` n `53` status `ready` deltaP `12.2382` edge `1.5081` maxDD `-12.3757`
- `news_risk_high->equity_4h` score `14.6295` n `50` status `ready` deltaP `44.7073` edge `1.0341` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `12.6067` n `53` status `ready` deltaP `39.6877` edge `1.6787` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `9.3838` n `50` status `ready` deltaP `22.2759` edge `1.5051` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.1287` n `50` status `ready` deltaP `50.2414` edge `0.3728` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `7.0284` n `50` status `ready` deltaP `43.9655` edge `0.2926` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.3709` n `50` status `ready` deltaP `47.2805` edge `0.17` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `4.6185` n `50` status `ready` deltaP `22.994` edge `0.2946` maxDD `-3.7082`
- `news_risk_high->crypto_alt_4h` score `4.4704` n `50` status `ready` deltaP `26.3841` edge `0.3402` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.304` n `50` status `ready` deltaP `21.7561` edge `0.3512` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `4.1081` n `50` status `ready` deltaP `37.1829` edge `0.1198` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.182` n `50` status `ready` deltaP `29.8293` edge `0.1013` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2964` n `50` status `ready` deltaP `25.5928` edge `0.0462` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.561` n `50` status `ready` deltaP `19.8922` edge `0.0276` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.8659` n `50` status `ready` deltaP `18.3448` edge `0.206` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.863` n `50` status `ready` deltaP `17.7425` edge `0.0903` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.8287` n `50` status `ready` deltaP `19.2934` edge `0.0828` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
