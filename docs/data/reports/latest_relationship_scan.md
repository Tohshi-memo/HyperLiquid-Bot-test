# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T17:07:30.647475+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8898`

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

- `market_context_high->unknown_4h` score `40.1554` n `91` status `ready` deltaP `-2.2246` edge `3.415` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `13.8954` n `49` status `ready` deltaP `43.5976` edge `0.8673` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `13.5596` n `49` status `ready` deltaP `45.0038` edge `0.8367` maxDD `-0.2073`
- `news_risk_high->equity_24h` score `7.8905` n `49` status `ready` deltaP `22.8592` edge `0.5151` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `7.6145` n `90` status `ready` deltaP `19.4858` edge `1.1437` maxDD `-16.7906`
- `news_risk_high->index_24h` score `5.8769` n `49` status `ready` deltaP `42.9809` edge `0.2032` maxDD `0.0`
- `news_risk_high->equity_4h` score `5.3158` n `49` status `ready` deltaP `30.5562` edge `0.2598` maxDD `-0.6421`
- `market_context_high->equity_24h` score `5.222` n `90` status `ready` deltaP `22.1336` edge `0.3305` maxDD `-1.0977`
- `news_risk_high->index_4h` score `4.3623` n `49` status `ready` deltaP `43.9958` edge `0.0747` maxDD `-0.025`
- `news_risk_high->crypto_major_1h` score `3.1781` n `49` status `ready` deltaP `12.6115` edge `0.2163` maxDD `-1.5096`
- `news_risk_high->commodity_24h` score `3.054` n `49` status `ready` deltaP `33.3534` edge `0.0406` maxDD `-0.0096`
- `news_risk_high->crypto_alt_1h` score `2.685` n `49` status `ready` deltaP `6.6388` edge `0.2112` maxDD `-1.2034`
- `news_risk_high->index_1h` score `2.3858` n `49` status `ready` deltaP `29.6866` edge `0.0149` maxDD `-0.1194`
- `market_context_high->crypto_alt_24h` score `1.637` n `90` status `ready` deltaP `11.1882` edge `0.7291` maxDD `-34.5048`
- `market_context_high->crypto_major_4h` score `1.6144` n `91` status `ready` deltaP `18.3162` edge `0.2179` maxDD `-6.9761`
- `market_context_high->metal_24h` score `1.4879` n `90` status `ready` deltaP `24.3385` edge `0.177` maxDD `-3.5466`
- `news_risk_high->metal_4h` score `1.1975` n `49` status `ready` deltaP `18.6007` edge `0.0711` maxDD `-0.993`
- `market_context_high->fx_4h` score `0.5661` n `91` status `ready` deltaP `16.4484` edge `0.0122` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.529` n `91` status `ready` deltaP `9.8408` edge `0.0027` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.3543` n `91` status `ready` deltaP `11.0417` edge `0.0607` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
