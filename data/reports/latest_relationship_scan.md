# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-22T02:52:24.240585+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8370`

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

- `risk_on_high->equity_1h` score `0.7138` n `37` status `ready` deltaP `16.4954` edge `0.0239` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.7138` n `37` status `ready` deltaP `16.4954` edge `0.0239` maxDD `-0.7219`
- `risk_on_high->index_1h` score `0.6041` n `37` status `ready` deltaP `14.699` edge `0.0065` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.6041` n `37` status `ready` deltaP `14.699` edge `0.0065` maxDD `-0.1637`
- `risk_on_high->commodity_24h` score `0.5558` n `37` status `ready` deltaP `16.4454` edge `0.0414` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.5558` n `37` status `ready` deltaP `16.4454` edge `0.0414` maxDD `-1.7154`
- `market_context_high->commodity_24h` score `0.2616` n `78` status `ready` deltaP `13.3962` edge `0.0518` maxDD `-3.6055`
- `market_context_high->index_1h` score `0.0785` n `78` status `ready` deltaP `6.5216` edge `0.0021` maxDD `-0.5082`
- `risk_on_high->fx_1h` score `0.0472` n `37` status `ready` deltaP `4.6529` edge `0.0009` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.0472` n `37` status `ready` deltaP `4.6529` edge `0.0009` maxDD `-0.0698`
- `risk_on_high->index_4h` score `-0.2366` n `37` status `ready` deltaP `7.3755` edge `0.005` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.2366` n `37` status `ready` deltaP `7.3755` edge `0.005` maxDD `-0.7604`
- `risk_on_high->fx_4h` score `-0.3505` n `37` status `ready` deltaP `-2.255` edge `-0.0035` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.3505` n `37` status `ready` deltaP `-2.255` edge `-0.0035` maxDD `-0.1126`
- `market_context_high->commodity_1h` score `-0.3582` n `78` status `ready` deltaP `1.6659` edge `0.0095` maxDD `-0.9891`
- `market_context_high->commodity_4h` score `-0.3615` n `78` status `ready` deltaP `5.7345` edge `0.0186` maxDD `-2.9203`
- `market_context_high->metal_1h` score `-0.5911` n `78` status `ready` deltaP `-5.3816` edge `-0.0024` maxDD `-0.6669`
- `risk_on_high->metal_1h` score `-0.7482` n `37` status `ready` deltaP `-5.8667` edge `0.0028` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.7482` n `37` status `ready` deltaP `-5.8667` edge `0.0028` maxDD `-0.0831`
- `risk_on_high->commodity_1h` score `-0.788` n `37` status `ready` deltaP `-2.2496` edge `-0.0195` maxDD `-0.9891`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
