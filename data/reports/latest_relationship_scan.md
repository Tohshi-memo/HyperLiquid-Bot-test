# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T12:22:29.680554+00:00`
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

- `market_context_high->unknown_4h` score `40.6615` n `90` status `ready` deltaP `-2.7981` edge `3.461` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `12.6045` n `51` status `ready` deltaP `43.6394` edge `0.7662` maxDD `-0.2073`
- `news_risk_high->crypto_alt_4h` score `12.1163` n `51` status `ready` deltaP `38.7613` edge `0.7704` maxDD `-0.8628`
- `news_risk_high->equity_24h` score `6.8746` n `51` status `ready` deltaP `20.1362` edge `0.4486` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `6.1773` n `90` status `ready` deltaP `16.3558` edge `0.9803` maxDD `-16.7906`
- `news_risk_high->index_24h` score `5.4465` n `51` status `ready` deltaP `39.8964` edge `0.1879` maxDD `0.0`
- `news_risk_high->equity_4h` score `4.1916` n `51` status `ready` deltaP `26.1926` edge `0.2071` maxDD `-1.5936`
- `news_risk_high->index_4h` score `3.9007` n `51` status `ready` deltaP `40.6115` edge `0.0671` maxDD `-0.3561`
- `market_context_high->equity_24h` score `3.8446` n `90` status `ready` deltaP `19.0904` edge `0.236` maxDD `-1.0977`
- `news_risk_high->crypto_major_1h` score `3.1347` n `51` status `ready` deltaP `13.0739` edge `0.2096` maxDD `-1.5096`
- `news_risk_high->commodity_24h` score `2.8835` n `51` status `ready` deltaP `32.7441` edge `0.0468` maxDD `-1.3174`
- `market_context_high->crypto_major_4h` score `2.7318` n `90` status `ready` deltaP `17.561` edge `0.207` maxDD `-4.047`
- `news_risk_high->crypto_alt_1h` score `2.6103` n `51` status `ready` deltaP `8.0897` edge `0.1953` maxDD `-1.2034`
- `news_risk_high->index_1h` score `2.3681` n `51` status `ready` deltaP `29.1946` edge `0.0167` maxDD `-0.1194`
- `market_context_high->metal_24h` score `1.4114` n `90` status `ready` deltaP `23.4369` edge `0.1732` maxDD `-3.5466`
- `news_risk_high->metal_4h` score `1.1326` n `51` status `ready` deltaP `17.6231` edge `0.0693` maxDD `-0.993`
- `market_context_high->fx_4h` score `0.7504` n `90` status `ready` deltaP `18.1673` edge `0.0161` maxDD `-0.3077`
- `market_context_high->crypto_alt_24h` score `0.6449` n `90` status `ready` deltaP `9.2689` edge `0.6147` maxDD `-34.5048`
- `market_context_high->fx_1h` score `0.549` n `90` status `ready` deltaP `10.0` edge `0.0033` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.236` n `90` status `ready` deltaP `10.8516` edge `0.0468` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
