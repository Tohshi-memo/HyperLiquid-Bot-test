# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T11:22:33.345832+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `9954`

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

- `market_context_high->unknown_24h` score `531.87` n `66` status `ready` deltaP `3.1196` edge `44.3017` maxDD `0.0`
- `news_risk_high->equity_24h` score `44.4026` n `50` status `ready` deltaP `48.8319` edge `3.4453` maxDD `-3.6503`
- `market_context_high->equity_24h` score `38.1715` n `66` status `ready` deltaP `42.6501` edge `3.0508` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `31.1752` n `66` status `ready` deltaP `57.8121` edge `2.3202` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `23.7363` n `50` status `ready` deltaP `46.3882` edge `2.8482` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `12.3093` n `50` status `ready` deltaP `39.5244` edge `0.8753` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `8.372` n `50` status `ready` deltaP `16.9636` edge `1.4108` maxDD `-29.0448`
- `market_context_high->index_24h` score `7.5244` n `66` status `ready` deltaP `44.9372` edge `0.3366` maxDD `-0.0653`
- `news_risk_high->commodity_24h` score `7.1595` n `50` status `ready` deltaP `47.3137` edge `0.2812` maxDD `0.0`
- `news_risk_high->index_24h` score `6.3281` n `50` status `ready` deltaP `40.513` edge `0.2876` maxDD `-0.4279`
- `market_context_high->metal_24h` score `6.2841` n `66` status `ready` deltaP `59.3719` edge `0.499` maxDD `-3.7989`
- `market_context_high->unknown_4h` score `5.8745` n `82` status `ready` deltaP `8.8415` edge `0.4306` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `5.4921` n `50` status `ready` deltaP `23.7378` edge `0.437` maxDD `-9.0062`
- `news_risk_high->metal_4h` score `5.0097` n `50` status `ready` deltaP `45.4512` edge `0.1521` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.816` n `50` status `ready` deltaP `28.2134` edge `0.3568` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `4.0127` n `50` status `ready` deltaP `21.6467` edge `0.2531` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.588` n `50` status `ready` deltaP `33.0671` edge `0.1039` maxDD `-0.3611`
- `market_context_high->crypto_major_24h` score `3.0485` n `66` status `ready` deltaP `12.6306` edge `1.2024` maxDD `-76.2717`
- `news_risk_high->index_4h` score `2.7632` n `50` status `ready` deltaP `27.0854` edge `0.0847` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2855` n `50` status `ready` deltaP `26.1916` edge `0.0413` maxDD `-0.3692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
