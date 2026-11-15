# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T07:22:33.104075+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `9936`

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

- `market_context_high->unknown_24h` score `542.9433` n `66` status `ready` deltaP `2.4263` edge `45.2291` maxDD `0.0`
- `news_risk_high->equity_24h` score `44.3846` n `50` status `ready` deltaP `48.8319` edge `3.4438` maxDD `-3.6503`
- `market_context_high->equity_24h` score `38.1535` n `66` status `ready` deltaP `42.6501` edge `3.0493` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `30.448` n `66` status `ready` deltaP `57.8121` edge `2.2596` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `23.663` n `50` status `ready` deltaP `46.3882` edge `2.8388` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `12.2423` n `50` status `ready` deltaP `38.8371` edge `0.8743` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `7.8993` n `50` status `ready` deltaP `16.9636` edge `1.3502` maxDD `-29.0448`
- `market_context_high->index_24h` score `7.5316` n `66` status `ready` deltaP `44.9372` edge `0.3372` maxDD `-0.0653`
- `news_risk_high->commodity_24h` score `7.3955` n `50` status `ready` deltaP `49.3934` edge `0.287` maxDD `0.0`
- `news_risk_high->index_24h` score `6.3353` n `50` status `ready` deltaP `40.513` edge `0.2882` maxDD `-0.4279`
- `market_context_high->metal_24h` score `6.0066` n `66` status `ready` deltaP `56.5989` edge `0.4819` maxDD `-3.7989`
- `news_risk_high->crypto_major_4h` score `5.5466` n `50` status `ready` deltaP `23.3394` edge `0.4442` maxDD `-9.0062`
- `news_risk_high->metal_4h` score `5.08` n `50` status `ready` deltaP `45.9696` edge `0.1545` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.9972` n `50` status `ready` deltaP `29.3394` edge `0.3644` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `3.978` n `50` status `ready` deltaP `21.0479` edge `0.2542` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.459` n `50` status `ready` deltaP `31.6195` edge `0.1028` maxDD `-0.3611`
- `market_context_high->crypto_major_24h` score `2.9357` n `66` status `ready` deltaP `12.6306` edge `1.193` maxDD `-76.2717`
- `news_risk_high->index_4h` score `2.8132` n `50` status `ready` deltaP `27.6195` edge `0.0853` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.3071` n `50` status `ready` deltaP `26.3413` edge `0.0421` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.2975` n `50` status `ready` deltaP `17.1976` edge `0.0236` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
