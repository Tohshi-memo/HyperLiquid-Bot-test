# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-20T11:37:30.027236+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8758`

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

- `risk_on_high->equity_1h` score `0.8082` n `37` status `ready` deltaP `16.3457` edge `0.037` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.8082` n `37` status `ready` deltaP `16.3457` edge `0.037` maxDD `-0.7219`
- `market_context_high->commodity_24h` score `0.6388` n `60` status `ready` deltaP `15.3125` edge `0.0363` maxDD `-1.8119`
- `risk_on_high->index_1h` score `0.594` n `37` status `ready` deltaP `14.2499` edge `0.0082` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.594` n `37` status `ready` deltaP `14.2499` edge `0.0082` maxDD `-0.1637`
- `market_context_high->index_1h` score `0.0684` n `78` status `ready` deltaP `6.0725` edge `0.0038` maxDD `-0.5082`
- `risk_on_high->fx_1h` score `0.0316` n `37` status `ready` deltaP `4.3535` edge `0.0009` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.0316` n `37` status `ready` deltaP `4.3535` edge `0.0009` maxDD `-0.0698`
- `risk_on_high->index_4h` score `-0.0229` n `37` status `ready` deltaP `9.4307` edge `0.0187` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.0229` n `37` status `ready` deltaP `9.4307` edge `0.0187` maxDD `-0.7604`
- `risk_on_high->equity_4h` score `-0.0305` n `37` status `ready` deltaP `5.8544` edge `0.0825` maxDD `-4.0351`
- `risk_on_and_context->equity_4h` score `-0.0305` n `37` status `ready` deltaP `5.8544` edge `0.0825` maxDD `-4.0351`
- `risk_on_high->commodity_24h` score `-0.0437` n `37` status `ready` deltaP `13.1053` edge `-0.0132` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `-0.0437` n `37` status `ready` deltaP `13.1053` edge `-0.0132` maxDD `-1.7154`
- `risk_on_high->fx_4h` score `-0.1502` n `37` status `ready` deltaP `1.0876` edge `-0.0001` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.1502` n `37` status `ready` deltaP `1.0876` edge `-0.0001` maxDD `-0.1126`
- `market_context_high->commodity_1h` score `-0.3895` n `78` status `ready` deltaP `2.2647` edge `0.0015` maxDD `-0.9891`
- `market_context_high->metal_1h` score `-0.5537` n `78` status `ready` deltaP `-4.7828` edge `-0.0016` maxDD `-0.6669`
- `market_context_high->commodity_4h` score `-0.6103` n `78` status `ready` deltaP `5.2533` edge `-0.0101` maxDD `-2.9203`
- `risk_on_high->metal_1h` score `-0.6907` n `37` status `ready` deltaP `-5.2679` edge `0.0036` maxDD `-0.0831`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
