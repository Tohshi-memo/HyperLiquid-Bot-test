# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T09:37:28.533119+00:00`
- Price records: `672`
- Market context records: `6906`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11684`

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

- `market_context_high->unknown_24h` score `0.2131` n `190` status `ready` deltaP `-4.7724` edge `0.4571` maxDD `-14.1708`
- `market_context_high->fx_1h` score `-0.1864` n `224` status `ready` deltaP `3.2854` edge `0.0027` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.3599` n `224` status `ready` deltaP `3.2587` edge `0.0247` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.4375` n `224` status `ready` deltaP `4.745` edge `0.0223` maxDD `-4.2314`
- `market_context_high->commodity_1h` score `-0.598` n `224` status `ready` deltaP `-0.5988` edge `-0.0042` maxDD `-2.1443`
- `market_context_high->fx_4h` score `-0.7489` n `224` status `ready` deltaP `15.0697` edge `0.0099` maxDD `-2.1765`
- `market_context_high->index_1h` score `-0.7752` n `224` status `ready` deltaP `-0.8795` edge `-0.0024` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.8394` n `224` status `ready` deltaP `-3.8441` edge `-0.0052` maxDD `-2.1427`
- `market_context_high->commodity_4h` score `-1.3175` n `224` status `ready` deltaP `-1.5789` edge `-0.0094` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.5654` n `224` status `ready` deltaP `-2.9619` edge `-0.0206` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.7536` n `224` status `ready` deltaP `2.0851` edge `-0.0207` maxDD `-13.1084`
- `market_context_high->index_4h` score `-1.9053` n `224` status `ready` deltaP `5.1612` edge `-0.0207` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-2.1654` n `224` status `ready` deltaP `2.7766` edge `0.0022` maxDD `-5.5324`
- `market_context_high->commodity_24h` score `-2.3301` n `190` status `ready` deltaP `-0.1131` edge `-0.0066` maxDD `-5.2791`
- `market_context_high->crypto_alt_4h` score `-2.7387` n `224` status `ready` deltaP `2.2104` edge `-0.0075` maxDD `-20.6678`
- `market_context_high->crypto_major_4h` score `-2.8345` n `224` status `ready` deltaP `-0.0871` edge `-0.0301` maxDD `-16.9508`
- `market_context_high->unknown_4h` score `-3.0047` n `224` status `ready` deltaP `-7.9704` edge `0.0393` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.1613` n `190` status `ready` deltaP `-5.587` edge `-0.0059` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.1365` n `224` status `ready` deltaP `2.5588` edge `-0.1375` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.3558` n `190` status `ready` deltaP `-13.6551` edge `-0.121` maxDD `-28.4043`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
