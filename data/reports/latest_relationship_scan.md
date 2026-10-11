# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T20:07:29.154948+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `8174`

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

- `market_context_high->unknown_24h` score `1380.8206` n `40` status `ready` deltaP `-22.2222` edge `115.2529` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `53.4106` n `89` status `ready` deltaP `-4.3145` edge `4.5377` maxDD `-2.3109`
- `market_context_high->equity_24h` score `8.7876` n `40` status `ready` deltaP `27.6736` edge `0.5907` maxDD `-1.0977`
- `market_context_high->unknown_1h` score `6.7957` n `101` status `ready` deltaP `-2.4708` edge `0.6164` maxDD `-1.0231`
- `market_context_high->index_24h` score `6.3964` n `40` status `ready` deltaP `52.4306` edge `0.1835` maxDD `0.0`
- `market_context_high->fx_24h` score `3.1515` n `40` status `ready` deltaP `35.7292` edge `0.0374` maxDD `-0.0374`
- `market_context_high->crypto_major_24h` score `1.4344` n `40` status `ready` deltaP `-21.1111` edge `0.5751` maxDD `-17.8526`
- `market_context_high->fx_4h` score `0.8095` n `89` status `ready` deltaP `13.2039` edge `0.0078` maxDD `-0.2692`
- `market_context_high->commodity_4h` score `0.4922` n `89` status `ready` deltaP `11.8885` edge `0.0151` maxDD `-1.6002`
- `market_context_high->crypto_alt_1h` score `0.4711` n `101` status `ready` deltaP `6.446` edge `0.0997` maxDD `-4.9401`
- `market_context_high->crypto_major_4h` score `0.3281` n `89` status `ready` deltaP `2.9443` edge `0.233` maxDD `-11.1784`
- `market_context_high->commodity_1h` score `0.2028` n `101` status `ready` deltaP `5.905` edge `0.0059` maxDD `-0.6025`
- `market_context_high->crypto_alt_4h` score `0.0828` n `89` status `ready` deltaP `-0.1267` edge `0.2673` maxDD `-13.8008`
- `market_context_high->metal_4h` score `0.0799` n `89` status `ready` deltaP `8.5401` edge `0.022` maxDD `-1.1153`
- `market_context_high->fx_1h` score `-0.0449` n `101` status `ready` deltaP `2.8769` edge `0.0013` maxDD `-0.271`
- `market_context_high->metal_1h` score `-0.1818` n `101` status `ready` deltaP `6.0206` edge `0.0036` maxDD `-0.7107`
- `market_context_high->crypto_major_1h` score `-0.1995` n `101` status `ready` deltaP `0.8863` edge `0.0574` maxDD `-3.7778`
- `market_context_high->index_4h` score `-0.5009` n `89` status `ready` deltaP `-0.0873` edge `0.0064` maxDD `-0.9364`
- `market_context_high->index_1h` score `-0.7039` n `101` status `ready` deltaP `-3.5809` edge `-0.0013` maxDD `-0.5392`
- `market_context_high->equity_1h` score `-0.967` n `101` status `ready` deltaP `-5.9421` edge `0.0026` maxDD `-2.2898`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
