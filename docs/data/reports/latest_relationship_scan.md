# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-22T14:52:30.304673+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7008`

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

- `risk_on_high->commodity_24h` score `0.5388` n `37` status `ready` deltaP `15.577` edge `0.045` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.5388` n `37` status `ready` deltaP `15.577` edge `0.045` maxDD `-1.7154`
- `risk_on_high->equity_1h` score `0.529` n `37` status `ready` deltaP `15.5972` edge `0.0062` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.529` n `37` status `ready` deltaP `15.5972` edge `0.0062` maxDD `-0.7219`
- `risk_on_high->index_1h` score `0.4966` n `37` status `ready` deltaP `13.0523` edge `0.0037` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.4966` n `37` status `ready` deltaP `13.0523` edge `0.0037` maxDD `-0.1637`
- `market_context_high->commodity_24h` score `0.2445` n `78` status `ready` deltaP `12.5278` edge `0.0554` maxDD `-3.6055`
- `risk_on_high->fx_1h` score `0.1087` n `37` status `ready` deltaP `5.7008` edge `0.0018` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.1087` n `37` status `ready` deltaP `5.7008` edge `0.0018` maxDD `-0.0698`
- `risk_on_high->fx_4h` score `-0.1404` n `37` status `ready` deltaP `0.6303` edge `0.0042` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.1404` n `37` status `ready` deltaP `0.6303` edge `0.0042` maxDD `-0.1126`
- `market_context_high->index_1h` score `-0.2547` n `85` status `ready` deltaP `3.0046` edge `-0.0025` maxDD `-0.6817`
- `market_context_high->commodity_1h` score `-0.4274` n `85` status `ready` deltaP `0.8454` edge `0.0061` maxDD `-0.9891`
- `risk_on_high->index_4h` score `-0.4627` n `37` status `ready` deltaP `4.8575` edge `-0.0072` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.4627` n `37` status `ready` deltaP `4.8575` edge `-0.0072` maxDD `-0.7604`
- `market_context_high->commodity_4h` score `-0.4867` n `78` status `ready` deltaP `4.796` edge `0.0088` maxDD `-2.9203`
- `market_context_high->metal_1h` score `-0.6169` n `85` status `ready` deltaP `-5.2307` edge `-0.0051` maxDD `-0.7966`
- `risk_on_high->metal_1h` score `-0.765` n `37` status `ready` deltaP `-5.8667` edge `0.0014` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.765` n `37` status `ready` deltaP `-5.8667` edge `0.0014` maxDD `-0.0831`
- `risk_on_high->commodity_1h` score `-0.8651` n `37` status `ready` deltaP `-3.4472` edge `-0.0214` maxDD `-0.9891`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
