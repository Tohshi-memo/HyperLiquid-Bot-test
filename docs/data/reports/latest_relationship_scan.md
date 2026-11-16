# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T22:07:39.822478+00:00`
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

- `market_context_high->unknown_24h` score `784.9853` n `40` status `ready` deltaP `3.6207` edge `65.3913` maxDD `0.0`
- `news_risk_high->equity_24h` score `53.881` n `50` status `ready` deltaP `59.2069` edge `4.166` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `20.1793` n `50` status `ready` deltaP `38.3448` edge `2.4458` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `14.6548` n `50` status `ready` deltaP `45.1429` edge `1.0333` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `12.9991` n `40` status `ready` deltaP `45.3448` edge `1.6913` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `12.239` n `40` status `ready` deltaP `18.6207` edge `1.5994` maxDD `-8.6878`
- `news_risk_high->crypto_alt_24h` score `9.5468` n `50` status `ready` deltaP `22.6207` edge `1.5237` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.0627` n `50` status `ready` deltaP `50.2414` edge `0.3673` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.5701` n `50` status `ready` deltaP `41.8966` edge `0.2682` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.4336` n `50` status `ready` deltaP `47.8541` edge `0.1714` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.5902` n `50` status `ready` deltaP `26.9666` edge `0.3463` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `4.5394` n `50` status `ready` deltaP `22.3952` edge `0.292` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `4.4269` n `50` status `ready` deltaP `22.1824` edge `0.3586` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `4.1226` n `50` status `ready` deltaP `37.3191` edge `0.1201` maxDD `-0.3611`
- `market_context_high->metal_24h` score `3.433` n `40` status `ready` deltaP `30.3448` edge `0.1818` maxDD `-4.5078`
- `news_risk_high->index_4h` score `3.2348` n `50` status `ready` deltaP `30.2796` edge `0.1027` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.3372` n `50` status `ready` deltaP `26.0419` edge `0.0466` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.5766` n `50` status `ready` deltaP `20.0419` edge `0.0279` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.8839` n `50` status `ready` deltaP `18.3448` edge `0.2083` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.863` n `50` status `ready` deltaP `17.8922` edge `0.0893` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
