# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-22T20:52:33.590059+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6804`

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

- `risk_on_high->equity_1h` score `0.6125` n `37` status `ready` deltaP `15.8966` edge `0.0149` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.6125` n `37` status `ready` deltaP `15.8966` edge `0.0149` maxDD `-0.7219`
- `risk_on_high->index_1h` score `0.4787` n `37` status `ready` deltaP `12.7529` edge `0.0034` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.4787` n `37` status `ready` deltaP `12.7529` edge `0.0034` maxDD `-0.1637`
- `risk_on_high->commodity_24h` score `0.4519` n `37` status `ready` deltaP `14.2818` edge `0.0425` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.4519` n `37` status `ready` deltaP `14.2818` edge `0.0425` maxDD `-1.7154`
- `market_context_high->commodity_24h` score `0.3545` n `74` status `ready` deltaP `14.2818` edge `0.0578` maxDD `-3.6055`
- `risk_on_high->fx_1h` score `0.1032` n `37` status `ready` deltaP `5.5511` edge `0.0021` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.1032` n `37` status `ready` deltaP `5.5511` edge `0.0021` maxDD `-0.0698`
- `market_context_high->fx_1h` score `-0.24` n `89` status `ready` deltaP `0.9352` edge `0.0005` maxDD `-0.3341`
- `risk_on_high->fx_4h` score `-0.2575` n `37` status `ready` deltaP `-1.3514` edge `0.0024` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.2575` n `37` status `ready` deltaP `-1.3514` edge `0.0024` maxDD `-0.1126`
- `market_context_high->index_1h` score `-0.3154` n `89` status `ready` deltaP `2.7316` edge `-0.005` maxDD `-0.9588`
- `risk_on_high->index_4h` score `-0.3799` n `37` status `ready` deltaP `5.9246` edge `-0.0037` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.3799` n `37` status `ready` deltaP `5.9246` edge `-0.0037` maxDD `-0.7604`
- `market_context_high->commodity_4h` score `-0.4349` n `89` status `ready` deltaP `5.2823` edge `0.0122` maxDD `-2.9203`
- `market_context_high->fx_4h` score `-0.438` n `89` status `ready` deltaP `2.809` edge `0.0054` maxDD `-0.5168`
- `market_context_high->commodity_1h` score `-0.4405` n `89` status `ready` deltaP `1.0883` edge `0.003` maxDD `-1.0053`
- `risk_on_high->metal_1h` score `-0.6488` n `37` status `ready` deltaP `-4.6691` edge `0.0031` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.6488` n `37` status `ready` deltaP `-4.6691` edge `0.0031` maxDD `-0.0831`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
