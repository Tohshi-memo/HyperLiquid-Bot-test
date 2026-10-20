# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-20T06:22:26.484307+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8337`

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

- `risk_on_high->equity_1h` score `0.791` n `37` status `ready` deltaP `16.4954` edge `0.0338` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.791` n `37` status `ready` deltaP `16.4954` edge `0.0338` maxDD `-0.7219`
- `risk_on_high->index_1h` score `0.559` n `37` status `ready` deltaP `13.6511` edge `0.0077` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.559` n `37` status `ready` deltaP `13.6511` edge `0.0077` maxDD `-0.1637`
- `market_context_high->commodity_24h` score `0.3076` n `60` status `ready` deltaP `15.3125` edge `0.0087` maxDD `-1.8119`
- `market_context_high->index_1h` score `0.0333` n `78` status `ready` deltaP `5.4737` edge `0.0033` maxDD `-0.5082`
- `risk_on_high->fx_1h` score `-0.0159` n `37` status `ready` deltaP `3.4553` edge `0.0008` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `-0.0159` n `37` status `ready` deltaP `3.4553` edge `0.0008` maxDD `-0.0698`
- `risk_on_high->index_4h` score `-0.064` n `37` status `ready` deltaP `8.8209` edge `0.0175` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.064` n `37` status `ready` deltaP `8.8209` edge `0.0175` maxDD `-0.7604`
- `risk_on_high->equity_4h` score `-0.1003` n `37` status `ready` deltaP `5.3971` edge `0.0766` maxDD `-4.0351`
- `risk_on_and_context->equity_4h` score `-0.1003` n `37` status `ready` deltaP `5.3971` edge `0.0766` maxDD `-4.0351`
- `risk_on_high->fx_4h` score `-0.2404` n `37` status `ready` deltaP `-0.4368` edge `-0.0015` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.2404` n `37` status `ready` deltaP `-0.4368` edge `-0.0015` maxDD `-0.1126`
- `risk_on_high->commodity_24h` score `-0.259` n `37` status `ready` deltaP `13.1053` edge `-0.0408` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `-0.259` n `37` status `ready` deltaP `13.1053` edge `-0.0408` maxDD `-1.7154`
- `market_context_high->commodity_1h` score `-0.2984` n `78` status `ready` deltaP `3.7617` edge `0.0032` maxDD `-0.9891`
- `market_context_high->metal_1h` score `-0.5467` n `78` status `ready` deltaP `-4.6331` edge `-0.0017` maxDD `-0.6669`
- `market_context_high->commodity_4h` score `-0.6035` n `78` status `ready` deltaP `6.0155` edge `-0.0143` maxDD `-2.9203`
- `risk_on_high->metal_1h` score `-0.6799` n `37` status `ready` deltaP `-5.1182` edge `0.0035` maxDD `-0.0831`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
