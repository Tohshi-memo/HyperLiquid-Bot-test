# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T12:07:28.033914+00:00`
- Price records: `672`
- Market context records: `8300`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5892`

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

- `news_risk_high->unknown_24h` score `5951.6762` n `54` status `ready` deltaP `35.4745` edge `495.7786` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.8203` n `54` status `ready` deltaP `25.1637` edge `0.4603` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.8903` n `54` status `ready` deltaP `20.9304` edge `0.1322` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.5514` n `54` status `ready` deltaP `21.5052` edge `0.0883` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.0171` n `54` status `ready` deltaP `9.7166` edge `0.2632` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.8915` n `54` status `ready` deltaP `14.8536` edge `0.102` maxDD `-1.1388`
- `news_risk_high->crypto_alt_4h` score `1.6035` n `54` status `ready` deltaP `17.9935` edge `0.2248` maxDD `-5.8012`
- `news_risk_high->crypto_major_1h` score `1.5622` n `54` status `ready` deltaP `10.6066` edge `0.0992` maxDD `-1.1783`
- `news_risk_high->metal_4h` score `1.174` n `54` status `ready` deltaP `10.6538` edge `0.0736` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.3405` n `54` status `ready` deltaP `5.7053` edge `0.0192` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1518` n `54` status `ready` deltaP `6.6977` edge `0.0029` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.0521` n `54` status `ready` deltaP `3.554` edge `0.0123` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.5055` n `54` status `ready` deltaP `3.698` edge `0.0063` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.1276` n `54` status `ready` deltaP `-8.6605` edge `-0.041` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.044` n `54` status `ready` deltaP `-20.544` edge `-0.049` maxDD `-5.4165`
- `news_risk_high->metal_24h` score `-5.8513` n `54` status `ready` deltaP `-22.1644` edge `-0.0628` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-8.81` n `54` status `ready` deltaP `-30.9621` edge `-0.197` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-10.8398` n `54` status `ready` deltaP `-5.9606` edge `-0.2696` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-11.915` n `54` status `ready` deltaP `-23.0324` edge `-0.2891` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-32.2167` n `54` status `ready` deltaP `-12.9051` edge `-1.1462` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
