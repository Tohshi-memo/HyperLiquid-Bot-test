# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T19:37:27.148856+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5072`

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

- `market_context_high->unknown_1h` score `97.0364` n `97` status `ready` deltaP `-0.1605` edge `8.1289` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `78.6134` n `97` status `ready` deltaP `2.7564` edge `6.5639` maxDD `-0.4928`
- `news_risk_high->crypto_major_4h` score `10.4333` n `65` status `ready` deltaP `36.8199` edge `0.6443` maxDD `-0.6258`
- `market_context_high->crypto_major_24h` score `8.9351` n `46` status `ready` deltaP `29.929` edge `0.6103` maxDD `-4.5519`
- `market_context_high->crypto_alt_24h` score `8.5669` n `46` status `ready` deltaP `23.4904` edge `0.6846` maxDD `-8.1838`
- `news_risk_high->crypto_alt_4h` score `7.4025` n `65` status `ready` deltaP `24.2073` edge `0.5899` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `6.893` n `65` status `ready` deltaP `20.9295` edge `0.4449` maxDD `-0.1344`
- `market_context_high->crypto_major_4h` score `4.7668` n `97` status `ready` deltaP `20.8009` edge `0.3289` maxDD `-3.294`
- `news_risk_high->index_24h` score `3.8189` n `65` status `ready` deltaP `26.7361` edge `0.14` maxDD `0.0`
- `news_risk_high->equity_4h` score `3.7678` n `65` status `ready` deltaP `25.4549` edge `0.2053` maxDD `-2.881`
- `news_risk_high->index_4h` score `3.2635` n `65` status `ready` deltaP `35.7247` edge `0.06` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.8453` n `65` status `ready` deltaP `11.9622` edge `0.1929` maxDD `-1.5096`
- `news_risk_high->metal_4h` score `2.6344` n `65` status `ready` deltaP `23.0418` edge `0.1075` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.2076` n `65` status `ready` deltaP `27.1142` edge `0.0182` maxDD `-0.1997`
- `market_context_high->crypto_major_1h` score `2.1069` n `97` status `ready` deltaP `14.8806` edge `0.1214` maxDD `-2.2692`
- `news_risk_high->crypto_alt_1h` score `1.6289` n `65` status `ready` deltaP `5.7669` edge `0.1492` maxDD `-2.4854`
- `market_context_high->crypto_alt_4h` score `1.5157` n `97` status `ready` deltaP `6.063` edge `0.2648` maxDD `-7.6465`
- `market_context_high->fx_4h` score `1.3813` n `97` status `ready` deltaP `24.8209` edge `0.0253` maxDD `-0.3868`
- `market_context_high->fx_24h` score `1.3654` n `46` status `ready` deltaP `25.536` edge `0.1066` maxDD `-1.8102`
- `market_context_high->fx_1h` score `0.9504` n `97` status `ready` deltaP `14.8666` edge `0.0065` maxDD `-0.113`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
