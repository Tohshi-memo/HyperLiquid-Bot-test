# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T09:37:33.367936+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7492`

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

- `news_risk_high->unknown_24h` score `623.572` n `135` status `ready` deltaP `1.9097` edge `51.9516` maxDD `0.0`
- `market_context_high->unknown_1h` score `493.6884` n `44` status `ready` deltaP `7.6075` edge `41.0949` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `421.1589` n `32` status `ready` deltaP `8.2317` edge `35.0417` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `17.3601` n `135` status `ready` deltaP `27.8588` edge `1.2819` maxDD `-1.0093`
- `news_risk_high->equity_24h` score `7.5129` n `135` status `ready` deltaP `26.4699` edge `0.6845` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `7.2153` n `135` status `ready` deltaP `23.9931` edge `0.7567` maxDD `-15.8971`
- `news_risk_high->index_24h` score `3.5896` n `135` status `ready` deltaP `32.662` edge `0.1292` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `3.1942` n `135` status `ready` deltaP `24.8379` edge `0.228` maxDD `-2.192`
- `news_risk_high->equity_4h` score `2.7707` n `135` status `ready` deltaP `28.5614` edge `0.2006` maxDD `-9.143`
- `market_context_high->fx_4h` score `2.6143` n `32` status `ready` deltaP `30.1829` edge `0.0297` maxDD `-0.0449`
- `market_context_high->crypto_alt_1h` score `2.2585` n `44` status `ready` deltaP `12.5885` edge `0.1706` maxDD `-3.6387`
- `market_context_high->crypto_major_4h` score `1.779` n `32` status `ready` deltaP `2.7439` edge `0.2003` maxDD `-3.294`
- `market_context_high->crypto_major_1h` score `1.679` n `44` status `ready` deltaP `10.1116` edge `0.1335` maxDD `-3.546`
- `news_risk_high->crypto_alt_4h` score `1.5937` n `135` status `ready` deltaP `10.0452` edge `0.3318` maxDD `-15.9436`
- `market_context_high->fx_1h` score `1.0295` n `44` status `ready` deltaP `15.5552` edge `0.0085` maxDD `-0.113`
- `news_risk_high->crypto_alt_1h` score `1.0082` n `135` status `ready` deltaP `8.9521` edge `0.1154` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.8948` n `135` status `ready` deltaP `9.2515` edge `0.0752` maxDD `-1.6514`
- `market_context_high->equity_1h` score `0.484` n `44` status `ready` deltaP `8.3424` edge `0.0573` maxDD `-2.4027`
- `news_risk_high->index_1h` score `0.4814` n `135` status `ready` deltaP `8.6682` edge `0.0111` maxDD `-0.302`
- `market_context_high->metal_1h` score `0.0244` n `44` status `ready` deltaP `3.1437` edge `0.013` maxDD `-0.4659`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
