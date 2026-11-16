# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T21:37:34.405060+00:00`
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

- `market_context_high->unknown_24h` score `630.2105` n `38` status `ready` deltaP `3.6207` edge `52.4934` maxDD `0.0`
- `news_risk_high->equity_24h` score `53.8258` n `50` status `ready` deltaP `59.2069` edge `4.1614` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `20.2885` n `50` status `ready` deltaP `38.6897` edge `2.4575` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `18.4218` n `38` status `ready` deltaP `15.8076` edge `1.5842` maxDD `-8.6878`
- `news_risk_high->equity_4h` score `14.6186` n `50` status `ready` deltaP `44.9909` edge `1.0313` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `12.6537` n `38` status `ready` deltaP `43.8476` edge `1.657` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `9.6232` n `50` status `ready` deltaP `22.9655` edge `1.5312` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.0579` n `50` status `ready` deltaP `50.2414` edge `0.3669` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.4825` n `50` status `ready` deltaP `41.5517` edge `0.2632` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.4481` n `50` status `ready` deltaP `48.0061` edge `0.1716` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.6649` n `50` status `ready` deltaP `27.2705` edge `0.3505` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `4.5622` n `50` status `ready` deltaP `22.5449` edge `0.2929` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `4.4762` n `50` status `ready` deltaP `22.3343` edge `0.3617` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `4.0839` n `50` status `ready` deltaP `37.0152` edge `0.1189` maxDD `-0.3611`
- `market_context_high->metal_24h` score `3.9099` n `38` status `ready` deltaP `32.9764` edge `0.1953` maxDD `-3.812`
- `news_risk_high->index_4h` score `3.2202` n `50` status `ready` deltaP `30.1277` edge `0.1025` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.3635` n `50` status `ready` deltaP `26.3413` edge `0.0468` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.5646` n `50` status `ready` deltaP `19.8922` edge `0.0279` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.8988` n `50` status `ready` deltaP `18.1916` edge `0.0919` maxDD `-6.1688`
- `news_risk_high->metal_24h` score `0.8925` n `50` status `ready` deltaP `18.3448` edge `0.2094` maxDD `-7.3825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
