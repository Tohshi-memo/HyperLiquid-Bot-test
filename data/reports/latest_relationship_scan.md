# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T22:32:43.796884+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5036`

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

- `market_context_high->unknown_1h` score `97.3112` n `97` status `ready` deltaP `-0.1605` edge `8.1518` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `78.7274` n `97` status `ready` deltaP `2.7564` edge `6.5734` maxDD `-0.4928`
- `news_risk_high->crypto_major_4h` score `10.088` n `65` status `ready` deltaP `35.1431` edge `0.6267` maxDD `-0.6258`
- `market_context_high->crypto_major_24h` score `7.8865` n `46` status `ready` deltaP `27.8457` edge `0.5368` maxDD `-4.5519`
- `market_context_high->crypto_alt_24h` score `7.1882` n `46` status `ready` deltaP `21.407` edge `0.5836` maxDD `-8.1838`
- `news_risk_high->crypto_alt_4h` score `7.1873` n `65` status `ready` deltaP `22.9878` edge `0.5801` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `5.8527` n `65` status `ready` deltaP `18.8462` edge `0.3721` maxDD `-0.1344`
- `market_context_high->crypto_major_4h` score `4.4214` n `97` status `ready` deltaP `19.1241` edge `0.3113` maxDD `-3.294`
- `news_risk_high->index_24h` score `3.7179` n `65` status `ready` deltaP `26.3889` edge `0.1339` maxDD `0.0`
- `news_risk_high->equity_4h` score `3.4415` n `65` status `ready` deltaP `23.6257` edge `0.1903` maxDD `-2.881`
- `news_risk_high->index_4h` score `3.1236` n `65` status `ready` deltaP `34.2003` edge `0.0585` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.6607` n `65` status `ready` deltaP `10.9143` edge `0.1845` maxDD `-1.5096`
- `news_risk_high->metal_4h` score `2.4102` n `65` status `ready` deltaP `21.3649` edge `0.1` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.1393` n `65` status `ready` deltaP `26.3657` edge `0.0175` maxDD `-0.1997`
- `market_context_high->crypto_major_1h` score `1.9222` n `97` status `ready` deltaP `13.8327` edge `0.113` maxDD `-2.2692`
- `news_risk_high->crypto_alt_1h` score `1.5354` n `65` status `ready` deltaP `5.3178` edge `0.1444` maxDD `-2.4854`
- `market_context_high->fx_4h` score `1.4334` n `97` status `ready` deltaP `25.2782` edge `0.0266` maxDD `-0.3868`
- `market_context_high->fx_24h` score `1.3724` n `46` status `ready` deltaP `25.536` edge `0.1075` maxDD `-1.8102`
- `market_context_high->crypto_alt_4h` score `1.3005` n `97` status `ready` deltaP `4.8435` edge `0.255` maxDD `-7.6465`
- `market_context_high->fx_1h` score `0.9252` n `97` status `ready` deltaP `14.5672` edge `0.0064` maxDD `-0.113`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
