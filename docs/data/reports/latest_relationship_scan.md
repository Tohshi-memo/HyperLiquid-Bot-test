# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T22:37:35.177185+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4296`

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

- `market_context_high->unknown_24h` score `988.7039` n `42` status `ready` deltaP `3.4483` edge `82.369` maxDD `0.0`
- `news_risk_high->equity_24h` score `53.953` n `50` status `ready` deltaP `59.2069` edge `4.172` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `20.0787` n `50` status `ready` deltaP `38.0` edge `2.4352` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `14.6496` n `50` status `ready` deltaP `45.0776` edge `1.0333` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `13.2098` n `42` status `ready` deltaP `46.6667` edge `1.7095` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `12.233` n `42` status `ready` deltaP `18.9245` edge `1.5966` maxDD `-8.6878`
- `news_risk_high->crypto_alt_24h` score `9.4902` n `50` status `ready` deltaP `22.4483` edge `1.5176` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.0675` n `50` status `ready` deltaP `50.2414` edge `0.3677` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.6481` n `50` status `ready` deltaP `42.2414` edge `0.2724` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.4119` n `50` status `ready` deltaP `47.6438` edge `0.171` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.5442` n `50` status `ready` deltaP `26.7519` edge `0.3439` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `4.5394` n `50` status `ready` deltaP `22.3952` edge `0.292` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `4.3906` n `50` status `ready` deltaP `21.9696` edge `0.357` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `4.1207` n `50` status `ready` deltaP `37.2511` edge `0.1204` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.2278` n `50` status `ready` deltaP `30.207` edge `0.1026` maxDD `-0.7999`
- `market_context_high->metal_24h` score `2.8943` n `42` status `ready` deltaP `27.9638` edge `0.1697` maxDD `-5.1946`
- `news_risk_high->metal_1h` score `2.336` n `50` status `ready` deltaP `26.0419` edge `0.0465` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.5886` n `50` status `ready` deltaP `20.1916` edge `0.0279` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.8753` n `50` status `ready` deltaP `18.3448` edge `0.2072` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.838` n `50` status `ready` deltaP `17.5928` edge `0.0881` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
