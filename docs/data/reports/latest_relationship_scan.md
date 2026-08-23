# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T14:44:33.617308+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14776`

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

- `news_risk_high->unknown_4h` score `14.0294` n `51` status `ready` deltaP `25.1733` edge `1.0059` maxDD `-0.0348`
- `risk_on_high->unknown_1h` score `4.7985` n `33` status `ready` deltaP `-9.5264` edge `0.7236` maxDD `-1.5916`
- `risk_on_and_context->unknown_1h` score `4.7985` n `33` status `ready` deltaP `-9.5264` edge `0.7236` maxDD `-1.5916`
- `news_risk_high->unknown_1h` score `3.4047` n `51` status `ready` deltaP `18.281` edge `0.1923` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `2.9681` n `51` status `ready` deltaP `35.1865` edge `0.0262` maxDD `-0.0746`
- `news_risk_high->equity_4h` score `2.7022` n `51` status `ready` deltaP `23.2694` edge `0.1471` maxDD `-2.164`
- `risk_on_high->metal_4h` score `2.2876` n `33` status `ready` deltaP `30.4093` edge `-0.0033` maxDD `-0.0367`
- `risk_on_and_context->metal_4h` score `2.2876` n `33` status `ready` deltaP `30.4093` edge `-0.0033` maxDD `-0.0367`
- `risk_on_high->equity_4h` score `1.5847` n `33` status `ready` deltaP `-1.686` edge `0.2574` maxDD `-0.773`
- `risk_on_and_context->equity_4h` score `1.5847` n `33` status `ready` deltaP `-1.686` edge `0.2574` maxDD `-0.773`
- `news_risk_high->fx_1h` score `1.1751` n `51` status `ready` deltaP `16.2469` edge `0.0066` maxDD `-0.0257`
- `market_context_high->crypto_alt_4h` score `1.1469` n `128` status `ready` deltaP `8.9558` edge `0.1823` maxDD `-7.0478`
- `market_context_high->unknown_1h` score `1.1329` n `128` status `ready` deltaP `6.2406` edge `0.0977` maxDD `-1.5916`
- `news_risk_high->equity_1h` score `0.7184` n `51` status `ready` deltaP `16.2469` edge `0.0202` maxDD `-0.9128`
- `risk_on_high->fx_4h` score `0.7158` n `33` status `ready` deltaP `16.6482` edge `0.004` maxDD `-0.1905`
- `risk_on_and_context->fx_4h` score `0.7158` n `33` status `ready` deltaP `16.6482` edge `0.004` maxDD `-0.1905`
- `market_context_high->unknown_4h` score `0.5514` n `128` status `ready` deltaP `20.8841` edge `-0.0761` maxDD `-0.3741`
- `market_context_high->commodity_24h` score `0.5466` n `112` status `ready` deltaP `-1.1657` edge `0.1008` maxDD `-0.7984`
- `news_risk_high->index_4h` score `0.5106` n `51` status `ready` deltaP `9.4333` edge `0.0194` maxDD `-0.1788`
- `risk_on_high->index_4h` score `0.3829` n `33` status `ready` deltaP `8.1856` edge `0.0425` maxDD `-0.1719`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
