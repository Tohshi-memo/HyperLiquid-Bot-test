# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T12:52:35.944021+00:00`
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

- `market_context_high->unknown_24h` score `100.0473` n `30` status `ready` deltaP `3.9861` edge `8.3107` maxDD `0.0`
- `news_risk_high->equity_24h` score `51.9331` n `50` status `ready` deltaP `56.4575` edge `4.022` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `21.517` n `50` status `ready` deltaP `42.5754` edge `2.5891` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `18.5192` n `30` status `ready` deltaP `14.7891` edge `1.5991` maxDD `-8.6878`
- `news_risk_high->equity_4h` score `12.943` n `50` status `ready` deltaP `40.8158` edge `0.9195` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `12.6526` n `30` status `ready` deltaP `44.5754` edge `1.652` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `10.262` n `50` status `ready` deltaP `25.4558` edge `1.5965` maxDD `-29.0448`
- `news_risk_high->index_24h` score `7.6626` n `50` status `ready` deltaP `47.4454` edge `0.3526` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.0412` n `50` status `ready` deltaP `41.0745` edge `0.2296` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.0925` n `50` status `ready` deltaP `45.3607` edge `0.1596` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `5.0349` n `50` status `ready` deltaP `28.7306` edge `0.3716` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.6649` n `50` status `ready` deltaP `22.5784` edge `0.3758` maxDD `-9.0062`
- `news_risk_high->equity_1h` score `4.0285` n `50` status `ready` deltaP `20.7485` edge `0.2604` maxDD `-3.7082`
- `market_context_high->metal_24h` score `3.8746` n `30` status `ready` deltaP `47.4293` edge `0.2697` maxDD `-3.7989`
- `news_risk_high->commodity_4h` score `3.7011` n `50` status `ready` deltaP `34.5114` edge `0.1037` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.7029` n `50` status `ready` deltaP `25.6408` edge `0.0893` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.1958` n `50` status `ready` deltaP `24.8443` edge `0.0428` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3154` n `50` status `ready` deltaP `17.3473` edge `0.0241` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.9961` n `50` status `ready` deltaP `18.7626` edge `0.2199` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.9152` n `50` status `ready` deltaP `18.491` edge `0.092` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
