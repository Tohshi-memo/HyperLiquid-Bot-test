# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-20T02:07:32.536205+00:00`
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

- `market_context_high->commodity_24h` score `1.4108` n `66` status `ready` deltaP `18.7973` edge `0.0774` maxDD `-1.8119`
- `risk_on_high->equity_1h` score `1.0224` n `39` status `ready` deltaP `18.1253` edge `0.0526` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `1.0224` n `39` status `ready` deltaP `18.1253` edge `0.0526` maxDD `-0.7219`
- `risk_on_high->index_1h` score `0.6383` n `39` status `ready` deltaP `14.9816` edge `0.009` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.6383` n `39` status `ready` deltaP `14.9816` edge `0.009` maxDD `-0.1637`
- `risk_on_high->commodity_24h` score `0.1506` n `39` status `ready` deltaP `15.1843` edge `-0.0089` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.1506` n `39` status `ready` deltaP `15.1843` edge `-0.0089` maxDD `-1.7154`
- `market_context_high->index_1h` score `0.0578` n `84` status `ready` deltaP `5.8241` edge `0.0041` maxDD `-0.5082`
- `risk_on_high->equity_4h` score `-0.054` n `39` status `ready` deltaP `5.8825` edge `0.0793` maxDD `-4.0351`
- `risk_on_and_context->equity_4h` score `-0.054` n `39` status `ready` deltaP `5.8825` edge `0.0793` maxDD `-4.0351`
- `risk_on_high->index_4h` score `-0.0643` n `39` status `ready` deltaP `8.7242` edge `0.0181` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.0643` n `39` status `ready` deltaP `8.7242` edge `0.0181` maxDD `-0.7604`
- `risk_on_high->fx_1h` score `-0.2598` n `39` status `ready` deltaP `0.2342` edge `-0.0003` maxDD `-0.0985`
- `risk_on_and_context->fx_1h` score `-0.2598` n `39` status `ready` deltaP `0.2342` edge `-0.0003` maxDD `-0.0985`
- `risk_on_high->metal_1h` score `-0.2654` n `39` status `ready` deltaP `-2.5181` edge `0.0088` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.2654` n `39` status `ready` deltaP `-2.5181` edge `0.0088` maxDD `-0.0831`
- `market_context_high->metal_1h` score `-0.3089` n `84` status `ready` deltaP `-0.8697` edge `0.0037` maxDD `-0.6669`
- `risk_on_high->fx_4h` score `-0.355` n `39` status `ready` deltaP `-2.6267` edge `-0.0016` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.355` n `39` status `ready` deltaP `-2.6267` edge `-0.0016` maxDD `-0.1126`
- `market_context_high->equity_1h` score `-0.3951` n `84` status `ready` deltaP `6.5868` edge `0.0006` maxDD `-4.6137`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
