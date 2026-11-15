# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T07:07:29.757613+00:00`
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

- `market_context_high->unknown_24h` score `543.8793` n `66` status `ready` deltaP `2.4263` edge `45.3071` maxDD `0.0`
- `news_risk_high->equity_24h` score `44.3738` n `50` status `ready` deltaP `48.8319` edge `3.4429` maxDD `-3.6503`
- `market_context_high->equity_24h` score `38.1427` n `66` status `ready` deltaP `42.6501` edge `3.0484` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `30.4012` n `66` status `ready` deltaP `57.8121` edge `2.2557` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `23.6466` n `50` status `ready` deltaP `46.3882` edge `2.8367` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `12.2218` n `50` status `ready` deltaP `38.6849` edge `0.8736` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `7.8689` n `50` status `ready` deltaP `16.9636` edge `1.3463` maxDD `-29.0448`
- `market_context_high->index_24h` score `7.5304` n `66` status `ready` deltaP `44.9372` edge `0.3371` maxDD `-0.0653`
- `news_risk_high->commodity_24h` score `7.4117` n `50` status `ready` deltaP `49.5667` edge `0.2872` maxDD `0.0`
- `news_risk_high->index_24h` score `6.3341` n `50` status `ready` deltaP `40.513` edge `0.2881` maxDD `-0.4279`
- `market_context_high->metal_24h` score `5.9866` n `66` status `ready` deltaP `56.4256` edge `0.4805` maxDD `-3.7989`
- `news_risk_high->crypto_major_4h` score `5.5274` n `50` status `ready` deltaP `23.3394` edge `0.4426` maxDD `-9.0062`
- `news_risk_high->metal_4h` score `5.0666` n `50` status `ready` deltaP `45.8174` edge `0.1544` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.9924` n `50` status `ready` deltaP `29.3394` edge `0.364` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `3.978` n `50` status `ready` deltaP `21.0479` edge `0.2542` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.459` n `50` status `ready` deltaP `31.6195` edge `0.1028` maxDD `-0.3611`
- `market_context_high->crypto_major_24h` score `2.9105` n `66` status `ready` deltaP `12.6306` edge `1.1909` maxDD `-76.2717`
- `news_risk_high->index_4h` score `2.801` n `50` status `ready` deltaP `27.4673` edge `0.0853` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.3083` n `50` status `ready` deltaP `26.3413` edge `0.0422` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.2975` n `50` status `ready` deltaP `17.1976` edge `0.0236` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
