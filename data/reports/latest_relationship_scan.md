# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-21T00:52:31.952965+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8806`

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

- `risk_on_high->equity_1h` score `0.6725` n `37` status `ready` deltaP `16.196` edge `0.0206` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.6725` n `37` status `ready` deltaP `16.196` edge `0.0206` maxDD `-0.7219`
- `risk_on_high->index_1h` score `0.5527` n `37` status `ready` deltaP `13.8008` edge `0.0059` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.5527` n `37` status `ready` deltaP `13.8008` edge `0.0059` maxDD `-0.1637`
- `risk_on_high->commodity_24h` score `0.2018` n `37` status `ready` deltaP `14.8414` edge `0.0067` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.2018` n `37` status `ready` deltaP `14.8414` edge `0.0067` maxDD `-1.7154`
- `risk_on_high->fx_1h` score `0.0643` n `37` status `ready` deltaP `4.9523` edge `0.0011` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.0643` n `37` status `ready` deltaP `4.9523` edge `0.0011` maxDD `-0.0698`
- `market_context_high->index_1h` score `0.0271` n `78` status `ready` deltaP `5.6234` edge `0.0015` maxDD `-0.5082`
- `risk_on_high->index_4h` score `-0.056` n `37` status `ready` deltaP `9.888` edge `0.0114` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.056` n `37` status `ready` deltaP `9.888` edge `0.0114` maxDD `-0.7604`
- `market_context_high->commodity_24h` score `-0.0925` n `78` status `ready` deltaP `11.7922` edge `0.0171` maxDD `-3.6055`
- `risk_on_high->fx_4h` score `-0.1787` n `37` status `ready` deltaP `0.6303` edge `-0.0007` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.1787` n `37` status `ready` deltaP `0.6303` edge `-0.0007` maxDD `-0.1126`
- `market_context_high->commodity_1h` score `-0.2313` n `78` status `ready` deltaP `3.9114` edge `0.0108` maxDD `-0.9891`
- `market_context_high->commodity_4h` score `-0.2776` n `78` status `ready` deltaP `7.6923` edge `0.0163` maxDD `-2.9203`
- `risk_on_high->equity_4h` score `-0.3586` n `37` status `ready` deltaP `7.0739` edge `0.0323` maxDD `-4.0351`
- `risk_on_and_context->equity_4h` score `-0.3586` n `37` status `ready` deltaP `7.0739` edge `0.0323` maxDD `-4.0351`
- `risk_on_high->commodity_1h` score `-0.6611` n `37` status `ready` deltaP `-0.0041` edge `-0.0182` maxDD `-0.9891`
- `risk_on_and_context->commodity_1h` score `-0.6611` n `37` status `ready` deltaP `-0.0041` edge `-0.0182` maxDD `-0.9891`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
