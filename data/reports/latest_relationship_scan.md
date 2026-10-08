# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T18:22:43.520116+00:00`
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

- `market_context_high->unknown_4h` score `40.231` n `91` status `ready` deltaP `-2.2246` edge `3.4213` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `14.4808` n `49` status `ready` deltaP `44.3598` edge `0.911` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `14.0034` n `49` status `ready` deltaP `45.766` edge `0.8686` maxDD `-0.2073`
- `news_risk_high->equity_24h` score `8.5106` n `49` status `ready` deltaP `23.7258` edge `0.561` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `8.1026` n `90` status `ready` deltaP `20.3524` edge `1.2005` maxDD `-16.7906`
- `news_risk_high->index_24h` score `6.0494` n `49` status `ready` deltaP `43.8475` edge `0.2118` maxDD `0.0`
- `market_context_high->equity_24h` score `5.8422` n `90` status `ready` deltaP `23.0002` edge `0.3764` maxDD `-1.0977`
- `news_risk_high->equity_4h` score `5.6456` n `49` status `ready` deltaP `31.3184` edge `0.2822` maxDD `-0.6421`
- `news_risk_high->index_4h` score `4.4689` n `49` status `ready` deltaP `44.758` edge `0.0785` maxDD `-0.025`
- `news_risk_high->crypto_major_1h` score `3.2512` n `49` status `ready` deltaP `12.9109` edge `0.2204` maxDD `-1.5096`
- `news_risk_high->commodity_24h` score `2.8107` n `49` status `ready` deltaP `32.4869` edge `0.0261` maxDD `-0.0096`
- `news_risk_high->crypto_alt_1h` score `2.8025` n `49` status `ready` deltaP `6.9382` edge `0.219` maxDD `-1.2034`
- `news_risk_high->index_1h` score `2.423` n `49` status `ready` deltaP `29.986` edge `0.016` maxDD `-0.1194`
- `market_context_high->crypto_alt_24h` score `2.1673` n `90` status `ready` deltaP `12.0547` edge `0.7913` maxDD `-34.5048`
- `market_context_high->crypto_major_4h` score `1.9028` n `91` status `ready` deltaP `19.0784` edge `0.2498` maxDD `-6.9761`
- `market_context_high->metal_24h` score `1.4977` n `90` status `ready` deltaP `24.5118` edge `0.1771` maxDD `-3.5466`
- `news_risk_high->metal_4h` score `1.2401` n `49` status `ready` deltaP `19.2104` edge `0.0725` maxDD `-0.993`
- `market_context_high->fx_4h` score `0.5783` n `91` status `ready` deltaP `16.6008` edge `0.0122` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.5015` n `91` status `ready` deltaP `9.5414` edge `0.0024` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.4018` n `91` status `ready` deltaP `11.3411` edge `0.0648` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
