# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T10:37:26.600706+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8574`

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

- `market_context_high->unknown_4h` score `40.5655` n `90` status `ready` deltaP `-2.7981` edge `3.453` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `11.1158` n `58` status `ready` deltaP `38.3305` edge `0.6911` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `8.3732` n `58` status `ready` deltaP `27.3182` edge `0.6152` maxDD `-4.9646`
- `news_risk_high->equity_24h` score `7.6336` n `58` status `ready` deltaP `19.8737` edge `0.5136` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `5.7057` n `90` status `ready` deltaP `15.1468` edge `0.9279` maxDD `-16.7906`
- `news_risk_high->index_24h` score `5.3534` n `58` status `ready` deltaP `38.6874` edge `0.1882` maxDD `0.0`
- `market_context_high->equity_24h` score `3.3627` n `90` status `ready` deltaP `17.8814` edge `0.2039` maxDD `-1.0977`
- `news_risk_high->index_4h` score `3.2847` n `58` status `ready` deltaP `35.5393` edge `0.063` maxDD `-0.4296`
- `news_risk_high->equity_4h` score `2.9059` n `58` status `ready` deltaP `20.2586` edge `0.1669` maxDD `-2.7837`
- `news_risk_high->crypto_major_1h` score `2.7788` n `58` status `ready` deltaP `11.3256` edge `0.1916` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.5402` n `90` status `ready` deltaP `16.9512` edge `0.1951` maxDD `-4.047`
- `news_risk_high->index_1h` score `2.4327` n `58` status `ready` deltaP `29.5375` edge `0.0198` maxDD `-0.1194`
- `news_risk_high->metal_4h` score `1.4412` n `58` status `ready` deltaP `21.0524` edge `0.086` maxDD `-0.993`
- `news_risk_high->crypto_alt_1h` score `1.4044` n `58` status `ready` deltaP `3.9026` edge `0.1412` maxDD `-2.3482`
- `market_context_high->metal_24h` score `1.3134` n `90` status `ready` deltaP `22.2279` edge `0.1687` maxDD `-3.5466`
- `market_context_high->fx_4h` score `0.8442` n `90` status `ready` deltaP `19.2344` edge `0.0168` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.5861` n `90` status `ready` deltaP `10.4491` edge `0.0034` maxDD `-0.271`
- `market_context_high->crypto_alt_24h` score `0.4916` n `90` status `ready` deltaP `9.0962` edge `0.5962` maxDD `-34.5048`
- `news_risk_high->equity_1h` score `0.4097` n `58` status `ready` deltaP `5.1053` edge `0.0591` maxDD `-0.7197`
- `news_risk_high->metal_1h` score `0.3637` n `58` status `ready` deltaP `10.7939` edge `0.0165` maxDD `-1.0132`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
