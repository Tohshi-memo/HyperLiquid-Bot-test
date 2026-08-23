# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T19:07:31.221658+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14856`

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

- `news_risk_high->unknown_4h` score `13.4425` n `51` status `ready` deltaP `24.1063` edge `0.9641` maxDD `-0.0348`
- `risk_on_high->unknown_1h` score `4.0268` n `37` status `ready` deltaP `-8.6624` edge `0.6189` maxDD `-1.5916`
- `risk_on_and_context->unknown_1h` score `4.0268` n `37` status `ready` deltaP `-8.6624` edge `0.6189` maxDD `-1.5916`
- `news_risk_high->unknown_1h` score `3.2105` n `51` status `ready` deltaP `16.9337` edge `0.1851` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.0047` n `51` status `ready` deltaP `35.6438` edge `0.0262` maxDD `-0.0746`
- `news_risk_high->equity_4h` score `2.6506` n `51` status `ready` deltaP `23.2694` edge `0.1428` maxDD `-2.164`
- `risk_on_high->metal_4h` score `2.1894` n `34` status `ready` deltaP `29.2414` edge `-0.0037` maxDD `-0.0367`
- `risk_on_and_context->metal_4h` score `2.1894` n `34` status `ready` deltaP `29.2414` edge `-0.0037` maxDD `-0.0367`
- `risk_on_high->equity_4h` score `1.6448` n `34` status `ready` deltaP `-0.26` edge `0.2556` maxDD `-0.773`
- `risk_on_and_context->equity_4h` score `1.6448` n `34` status `ready` deltaP `-0.26` edge `0.2556` maxDD `-0.773`
- `news_risk_high->fx_1h` score `1.1631` n `51` status `ready` deltaP `16.0972` edge `0.0066` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `0.9806` n `141` status `ready` deltaP `6.212` edge `0.0852` maxDD `-1.5916`
- `market_context_high->crypto_alt_4h` score `0.9347` n `130` status `ready` deltaP `8.9282` edge `0.1648` maxDD `-7.0478`
- `news_risk_high->equity_1h` score `0.6943` n `51` status `ready` deltaP `15.9475` edge `0.0191` maxDD `-0.9128`
- `market_context_high->commodity_24h` score `0.598` n `109` status `ready` deltaP `-1.9782` edge `0.1105` maxDD `-0.7984`
- `risk_on_high->fx_4h` score `0.5975` n `34` status `ready` deltaP `15.0556` edge `0.0037` maxDD `-0.1972`
- `risk_on_and_context->fx_4h` score `0.5975` n `34` status `ready` deltaP `15.0556` edge `0.0037` maxDD `-0.1972`
- `news_risk_high->index_4h` score `0.4657` n `51` status `ready` deltaP `8.9759` edge `0.0187` maxDD `-0.1788`
- `risk_on_high->index_4h` score `0.4263` n `34` status `ready` deltaP `8.9759` edge `0.0428` maxDD `-0.1719`
- `risk_on_and_context->index_4h` score `0.4263` n `34` status `ready` deltaP `8.9759` edge `0.0428` maxDD `-0.1719`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
