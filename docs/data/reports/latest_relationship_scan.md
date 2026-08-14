# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-14T19:07:27.656289+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11796`

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

- `market_context_high->unknown_24h` score `136.1233` n `128` status `ready` deltaP `-33.2466` edge `11.8565` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `32.7591` n `32` status `ready` deltaP `-46.5278` edge `4.5851` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `32.7591` n `32` status `ready` deltaP `-46.5278` edge `4.5851` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `10.3766` n `36` status `ready` deltaP `13.1944` edge `0.8147` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.6487` n `36` status `ready` deltaP `40.2439` edge `0.3691` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.9593` n `128` status `ready` deltaP `28.0381` edge `0.2321` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `4.5354` n `32` status `ready` deltaP `30.3819` edge `0.1754` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.5354` n `32` status `ready` deltaP `30.3819` edge `0.1754` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.674` n `32` status `ready` deltaP `18.5213` edge `0.1176` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.674` n `32` status `ready` deltaP `18.5213` edge `0.1176` maxDD `-0.1258`
- `risk_on_high->crypto_major_24h` score `2.6686` n `32` status `ready` deltaP `19.4444` edge `0.3281` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `2.6686` n `32` status `ready` deltaP `19.4444` edge `0.3281` maxDD `-6.2481`
- `news_risk_high->index_24h` score `2.3691` n `36` status `ready` deltaP `17.0139` edge `0.084` maxDD `0.0`
- `news_risk_high->index_4h` score `1.9168` n `36` status `ready` deltaP `22.0528` edge `0.0259` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.7382` n `36` status `ready` deltaP `8.5829` edge `0.1195` maxDD `-0.5496`
- `market_context_high->commodity_4h` score `1.7262` n `128` status `ready` deltaP `16.9588` edge `0.0779` maxDD `-0.7687`
- `risk_on_high->commodity_1h` score `1.2791` n `32` status `ready` deltaP `13.6602` edge `0.0388` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2791` n `32` status `ready` deltaP `13.6602` edge `0.0388` maxDD `-0.1957`
- `risk_on_high->fx_24h` score `1.0959` n `32` status `ready` deltaP `13.1944` edge `0.0218` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.0959` n `32` status `ready` deltaP `13.1944` edge `0.0218` maxDD `-0.1418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
