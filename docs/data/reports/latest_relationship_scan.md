# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-22T18:37:30.470254+00:00`
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

- `risk_on_high->equity_1h` score `0.6187` n `37` status `ready` deltaP `16.0463` edge `0.0147` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.6187` n `37` status `ready` deltaP `16.0463` edge `0.0147` maxDD `-0.7219`
- `risk_on_high->index_1h` score `0.4779` n `37` status `ready` deltaP `12.7529` edge `0.0033` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.4779` n `37` status `ready` deltaP `12.7529` edge `0.0033` maxDD `-0.1637`
- `risk_on_high->commodity_24h` score `0.4714` n `37` status `ready` deltaP `14.5513` edge `0.0432` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.4714` n `37` status `ready` deltaP `14.5513` edge `0.0432` maxDD `-1.7154`
- `market_context_high->commodity_24h` score `0.3233` n `75` status `ready` deltaP `13.7585` edge `0.0573` maxDD `-3.6055`
- `risk_on_high->fx_1h` score `0.0877` n `37` status `ready` deltaP `5.2517` edge `0.0021` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.0877` n `37` status `ready` deltaP `5.2517` edge `0.0021` maxDD `-0.0698`
- `risk_on_high->fx_4h` score `-0.2132` n `37` status `ready` deltaP `-0.5892` edge `0.003` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.2132` n `37` status `ready` deltaP `-0.5892` edge `0.003` maxDD `-0.1126`
- `market_context_high->index_1h` score `-0.2839` n `90` status `ready` deltaP `3.2934` edge `-0.0047` maxDD `-0.9588`
- `market_context_high->fx_1h` score `-0.3019` n `90` status `ready` deltaP `0.0865` edge `-0.0006` maxDD `-0.4278`
- `risk_on_high->index_4h` score `-0.4225` n `37` status `ready` deltaP `5.3148` edge `-0.0051` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.4225` n `37` status `ready` deltaP `5.3148` edge `-0.0051` maxDD `-0.7604`
- `market_context_high->commodity_1h` score `-0.4919` n `90` status `ready` deltaP `0.1896` edge `0.0024` maxDD `-1.0053`
- `market_context_high->commodity_4h` score `-0.6303` n `85` status `ready` deltaP `2.9645` edge `0.0026` maxDD `-2.9203`
- `market_context_high->fx_4h` score `-0.6608` n `85` status `ready` deltaP `0.174` edge `0.0044` maxDD `-0.5168`
- `risk_on_high->metal_1h` score `-0.6907` n `37` status `ready` deltaP `-5.1182` edge `0.0026` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.6907` n `37` status `ready` deltaP `-5.1182` edge `0.0026` maxDD `-0.0831`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
