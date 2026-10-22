# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-22T19:07:34.230786+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6668`

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

- `risk_on_high->equity_1h` score `0.6499` n `37` status `ready` deltaP `16.3457` edge `0.0167` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.6499` n `37` status `ready` deltaP `16.3457` edge `0.0167` maxDD `-0.7219`
- `risk_on_high->index_1h` score `0.4966` n `37` status `ready` deltaP `13.0523` edge `0.0037` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.4966` n `37` status `ready` deltaP `13.0523` edge `0.0037` maxDD `-0.1637`
- `risk_on_high->commodity_24h` score `0.462` n `37` status `ready` deltaP `14.4009` edge `0.043` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.462` n `37` status `ready` deltaP `14.4009` edge `0.043` maxDD `-1.7154`
- `market_context_high->commodity_24h` score `0.314` n `75` status `ready` deltaP `13.6081` edge `0.0571` maxDD `-3.6055`
- `risk_on_high->fx_1h` score `0.0877` n `37` status `ready` deltaP `5.2517` edge `0.0021` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.0877` n `37` status `ready` deltaP `5.2517` edge `0.0021` maxDD `-0.0698`
- `risk_on_high->fx_4h` score `-0.2314` n `37` status `ready` deltaP `-0.8941` edge `0.0027` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.2314` n `37` status `ready` deltaP `-0.8941` edge `0.0027` maxDD `-0.1126`
- `market_context_high->index_1h` score `-0.2652` n `90` status `ready` deltaP `3.5928` edge `-0.0043` maxDD `-0.9588`
- `market_context_high->fx_1h` score `-0.3019` n `90` status `ready` deltaP `0.0865` edge `-0.0006` maxDD `-0.4278`
- `risk_on_high->index_4h` score `-0.4028` n `37` status `ready` deltaP `5.6197` edge `-0.0046` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.4028` n `37` status `ready` deltaP `5.6197` edge `-0.0046` maxDD `-0.7604`
- `market_context_high->commodity_1h` score `-0.4826` n `90` status `ready` deltaP `0.3393` edge `0.0026` maxDD `-1.0053`
- `market_context_high->commodity_4h` score `-0.5777` n `87` status `ready` deltaP `3.6603` edge `0.0047` maxDD `-2.9203`
- `market_context_high->fx_4h` score `-0.5862` n `87` status `ready` deltaP `1.032` edge `0.0049` maxDD `-0.5168`
- `risk_on_high->metal_1h` score `-0.6763` n `37` status `ready` deltaP `-4.9685` edge `0.0028` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.6763` n `37` status `ready` deltaP `-4.9685` edge `0.0028` maxDD `-0.0831`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
