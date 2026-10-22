# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-22T12:52:33.156582+00:00`
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

- `risk_on_high->commodity_24h` score `0.5884` n `37` status `ready` deltaP `16.1423` edge `0.0476` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.5884` n `37` status `ready` deltaP `16.1423` edge `0.0476` maxDD `-1.7154`
- `risk_on_high->index_1h` score `0.5247` n `37` status `ready` deltaP `13.5014` edge `0.0043` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.5247` n `37` status `ready` deltaP `13.5014` edge `0.0043` maxDD `-0.1637`
- `risk_on_high->equity_1h` score `0.5204` n `37` status `ready` deltaP `15.5972` edge `0.0051` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.5204` n `37` status `ready` deltaP `15.5972` edge `0.0051` maxDD `-0.7219`
- `market_context_high->commodity_24h` score `0.2942` n `78` status `ready` deltaP `13.0931` edge `0.058` maxDD `-3.6055`
- `risk_on_high->fx_1h` score `0.0721` n `37` status `ready` deltaP `5.102` edge `0.0011` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.0721` n `37` status `ready` deltaP `5.102` edge `0.0011` maxDD `-0.0698`
- `market_context_high->index_1h` score `-0.0688` n `79` status `ready` deltaP `4.6748` edge `-0.0002` maxDD `-0.5158`
- `risk_on_high->fx_4h` score `-0.1679` n `37` status `ready` deltaP `0.4779` edge `0.0017` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.1679` n `37` status `ready` deltaP `0.4779` edge `0.0017` maxDD `-0.1126`
- `market_context_high->commodity_1h` score `-0.3823` n `79` status `ready` deltaP `1.3682` edge `0.0084` maxDD `-0.9891`
- `risk_on_high->index_4h` score `-0.3911` n `37` status `ready` deltaP `5.6197` edge `-0.0031` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.3911` n `37` status `ready` deltaP `5.6197` edge `-0.0031` maxDD `-0.7604`
- `market_context_high->commodity_4h` score `-0.4246` n `78` status `ready` deltaP `5.4057` edge `0.0127` maxDD `-2.9203`
- `market_context_high->metal_1h` score `-0.5663` n `79` status `ready` deltaP `-4.7847` edge `-0.0032` maxDD `-0.6669`
- `risk_on_high->metal_1h` score `-0.7914` n `37` status `ready` deltaP `-6.0164` edge `0.0002` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.7914` n `37` status `ready` deltaP `-6.0164` edge `0.0002` maxDD `-0.0831`
- `risk_on_high->commodity_1h` score `-0.8488` n `37` status `ready` deltaP `-3.1478` edge `-0.0213` maxDD `-0.9891`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
