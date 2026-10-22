# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-22T12:22:35.838539+00:00`
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

- `risk_on_high->commodity_24h` score `0.6011` n `37` status `ready` deltaP `16.2813` edge `0.0483` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.6011` n `37` status `ready` deltaP `16.2813` edge `0.0483` maxDD `-1.7154`
- `risk_on_high->equity_1h` score `0.536` n `37` status `ready` deltaP `15.5972` edge `0.0071` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.536` n `37` status `ready` deltaP `15.5972` edge `0.0071` maxDD `-0.7219`
- `risk_on_high->index_1h` score `0.5348` n `37` status `ready` deltaP `13.6511` edge `0.0046` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.5348` n `37` status `ready` deltaP `13.6511` edge `0.0046` maxDD `-0.1637`
- `market_context_high->commodity_24h` score `0.3069` n `78` status `ready` deltaP `13.2321` edge `0.0587` maxDD `-3.6055`
- `risk_on_high->fx_1h` score `0.0884` n `37` status `ready` deltaP `5.4014` edge `0.0012` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.0884` n `37` status `ready` deltaP `5.4014` edge `0.0012` maxDD `-0.0698`
- `market_context_high->index_1h` score `0.0091` n `78` status `ready` deltaP `5.4737` edge `0.0002` maxDD `-0.5082`
- `risk_on_high->fx_4h` score `-0.19` n `37` status `ready` deltaP `0.173` edge `0.0009` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.19` n `37` status `ready` deltaP `0.173` edge `0.0009` maxDD `-0.1126`
- `risk_on_high->index_4h` score `-0.3651` n `37` status `ready` deltaP `5.9246` edge `-0.0018` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.3651` n `37` status `ready` deltaP `5.9246` edge `-0.0018` maxDD `-0.7604`
- `market_context_high->commodity_1h` score `-0.4096` n `78` status `ready` deltaP `0.9174` edge `0.0079` maxDD `-0.9891`
- `market_context_high->commodity_4h` score `-0.4207` n `78` status `ready` deltaP `5.4057` edge `0.0132` maxDD `-2.9203`
- `market_context_high->metal_1h` score `-0.6168` n `78` status `ready` deltaP `-5.5313` edge `-0.0047` maxDD `-0.6669`
- `risk_on_high->metal_1h` score `-0.7878` n `37` status `ready` deltaP `-6.0164` edge `0.0005` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.7878` n `37` status `ready` deltaP `-6.0164` edge `0.0005` maxDD `-0.0831`
- `risk_on_high->commodity_1h` score `-0.8394` n `37` status `ready` deltaP `-2.9981` edge `-0.0211` maxDD `-0.9891`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
