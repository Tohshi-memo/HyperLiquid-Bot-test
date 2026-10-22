# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-22T22:22:28.294280+00:00`
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

- `risk_on_high->equity_1h` score `0.5984` n `37` status `ready` deltaP `15.7469` edge `0.0141` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.5984` n `37` status `ready` deltaP `15.7469` edge `0.0141` maxDD `-0.7219`
- `risk_on_high->index_1h` score `0.4966` n `37` status `ready` deltaP `13.0523` edge `0.0037` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.4966` n `37` status `ready` deltaP `13.0523` edge `0.0037` maxDD `-0.1637`
- `market_context_high->commodity_24h` score `0.4512` n `72` status `ready` deltaP `15.812` edge `0.06` maxDD `-3.6055`
- `risk_on_high->commodity_24h` score `0.4479` n `37` status `ready` deltaP `14.1604` edge `0.0428` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.4479` n `37` status `ready` deltaP `14.1604` edge `0.0428` maxDD `-1.7154`
- `risk_on_high->fx_1h` score `0.1025` n `37` status `ready` deltaP `5.5511` edge `0.002` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.1025` n `37` status `ready` deltaP `5.5511` edge `0.002` maxDD `-0.0698`
- `market_context_high->fx_1h` score `-0.151` n `87` status `ready` deltaP `2.0717` edge `0.0023` maxDD `-0.1712`
- `risk_on_high->fx_4h` score `-0.2306` n `37` status `ready` deltaP `-0.8941` edge `0.0028` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.2306` n `37` status `ready` deltaP `-0.8941` edge `0.0028` maxDD `-0.1126`
- `market_context_high->fx_4h` score `-0.2875` n `87` status `ready` deltaP `4.4803` edge `0.0068` maxDD `-0.5168`
- `risk_on_high->index_4h` score `-0.3522` n `37` status `ready` deltaP `6.3819` edge `-0.0032` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.3522` n `37` status `ready` deltaP `6.3819` edge `-0.0032` maxDD `-0.7604`
- `market_context_high->commodity_4h` score `-0.4054` n `87` status `ready` deltaP `5.6542` edge `0.0135` maxDD `-2.9203`
- `market_context_high->commodity_1h` score `-0.4459` n `87` status `ready` deltaP `1.029` edge `0.0027` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.4612` n `87` status `ready` deltaP `3.0181` edge `-0.0049` maxDD `-0.9588`
- `risk_on_high->metal_1h` score `-0.6428` n `37` status `ready` deltaP `-4.6691` edge `0.0036` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.6428` n `37` status `ready` deltaP `-4.6691` edge `0.0036` maxDD `-0.0831`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
