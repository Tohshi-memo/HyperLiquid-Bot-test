# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T14:37:32.595419+00:00`
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

- `market_context_high->unknown_24h` score `73.5747` n `30` status `ready` deltaP `3.9792` edge `6.1047` maxDD `0.0`
- `news_risk_high->equity_24h` score `52.6217` n `50` status `ready` deltaP `57.5502` edge `4.0721` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `21.5578` n `50` status `ready` deltaP `42.4291` edge `2.5953` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `18.7006` n `30` status `ready` deltaP `15.1672` edge `1.6117` maxDD `-8.6878`
- `news_risk_high->equity_4h` score `13.5257` n `50` status `ready` deltaP `41.7994` edge `0.9615` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `12.6933` n `30` status `ready` deltaP `44.4291` edge `1.6582` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `10.38` n `50` status `ready` deltaP `25.8339` edge `1.6091` maxDD `-29.0448`
- `news_risk_high->index_24h` score `7.8149` n `50` status `ready` deltaP `48.5536` edge `0.3579` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.0937` n `50` status `ready` deltaP `41.1765` edge `0.2333` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `5.1951` n `50` status `ready` deltaP `29.3982` edge `0.3805` maxDD `-9.4848`
- `news_risk_high->metal_4h` score `5.101` n `50` status `ready` deltaP `45.4225` edge `0.1599` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.7806` n `50` status `ready` deltaP `23.0942` edge `0.382` maxDD `-9.0062`
- `news_risk_high->equity_1h` score `4.0968` n `50` status `ready` deltaP `21.1976` edge `0.2631` maxDD `-3.7082`
- `market_context_high->metal_24h` score `3.8458` n `30` status `ready` deltaP `47.1165` edge `0.2681` maxDD `-3.7989`
- `news_risk_high->commodity_4h` score `3.8363` n `50` status `ready` deltaP `35.4954` edge `0.1084` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.835` n `50` status `ready` deltaP `26.6322` edge `0.0937` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2425` n `50` status `ready` deltaP `25.2934` edge `0.0437` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3298` n `50` status `ready` deltaP `17.497` edge `0.0243` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.9673` n `50` status `ready` deltaP `18.4498` edge `0.2183` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.9292` n `50` status `ready` deltaP `18.491` edge `0.0938` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
