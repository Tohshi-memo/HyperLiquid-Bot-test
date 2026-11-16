# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T21:22:28.625865+00:00`
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

- `market_context_high->unknown_24h` score `514.5389` n `37` status `ready` deltaP `3.6207` edge `42.8541` maxDD `0.0`
- `news_risk_high->equity_24h` score `53.7934` n `50` status `ready` deltaP `59.2069` edge `4.1587` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `20.3412` n `50` status `ready` deltaP `38.8621` edge `2.4631` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `18.2031` n `37` status `ready` deltaP `14.273` edge `1.5762` maxDD `-8.6878`
- `news_risk_high->equity_4h` score `14.5885` n `50` status `ready` deltaP `44.8389` edge `1.0298` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `12.4869` n `37` status `ready` deltaP `43.0243` edge `1.6411` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `9.661` n `50` status `ready` deltaP `23.1379` edge `1.5349` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.0555` n `50` status `ready` deltaP `50.2414` edge `0.3667` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.4363` n `50` status `ready` deltaP `41.3793` edge `0.2605` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.4324` n `50` status `ready` deltaP `47.8541` edge `0.1713` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.6963` n `50` status `ready` deltaP `27.4225` edge `0.3521` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `4.5658` n `50` status `ready` deltaP `22.5449` edge `0.2932` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `4.4834` n `50` status `ready` deltaP `22.3343` edge `0.3623` maxDD `-9.0062`
- `market_context_high->metal_24h` score `4.1049` n `37` status `ready` deltaP `34.3989` edge `0.2019` maxDD `-3.7989`
- `news_risk_high->commodity_4h` score `4.0621` n `50` status `ready` deltaP `36.8632` edge `0.1181` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.2057` n `50` status `ready` deltaP `29.9757` edge `0.1023` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.3635` n `50` status `ready` deltaP `26.3413` edge `0.0468` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.5634` n `50` status `ready` deltaP `19.8922` edge `0.0278` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.9113` n `50` status `ready` deltaP `18.3413` edge `0.0925` maxDD `-6.1688`
- `news_risk_high->metal_24h` score `0.8964` n `50` status `ready` deltaP `18.3448` edge `0.2099` maxDD `-7.3825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
