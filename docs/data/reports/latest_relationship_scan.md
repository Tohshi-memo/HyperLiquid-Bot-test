# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T17:53:05.302222+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8914`

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

- `market_context_high->unknown_4h` score `40.201` n `91` status `ready` deltaP `-2.2246` edge `3.4188` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `14.2512` n `49` status `ready` deltaP `44.0549` edge `0.8939` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `13.8314` n `49` status `ready` deltaP `45.4611` edge `0.8563` maxDD `-0.2073`
- `news_risk_high->equity_24h` score `8.2753` n `49` status `ready` deltaP `23.3792` edge `0.5437` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `7.9177` n `90` status `ready` deltaP `20.0057` edge `1.1791` maxDD `-16.7906`
- `news_risk_high->index_24h` score `5.9821` n `49` status `ready` deltaP `43.5009` edge `0.2085` maxDD `0.0`
- `market_context_high->equity_24h` score `5.6068` n `90` status `ready` deltaP `22.6536` edge `0.3591` maxDD `-1.0977`
- `news_risk_high->equity_4h` score `5.5192` n `49` status `ready` deltaP `31.0135` edge `0.2737` maxDD `-0.6421`
- `news_risk_high->index_4h` score `4.4253` n `49` status `ready` deltaP `44.4531` edge `0.0769` maxDD `-0.025`
- `news_risk_high->crypto_major_1h` score `3.2596` n `49` status `ready` deltaP `12.9109` edge `0.2211` maxDD `-1.5096`
- `news_risk_high->commodity_24h` score `2.9116` n `49` status `ready` deltaP `32.8335` edge `0.0322` maxDD `-0.0096`
- `news_risk_high->crypto_alt_1h` score `2.8073` n `49` status `ready` deltaP `6.9382` edge `0.2194` maxDD `-1.2034`
- `news_risk_high->index_1h` score `2.4206` n `49` status `ready` deltaP `29.986` edge `0.0158` maxDD `-0.1194`
- `market_context_high->crypto_alt_24h` score `1.962` n `90` status `ready` deltaP `11.7081` edge `0.7673` maxDD `-34.5048`
- `market_context_high->crypto_major_4h` score `1.7911` n `91` status `ready` deltaP `18.7735` edge `0.2375` maxDD `-6.9761`
- `market_context_high->metal_24h` score `1.4993` n `90` status `ready` deltaP `24.5118` edge `0.1773` maxDD `-3.5466`
- `news_risk_high->metal_4h` score `1.2188` n `49` status `ready` deltaP `18.9055` edge `0.0718` maxDD `-0.993`
- `market_context_high->fx_4h` score `0.5527` n `91` status `ready` deltaP `16.2959` edge `0.0121` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.5146` n `91` status `ready` deltaP `9.6911` edge `0.0025` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.4073` n `91` status `ready` deltaP `11.3411` edge `0.0655` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
