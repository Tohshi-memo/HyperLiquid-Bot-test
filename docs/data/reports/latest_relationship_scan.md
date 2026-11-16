# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T23:37:24.780067+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4392`

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

- `market_context_high->unknown_24h` score `1350.8423` n `46` status `ready` deltaP `3.4483` edge `112.5472` maxDD `0.0`
- `news_risk_high->equity_24h` score `54.1966` n `50` status `ready` deltaP `59.2069` edge `4.1923` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `19.9391` n `50` status `ready` deltaP `37.6552` edge `2.4196` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `17.9619` n `46` status `ready` deltaP `15.4048` edge `1.5517` maxDD `-8.9392`
- `news_risk_high->equity_4h` score `14.6623` n `50` status `ready` deltaP `45.0122` edge `1.0348` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `13.0721` n `46` status `ready` deltaP `44.8726` edge `1.7038` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `9.4481` n `50` status `ready` deltaP `22.4483` edge `1.5122` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.0915` n `50` status `ready` deltaP `50.2414` edge `0.3697` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.7759` n `50` status `ready` deltaP `42.7586` edge `0.2796` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.4341` n `50` status `ready` deltaP `47.8902` edge `0.1712` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `4.6053` n `50` status `ready` deltaP `22.8443` edge `0.2945` maxDD `-3.7082`
- `news_risk_high->crypto_alt_4h` score `4.4836` n `50` status `ready` deltaP `26.3841` edge `0.3413` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.3582` n `50` status `ready` deltaP `21.9085` edge `0.3547` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `4.1141` n `50` status `ready` deltaP `37.1829` edge `0.1203` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.2183` n `50` status `ready` deltaP `30.1341` edge `0.1023` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.3372` n `50` status `ready` deltaP `26.0419` edge `0.0466` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.6018` n `50` status `ready` deltaP `20.3413` edge `0.028` maxDD `-0.4103`
- `market_context_high->metal_24h` score `1.5461` n `46` status `ready` deltaP `23.8231` edge `0.1302` maxDD `-7.4811`
- `news_risk_high->metal_24h` score `0.8706` n `50` status `ready` deltaP `18.3448` edge `0.2066` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.8638` n `50` status `ready` deltaP `17.7425` edge `0.0904` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
