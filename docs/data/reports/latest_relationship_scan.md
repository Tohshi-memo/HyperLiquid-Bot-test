# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T07:22:26.639032+00:00`
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

- `market_context_high->unknown_4h` score `39.1351` n `90` status `ready` deltaP `-2.7981` edge `3.3338` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `11.1994` n `62` status `ready` deltaP `39.4965` edge `0.6903` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.2846` n `62` status `ready` deltaP `23.5445` edge `0.5845` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `7.1956` n `62` status `ready` deltaP `18.4189` edge `0.4868` maxDD `-0.1298`
- `news_risk_high->index_24h` score `5.1715` n `62` status `ready` deltaP `37.8238` edge `0.1788` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `5.0476` n `90` status `ready` deltaP `12.9015` edge `0.8585` maxDD `-16.7906`
- `news_risk_high->index_4h` score `3.1485` n `62` status `ready` deltaP `34.1365` edge `0.061` maxDD `-0.4296`
- `market_context_high->crypto_major_4h` score `2.6946` n `90` status `ready` deltaP `17.561` edge `0.2039` maxDD `-4.047`
- `market_context_high->equity_24h` score `2.6911` n `90` status `ready` deltaP `15.9816` edge `0.1606` maxDD `-1.0977`
- `news_risk_high->equity_4h` score `2.6325` n `62` status `ready` deltaP `19.3008` edge `0.1505` maxDD `-2.7837`
- `news_risk_high->crypto_major_1h` score `2.5906` n `62` status `ready` deltaP `10.7736` edge `0.1796` maxDD `-1.5096`
- `news_risk_high->index_1h` score `2.117` n `62` status `ready` deltaP `26.2218` edge `0.0166` maxDD `-0.1997`
- `news_risk_high->unknown_4h` score `1.9147` n `62` status `ready` deltaP `-5.7731` edge `0.3226` maxDD `-5.6309`
- `news_risk_high->metal_4h` score `1.4513` n `62` status `ready` deltaP `21.0956` edge `0.087` maxDD `-0.993`
- `market_context_high->metal_24h` score `1.2572` n `90` status `ready` deltaP `21.5371` edge `0.1661` maxDD `-3.5466`
- `news_risk_high->crypto_alt_1h` score `1.251` n `62` status `ready` deltaP `3.757` edge `0.1311` maxDD `-2.4854`
- `market_context_high->fx_4h` score `1.0049` n `90` status `ready` deltaP `21.0637` edge `0.018` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.6508` n `90` status `ready` deltaP `11.1976` edge `0.0038` maxDD `-0.271`
- `market_context_high->crypto_alt_24h` score `0.3356` n `90` status `ready` deltaP `8.0599` edge `0.5831` maxDD `-34.5048`
- `market_context_high->crypto_major_1h` score `0.2188` n `90` status `ready` deltaP `10.7019` edge `0.0456` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
