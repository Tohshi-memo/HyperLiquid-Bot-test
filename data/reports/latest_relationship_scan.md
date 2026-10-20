# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-20T09:07:30.535008+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8323`

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

- `risk_on_high->equity_1h` score `0.8121` n `37` status `ready` deltaP `16.4954` edge `0.0365` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.8121` n `37` status `ready` deltaP `16.4954` edge `0.0365` maxDD `-0.7219`
- `risk_on_high->index_1h` score `0.6096` n `37` status `ready` deltaP `14.5493` edge `0.0082` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.6096` n `37` status `ready` deltaP `14.5493` edge `0.0082` maxDD `-0.1637`
- `market_context_high->commodity_24h` score `0.4468` n `60` status `ready` deltaP `15.3125` edge `0.0203` maxDD `-1.8119`
- `market_context_high->index_1h` score `0.0839` n `78` status `ready` deltaP `6.3719` edge `0.0038` maxDD `-0.5082`
- `risk_on_high->fx_1h` score `-0.0245` n `37` status `ready` deltaP `3.3056` edge `0.0007` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `-0.0245` n `37` status `ready` deltaP `3.3056` edge `0.0007` maxDD `-0.0698`
- `risk_on_high->equity_4h` score `-0.0282` n `37` status `ready` deltaP `5.8544` edge `0.0828` maxDD `-4.0351`
- `risk_on_and_context->equity_4h` score `-0.0282` n `37` status `ready` deltaP `5.8544` edge `0.0828` maxDD `-4.0351`
- `risk_on_high->index_4h` score `-0.0347` n `37` status `ready` deltaP `9.2782` edge `0.0182` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.0347` n `37` status `ready` deltaP `9.2782` edge `0.0182` maxDD `-0.7604`
- `risk_on_high->commodity_24h` score `-0.1685` n `37` status `ready` deltaP `13.1053` edge `-0.0292` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `-0.1685` n `37` status `ready` deltaP `13.1053` edge `-0.0292` maxDD `-1.7154`
- `risk_on_high->fx_4h` score `-0.223` n `37` status `ready` deltaP `-0.1319` edge `-0.0013` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.223` n `37` status `ready` deltaP `-0.1319` edge `-0.0013` maxDD `-0.1126`
- `market_context_high->commodity_1h` score `-0.3747` n `78` status `ready` deltaP `2.5641` edge `0.0014` maxDD `-0.9891`
- `market_context_high->metal_1h` score `-0.5459` n `78` status `ready` deltaP `-4.6331` edge `-0.0016` maxDD `-0.6669`
- `market_context_high->commodity_4h` score `-0.6595` n `78` status `ready` deltaP `5.2533` edge `-0.0164` maxDD `-2.9203`
- `risk_on_high->metal_1h` score `-0.6787` n `37` status `ready` deltaP `-5.1182` edge `0.0036` maxDD `-0.0831`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
