# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-22T12:37:29.759957+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7500`

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

- `risk_on_high->commodity_24h` score `0.5952` n `37` status `ready` deltaP `16.2119` edge `0.048` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.5952` n `37` status `ready` deltaP `16.2119` edge `0.048` maxDD `-1.7154`
- `risk_on_high->equity_1h` score `0.5282` n `37` status `ready` deltaP `15.5972` edge `0.0061` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.5282` n `37` status `ready` deltaP `15.5972` edge `0.0061` maxDD `-0.7219`
- `risk_on_high->index_1h` score `0.5254` n `37` status `ready` deltaP `13.5014` edge `0.0044` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.5254` n `37` status `ready` deltaP `13.5014` edge `0.0044` maxDD `-0.1637`
- `market_context_high->commodity_24h` score `0.3009` n `78` status `ready` deltaP `13.1627` edge `0.0584` maxDD `-3.6055`
- `risk_on_high->fx_1h` score `0.0806` n `37` status `ready` deltaP `5.2517` edge `0.0012` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.0806` n `37` status `ready` deltaP `5.2517` edge `0.0012` maxDD `-0.0698`
- `market_context_high->index_1h` score `-0.0002` n `78` status `ready` deltaP `5.324` edge `0.0` maxDD `-0.5082`
- `risk_on_high->fx_4h` score `-0.1789` n `37` status `ready` deltaP `0.3254` edge `0.0013` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.1789` n `37` status `ready` deltaP `0.3254` edge `0.0013` maxDD `-0.1126`
- `risk_on_high->index_4h` score `-0.3785` n `37` status `ready` deltaP `5.7721` edge `-0.0025` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.3785` n `37` status `ready` deltaP `5.7721` edge `-0.0025` maxDD `-0.7604`
- `market_context_high->commodity_1h` score `-0.4104` n `78` status `ready` deltaP `0.9174` edge `0.0078` maxDD `-0.9891`
- `market_context_high->commodity_4h` score `-0.4222` n `78` status `ready` deltaP `5.4057` edge `0.013` maxDD `-2.9203`
- `market_context_high->metal_1h` score `-0.6176` n `78` status `ready` deltaP `-5.5313` edge `-0.0048` maxDD `-0.6669`
- `risk_on_high->metal_1h` score `-0.789` n `37` status `ready` deltaP `-6.0164` edge `0.0004` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.789` n `37` status `ready` deltaP `-6.0164` edge `0.0004` maxDD `-0.0831`
- `risk_on_high->commodity_1h` score `-0.8402` n `37` status `ready` deltaP `-2.9981` edge `-0.0212` maxDD `-0.9891`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
