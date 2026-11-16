# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T13:52:34.927305+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4064`

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

- `market_context_high->unknown_24h` score `84.2511` n `30` status `ready` deltaP `3.9792` edge `6.9944` maxDD `0.0`
- `news_risk_high->equity_24h` score `52.3257` n `50` status `ready` deltaP `57.0311` edge `4.0509` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `21.5886` n `50` status `ready` deltaP `42.6021` edge `2.5981` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `18.7168` n `30` status `ready` deltaP `15.3402` edge `1.6119` maxDD `-8.6878`
- `news_risk_high->equity_4h` score `13.266` n `50` status `ready` deltaP `41.3435` edge `0.9429` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `12.7242` n `30` status `ready` deltaP `44.6021` edge `1.661` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `10.3905` n `50` status `ready` deltaP `26.0069` edge `1.6093` maxDD `-29.0448`
- `news_risk_high->index_24h` score `7.7458` n `50` status `ready` deltaP `48.0346` edge `0.3556` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.0841` n `50` status `ready` deltaP `41.1765` edge `0.2325` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `5.1854` n `50` status `ready` deltaP `29.2462` edge `0.3807` maxDD `-9.4848`
- `news_risk_high->metal_4h` score `5.0877` n `50` status `ready` deltaP `45.2705` edge `0.1598` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.7708` n `50` status `ready` deltaP `22.9422` edge `0.3822` maxDD `-9.0062`
- `news_risk_high->equity_1h` score `4.0859` n `50` status `ready` deltaP `21.1211` edge `0.2627` maxDD `-3.7082`
- `market_context_high->metal_24h` score `3.8595` n `30` status `ready` deltaP `47.2895` edge `0.2687` maxDD `-3.7989`
- `news_risk_high->commodity_4h` score `3.771` n `50` status `ready` deltaP `35.0395` edge `0.106` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.7757` n `50` status `ready` deltaP `26.1763` edge `0.0918` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2182` n `50` status `ready` deltaP `25.0643` edge `0.0432` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3225` n `50` status `ready` deltaP `17.42` edge `0.0242` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.981` n `50` status `ready` deltaP `18.6228` edge `0.2189` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.9538` n `50` status `ready` deltaP `18.7085` edge `0.0955` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
