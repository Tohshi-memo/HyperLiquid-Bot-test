# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T20:22:35.414910+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4400`

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

- `market_context_high->unknown_24h` score `196.1428` n `33` status `ready` deltaP `3.9655` edge `16.3188` maxDD `0.0`
- `news_risk_high->equity_24h` score `53.6614` n `50` status `ready` deltaP `59.2069` edge `4.1477` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `20.5073` n `50` status `ready` deltaP `39.2069` edge `2.4821` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `18.4723` n `33` status `ready` deltaP `15.6739` edge `1.5893` maxDD `-8.6878`
- `news_risk_high->equity_4h` score `14.4366` n `50` status `ready` deltaP `44.231` edge `1.0212` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `12.4083` n `33` status `ready` deltaP `44.8433` edge `1.6189` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `9.7589` n `50` status `ready` deltaP `23.3103` edge `1.5463` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.0423` n `50` status `ready` deltaP `50.2414` edge `0.3656` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.3595` n `50` status `ready` deltaP `41.3793` edge `0.2541` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.3585` n `50` status `ready` deltaP `47.2462` edge `0.1692` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.7614` n `50` status `ready` deltaP `27.7264` edge `0.3555` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `4.4732` n `50` status `ready` deltaP `22.0179` edge `0.289` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `4.4605` n `50` status `ready` deltaP `22.1824` edge `0.3614` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `4.0633` n `50` status `ready` deltaP `36.8632` edge `0.1182` maxDD `-0.3611`
- `market_context_high->metal_24h` score `3.2881` n `33` status `ready` deltaP `40.9509` edge `0.2377` maxDD `-3.7989`
- `news_risk_high->index_4h` score `3.1402` n `50` status `ready` deltaP `29.3678` edge `0.1009` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.3008` n `50` status `ready` deltaP `25.8117` edge `0.0451` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.5271` n `50` status `ready` deltaP `19.5127` edge `0.0273` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.901` n `50` status `ready` deltaP `18.3448` edge `0.2105` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.8961` n `50` status `ready` deltaP `18.2601` edge `0.0911` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
