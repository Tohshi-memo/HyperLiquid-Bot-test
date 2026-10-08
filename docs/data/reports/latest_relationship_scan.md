# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T19:07:31.316104+00:00`
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

- `market_context_high->unknown_4h` score `40.2034` n `91` status `ready` deltaP `-2.2246` edge `3.419` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `14.7622` n `49` status `ready` deltaP `44.8171` edge `0.9314` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `14.2212` n `49` status `ready` deltaP `46.2233` edge `0.8837` maxDD `-0.2073`
- `news_risk_high->equity_24h` score `8.8486` n `49` status `ready` deltaP `24.2457` edge `0.5857` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `8.3574` n `90` status `ready` deltaP `20.8723` edge `1.2297` maxDD `-16.7906`
- `market_context_high->equity_24h` score `6.1802` n `90` status `ready` deltaP `23.5201` edge `0.4011` maxDD `-1.0977`
- `news_risk_high->index_24h` score `6.1474` n `49` status `ready` deltaP `44.3674` edge `0.2165` maxDD `0.0`
- `news_risk_high->equity_4h` score `5.8141` n `49` status `ready` deltaP `31.7757` edge `0.2932` maxDD `-0.6421`
- `news_risk_high->index_4h` score `4.5271` n `49` status `ready` deltaP `45.2153` edge `0.0803` maxDD `-0.025`
- `news_risk_high->crypto_major_1h` score `3.2092` n `49` status `ready` deltaP `12.9109` edge `0.2169` maxDD `-1.5096`
- `news_risk_high->crypto_alt_1h` score `2.7222` n `49` status `ready` deltaP `6.7885` edge `0.2133` maxDD `-1.2034`
- `news_risk_high->commodity_24h` score `2.6971` n `49` status `ready` deltaP `31.9669` edge `0.0201` maxDD `-0.0096`
- `market_context_high->crypto_alt_24h` score `2.4338` n `90` status `ready` deltaP `12.5747` edge `0.822` maxDD `-34.5048`
- `news_risk_high->index_1h` score `2.4254` n `49` status `ready` deltaP `29.986` edge `0.0162` maxDD `-0.1194`
- `market_context_high->crypto_major_4h` score `2.0444` n `91` status `ready` deltaP `19.5357` edge `0.2649` maxDD `-6.9761`
- `market_context_high->metal_24h` score `1.4801` n `90` status `ready` deltaP `24.3385` edge `0.176` maxDD `-3.5466`
- `news_risk_high->metal_4h` score `1.2527` n `49` status `ready` deltaP `19.3629` edge `0.0731` maxDD `-0.993`
- `market_context_high->fx_4h` score `0.5917` n `91` status `ready` deltaP `16.7533` edge `0.0123` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.4631` n `91` status `ready` deltaP `9.0923` edge `0.0022` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.3745` n `91` status `ready` deltaP `11.3411` edge `0.0613` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
