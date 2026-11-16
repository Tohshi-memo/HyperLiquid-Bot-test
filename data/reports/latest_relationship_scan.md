# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T23:07:29.967042+00:00`
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

- `market_context_high->unknown_24h` score `1179.6815` n `44` status `ready` deltaP `3.4483` edge `98.2838` maxDD `0.0`
- `news_risk_high->equity_24h` score `54.0682` n `50` status `ready` deltaP `59.2069` edge `4.1816` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `20.0042` n `50` status `ready` deltaP `37.8276` edge `2.4268` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `14.6664` n `50` status `ready` deltaP `45.0776` edge `1.0347` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `13.2036` n `44` status `ready` deltaP `45.7367` edge `1.7149` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `12.0188` n `44` status `ready` deltaP `17.0847` edge `1.5814` maxDD `-8.6878`
- `news_risk_high->crypto_alt_24h` score `9.466` n `50` status `ready` deltaP `22.4483` edge `1.5145` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.0783` n `50` status `ready` deltaP `50.2414` edge `0.3686` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.7051` n `50` status `ready` deltaP `42.4138` edge `0.276` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.4387` n `50` status `ready` deltaP `47.9482` edge `0.1712` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `4.5801` n `50` status `ready` deltaP `22.6946` edge `0.2934` maxDD `-3.7082`
- `news_risk_high->crypto_alt_4h` score `4.5189` n `50` status `ready` deltaP `26.5997` edge `0.3428` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.3714` n `50` status `ready` deltaP `21.9696` edge `0.3554` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `4.1207` n `50` status `ready` deltaP `37.2511` edge `0.1204` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.2266` n `50` status `ready` deltaP `30.207` edge `0.1025` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.3372` n `50` status `ready` deltaP `26.0419` edge `0.0466` maxDD `-0.3692`
- `market_context_high->metal_24h` score `2.2599` n `44` status `ready` deltaP `25.7993` edge `0.1521` maxDD `-6.195`
- `news_risk_high->index_1h` score `1.5886` n `50` status `ready` deltaP `20.1916` edge `0.0279` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.8714` n `50` status `ready` deltaP `18.3448` edge `0.2067` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.8427` n `50` status `ready` deltaP `17.5928` edge `0.0887` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
