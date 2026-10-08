# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T14:37:37.372025+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8739`

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

- `market_context_high->unknown_4h` score `40.6293` n `90` status `ready` deltaP `-2.6456` edge `3.4573` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `13.2402` n `49` status `ready` deltaP `42.6829` edge `0.8188` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `13.0266` n `49` status `ready` deltaP `43.9367` edge `0.7994` maxDD `-0.2073`
- `news_risk_high->equity_24h` score `7.0226` n `49` status `ready` deltaP `21.3704` edge `0.4527` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `6.7471` n `90` status `ready` deltaP `17.9102` edge `1.043` maxDD `-16.7906`
- `news_risk_high->index_24h` score `5.6213` n `49` status `ready` deltaP `41.4508` edge `0.1921` maxDD `0.0`
- `news_risk_high->equity_4h` score `5.0242` n `49` status `ready` deltaP `29.6416` edge `0.2416` maxDD `-0.6421`
- `market_context_high->equity_24h` score `4.3541` n `90` status `ready` deltaP `20.6448` edge `0.2681` maxDD `-1.0977`
- `news_risk_high->index_4h` score `4.3173` n `49` status `ready` deltaP `43.5385` edge `0.074` maxDD `-0.025`
- `news_risk_high->commodity_24h` score `3.4219` n `49` status `ready` deltaP `34.9512` edge `0.0606` maxDD `-0.0096`
- `news_risk_high->crypto_major_1h` score `2.955` n `49` status `ready` deltaP `12.1624` edge `0.2007` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.8992` n `90` status `ready` deltaP `18.0183` edge `0.2179` maxDD `-4.047`
- `news_risk_high->crypto_alt_1h` score `2.451` n `49` status `ready` deltaP `6.7885` edge `0.1907` maxDD `-1.2034`
- `news_risk_high->index_1h` score `2.4038` n `49` status `ready` deltaP `29.8363` edge `0.0154` maxDD `-0.1194`
- `market_context_high->metal_24h` score `1.3887` n `90` status `ready` deltaP `23.0915` edge `0.1726` maxDD `-3.5466`
- `news_risk_high->metal_4h` score `1.1785` n `49` status `ready` deltaP `18.2958` edge `0.0707` maxDD `-0.993`
- `market_context_high->crypto_alt_24h` score `0.8505` n `90` status `ready` deltaP `9.787` edge `0.6376` maxDD `-34.5048`
- `market_context_high->fx_4h` score `0.6301` n `90` status `ready` deltaP `16.9478` edge `0.0142` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.5458` n `91` status `ready` deltaP `9.9905` edge `0.0031` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.2093` n `91` status `ready` deltaP `10.5926` edge `0.0451` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
