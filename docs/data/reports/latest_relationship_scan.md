# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T23:22:38.380184+00:00`
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

- `market_context_high->unknown_24h` score `1267.5299` n `45` status `ready` deltaP `3.4483` edge `105.6045` maxDD `0.0`
- `news_risk_high->equity_24h` score `54.127` n `50` status `ready` deltaP `59.2069` edge `4.1865` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `19.9625` n `50` status `ready` deltaP `37.6552` edge `2.4226` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `18.3125` n `45` status `ready` deltaP `16.2261` edge `1.5723` maxDD `-8.6878`
- `news_risk_high->equity_4h` score `14.6712` n `50` status `ready` deltaP `45.0776` edge `1.0351` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `13.2566` n `45` status `ready` deltaP `46.3219` edge `1.7178` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `9.4528` n `50` status `ready` deltaP `22.4483` edge `1.5128` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.0843` n `50` status `ready` deltaP `50.2414` edge `0.3691` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.7393` n `50` status `ready` deltaP `42.5862` edge `0.2777` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.4387` n `50` status `ready` deltaP `47.9482` edge `0.1712` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `4.5957` n `50` status `ready` deltaP `22.8443` edge `0.2937` maxDD `-3.7082`
- `news_risk_high->crypto_alt_4h` score `4.4947` n `50` status `ready` deltaP `26.4475` edge `0.3418` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.3449` n `50` status `ready` deltaP `21.8174` edge `0.3542` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `4.1195` n `50` status `ready` deltaP `37.2511` edge `0.1203` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.2254` n `50` status `ready` deltaP `30.207` edge `0.1024` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.3372` n `50` status `ready` deltaP `26.0419` edge `0.0466` maxDD `-0.3692`
- `market_context_high->metal_24h` score `1.91` n `45` status `ready` deltaP `24.7892` edge `0.1415` maxDD `-6.8076`
- `news_risk_high->index_1h` score `1.6006` n `50` status `ready` deltaP `20.3413` edge `0.0279` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.8706` n `50` status `ready` deltaP `18.3448` edge `0.2066` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.856` n `50` status `ready` deltaP `17.7425` edge `0.0894` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
