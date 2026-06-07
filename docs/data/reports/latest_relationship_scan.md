# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T10:07:22.809773+00:00`
- Price records: `672`
- Market context records: `3167`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `8854`

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

- `market_context_high->commodity_24h` score `13.8055` n `101` status `ready` deltaP `47.2171` edge `0.8785` maxDD `-2.0927`
- `market_context_high->crypto_alt_24h` score `11.8811` n `101` status `ready` deltaP `15.4531` edge `2.4178` maxDD `-71.142`
- `market_context_high->unknown_24h` score `11.7612` n `101` status `ready` deltaP `20.2643` edge `0.8938` maxDD `-1.9039`
- `market_context_high->index_24h` score `6.1976` n `101` status `ready` deltaP `29.2216` edge `0.8552` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.6896` n `101` status `ready` deltaP `14.0179` edge `1.3494` maxDD `-53.663`
- `market_context_high->commodity_4h` score `3.0202` n `134` status `ready` deltaP `18.8979` edge `0.1715` maxDD `-1.9973`
- `market_context_high->fx_24h` score `0.7964` n `101` status `ready` deltaP `12.8747` edge `0.0033` maxDD `-0.4876`
- `market_context_high->commodity_1h` score `0.2255` n `134` status `ready` deltaP `4.4776` edge `0.0312` maxDD `-1.7142`
- `market_context_high->unknown_4h` score `-0.237` n `134` status `ready` deltaP `11.0506` edge `0.1288` maxDD `-14.7778`
- `market_context_high->crypto_alt_1h` score `-0.3716` n `134` status `ready` deltaP `6.2718` edge `0.1235` maxDD `-14.7034`
- `market_context_high->index_1h` score `-0.3927` n `134` status `ready` deltaP `5.6752` edge `0.0181` maxDD `-4.5023`
- `market_context_high->index_4h` score `-0.9609` n `134` status `ready` deltaP `15.1665` edge `0.0666` maxDD `-17.6057`
- `market_context_high->crypto_major_1h` score `-1.0295` n `134` status `ready` deltaP `3.1504` edge `0.0733` maxDD `-15.1032`
- `market_context_high->fx_1h` score `-1.0693` n `134` status `ready` deltaP `-9.5451` edge `-0.0052` maxDD `-0.7941`
- `market_context_high->equity_1h` score `-1.3392` n `134` status `ready` deltaP `3.7313` edge `0.0121` maxDD `-8.8863`
- `market_context_high->fx_4h` score `-1.356` n `134` status `ready` deltaP `-11.7401` edge `-0.0071` maxDD `-1.4115`
- `market_context_high->metal_1h` score `-2.0644` n `134` status `ready` deltaP `-3.5794` edge `-0.0088` maxDD `-7.4828`
- `market_context_high->crypto_alt_4h` score `-2.1239` n `134` status `ready` deltaP `18.1175` edge `0.4114` maxDD `-58.6918`
- `market_context_high->unknown_1h` score `-2.8731` n `134` status `ready` deltaP `2.9717` edge `-0.0566` maxDD `-14.2111`
- `market_context_high->crypto_major_4h` score `-3.5805` n `134` status `ready` deltaP `11.3602` edge `0.2576` maxDD `-54.3896`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
