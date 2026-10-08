# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T07:07:29.115083+00:00`
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

- `market_context_high->unknown_4h` score `39.0643` n `90` status `ready` deltaP `-2.7981` edge `3.3279` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `11.215` n `62` status `ready` deltaP `39.4965` edge `0.6916` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.3196` n `62` status `ready` deltaP `23.6969` edge `0.5864` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `7.1338` n `62` status `ready` deltaP `18.2462` edge `0.4828` maxDD `-0.1298`
- `news_risk_high->index_24h` score `5.1505` n `62` status `ready` deltaP `37.6511` edge `0.1782` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `4.991` n `90` status `ready` deltaP `12.7288` edge `0.8524` maxDD `-16.7906`
- `news_risk_high->index_4h` score `3.1497` n `62` status `ready` deltaP `34.1365` edge `0.0611` maxDD `-0.4296`
- `market_context_high->crypto_major_4h` score `2.7102` n `90` status `ready` deltaP `17.561` edge `0.2052` maxDD `-4.047`
- `market_context_high->equity_24h` score `2.6293` n `90` status `ready` deltaP `15.8089` edge `0.1566` maxDD `-1.0977`
- `news_risk_high->equity_4h` score `2.6277` n `62` status `ready` deltaP `19.3008` edge `0.1501` maxDD `-2.7837`
- `news_risk_high->crypto_major_1h` score `2.6002` n `62` status `ready` deltaP `10.7736` edge `0.1804` maxDD `-1.5096`
- `news_risk_high->index_1h` score `2.1026` n `62` status `ready` deltaP `26.0721` edge `0.0164` maxDD `-0.1997`
- `news_risk_high->unknown_4h` score `1.8439` n `62` status `ready` deltaP `-5.7731` edge `0.3167` maxDD `-5.6309`
- `news_risk_high->metal_4h` score `1.4536` n `62` status `ready` deltaP `21.0956` edge `0.0873` maxDD `-0.993`
- `news_risk_high->crypto_alt_1h` score `1.2785` n `62` status `ready` deltaP `3.9067` edge `0.1324` maxDD `-2.4854`
- `market_context_high->metal_24h` score `1.2549` n `90` status `ready` deltaP `21.5371` edge `0.1658` maxDD `-3.5466`
- `market_context_high->fx_4h` score `1.0061` n `90` status `ready` deltaP `21.0637` edge `0.0181` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.6508` n `90` status `ready` deltaP `11.1976` edge `0.0038` maxDD `-0.271`
- `market_context_high->crypto_alt_24h` score `0.3094` n `90` status `ready` deltaP `7.8872` edge `0.5809` maxDD `-34.5048`
- `market_context_high->crypto_major_1h` score `0.2251` n `90` status `ready` deltaP `10.7019` edge `0.0464` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
