# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T12:07:30.379358+00:00`
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

- `market_context_high->unknown_4h` score `40.6843` n `90` status `ready` deltaP `-2.7981` edge `3.4629` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `12.4447` n `52` status `ready` deltaP `43.5623` edge `0.7534` maxDD `-0.2073`
- `news_risk_high->crypto_alt_4h` score `11.5343` n `52` status `ready` deltaP `36.9137` edge `0.7456` maxDD `-1.4399`
- `news_risk_high->equity_24h` score `6.9929` n `52` status `ready` deltaP `20.1143` edge `0.4586` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `6.1106` n `90` status `ready` deltaP `16.183` edge `0.9729` maxDD `-16.7906`
- `news_risk_high->index_24h` score `5.4315` n `52` status `ready` deltaP `39.7237` edge `0.1878` maxDD `0.0`
- `news_risk_high->equity_4h` score `3.8191` n `52` status `ready` deltaP `24.4958` edge `0.1937` maxDD `-2.0995`
- `market_context_high->equity_24h` score `3.7816` n `90` status `ready` deltaP `18.9177` edge `0.2319` maxDD `-1.0977`
- `news_risk_high->index_4h` score `3.6698` n `52` status `ready` deltaP `38.8016` edge `0.0648` maxDD `-0.4127`
- `news_risk_high->crypto_major_1h` score `3.174` n `52` status `ready` deltaP `13.5652` edge `0.2096` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.6992` n `90` status `ready` deltaP `17.4085` edge `0.2053` maxDD `-4.047`
- `news_risk_high->commodity_24h` score `2.4395` n `52` status `ready` deltaP `31.1445` edge `0.0331` maxDD `-1.9951`
- `news_risk_high->crypto_alt_1h` score `2.4364` n `52` status `ready` deltaP `6.9208` edge `0.1886` maxDD `-1.2034`
- `news_risk_high->index_1h` score `2.4126` n `52` status `ready` deltaP `29.5716` edge `0.0179` maxDD `-0.1194`
- `market_context_high->metal_24h` score `1.3993` n `90` status `ready` deltaP `23.2642` edge `0.1728` maxDD `-3.5466`
- `news_risk_high->metal_4h` score `1.1698` n `52` status `ready` deltaP `18.1871` edge `0.0703` maxDD `-0.993`
- `market_context_high->fx_4h` score `0.7638` n `90` status `ready` deltaP `18.3198` edge `0.0162` maxDD `-0.3077`
- `market_context_high->crypto_alt_24h` score `0.6239` n `90` status `ready` deltaP `9.2689` edge `0.612` maxDD `-34.5048`
- `market_context_high->fx_1h` score `0.5609` n `90` status `ready` deltaP `10.1497` edge `0.0033` maxDD `-0.271`
- `news_risk_high->equity_1h` score `0.3357` n `52` status `ready` deltaP `4.5256` edge `0.0568` maxDD `-0.7197`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
