# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T14:07:26.196524+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `9980`

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

- `market_context_high->unknown_24h` score `534.6422` n `64` status `ready` deltaP `3.8128` edge `44.5281` maxDD `0.0`
- `news_risk_high->equity_24h` score `44.5227` n `50` status `ready` deltaP `49.1785` edge `3.453` maxDD `-3.6503`
- `market_context_high->equity_24h` score `39.8402` n `64` status `ready` deltaP `45.5535` edge `3.1705` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `32.7937` n `64` status `ready` deltaP `60.4636` edge `2.4374` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `23.6076` n `50` status `ready` deltaP `46.3882` edge `2.8317` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `12.1615` n `50` status `ready` deltaP `38.4573` edge `0.8701` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `8.7004` n `50` status `ready` deltaP `16.9636` edge `1.4529` maxDD `-29.0448`
- `market_context_high->index_24h` score `8.0048` n `64` status `ready` deltaP `48.692` edge `0.3511` maxDD `-0.0251`
- `news_risk_high->commodity_24h` score `6.943` n `50` status `ready` deltaP `45.9272` edge `0.2724` maxDD `0.0`
- `market_context_high->metal_24h` score `6.4476` n `64` status `ready` deltaP `60.8048` edge `0.5104` maxDD `-3.7989`
- `news_risk_high->index_24h` score `6.4106` n `50` status `ready` deltaP `41.3795` edge `0.2887` maxDD `-0.4279`
- `news_risk_high->crypto_major_4h` score `5.1129` n `50` status `ready` deltaP `22.8232` edge `0.4115` maxDD `-9.0062`
- `market_context_high->crypto_major_24h` score `5.0194` n `64` status `ready` deltaP `13.3882` edge `1.2628` maxDD `-69.0352`
- `news_risk_high->metal_4h` score `4.8686` n `50` status `ready` deltaP `43.9268` edge `0.1505` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.3832` n `50` status `ready` deltaP `26.689` edge `0.3309` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `4.0175` n `50` status `ready` deltaP `21.6467` edge `0.2535` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.7086` n `50` status `ready` deltaP `34.439` edge `0.1048` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.6585` n `50` status `ready` deltaP `25.8659` edge `0.0841` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2484` n `50` status `ready` deltaP `25.7425` edge `0.0412` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.2831` n `50` status `ready` deltaP `17.0479` edge `0.0234` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
