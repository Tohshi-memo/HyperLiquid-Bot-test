# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-20T13:52:29.389553+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8877`

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

- `market_context_high->commodity_24h` score `1.2556` n `67` status `ready` deltaP `19.3174` edge `0.061` maxDD `-1.8119`
- `risk_on_high->equity_1h` score `0.7973` n `37` status `ready` deltaP `16.196` edge `0.0366` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.7973` n `37` status `ready` deltaP `16.196` edge `0.0366` maxDD `-0.7219`
- `risk_on_high->index_1h` score `0.5924` n `37` status `ready` deltaP `14.2499` edge `0.008` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.5924` n `37` status `ready` deltaP `14.2499` edge `0.008` maxDD `-0.1637`
- `risk_on_high->equity_4h` score `0.0864` n `37` status `ready` deltaP `6.6166` edge `0.0924` maxDD `-4.0351`
- `risk_on_and_context->equity_4h` score `0.0864` n `37` status `ready` deltaP `6.6166` edge `0.0924` maxDD `-4.0351`
- `market_context_high->index_1h` score `0.0668` n `78` status `ready` deltaP `6.0725` edge `0.0036` maxDD `-0.5082`
- `risk_on_high->commodity_24h` score `0.0335` n `37` status `ready` deltaP `13.1053` edge `-0.0033` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.0335` n `37` status `ready` deltaP `13.1053` edge `-0.0033` maxDD `-1.7154`
- `risk_on_high->fx_1h` score `0.0238` n `37` status `ready` deltaP `4.2038` edge `0.0009` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.0238` n `37` status `ready` deltaP `4.2038` edge `0.0009` maxDD `-0.0698`
- `risk_on_high->index_4h` score `0.0079` n `37` status `ready` deltaP `9.888` edge `0.0196` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `0.0079` n `37` status `ready` deltaP `9.888` edge `0.0196` maxDD `-0.7604`
- `risk_on_high->fx_4h` score `-0.1502` n `37` status `ready` deltaP `1.0876` edge `-0.0001` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.1502` n `37` status `ready` deltaP `1.0876` edge `-0.0001` maxDD `-0.1126`
- `market_context_high->commodity_1h` score `-0.2944` n `78` status `ready` deltaP `3.3126` edge `0.0067` maxDD `-0.9891`
- `market_context_high->commodity_4h` score `-0.4785` n `78` status `ready` deltaP `6.1679` edge `0.0007` maxDD `-2.9203`
- `market_context_high->metal_1h` score `-0.6036` n `78` status `ready` deltaP `-5.5313` edge `-0.003` maxDD `-0.6669`
- `risk_on_high->commodity_1h` score `-0.7242` n `37` status `ready` deltaP `-0.6029` edge `-0.0223` maxDD `-0.9891`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
