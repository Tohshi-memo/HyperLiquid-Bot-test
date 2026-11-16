# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T21:07:26.299728+00:00`
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

- `market_context_high->unknown_24h` score `450.2662` n `36` status `ready` deltaP `3.7931` edge `37.4969` maxDD `0.0`
- `news_risk_high->equity_24h` score `53.7634` n `50` status `ready` deltaP `59.2069` edge `4.1562` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `20.393` n `50` status `ready` deltaP `39.0345` edge `2.4686` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `17.9839` n `36` status `ready` deltaP `12.6436` edge `1.5688` maxDD `-8.6878`
- `news_risk_high->equity_4h` score `14.5547` n `50` status `ready` deltaP `44.6869` edge `1.028` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `12.3383` n `36` status `ready` deltaP `42.1456` edge `1.6279` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `9.7012` n `50` status `ready` deltaP `23.3103` edge `1.5389` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.0531` n `50` status `ready` deltaP `50.2414` edge `0.3665` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.4123` n `50` status `ready` deltaP `41.3793` edge `0.2585` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.4154` n `50` status `ready` deltaP `47.7021` edge `0.1709` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.7059` n `50` status `ready` deltaP `27.4225` edge `0.3529` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `4.5406` n `50` status `ready` deltaP `22.3952` edge `0.2921` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `4.4641` n `50` status `ready` deltaP `22.1824` edge `0.3617` maxDD `-9.0062`
- `market_context_high->metal_24h` score `4.3162` n `36` status `ready` deltaP `35.9004` edge `0.2095` maxDD `-3.7989`
- `news_risk_high->commodity_4h` score `4.0597` n `50` status `ready` deltaP `36.8632` edge `0.1179` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.1911` n `50` status `ready` deltaP `29.8237` edge `0.1021` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.3467` n `50` status `ready` deltaP `26.1916` edge `0.0464` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.5622` n `50` status `ready` deltaP `19.8922` edge `0.0277` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.9113` n `50` status `ready` deltaP `18.3413` edge `0.0925` maxDD `-6.1688`
- `news_risk_high->metal_24h` score `0.8987` n `50` status `ready` deltaP `18.3448` edge `0.2102` maxDD `-7.3825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
