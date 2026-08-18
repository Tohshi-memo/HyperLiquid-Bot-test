# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T01:22:24.838341+00:00`
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

- `risk_on_high->unknown_1h` score `9.0499` n `32` status `ready` deltaP `4.0045` edge `0.7556` maxDD `-0.5845`
- `risk_on_and_context->unknown_1h` score `9.0499` n `32` status `ready` deltaP `4.0045` edge `0.7556` maxDD `-0.5845`
- `market_context_high->crypto_major_24h` score `5.1704` n `73` status `ready` deltaP `18.0836` edge `0.4311` maxDD `-4.9964`
- `market_context_high->equity_24h` score `2.5444` n `73` status `ready` deltaP `16.9844` edge `0.0988` maxDD `0.0`
- `risk_on_high->fx_4h` score `1.7212` n `32` status `ready` deltaP `22.2561` edge `0.0078` maxDD `-0.0192`
- `risk_on_and_context->fx_4h` score `1.7212` n `32` status `ready` deltaP `22.2561` edge `0.0078` maxDD `-0.0192`
- `market_context_high->index_24h` score `1.0622` n `73` status `ready` deltaP `17.6942` edge `-0.0251` maxDD `-0.0141`
- `risk_on_high->fx_1h` score `0.6623` n `32` status `ready` deltaP `10.4229` edge `0.0075` maxDD `-0.0771`
- `risk_on_and_context->fx_1h` score `0.6623` n `32` status `ready` deltaP `10.4229` edge `0.0075` maxDD `-0.0771`
- `risk_on_high->index_1h` score `0.5374` n `32` status `ready` deltaP `11.5644` edge `0.0052` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.5374` n `32` status `ready` deltaP `11.5644` edge `0.0052` maxDD `-0.3343`
- `risk_on_high->crypto_major_1h` score `0.5367` n `32` status `ready` deltaP `7.7283` edge `0.0238` maxDD `-1.1144`
- `risk_on_and_context->crypto_major_1h` score `0.5367` n `32` status `ready` deltaP `7.7283` edge `0.0238` maxDD `-1.1144`
- `market_context_high->commodity_4h` score `0.5249` n `114` status `ready` deltaP `11.7111` edge `0.0507` maxDD `-2.4692`
- `risk_on_high->commodity_4h` score `0.4685` n `32` status `ready` deltaP `6.1738` edge `0.0818` maxDD `-1.3651`
- `risk_on_and_context->commodity_4h` score `0.4685` n `32` status `ready` deltaP `6.1738` edge `0.0818` maxDD `-1.3651`
- `market_context_high->commodity_24h` score `0.2015` n `73` status `ready` deltaP `12.6469` edge `0.1158` maxDD `-4.666`
- `risk_on_high->equity_1h` score `0.1926` n `32` status `ready` deltaP `9.4499` edge `0.0074` maxDD `-1.6811`
- `risk_on_and_context->equity_1h` score `0.1926` n `32` status `ready` deltaP `9.4499` edge `0.0074` maxDD `-1.6811`
- `market_context_high->index_1h` score `0.1564` n `114` status `ready` deltaP `7.7267` edge `0.0035` maxDD `-0.3584`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
