# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-22T13:52:27.952743+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7698`

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

- `risk_on_high->commodity_24h` score `0.5645` n `37` status `ready` deltaP `15.8614` edge `0.0464` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.5645` n `37` status `ready` deltaP `15.8614` edge `0.0464` maxDD `-1.7154`
- `risk_on_high->index_1h` score `0.5052` n `37` status `ready` deltaP `13.202` edge `0.0038` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.5052` n `37` status `ready` deltaP `13.202` edge `0.0038` maxDD `-0.1637`
- `risk_on_high->equity_1h` score `0.4986` n `37` status `ready` deltaP `15.4475` edge `0.0033` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.4986` n `37` status `ready` deltaP `15.4475` edge `0.0033` maxDD `-0.7219`
- `market_context_high->commodity_24h` score `0.2702` n `78` status `ready` deltaP `12.8122` edge `0.0568` maxDD `-3.6055`
- `risk_on_high->fx_1h` score `0.0814` n `37` status `ready` deltaP `5.2517` edge `0.0013` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.0814` n `37` status `ready` deltaP `5.2517` edge `0.0013` maxDD `-0.0698`
- `risk_on_high->fx_4h` score `-0.149` n `37` status `ready` deltaP `0.6303` edge `0.0031` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.149` n `37` status `ready` deltaP `0.6303` edge `0.0031` maxDD `-0.1126`
- `market_context_high->index_1h` score `-0.1863` n `82` status `ready` deltaP `3.7425` edge `-0.0003` maxDD `-0.5491`
- `market_context_high->commodity_1h` score `-0.2861` n `82` status `ready` deltaP `2.6325` edge `0.0123` maxDD `-0.9891`
- `risk_on_high->index_4h` score `-0.4423` n `37` status `ready` deltaP `5.0099` edge `-0.0056` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.4423` n `37` status `ready` deltaP `5.0099` edge `-0.0056` maxDD `-0.7604`
- `market_context_high->commodity_4h` score `-0.4671` n `78` status `ready` deltaP `4.9484` edge `0.0103` maxDD `-2.9203`
- `market_context_high->metal_1h` score `-0.5244` n `82` status `ready` deltaP `-4.0237` edge `-0.0029` maxDD `-0.6669`
- `market_context_high->fx_1h` score `-0.6959` n `82` status `ready` deltaP `-6.1195` edge `-0.0042` maxDD `-0.5374`
- `risk_on_high->metal_1h` score `-0.801` n `37` status `ready` deltaP `-6.1661` edge `0.0004` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.801` n `37` status `ready` deltaP `-6.1661` edge `0.0004` maxDD `-0.0831`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
