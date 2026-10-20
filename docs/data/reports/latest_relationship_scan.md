# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-20T04:22:30.515566+00:00`
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

- `risk_on_high->equity_1h` score `0.7365` n `37` status `ready` deltaP `16.0463` edge `0.0298` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.7365` n `37` status `ready` deltaP `16.0463` edge `0.0298` maxDD `-0.7219`
- `risk_on_high->index_1h` score `0.5138` n `37` status `ready` deltaP `12.9026` edge `0.0069` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.5138` n `37` status `ready` deltaP `12.9026` edge `0.0069` maxDD `-0.1637`
- `market_context_high->commodity_24h` score `0.1852` n `60` status `ready` deltaP `15.3125` edge `-0.0015` maxDD `-1.8119`
- `market_context_high->index_1h` score `-0.0118` n `78` status `ready` deltaP `4.7252` edge `0.0025` maxDD `-0.5082`
- `risk_on_high->fx_1h` score `-0.0408` n `37` status `ready` deltaP `3.0062` edge `0.0006` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `-0.0408` n `37` status `ready` deltaP `3.0062` edge `0.0006` maxDD `-0.0698`
- `risk_on_high->index_4h` score `-0.1445` n `37` status `ready` deltaP `7.6014` edge `0.0153` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.1445` n `37` status `ready` deltaP `7.6014` edge `0.0153` maxDD `-0.7604`
- `risk_on_high->fx_4h` score `-0.2048` n `37` status `ready` deltaP `0.173` edge `-0.001` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.2048` n `37` status `ready` deltaP `0.173` edge `-0.001` maxDD `-0.1126`
- `risk_on_high->equity_4h` score `-0.219` n `37` status `ready` deltaP `4.33` edge `0.0685` maxDD `-4.0351`
- `risk_on_and_context->equity_4h` score `-0.219` n `37` status `ready` deltaP `4.33` edge `0.0685` maxDD `-4.0351`
- `market_context_high->commodity_1h` score `-0.3077` n `78` status `ready` deltaP `3.612` edge `0.003` maxDD `-0.9891`
- `risk_on_high->commodity_24h` score `-0.3386` n `37` status `ready` deltaP `13.1053` edge `-0.051` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `-0.3386` n `37` status `ready` deltaP `13.1053` edge `-0.051` maxDD `-1.7154`
- `market_context_high->commodity_4h` score `-0.5506` n `78` status `ready` deltaP `6.7777` edge `-0.0126` maxDD `-2.9203`
- `market_context_high->metal_1h` score `-0.567` n `78` status `ready` deltaP `-4.9325` edge `-0.0023` maxDD `-0.6669`
- `risk_on_high->metal_1h` score `-0.7111` n `37` status `ready` deltaP `-5.4176` edge `0.0029` maxDD `-0.0831`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
