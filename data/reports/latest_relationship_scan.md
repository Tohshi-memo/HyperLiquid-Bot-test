# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T19:52:28.800622+00:00`
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

- `market_context_high->unknown_1h` score `97.1912` n `97` status `ready` deltaP `-0.1605` edge `8.1418` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `78.6434` n `97` status `ready` deltaP `2.7564` edge `6.5664` maxDD `-0.4928`
- `news_risk_high->crypto_major_4h` score `10.4067` n `65` status `ready` deltaP `36.6675` edge `0.6431` maxDD `-0.6258`
- `market_context_high->crypto_major_24h` score `8.8468` n `46` status `ready` deltaP `29.7554` edge `0.6041` maxDD `-4.5519`
- `market_context_high->crypto_alt_24h` score `8.439` n `46` status `ready` deltaP `23.3167` edge `0.6751` maxDD `-8.1838`
- `news_risk_high->crypto_alt_4h` score `7.3771` n `65` status `ready` deltaP `24.0549` edge `0.5888` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `6.8083` n `65` status `ready` deltaP `20.7559` edge `0.439` maxDD `-0.1344`
- `market_context_high->crypto_major_4h` score `4.7402` n `97` status `ready` deltaP `20.6485` edge `0.3277` maxDD `-3.294`
- `news_risk_high->index_24h` score `3.8129` n `65` status `ready` deltaP `26.7361` edge `0.1395` maxDD `0.0`
- `news_risk_high->equity_4h` score `3.7485` n `65` status `ready` deltaP `25.3025` edge `0.2047` maxDD `-2.881`
- `news_risk_high->index_4h` score `3.2501` n `65` status `ready` deltaP `35.5723` edge `0.0599` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.8298` n `65` status `ready` deltaP `11.8125` edge `0.1926` maxDD `-1.5096`
- `news_risk_high->metal_4h` score `2.6186` n `65` status `ready` deltaP `22.8893` edge `0.1072` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.2196` n `65` status `ready` deltaP `27.2639` edge `0.0182` maxDD `-0.1997`
- `market_context_high->crypto_major_1h` score `2.0913` n `97` status `ready` deltaP `14.7309` edge `0.1211` maxDD `-2.2692`
- `news_risk_high->crypto_alt_1h` score `1.611` n `65` status `ready` deltaP `5.6172` edge `0.1487` maxDD `-2.4854`
- `market_context_high->crypto_alt_4h` score `1.4903` n `97` status `ready` deltaP `5.9106` edge `0.2637` maxDD `-7.6465`
- `market_context_high->fx_4h` score `1.3813` n `97` status `ready` deltaP `24.8209` edge `0.0253` maxDD `-0.3868`
- `market_context_high->fx_24h` score `1.3654` n `46` status `ready` deltaP `25.536` edge `0.1066` maxDD `-1.8102`
- `market_context_high->fx_1h` score `0.9504` n `97` status `ready` deltaP `14.8666` edge `0.0065` maxDD `-0.113`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
