# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T11:52:30.604072+00:00`
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

- `market_context_high->unknown_4h` score `40.6867` n `90` status `ready` deltaP `-2.7981` edge `3.4631` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `12.1112` n `53` status `ready` deltaP `41.7481` edge `0.7377` maxDD `-0.2073`
- `news_risk_high->crypto_alt_4h` score `10.9251` n `53` status `ready` deltaP `35.1357` edge `0.7196` maxDD `-2.1398`
- `news_risk_high->equity_24h` score `7.0879` n `53` status `ready` deltaP `20.0867` edge `0.4667` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `6.0462` n `90` status `ready` deltaP `16.0103` edge `0.9658` maxDD `-16.7906`
- `news_risk_high->index_24h` score `5.4129` n `53` status `ready` deltaP `39.5509` edge `0.1874` maxDD `0.0`
- `market_context_high->equity_24h` score `3.7161` n `90` status `ready` deltaP `18.745` edge `0.2276` maxDD `-1.0977`
- `news_risk_high->equity_4h` score `3.4904` n `53` status `ready` deltaP `22.863` edge `0.1849` maxDD `-2.3829`
- `news_risk_high->index_4h` score `3.4612` n `53` status `ready` deltaP `37.0599` edge `0.0633` maxDD `-0.421`
- `news_risk_high->crypto_major_1h` score `3.0064` n `53` status `ready` deltaP `12.2952` edge `0.2041` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.6788` n `90` status `ready` deltaP `17.4085` edge `0.2036` maxDD `-4.047`
- `news_risk_high->index_1h` score `2.4453` n `53` status `ready` deltaP `29.9345` edge `0.0182` maxDD `-0.1194`
- `news_risk_high->crypto_alt_1h` score `2.194` n `53` status `ready` deltaP `5.796` edge `0.1759` maxDD `-1.2034`
- `market_context_high->metal_24h` score `1.3856` n `90` status `ready` deltaP `23.0915` edge `0.1722` maxDD `-3.5466`
- `news_risk_high->commodity_24h` score `1.3062` n `53` status `ready` deltaP `29.6118` edge `0.02` maxDD `-2.6627`
- `news_risk_high->metal_4h` score `1.1985` n `53` status `ready` deltaP `18.7241` edge `0.0704` maxDD `-0.993`
- `market_context_high->fx_4h` score `0.7772` n `90` status `ready` deltaP `18.4722` edge `0.0163` maxDD `-0.3077`
- `market_context_high->crypto_alt_24h` score `0.6059` n `90` status `ready` deltaP `9.2689` edge `0.6097` maxDD `-34.5048`
- `market_context_high->fx_1h` score `0.5741` n `90` status `ready` deltaP `10.2994` edge `0.0034` maxDD `-0.271`
- `news_risk_high->equity_1h` score `0.3943` n `53` status `ready` deltaP `5.2876` edge `0.0566` maxDD `-0.7197`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
