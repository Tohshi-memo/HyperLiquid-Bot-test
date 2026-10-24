# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-24T17:24:19.339348+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7566`

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

- `market_context_high->unknown_4h` score `13.8502` n `107` status `ready` deltaP `-1.9631` edge `1.2008` maxDD `-1.016`
- `risk_on_high->index_1h` score `0.467` n `37` status `ready` deltaP `12.7529` edge `0.0019` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.467` n `37` status `ready` deltaP `12.7529` edge `0.0019` maxDD `-0.1637`
- `risk_on_high->equity_1h` score `0.4337` n `37` status `ready` deltaP `14.5493` edge `0.0009` maxDD `-0.7172`
- `risk_on_and_context->equity_1h` score `0.4337` n `37` status `ready` deltaP `14.5493` edge `0.0009` maxDD `-0.7172`
- `market_context_high->commodity_24h` score `0.3206` n `82` status `ready` deltaP `13.766` edge `0.0569` maxDD `-3.6055`
- `risk_on_high->fx_1h` score `0.2262` n `37` status `ready` deltaP `7.7966` edge `0.0029` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.2262` n `37` status `ready` deltaP `7.7966` edge `0.0029` maxDD `-0.0698`
- `risk_on_high->fx_4h` score `0.0345` n `37` status `ready` deltaP `3.6791` edge `0.0063` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `0.0345` n `37` status `ready` deltaP `3.6791` edge `0.0063` maxDD `-0.1126`
- `risk_on_high->commodity_24h` score `-0.0039` n `37` status `ready` deltaP `8.5914` edge `0.022` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `-0.0039` n `37` status `ready` deltaP `8.5914` edge `0.022` maxDD `-1.7154`
- `market_context_high->commodity_4h` score `-0.2072` n `107` status `ready` deltaP `6.7316` edge `0.0273` maxDD `-2.8998`
- `market_context_high->fx_1h` score `-0.2258` n `111` status `ready` deltaP `0.5893` edge `0.0026` maxDD `-0.1712`
- `market_context_high->commodity_1h` score `-0.306` n `111` status `ready` deltaP `3.4661` edge `0.0044` maxDD `-1.0053`
- `risk_on_high->index_4h` score `-0.4124` n `37` status `ready` deltaP `6.2294` edge `-0.0099` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.4124` n `37` status `ready` deltaP `6.2294` edge `-0.0099` maxDD `-0.7604`
- `market_context_high->fx_4h` score `-0.4341` n `107` status `ready` deltaP `-0.1097` edge `0.0057` maxDD `-0.5168`
- `risk_on_high->metal_1h` score `-0.4391` n `37` status `ready` deltaP `-2.5733` edge `0.0066` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.4391` n `37` status `ready` deltaP `-2.5733` edge `0.0066` maxDD `-0.0831`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
