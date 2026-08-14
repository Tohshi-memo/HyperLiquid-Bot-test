# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-14T15:22:26.214414+00:00`
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

- `market_context_high->unknown_24h` score `117.3261` n `136` status `ready` deltaP `-33.5376` edge `10.292` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `32.8492` n `32` status `ready` deltaP `-45.4861` edge `4.5897` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `32.8492` n `32` status `ready` deltaP `-45.4861` edge `4.5897` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `9.7434` n `36` status `ready` deltaP `10.5902` edge `0.7793` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.2336` n `36` status `ready` deltaP `38.4146` edge `0.3467` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.7642` n `32` status `ready` deltaP `32.1181` edge `0.1829` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.7642` n `32` status `ready` deltaP `32.1181` edge `0.1829` maxDD `0.0`
- `market_context_high->commodity_24h` score `3.619` n `136` status `ready` deltaP `24.0299` edge `0.1997` maxDD `-1.9989`
- `risk_on_high->commodity_4h` score `2.9382` n `32` status `ready` deltaP `20.503` edge `0.1264` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.9382` n `32` status `ready` deltaP `20.503` edge `0.1264` maxDD `-0.1258`
- `risk_on_high->crypto_major_24h` score `2.1276` n `32` status `ready` deltaP `16.8403` edge `0.2761` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `2.1276` n `32` status `ready` deltaP `16.8403` edge `0.2761` maxDD `-6.2481`
- `news_risk_high->index_24h` score `2.108` n `36` status `ready` deltaP `14.4097` edge `0.0796` maxDD `0.0`
- `news_risk_high->equity_1h` score `1.7178` n `36` status `ready` deltaP `8.7326` edge `0.1168` maxDD `-0.5496`
- `news_risk_high->index_4h` score `1.6957` n `36` status `ready` deltaP `19.9187` edge `0.0217` maxDD `-0.0546`
- `risk_on_high->commodity_1h` score `1.2935` n `32` status `ready` deltaP `13.6602` edge `0.04` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2935` n `32` status `ready` deltaP `13.6602` edge `0.04` maxDD `-0.1957`
- `risk_on_high->fx_24h` score `1.1881` n `32` status `ready` deltaP `14.0625` edge `0.0237` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.1881` n `32` status `ready` deltaP `14.0625` edge `0.0237` maxDD `-0.1418`
- `market_context_high->commodity_4h` score `1.1664` n `136` status `ready` deltaP `14.4368` edge `0.0648` maxDD `-2.1077`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
