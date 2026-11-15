# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T09:22:23.354551+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `9948`

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

- `market_context_high->unknown_24h` score `535.3893` n `66` status `ready` deltaP `2.4263` edge `44.5996` maxDD `0.0`
- `news_risk_high->equity_24h` score `44.3702` n `50` status `ready` deltaP `48.8319` edge `3.4426` maxDD `-3.6503`
- `market_context_high->equity_24h` score `38.1391` n `66` status `ready` deltaP `42.6501` edge `3.0481` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `30.8128` n `66` status `ready` deltaP `57.8121` edge `2.29` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `23.7386` n `50` status `ready` deltaP `46.3882` edge `2.8485` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `12.3527` n `50` status `ready` deltaP `39.6768` edge `0.8779` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `8.1364` n `50` status `ready` deltaP `16.9636` edge `1.3806` maxDD `-29.0448`
- `market_context_high->index_24h` score `7.5232` n `66` status `ready` deltaP `44.9372` edge `0.3365` maxDD `-0.0653`
- `news_risk_high->commodity_24h` score `7.2691` n `50` status `ready` deltaP `48.3536` edge `0.2834` maxDD `0.0`
- `news_risk_high->index_24h` score `6.3269` n `50` status `ready` deltaP `40.513` edge `0.2875` maxDD `-0.4279`
- `market_context_high->metal_24h` score `6.1457` n `66` status `ready` deltaP `57.9854` edge `0.4905` maxDD `-3.7989`
- `news_risk_high->crypto_major_4h` score `5.6877` n `50` status `ready` deltaP `23.7378` edge `0.4533` maxDD `-9.0062`
- `news_risk_high->metal_4h` score `5.0923` n `50` status `ready` deltaP `46.2134` edge `0.1539` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `5.0645` n `50` status `ready` deltaP `29.2805` edge `0.3704` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `3.9924` n `50` status `ready` deltaP `21.3473` edge `0.2534` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.5064` n `50` status `ready` deltaP `32.1524` edge `0.1032` maxDD `-0.3611`
- `market_context_high->crypto_major_24h` score `3.0521` n `66` status `ready` deltaP `12.6306` edge `1.2027` maxDD `-76.2717`
- `news_risk_high->index_4h` score `2.8302` n `50` status `ready` deltaP `27.8476` edge `0.0852` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.3131` n `50` status `ready` deltaP `26.491` edge `0.0416` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.2963` n `50` status `ready` deltaP `17.1976` edge `0.0235` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
