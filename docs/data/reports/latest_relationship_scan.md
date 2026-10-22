# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-22T14:22:30.236740+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7680`

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

- `risk_on_high->commodity_24h` score `0.5516` n `37` status `ready` deltaP `15.7197` edge `0.0457` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.5516` n `37` status `ready` deltaP `15.7197` edge `0.0457` maxDD `-1.7154`
- `risk_on_high->index_1h` score `0.4951` n `37` status `ready` deltaP `13.0523` edge `0.0035` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.4951` n `37` status `ready` deltaP `13.0523` edge `0.0035` maxDD `-0.1637`
- `risk_on_high->equity_1h` score `0.4846` n `37` status `ready` deltaP `15.2978` edge `0.0025` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.4846` n `37` status `ready` deltaP `15.2978` edge `0.0025` maxDD `-0.7219`
- `market_context_high->commodity_24h` score `0.2574` n `78` status `ready` deltaP `12.6705` edge `0.0561` maxDD `-3.6055`
- `risk_on_high->fx_1h` score `0.0908` n `37` status `ready` deltaP `5.4014` edge `0.0015` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.0908` n `37` status `ready` deltaP `5.4014` edge `0.0015` maxDD `-0.0698`
- `risk_on_high->fx_4h` score `-0.1443` n `37` status `ready` deltaP `0.6303` edge `0.0037` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.1443` n `37` status `ready` deltaP `0.6303` edge `0.0037` maxDD `-0.1126`
- `market_context_high->index_1h` score `-0.1941` n `84` status `ready` deltaP `3.5928` edge `-0.0003` maxDD `-0.5491`
- `market_context_high->commodity_1h` score `-0.372` n `84` status `ready` deltaP `1.4756` edge `0.009` maxDD `-0.9891`
- `risk_on_high->index_4h` score `-0.4588` n `37` status `ready` deltaP `4.8575` edge `-0.0067` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.4588` n `37` status `ready` deltaP `4.8575` edge `-0.0067` maxDD `-0.7604`
- `market_context_high->commodity_4h` score `-0.482` n `78` status `ready` deltaP `4.796` edge `0.0094` maxDD `-2.9203`
- `market_context_high->metal_1h` score `-0.5973` n `84` status `ready` deltaP `-4.8902` edge `-0.0053` maxDD `-0.7612`
- `risk_on_high->metal_1h` score `-0.783` n `37` status `ready` deltaP `-6.0164` edge `0.0009` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.783` n `37` status `ready` deltaP `-6.0164` edge `0.0009` maxDD `-0.0831`
- `risk_on_high->commodity_1h` score `-0.8682` n `37` status `ready` deltaP `-3.4472` edge `-0.0218` maxDD `-0.9891`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
