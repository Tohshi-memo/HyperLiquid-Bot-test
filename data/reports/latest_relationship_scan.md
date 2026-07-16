# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T16:22:26.655396+00:00`
- Price records: `672`
- Market context records: `6935`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11706`

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

- `market_context_high->fx_1h` score `-0.2389` n `232` status `ready` deltaP `2.3952` edge `0.0019` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.4197` n `232` status `ready` deltaP `3.0224` edge `0.0213` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.6414` n `232` status `ready` deltaP `3.4715` edge `0.0175` maxDD `-4.5273`
- `market_context_high->metal_1h` score `-0.7005` n `232` status `ready` deltaP `-1.9384` edge `-0.0001` maxDD `-2.1427`
- `market_context_high->index_1h` score `-0.7102` n `232` status `ready` deltaP `-0.0052` edge `0.0001` maxDD `-2.2895`
- `market_context_high->fx_4h` score `-0.821` n `224` status `ready` deltaP `13.6978` edge `0.0098` maxDD `-2.1765`
- `market_context_high->unknown_24h` score `-0.9725` n `215` status `ready` deltaP `-7.2782` edge `0.3428` maxDD `-15.8495`
- `market_context_high->commodity_1h` score `-1.1409` n `232` status `ready` deltaP `-1.91` edge `-0.0135` maxDD `-2.1742`
- `market_context_high->unknown_1h` score `-1.5829` n `232` status `ready` deltaP `-2.1603` edge `-0.0274` maxDD `-3.2083`
- `market_context_high->commodity_4h` score `-1.5971` n `224` status `ready` deltaP `-3.8655` edge `-0.03` maxDD `-5.5853`
- `market_context_high->index_4h` score `-1.645` n `224` status `ready` deltaP `8.6673` edge `-0.0107` maxDD `-11.3047`
- `market_context_high->equity_1h` score `-1.7742` n `232` status `ready` deltaP `2.8443` edge `-0.0158` maxDD `-14.1162`
- `market_context_high->metal_4h` score `-1.9222` n `224` status `ready` deltaP `5.368` edge `0.0161` maxDD `-5.5324`
- `market_context_high->crypto_alt_4h` score `-2.7735` n `224` status `ready` deltaP `1.6006` edge `-0.0079` maxDD `-20.6678`
- `market_context_high->crypto_major_4h` score `-2.7785` n `224` status `ready` deltaP `-0.2396` edge `-0.0219` maxDD `-16.9508`
- `market_context_high->unknown_4h` score `-2.9827` n `224` status `ready` deltaP `-7.6655` edge `0.0391` maxDD `-10.2579`
- `market_context_high->commodity_24h` score `-3.3221` n `215` status `ready` deltaP `-3.8878` edge `-0.0641` maxDD `-5.2791`
- `market_context_high->fx_24h` score `-4.2002` n `215` status `ready` deltaP `-5.5629` edge `-0.0093` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-6.4681` n `224` status `ready` deltaP `6.2173` edge `-0.0762` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.8489` n `215` status `ready` deltaP `-13.095` edge `-0.1183` maxDD `-33.9764`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
