# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T06:37:25.097624+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `9718`

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

- `market_context_high->unknown_24h` score `545.7489` n `66` status `ready` deltaP `2.4263` edge `45.4629` maxDD `0.0`
- `news_risk_high->equity_24h` score `44.3426` n `50` status `ready` deltaP `48.8319` edge `3.4403` maxDD `-3.6503`
- `market_context_high->equity_24h` score `38.1115` n `66` status `ready` deltaP `42.6501` edge `3.0458` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `30.2668` n `66` status `ready` deltaP `57.8121` edge `2.2445` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `23.5912` n `50` status `ready` deltaP `46.3882` edge `2.8296` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `12.183` n `50` status `ready` deltaP `38.3805` edge `0.8724` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `7.7815` n `50` status `ready` deltaP `16.9636` edge `1.3351` maxDD `-29.0448`
- `market_context_high->index_24h` score `7.528` n `66` status `ready` deltaP `44.9372` edge `0.3369` maxDD `-0.0653`
- `news_risk_high->commodity_24h` score `7.428` n `50` status `ready` deltaP `49.74` edge `0.2874` maxDD `0.0`
- `news_risk_high->index_24h` score `6.3317` n `50` status `ready` deltaP `40.513` edge `0.2879` maxDD `-0.4279`
- `market_context_high->metal_24h` score `5.9437` n `66` status `ready` deltaP `56.079` edge `0.4773` maxDD `-3.7989`
- `news_risk_high->crypto_major_4h` score `5.4962` n `50` status `ready` deltaP `23.3394` edge `0.44` maxDD `-9.0062`
- `news_risk_high->metal_4h` score `5.0411` n `50` status `ready` deltaP `45.5129` edge `0.1543` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.9998` n `50` status `ready` deltaP `29.4916` edge `0.3636` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `3.9648` n `50` status `ready` deltaP `20.8982` edge `0.2541` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.4578` n `50` status `ready` deltaP `31.6195` edge `0.1027` maxDD `-0.3611`
- `market_context_high->crypto_major_24h` score `2.8253` n `66` status `ready` deltaP `12.6306` edge `1.1838` maxDD `-76.2717`
- `news_risk_high->index_4h` score `2.7998` n `50` status `ready` deltaP `27.4673` edge `0.0852` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.3095` n `50` status `ready` deltaP `26.3413` edge `0.0423` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.2735` n `50` status `ready` deltaP `16.8982` edge `0.0236` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
