# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-17T18:32:28.426472+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11835`

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

- `risk_on_high->unknown_1h` score `7.2104` n `35` status `ready` deltaP `1.5204` edge `0.6302` maxDD `-0.8243`
- `risk_on_and_context->unknown_1h` score `7.2104` n `35` status `ready` deltaP `1.5204` edge `0.6302` maxDD `-0.8243`
- `market_context_high->crypto_major_24h` score `4.0232` n `82` status `ready` deltaP `14.258` edge `0.361` maxDD `-4.9964`
- `market_context_high->equity_24h` score `2.3584` n `82` status `ready` deltaP `16.9844` edge `0.0833` maxDD `0.0`
- `market_context_high->index_24h` score `1.2725` n `82` status `ready` deltaP `18.8908` edge `-0.0199` maxDD `0.0`
- `risk_on_high->fx_4h` score `1.1989` n `35` status `ready` deltaP `16.5166` edge `0.0039` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `1.1989` n `35` status `ready` deltaP `16.5166` edge `0.0039` maxDD `-0.1285`
- `risk_on_high->crypto_major_1h` score `0.9235` n `35` status `ready` deltaP `11.1381` edge `0.0333` maxDD `-1.1144`
- `risk_on_and_context->crypto_major_1h` score `0.9235` n `35` status `ready` deltaP `11.1381` edge `0.0333` maxDD `-1.1144`
- `risk_on_high->index_1h` score `0.8103` n `35` status `ready` deltaP `13.88` edge `0.0125` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.8103` n `35` status `ready` deltaP `13.88` edge `0.0125` maxDD `-0.3343`
- `risk_on_high->equity_1h` score `0.7564` n `35` status `ready` deltaP `12.5518` edge `0.0337` maxDD `-1.6811`
- `risk_on_and_context->equity_1h` score `0.7564` n `35` status `ready` deltaP `12.5518` edge `0.0337` maxDD `-1.6811`
- `market_context_high->commodity_4h` score `0.5803` n `133` status `ready` deltaP `12.4638` edge `0.0503` maxDD `-2.4692`
- `risk_on_high->commodity_4h` score `0.4336` n `35` status `ready` deltaP `2.8397` edge `0.0801` maxDD `-1.3651`
- `risk_on_and_context->commodity_4h` score `0.4336` n `35` status `ready` deltaP `2.8397` edge `0.0801` maxDD `-1.3651`
- `market_context_high->commodity_24h` score `0.1481` n `82` status `ready` deltaP `16.2616` edge `0.0939` maxDD `-4.666`
- `risk_on_high->fx_1h` score `0.0904` n `35` status `ready` deltaP `4.8089` edge `0.0023` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.0904` n `35` status `ready` deltaP `4.8089` edge `0.0023` maxDD `-0.1547`
- `risk_on_high->crypto_major_4h` score `-0.0361` n `35` status `ready` deltaP `1.0132` edge `0.0598` maxDD `-2.0278`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
