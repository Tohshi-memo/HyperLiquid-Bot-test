# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T15:52:36.192446+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8888`

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

- `market_context_high->unknown_4h` score `40.1542` n `91` status `ready` deltaP `-2.2246` edge `3.4149` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `13.4252` n `49` status `ready` deltaP `42.8354` edge `0.8332` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `13.1974` n `49` status `ready` deltaP `44.2416` edge `0.8116` maxDD `-0.2073`
- `news_risk_high->equity_24h` score `7.3892` n `49` status `ready` deltaP `22.1135` edge `0.4783` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `7.15` n `90` status `ready` deltaP `18.6966` edge `1.0894` maxDD `-16.7906`
- `news_risk_high->index_24h` score `5.7328` n `49` status `ready` deltaP `42.2145` edge `0.1963` maxDD `0.0`
- `news_risk_high->equity_4h` score `5.0664` n `49` status `ready` deltaP `29.794` edge `0.2441` maxDD `-0.6421`
- `market_context_high->equity_24h` score `4.7208` n `90` status `ready` deltaP `21.3879` edge `0.2937` maxDD `-1.0977`
- `news_risk_high->index_4h` score `4.2809` n `49` status `ready` deltaP `43.2336` edge `0.073` maxDD `-0.025`
- `news_risk_high->commodity_24h` score `3.2489` n `49` status `ready` deltaP `34.1537` edge `0.0515` maxDD `-0.0096`
- `news_risk_high->crypto_major_1h` score `3.1121` n `49` status `ready` deltaP `12.4618` edge `0.2118` maxDD `-1.5096`
- `news_risk_high->crypto_alt_1h` score `2.6202` n `49` status `ready` deltaP `6.6388` edge `0.2058` maxDD `-1.2034`
- `news_risk_high->index_1h` score `2.4002` n `49` status `ready` deltaP `29.8363` edge `0.0151` maxDD `-0.1194`
- `market_context_high->metal_24h` score `1.4328` n `90` status `ready` deltaP `23.7139` edge `0.1741` maxDD `-3.5466`
- `market_context_high->crypto_major_4h` score `1.379` n `91` status `ready` deltaP `17.554` edge `0.1928` maxDD `-6.9761`
- `news_risk_high->metal_4h` score `1.1731` n `49` status `ready` deltaP `18.2958` edge `0.07` maxDD `-0.993`
- `market_context_high->crypto_alt_24h` score `1.1655` n `90` status `ready` deltaP `10.3999` edge `0.6739` maxDD `-34.5048`
- `market_context_high->fx_4h` score `0.5903` n `91` status `ready` deltaP `16.6008` edge `0.0132` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.5326` n `91` status `ready` deltaP `9.8408` edge `0.003` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.3114` n `91` status `ready` deltaP `10.892` edge `0.0562` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
