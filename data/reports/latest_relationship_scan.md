# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T14:22:35.495625+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `9996`

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

- `market_context_high->unknown_24h` score `534.653` n `64` status `ready` deltaP `3.8128` edge `44.529` maxDD `0.0`
- `news_risk_high->equity_24h` score `44.5287` n `50` status `ready` deltaP `49.1785` edge `3.4535` maxDD `-3.6503`
- `market_context_high->equity_24h` score `39.8462` n `64` status `ready` deltaP `45.5535` edge `3.171` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `32.8285` n `64` status `ready` deltaP `60.4636` edge `2.4403` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `23.5795` n `50` status `ready` deltaP `46.3882` edge `2.8281` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `12.1579` n `50` status `ready` deltaP `38.4573` edge `0.8698` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `8.723` n `50` status `ready` deltaP `16.9636` edge `1.4558` maxDD `-29.0448`
- `market_context_high->index_24h` score `8.0199` n `64` status `ready` deltaP `48.8654` edge `0.3512` maxDD `-0.0251`
- `news_risk_high->commodity_24h` score `6.937` n `50` status `ready` deltaP `45.9272` edge `0.2719` maxDD `0.0`
- `market_context_high->metal_24h` score `6.4652` n `64` status `ready` deltaP `60.9781` edge `0.5115` maxDD `-3.7989`
- `news_risk_high->index_24h` score `6.4256` n `50` status `ready` deltaP `41.5529` edge `0.2888` maxDD `-0.4279`
- `news_risk_high->crypto_major_4h` score `5.1021` n `50` status `ready` deltaP `22.8232` edge `0.4106` maxDD `-9.0062`
- `market_context_high->crypto_major_24h` score `4.9762` n `64` status `ready` deltaP `13.3882` edge `1.2592` maxDD `-69.0352`
- `news_risk_high->metal_4h` score `4.8552` n `50` status `ready` deltaP `43.7744` edge `0.1504` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.37` n `50` status `ready` deltaP `26.689` edge `0.3298` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `4.0175` n `50` status `ready` deltaP `21.6467` edge `0.2535` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.7244` n `50` status `ready` deltaP `34.5915` edge `0.1051` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.6463` n `50` status `ready` deltaP `25.7134` edge `0.0841` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2484` n `50` status `ready` deltaP `25.7425` edge `0.0412` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.2831` n `50` status `ready` deltaP `17.0479` edge `0.0234` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
