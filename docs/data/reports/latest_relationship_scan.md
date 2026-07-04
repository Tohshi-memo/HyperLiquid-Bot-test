# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T05:37:30.589987+00:00`
- Price records: `672`
- Market context records: `5632`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8743`

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

- `market_context_high->equity_24h` score `2.9443` n `174` status `ready` deltaP `15.0084` edge `0.6532` maxDD `-31.6316`
- `market_context_high->fx_24h` score `1.3616` n `174` status `ready` deltaP `22.1325` edge `0.0633` maxDD `-1.457`
- `market_context_high->crypto_major_4h` score `0.7716` n `237` status `ready` deltaP `10.8521` edge `0.2212` maxDD `-14.0065`
- `market_context_high->equity_4h` score `0.4661` n `237` status `ready` deltaP `7.3814` edge `0.1535` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `-0.203` n `237` status `ready` deltaP `5.4596` edge `0.1316` maxDD `-9.46`
- `market_context_high->fx_1h` score `-0.2883` n `237` status `ready` deltaP `1.4496` edge `0.001` maxDD `-0.4764`
- `market_context_high->equity_1h` score `-0.4337` n `237` status `ready` deltaP `4.7172` edge `0.0331` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.5332` n `237` status `ready` deltaP `-0.1567` edge `0.0002` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.6381` n `237` status `ready` deltaP `1.2867` edge `0.0344` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.6517` n `237` status `ready` deltaP `4.131` edge `0.0427` maxDD `-6.9639`
- `market_context_high->index_1h` score `-0.9669` n `237` status `ready` deltaP `0.1295` edge `0.0054` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-1.0584` n `237` status `ready` deltaP `-0.878` edge `-0.0058` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.3256` n `237` status `ready` deltaP `1.0658` edge `0.0063` maxDD `-1.335`
- `market_context_high->index_4h` score `-1.9454` n `237` status `ready` deltaP `-0.6219` edge `0.0092` maxDD `-3.04`
- `market_context_high->index_24h` score `-2.3574` n `174` status `ready` deltaP `10.0874` edge `0.0292` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.934` n `237` status `ready` deltaP `-12.5399` edge `-0.0542` maxDD `-11.7351`
- `market_context_high->crypto_major_24h` score `-3.7653` n `174` status `ready` deltaP `5.813` edge `0.1015` maxDD `-29.6555`
- `market_context_high->commodity_4h` score `-3.9686` n `237` status `ready` deltaP `-3.8643` edge `-0.0374` maxDD `-14.071`
- `market_context_high->metal_24h` score `-8.2607` n `174` status `ready` deltaP `-10.9315` edge `-0.2501` maxDD `-32.8874`
- `market_context_high->crypto_alt_24h` score `-13.2642` n `174` status `ready` deltaP `-4.4001` edge `-0.2063` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
