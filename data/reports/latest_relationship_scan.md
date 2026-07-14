# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T06:52:28.302850+00:00`
- Price records: `672`
- Market context records: `6685`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11784`

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

- `market_context_high->unknown_1h` score `2.4425` n `197` status `ready` deltaP `-4.9135` edge `0.3264` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `0.9412` n `197` status `ready` deltaP `11.5439` edge `0.1883` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `0.2569` n `197` status `ready` deltaP `8.6097` edge `0.05` maxDD `-4.2122`
- `market_context_high->unknown_24h` score `0.0542` n `197` status `ready` deltaP `-2.7787` edge `0.4007` maxDD `-12.3511`
- `market_context_high->crypto_alt_1h` score `0.0439` n `197` status `ready` deltaP `5.5313` edge `0.0432` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.2427` n `197` status `ready` deltaP `2.6558` edge `0.0014` maxDD `-0.6845`
- `market_context_high->index_1h` score `-0.4977` n `197` status `ready` deltaP `0.5859` edge `0.0037` maxDD `-0.7136`
- `market_context_high->commodity_1h` score `-0.574` n `197` status `ready` deltaP `0.4225` edge `-0.0081` maxDD `-2.1314`
- `market_context_high->metal_1h` score `-0.6175` n `197` status `ready` deltaP `-4.0412` edge `0.0003` maxDD `-1.2017`
- `market_context_high->index_4h` score `-0.8613` n `197` status `ready` deltaP `10.9121` edge `0.0048` maxDD `-5.7046`
- `market_context_high->unknown_4h` score `-0.8823` n `197` status `ready` deltaP `-14.2581` edge `0.2621` maxDD `-10.5788`
- `market_context_high->equity_1h` score `-0.8944` n `197` status `ready` deltaP `3.475` edge `0.005` maxDD `-3.8827`
- `market_context_high->fx_4h` score `-1.3841` n `197` status `ready` deltaP `6.609` edge `-0.0003` maxDD `-3.3635`
- `market_context_high->crypto_major_4h` score `-1.4271` n `197` status `ready` deltaP `8.8329` edge `0.0896` maxDD `-16.8495`
- `market_context_high->commodity_4h` score `-1.5468` n `197` status `ready` deltaP `-2.4948` edge `-0.0322` maxDD `-5.6246`
- `market_context_high->crypto_alt_4h` score `-1.6902` n `197` status `ready` deltaP `6.5982` edge `0.0795` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.1354` n `197` status `ready` deltaP `-1.4137` edge `0.0217` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-3.178` n `197` status `ready` deltaP `8.022` edge `-0.034` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-5.9156` n `197` status `ready` deltaP `-11.5702` edge `-0.0097` maxDD `-9.8236`
- `market_context_high->metal_24h` score `-6.9961` n `197` status `ready` deltaP `-6.3487` edge `-0.0061` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
