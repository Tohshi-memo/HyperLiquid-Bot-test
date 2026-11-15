# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T10:22:27.666555+00:00`
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

- `market_context_high->unknown_24h` score `531.7257` n `66` status `ready` deltaP `2.4263` edge `44.2943` maxDD `0.0`
- `news_risk_high->equity_24h` score `44.3774` n `50` status `ready` deltaP `48.8319` edge `3.4432` maxDD `-3.6503`
- `market_context_high->equity_24h` score `38.1463` n `66` status `ready` deltaP `42.6501` edge `3.0487` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `30.9904` n `66` status `ready` deltaP `57.8121` edge `2.3048` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `23.748` n `50` status `ready` deltaP `46.3882` edge `2.8497` maxDD `-6.8139`
- `market_context_high->unknown_4h` score `16.7933` n `78` status `ready` deltaP `8.8415` edge `1.3405` maxDD `0.0`
- `news_risk_high->equity_4h` score `12.3443` n `50` status `ready` deltaP `39.6768` edge `0.8772` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `8.2519` n `50` status `ready` deltaP `16.9636` edge `1.3954` maxDD `-29.0448`
- `market_context_high->index_24h` score `7.522` n `66` status `ready` deltaP `44.9372` edge `0.3364` maxDD `-0.0653`
- `news_risk_high->commodity_24h` score `7.2083` n `50` status `ready` deltaP `47.8336` edge `0.2818` maxDD `0.0`
- `news_risk_high->index_24h` score `6.3257` n `50` status `ready` deltaP `40.513` edge `0.2874` maxDD `-0.4279`
- `market_context_high->metal_24h` score `6.2146` n `66` status `ready` deltaP `58.6787` edge `0.4947` maxDD `-3.7989`
- `news_risk_high->crypto_major_4h` score `5.6133` n `50` status `ready` deltaP `23.7378` edge `0.4471` maxDD `-9.0062`
- `news_risk_high->metal_4h` score `5.0559` n `50` status `ready` deltaP `45.9085` edge `0.1529` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.9667` n `50` status `ready` deltaP `28.8232` edge `0.3653` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `4.0139` n `50` status `ready` deltaP `21.6467` edge `0.2532` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.5332` n `50` status `ready` deltaP `32.4573` edge `0.1034` maxDD `-0.3611`
- `market_context_high->crypto_major_24h` score `3.0665` n `66` status `ready` deltaP `12.6306` edge `1.2039` maxDD `-76.2717`
- `news_risk_high->index_4h` score `2.7912` n `50` status `ready` deltaP `27.3902` edge `0.085` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2855` n `50` status `ready` deltaP `26.1916` edge `0.0413` maxDD `-0.3692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
