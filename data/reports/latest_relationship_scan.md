# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T15:07:27.576617+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4080`

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

- `market_context_high->unknown_24h` score `63.9303` n `30` status `ready` deltaP `3.9792` edge `5.301` maxDD `0.0`
- `news_risk_high->equity_24h` score `52.8102` n `50` status `ready` deltaP `57.8962` edge `4.0855` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `21.507` n `50` status `ready` deltaP `42.083` edge `2.5911` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `18.6544` n `30` status `ready` deltaP `14.9942` edge `1.609` maxDD `-8.6878`
- `news_risk_high->equity_4h` score `13.7204` n `50` status `ready` deltaP `42.1033` edge `0.9757` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `12.6426` n `30` status `ready` deltaP `44.083` edge `1.654` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `10.3499` n `50` status `ready` deltaP `25.6609` edge `1.6064` maxDD `-29.0448`
- `news_risk_high->index_24h` score `7.8618` n `50` status `ready` deltaP `48.8997` edge `0.3595` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.0985` n `50` status `ready` deltaP `41.1765` edge `0.2337` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `5.1831` n `50` status `ready` deltaP `29.3982` edge `0.3795` maxDD `-9.4848`
- `news_risk_high->metal_4h` score `5.0901` n `50` status `ready` deltaP `45.2705` edge `0.16` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.7964` n `50` status `ready` deltaP `23.2462` edge `0.3823` maxDD `-9.0062`
- `news_risk_high->equity_1h` score `4.1424` n `50` status `ready` deltaP `21.3473` edge `0.2659` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.8834` n `50` status `ready` deltaP `35.7994` edge `0.1103` maxDD `-0.3611`
- `market_context_high->metal_24h` score `3.8314` n `30` status `ready` deltaP `46.9435` edge `0.2674` maxDD `-3.7989`
- `news_risk_high->index_4h` score `2.8773` n `50` status `ready` deltaP `26.9362` edge `0.0952` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2545` n `50` status `ready` deltaP `25.4431` edge `0.0437` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3454` n `50` status `ready` deltaP `17.6467` edge `0.0246` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.9529` n `50` status `ready` deltaP `18.2768` edge `0.2176` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.9089` n `50` status `ready` deltaP `18.491` edge `0.0912` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
