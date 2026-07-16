# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T15:22:25.759793+00:00`
- Price records: `672`
- Market context records: `6931`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11706`

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

- `market_context_high->fx_1h` score `-0.2151` n `228` status `ready` deltaP `2.8233` edge `0.0021` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.4256` n `228` status `ready` deltaP `2.8575` edge `0.0219` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.5093` n `228` status `ready` deltaP `4.1627` edge `0.0202` maxDD `-4.2314`
- `market_context_high->unknown_24h` score `-0.6759` n `211` status `ready` deltaP `-6.4141` edge `0.3628` maxDD `-14.8687`
- `market_context_high->index_1h` score `-0.7155` n `228` status `ready` deltaP `-0.0762` edge `-0.0001` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.7354` n `228` status `ready` deltaP `-2.5055` edge `-0.0008` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-0.8138` n `224` status `ready` deltaP `13.8502` edge `0.0097` maxDD `-2.1765`
- `market_context_high->commodity_1h` score `-1.0957` n `228` status `ready` deltaP `-1.6257` edge `-0.012` maxDD `-2.1443`
- `market_context_high->unknown_1h` score `-1.5448` n `228` status `ready` deltaP `-2.1195` edge `-0.0245` maxDD `-3.2083`
- `market_context_high->commodity_4h` score `-1.5947` n `224` status `ready` deltaP `-3.8655` edge `-0.0297` maxDD `-5.5853`
- `market_context_high->equity_1h` score `-1.6404` n `228` status `ready` deltaP `3.2724` edge `-0.0141` maxDD `-13.1084`
- `market_context_high->index_4h` score `-1.6663` n `224` status `ready` deltaP `8.3624` edge `-0.0114` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-1.9222` n `224` status `ready` deltaP `5.368` edge `0.0161` maxDD `-5.5324`
- `market_context_high->crypto_alt_4h` score `-2.7476` n `224` status `ready` deltaP `1.753` edge `-0.0056` maxDD `-20.6678`
- `market_context_high->crypto_major_4h` score `-2.7667` n `224` status `ready` deltaP `-0.0871` edge `-0.0214` maxDD `-16.9508`
- `market_context_high->unknown_4h` score `-2.9755` n `224` status `ready` deltaP `-7.6655` edge `0.0397` maxDD `-10.2579`
- `market_context_high->commodity_24h` score `-3.1661` n `211` status `ready` deltaP `-3.0333` edge `-0.0568` maxDD `-5.2791`
- `market_context_high->fx_24h` score `-4.1173` n `211` status `ready` deltaP `-4.7517` edge `-0.0078` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-6.5706` n `224` status `ready` deltaP `5.76` edge `-0.0863` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.716` n `211` status `ready` deltaP `-12.5219` edge `-0.1167` maxDD `-33.0475`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
