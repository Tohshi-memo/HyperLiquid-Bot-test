# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T12:52:29.741090+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7070`

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

- `market_context_high->unknown_1h` score `326.7867` n `50` status `ready` deltaP `7.7305` edge `27.1856` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `280.9888` n `50` status `ready` deltaP `6.8598` edge `23.37` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.0504` n `116` status `ready` deltaP `31.7828` edge `1.3966` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `9.2519` n `50` status `ready` deltaP `30.4375` edge `0.7097` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.0855` n `50` status `ready` deltaP `18.9146` edge `0.5347` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.5793` n `50` status `ready` deltaP `15.2744` edge `0.4091` maxDD `-7.6792`
- `news_risk_high->equity_4h` score `4.294` n `123` status `ready` deltaP `29.7764` edge `0.2082` maxDD `-1.2436`
- `market_context_high->equity_24h` score `3.6958` n `50` status `ready` deltaP `17.1319` edge `0.5458` maxDD `-11.8957`
- `news_risk_high->equity_24h` score `3.2265` n `116` status `ready` deltaP `21.5457` edge `0.5049` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `3.2099` n `116` status `ready` deltaP `20.8513` edge `0.5879` maxDD `-15.8971`
- `market_context_high->crypto_alt_24h` score `3.2098` n `50` status `ready` deltaP `7.5069` edge `0.3884` maxDD `-11.6768`
- `market_context_high->fx_4h` score `2.9996` n `50` status `ready` deltaP `33.9085` edge `0.0374` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `2.9195` n `50` status `ready` deltaP `14.5988` edge `0.191` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `2.7011` n `50` status `ready` deltaP `12.7066` edge `0.2067` maxDD `-3.6387`
- `news_risk_high->index_24h` score `2.4146` n `116` status `ready` deltaP `23.5692` edge `0.0919` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `2.2371` n `116` status `ready` deltaP `26.3111` edge `0.2388` maxDD `-2.192`
- `market_context_high->fx_1h` score `1.4448` n `50` status `ready` deltaP `20.3413` edge `0.0112` maxDD `-0.113`
- `news_risk_high->crypto_alt_4h` score `1.1684` n `123` status `ready` deltaP `8.689` edge `0.2401` maxDD `-10.7193`
- `news_risk_high->equity_1h` score `0.8459` n `129` status `ready` deltaP `8.4227` edge `0.068` maxDD `-0.9592`
- `market_context_high->index_24h` score `0.7104` n `50` status `ready` deltaP `12.5347` edge `0.0646` maxDD `-1.2338`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
