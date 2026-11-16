# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T13:07:24.040376+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4058`

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

- `market_context_high->unknown_24h` score `99.6849` n `30` status `ready` deltaP `3.9861` edge `8.2805` maxDD `0.0`
- `news_risk_high->equity_24h` score `52.0525` n `50` status `ready` deltaP `56.6308` edge `4.0308` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `21.5428` n `50` status `ready` deltaP `42.5754` edge `2.5924` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `18.5906` n `30` status `ready` deltaP `14.9624` edge `1.6039` maxDD `-8.6878`
- `news_risk_high->equity_4h` score `13.044` n `50` status `ready` deltaP `40.968` edge `0.9269` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `12.6783` n `30` status `ready` deltaP `44.5754` edge `1.6553` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `10.3085` n `50` status `ready` deltaP `25.6291` edge `1.6013` maxDD `-29.0448`
- `news_risk_high->index_24h` score `7.6873` n `50` status `ready` deltaP `47.6187` edge `0.3535` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.0496` n `50` status `ready` deltaP `41.0745` edge `0.2303` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `5.0951` n `50` status `ready` deltaP `28.8828` edge `0.3756` maxDD `-9.4848`
- `news_risk_high->metal_4h` score `5.0925` n `50` status `ready` deltaP `45.3607` edge `0.1596` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.7009` n `50` status `ready` deltaP `22.5784` edge `0.3788` maxDD `-9.0062`
- `news_risk_high->equity_1h` score `4.0524` n `50` status `ready` deltaP `20.8982` edge `0.2614` maxDD `-3.7082`
- `market_context_high->metal_24h` score `3.8632` n `30` status `ready` deltaP `47.256` edge `0.2694` maxDD `-3.7989`
- `news_risk_high->commodity_4h` score `3.7217` n `50` status `ready` deltaP `34.6636` edge `0.1044` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.7247` n `50` status `ready` deltaP `25.793` edge `0.0901` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.1838` n `50` status `ready` deltaP `24.6946` edge `0.0428` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3154` n `50` status `ready` deltaP `17.3473` edge `0.0241` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.9847` n `50` status `ready` deltaP `18.5893` edge `0.2196` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.9432` n `50` status `ready` deltaP `18.6407` edge `0.0946` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
