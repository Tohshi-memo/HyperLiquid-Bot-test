# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T18:37:36.749974+00:00`
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

- `market_context_high->unknown_4h` score `40.2262` n `91` status `ready` deltaP `-2.2246` edge `3.4209` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `14.577` n `49` status `ready` deltaP `44.5122` edge `0.918` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `14.0804` n `49` status `ready` deltaP `45.9184` edge `0.874` maxDD `-0.2073`
- `news_risk_high->equity_24h` score `8.6217` n `49` status `ready` deltaP `23.8991` edge `0.5691` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `8.1873` n `90` status `ready` deltaP `20.5257` edge `1.2102` maxDD `-16.7906`
- `news_risk_high->index_24h` score `6.0825` n `49` status `ready` deltaP `44.0208` edge `0.2134` maxDD `0.0`
- `market_context_high->equity_24h` score `5.9532` n `90` status `ready` deltaP `23.1735` edge `0.3845` maxDD `-1.0977`
- `news_risk_high->equity_4h` score `5.7045` n `49` status `ready` deltaP `31.4708` edge `0.2861` maxDD `-0.6421`
- `news_risk_high->index_4h` score `4.4895` n `49` status `ready` deltaP `44.9104` edge `0.0792` maxDD `-0.025`
- `news_risk_high->crypto_major_1h` score `3.2356` n `49` status `ready` deltaP `12.9109` edge `0.2191` maxDD `-1.5096`
- `news_risk_high->commodity_24h` score `2.768` n `49` status `ready` deltaP `32.3135` edge `0.0237` maxDD `-0.0096`
- `news_risk_high->crypto_alt_1h` score `2.763` n `49` status `ready` deltaP `6.7885` edge `0.2167` maxDD `-1.2034`
- `news_risk_high->index_1h` score `2.423` n `49` status `ready` deltaP `29.986` edge `0.016` maxDD `-0.1194`
- `market_context_high->crypto_alt_24h` score `2.2558` n `90` status `ready` deltaP `12.228` edge `0.8015` maxDD `-34.5048`
- `market_context_high->crypto_major_4h` score `1.9529` n `91` status `ready` deltaP `19.2308` edge `0.2552` maxDD `-6.9761`
- `market_context_high->metal_24h` score `1.4946` n `90` status `ready` deltaP `24.5118` edge `0.1767` maxDD `-3.5466`
- `news_risk_high->metal_4h` score `1.2504` n `49` status `ready` deltaP `19.3629` edge `0.0728` maxDD `-0.993`
- `market_context_high->fx_4h` score `0.5905` n `91` status `ready` deltaP `16.7533` edge `0.0122` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.4895` n `91` status `ready` deltaP `9.3917` edge `0.0024` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.3917` n `91` status `ready` deltaP `11.3411` edge `0.0635` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
