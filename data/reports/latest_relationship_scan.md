# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-20T03:22:24.922802+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8301`

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

- `risk_on_high->equity_1h` score `0.8434` n `38` status `ready` deltaP `16.9634` edge `0.0374` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.8434` n `38` status `ready` deltaP `16.9634` edge `0.0374` maxDD `-0.7219`
- `risk_on_high->index_1h` score `0.5677` n `38` status `ready` deltaP `13.8197` edge `0.0077` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.5677` n `38` status `ready` deltaP `13.8197` edge `0.0077` maxDD `-0.1637`
- `market_context_high->commodity_24h` score `0.3651` n `61` status `ready` deltaP `15.9409` edge `0.0093` maxDD `-1.8119`
- `market_context_high->index_1h` score `0.014` n `79` status `ready` deltaP `5.1921` edge `0.0027` maxDD `-0.5082`
- `risk_on_high->index_4h` score `-0.0948` n `38` status `ready` deltaP `8.2718` edge `0.0172` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.0948` n `38` status `ready` deltaP `8.2718` edge `0.0172` maxDD `-0.7604`
- `risk_on_high->equity_4h` score `-0.1103` n `38` status `ready` deltaP `5.2952` edge `0.076` maxDD `-4.0351`
- `risk_on_and_context->equity_4h` score `-0.1103` n `38` status `ready` deltaP `5.2952` edge `0.076` maxDD `-4.0351`
- `risk_on_high->commodity_24h` score `-0.1138` n `38` status `ready` deltaP `14.1721` edge `-0.0293` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `-0.1138` n `38` status `ready` deltaP `14.1721` edge `-0.0293` maxDD `-1.7154`
- `risk_on_high->fx_1h` score `-0.1531` n `38` status `ready` deltaP `1.5837` edge `0.0001` maxDD `-0.0895`
- `risk_on_and_context->fx_1h` score `-0.1531` n `38` status `ready` deltaP `1.5837` edge `0.0001` maxDD `-0.0895`
- `risk_on_high->fx_4h` score `-0.2721` n `38` status `ready` deltaP `-1.1072` edge `-0.0011` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.2721` n `38` status `ready` deltaP `-1.1072` edge `-0.0011` maxDD `-0.1126`
- `market_context_high->commodity_1h` score `-0.3447` n `79` status `ready` deltaP `3.0963` edge `0.0017` maxDD `-0.9891`
- `risk_on_high->metal_1h` score `-0.3699` n `38` status `ready` deltaP `-4.0025` edge `0.0053` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.3699` n `38` status `ready` deltaP `-4.0025` edge `0.0053` maxDD `-0.0831`
- `market_context_high->metal_1h` score `-0.5273` n `79` status `ready` deltaP `-4.3356` edge `-0.0012` maxDD `-0.6669`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
