# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T19:07:26.790613+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8954`

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

- `market_context_high->crypto_major_24h` score `6.9939` n `62` status `ready` deltaP `25.1568` edge `1.2059` maxDD `-31.8231`
- `risk_on_high->crypto_alt_4h` score `4.5486` n `48` status `ready` deltaP `19.563` edge `0.2934` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `4.5486` n `48` status `ready` deltaP `19.563` edge `0.2934` maxDD `-1.9151`
- `market_context_high->crypto_alt_4h` score `3.8467` n `100` status `ready` deltaP `14.6463` edge `0.3678` maxDD `-9.2574`
- `risk_on_high->crypto_major_4h` score `3.8276` n `48` status `ready` deltaP `34.1972` edge `0.348` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.8276` n `48` status `ready` deltaP `34.1972` edge `0.348` maxDD `-4.1548`
- `market_context_high->crypto_major_4h` score `3.498` n `100` status `ready` deltaP `18.0305` edge `0.3272` maxDD `-7.4722`
- `market_context_high->crypto_alt_24h` score `2.5167` n `62` status `ready` deltaP `13.1776` edge `0.9118` maxDD `-47.4926`
- `market_context_high->crypto_alt_1h` score `1.6161` n `100` status `ready` deltaP `12.2036` edge `0.1484` maxDD `-4.9401`
- `risk_on_high->crypto_alt_1h` score `0.9946` n `48` status `ready` deltaP `6.5369` edge `0.099` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `0.9946` n `48` status `ready` deltaP `6.5369` edge `0.099` maxDD `-2.4421`
- `market_context_high->unknown_4h` score `0.9253` n `100` status `ready` deltaP `-3.7744` edge `0.1669` maxDD `-1.8373`
- `market_context_high->crypto_major_1h` score `0.716` n `100` status `ready` deltaP `4.6467` edge `0.105` maxDD `-3.4384`
- `risk_on_high->crypto_major_1h` score `0.4537` n `48` status `ready` deltaP `5.8134` edge `0.0847` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `0.4537` n `48` status `ready` deltaP `5.8134` edge `0.0847` maxDD `-3.2233`
- `market_context_high->index_1h` score `0.0429` n `100` status `ready` deltaP `5.2012` edge `0.0039` maxDD `-0.3122`
- `market_context_high->metal_1h` score `-0.1357` n `100` status `ready` deltaP `6.1018` edge `0.0041` maxDD `-0.4868`
- `market_context_high->metal_4h` score `-0.2544` n `100` status `ready` deltaP `9.5244` edge `0.0106` maxDD `-1.624`
- `risk_on_high->metal_1h` score `-0.3183` n `48` status `ready` deltaP `3.2685` edge `0.0036` maxDD `-0.4868`
- `risk_on_and_context->metal_1h` score `-0.3183` n `48` status `ready` deltaP `3.2685` edge `0.0036` maxDD `-0.4868`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
