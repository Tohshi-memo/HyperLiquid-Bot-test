# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T04:37:25.478380+00:00`
- Price records: `672`
- Market context records: `5845`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10128`

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

- `news_risk_high->fx_1h` score `1.9639` n `30` status `ready` deltaP `23.7824` edge `0.019` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `0.7981` n `30` status `ready` deltaP `11.0878` edge `0.0751` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.7556` n `259` status `ready` deltaP `7.8827` edge `0.1562` maxDD `-6.9958`
- `news_risk_high->crypto_alt_1h` score `0.1616` n `30` status `ready` deltaP `4.5709` edge `0.0364` maxDD `-1.6923`
- `market_context_high->fx_1h` score `-0.3259` n `259` status `ready` deltaP `1.0283` edge `-0.0001` maxDD `-0.5499`
- `market_context_high->equity_1h` score `-0.3544` n `259` status `ready` deltaP `4.6142` edge `0.0404` maxDD `-5.0555`
- `news_risk_high->metal_1h` score `-0.4297` n `30` status `ready` deltaP `1.3872` edge `-0.0277` maxDD `-1.2643`
- `market_context_high->metal_1h` score `-0.4541` n `259` status `ready` deltaP `3.6524` edge `0.0049` maxDD `-2.0339`
- `market_context_high->commodity_1h` score `-0.5071` n `259` status `ready` deltaP `-0.5873` edge `-0.001` maxDD `-2.1412`
- `market_context_high->equity_24h` score `-0.7241` n `231` status `ready` deltaP `16.7028` edge `0.3362` maxDD `-31.6316`
- `market_context_high->crypto_major_1h` score `-0.7581` n `259` status `ready` deltaP `3.7391` edge `0.044` maxDD `-6.2348`
- `market_context_high->index_1h` score `-0.8459` n `259` status `ready` deltaP `1.2728` edge `0.0058` maxDD `-0.7819`
- `market_context_high->crypto_alt_1h` score `-0.9566` n `259` status `ready` deltaP `2.3444` edge `0.0381` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.1779` n `259` status `ready` deltaP `0.4968` edge `0.0144` maxDD `-3.165`
- `news_risk_high->index_1h` score `-1.2346` n `30` status `ready` deltaP `-12.3952` edge `-0.0242` maxDD `-1.1161`
- `market_context_high->fx_4h` score `-1.7221` n `259` status `ready` deltaP `-3.5668` edge `-0.0021` maxDD `-2.2593`
- `market_context_high->fx_24h` score `-1.7672` n `231` status `ready` deltaP `5.6141` edge `0.0178` maxDD `-5.5435`
- `market_context_high->metal_4h` score `-2.0982` n `259` status `ready` deltaP `-4.2788` edge `-0.0401` maxDD `-8.6964`
- `market_context_high->commodity_4h` score `-2.3055` n `259` status `ready` deltaP `-0.0283` edge `-0.0127` maxDD `-7.0053`
- `market_context_high->crypto_major_4h` score `-2.8481` n `259` status `ready` deltaP `7.3042` edge `0.1512` maxDD `-25.6458`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
