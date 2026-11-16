# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T17:37:30.944864+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4232`

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

- `news_risk_high->equity_24h` score `53.4374` n `50` status `ready` deltaP `59.1073` edge `4.1297` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `21.1289` n `50` status `ready` deltaP `40.872` edge `2.5507` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `18.3956` n `30` status `ready` deltaP `14.1291` edge `1.5932` maxDD `-8.6878`
- `news_risk_high->equity_4h` score `14.1728` n `50` status `ready` deltaP `43.1829` edge `1.0062` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `12.2645` n `30` status `ready` deltaP `42.872` edge `1.6136` maxDD `-22.8301`
- `market_context_high->unknown_24h` score `11.5275` n `30` status `ready` deltaP `3.9792` edge `0.9341` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `10.1817` n `50` status `ready` deltaP `24.7958` edge `1.5906` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.0103` n `50` status `ready` deltaP `50.1107` edge `0.3638` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.1393` n `50` status `ready` deltaP `41.1765` edge `0.2371` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.1807` n `50` status `ready` deltaP `45.9085` edge `0.1633` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `5.0029` n `50` status `ready` deltaP `28.9756` edge `0.3673` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.6269` n `50` status `ready` deltaP `22.8232` edge `0.371` maxDD `-9.0062`
- `news_risk_high->equity_1h` score `4.4267` n `50` status `ready` deltaP `21.7964` edge `0.2866` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `4.0151` n `50` status `ready` deltaP `36.7256` edge `0.1151` maxDD `-0.3611`
- `market_context_high->metal_24h` score `3.8049` n `30` status `ready` deltaP `46.9435` edge `0.264` maxDD `-3.7989`
- `news_risk_high->index_4h` score `2.9862` n `50` status `ready` deltaP `27.8476` edge `0.0982` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2748` n `50` status `ready` deltaP `25.5928` edge `0.0444` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.4281` n `50` status `ready` deltaP `18.3952` edge `0.0265` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.9264` n `50` status `ready` deltaP `18.2768` edge `0.2142` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.9206` n `50` status `ready` deltaP `18.3413` edge `0.0937` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
