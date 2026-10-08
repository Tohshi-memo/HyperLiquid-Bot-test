# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T10:07:29.650034+00:00`
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

- `market_context_high->unknown_4h` score `40.3447` n `90` status `ready` deltaP `-2.7981` edge `3.4346` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `11.1482` n `60` status `ready` deltaP `38.4655` edge `0.6929` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.8061` n `60` status `ready` deltaP `24.8069` edge `0.5957` maxDD `-5.1792`
- `news_risk_high->equity_24h` score `7.6808` n `60` status `ready` deltaP `19.7582` edge `0.5183` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `5.5902` n `90` status `ready` deltaP `14.8013` edge `0.9154` maxDD `-16.7906`
- `news_risk_high->index_24h` score `5.3054` n `60` status `ready` deltaP `38.342` edge `0.1865` maxDD `0.0`
- `news_risk_high->index_4h` score `3.2891` n `60` status `ready` deltaP `35.5793` edge `0.0631` maxDD `-0.4296`
- `market_context_high->equity_24h` score `3.227` n `90` status `ready` deltaP `17.536` edge `0.1949` maxDD `-1.0977`
- `news_risk_high->equity_4h` score `2.8519` n `60` status `ready` deltaP `20.5284` edge `0.1606` maxDD `-2.7837`
- `news_risk_high->crypto_major_1h` score `2.836` n `60` status `ready` deltaP `12.3254` edge `0.1897` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.5077` n `90` status `ready` deltaP `16.7988` edge `0.1934` maxDD `-4.047`
- `news_risk_high->index_1h` score `2.3236` n `60` status `ready` deltaP `28.3533` edge `0.0186` maxDD `-0.1194`
- `news_risk_high->crypto_alt_1h` score `1.5001` n `60` status `ready` deltaP `5.1896` edge `0.1406` maxDD `-2.3482`
- `news_risk_high->metal_4h` score `1.4962` n `60` status `ready` deltaP `21.8394` edge `0.0878` maxDD `-0.993`
- `market_context_high->metal_24h` score `1.2861` n `90` status `ready` deltaP `21.8825` edge `0.1675` maxDD `-3.5466`
- `news_risk_high->unknown_4h` score `1.0592` n `60` status `ready` deltaP `-6.687` edge `0.2574` maxDD `-5.6309`
- `market_context_high->fx_4h` score `0.8722` n `90` status `ready` deltaP `19.5393` edge `0.0171` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.5993` n `90` status `ready` deltaP `10.5988` edge `0.0035` maxDD `-0.271`
- `market_context_high->crypto_alt_24h` score `0.4636` n `90` status `ready` deltaP `9.0962` edge `0.5926` maxDD `-34.5048`
- `news_risk_high->metal_1h` score `0.2217` n `60` status `ready` deltaP `8.7824` edge `0.0117` maxDD `-1.0132`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
