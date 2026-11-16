# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T17:22:25.182221+00:00`
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

- `news_risk_high->equity_24h` score `53.4194` n `50` status `ready` deltaP `59.1073` edge `4.1282` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `21.2019` n `50` status `ready` deltaP `41.045` edge `2.5589` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `18.4718` n `30` status `ready` deltaP `14.3022` edge `1.5984` maxDD `-8.6878`
- `market_context_high->unknown_24h` score `16.7475` n `30` status `ready` deltaP `3.9792` edge `1.3691` maxDD `0.0`
- `news_risk_high->equity_4h` score `14.1782` n `50` status `ready` deltaP `43.2511` edge `1.0062` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `12.3374` n `30` status `ready` deltaP `43.045` edge `1.6218` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `10.2313` n `50` status `ready` deltaP `24.9689` edge `1.5958` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.0079` n `50` status `ready` deltaP `50.1107` edge `0.3636` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.1333` n `50` status `ready` deltaP `41.1765` edge `0.2366` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.1698` n `50` status `ready` deltaP `45.8174` edge `0.163` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `5.0161` n `50` status `ready` deltaP `29.035` edge `0.368` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.6389` n `50` status `ready` deltaP `22.8828` edge `0.3716` maxDD `-9.0062`
- `news_risk_high->equity_1h` score `4.4231` n `50` status `ready` deltaP `21.7964` edge `0.2863` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `4.0278` n `50` status `ready` deltaP `36.7945` edge `0.1157` maxDD `-0.3611`
- `market_context_high->metal_24h` score `3.8103` n `30` status `ready` deltaP `46.9435` edge `0.2647` maxDD `-3.7989`
- `news_risk_high->index_4h` score `2.979` n `50` status `ready` deltaP `27.7717` edge `0.0981` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2904` n `50` status `ready` deltaP `25.7425` edge `0.0447` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.4269` n `50` status `ready` deltaP `18.3952` edge `0.0264` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.9378` n `50` status `ready` deltaP `18.491` edge `0.0949` maxDD `-6.1688`
- `news_risk_high->metal_24h` score `0.9318` n `50` status `ready` deltaP `18.2768` edge `0.2149` maxDD `-7.3825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
