# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-22T21:07:33.972475+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6792`

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

- `risk_on_high->equity_1h` score `0.6164` n `37` status `ready` deltaP `15.8966` edge `0.0154` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.6164` n `37` status `ready` deltaP `15.8966` edge `0.0154` maxDD `-0.7219`
- `risk_on_high->index_1h` score `0.4881` n `37` status `ready` deltaP `12.9026` edge `0.0036` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.4881` n `37` status `ready` deltaP `12.9026` edge `0.0036` maxDD `-0.1637`
- `risk_on_high->commodity_24h` score `0.4479` n `37` status `ready` deltaP `14.2053` edge `0.0425` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.4479` n `37` status `ready` deltaP `14.2053` edge `0.0425` maxDD `-1.7154`
- `market_context_high->commodity_24h` score `0.4006` n `73` status `ready` deltaP `15.0198` edge `0.0588` maxDD `-3.6055`
- `risk_on_high->fx_1h` score `0.1032` n `37` status `ready` deltaP `5.5511` edge `0.0021` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.1032` n `37` status `ready` deltaP `5.5511` edge `0.0021` maxDD `-0.0698`
- `market_context_high->fx_1h` score `-0.1958` n `88` status `ready` deltaP `1.497` edge `0.0014` maxDD `-0.252`
- `risk_on_high->fx_4h` score `-0.2575` n `37` status `ready` deltaP `-1.3514` edge `0.0024` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.2575` n `37` status `ready` deltaP `-1.3514` edge `0.0024` maxDD `-0.1126`
- `risk_on_high->index_4h` score `-0.3712` n `37` status `ready` deltaP `6.077` edge `-0.0036` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.3712` n `37` status `ready` deltaP `6.077` edge `-0.0036` maxDD `-0.7604`
- `market_context_high->fx_4h` score `-0.384` n `88` status `ready` deltaP `3.4091` edge `0.0059` maxDD `-0.5168`
- `market_context_high->commodity_4h` score `-0.4006` n `88` status `ready` deltaP `5.8066` edge `0.0131` maxDD `-2.9203`
- `market_context_high->commodity_1h` score `-0.4063` n `88` status `ready` deltaP `1.7012` edge `0.0033` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.5205` n `88` status `ready` deltaP `2.3067` edge `-0.0051` maxDD `-0.9588`
- `risk_on_high->metal_1h` score `-0.65` n `37` status `ready` deltaP `-4.6691` edge `0.003` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.65` n `37` status `ready` deltaP `-4.6691` edge `0.003` maxDD `-0.0831`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
