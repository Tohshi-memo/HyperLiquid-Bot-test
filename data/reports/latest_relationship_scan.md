# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T13:07:29.077762+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8747`

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

- `market_context_high->unknown_4h` score `40.7637` n `90` status `ready` deltaP `-2.6456` edge `3.4685` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `13.245` n `49` status `ready` deltaP `42.6829` edge `0.8192` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `12.9678` n `49` status `ready` deltaP `43.9367` edge `0.7945` maxDD `-0.2073`
- `news_risk_high->equity_24h` score `6.6973` n `49` status `ready` deltaP `20.3341` edge `0.4325` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `6.3898` n `90` status `ready` deltaP `16.8739` edge `1.0041` maxDD `-16.7906`
- `news_risk_high->index_24h` score `5.5072` n `49` status `ready` deltaP `40.4145` edge `0.1895` maxDD `0.0`
- `news_risk_high->equity_4h` score `5.0856` n `49` status `ready` deltaP `29.794` edge `0.2457` maxDD `-0.6421`
- `news_risk_high->index_4h` score `4.4083` n `49` status `ready` deltaP `44.3007` edge `0.0765` maxDD `-0.025`
- `market_context_high->equity_24h` score `4.0288` n `90` status `ready` deltaP `19.6085` edge `0.2479` maxDD `-1.0977`
- `news_risk_high->commodity_24h` score `3.6584` n `49` status `ready` deltaP `35.9875` edge `0.0734` maxDD `-0.0096`
- `news_risk_high->crypto_major_1h` score `2.9706` n `49` status `ready` deltaP `12.1624` edge `0.202` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.8404` n `90` status `ready` deltaP `18.0183` edge `0.213` maxDD `-4.047`
- `news_risk_high->crypto_alt_1h` score `2.5145` n `49` status `ready` deltaP `6.9382` edge `0.195` maxDD `-1.2034`
- `news_risk_high->index_1h` score `2.4433` n `49` status `ready` deltaP `30.2854` edge `0.0157` maxDD `-0.1194`
- `market_context_high->metal_24h` score `1.4106` n `90` status `ready` deltaP `23.4369` edge `0.1731` maxDD `-3.5466`
- `news_risk_high->metal_4h` score `1.1935` n `49` status `ready` deltaP `18.4482` edge `0.0716` maxDD `-0.993`
- `market_context_high->crypto_alt_24h` score `0.7623` n `90` status `ready` deltaP `9.787` edge `0.6263` maxDD `-34.5048`
- `market_context_high->fx_4h` score `0.709` n `90` status `ready` deltaP `17.71` edge `0.0157` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.5853` n `91` status `ready` deltaP `10.4396` edge `0.0034` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.2194` n `91` status `ready` deltaP `10.5926` edge `0.0464` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
