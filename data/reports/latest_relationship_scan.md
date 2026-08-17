# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-17T04:37:31.718705+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11865`

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

- `market_context_high->commodity_24h` score `3.585` n `71` status `ready` deltaP `32.7709` edge `0.1279` maxDD `-0.8098`
- `risk_on_high->crypto_major_1h` score `1.7575` n `30` status `ready` deltaP `18.6527` edge `0.0527` maxDD `-1.1144`
- `risk_on_and_context->crypto_major_1h` score `1.7575` n `30` status `ready` deltaP `18.6527` edge `0.0527` maxDD `-1.1144`
- `market_context_high->crypto_major_24h` score `1.6293` n `71` status `ready` deltaP `3.0199` edge `0.2533` maxDD `-5.6792`
- `market_context_high->equity_24h` score `1.5366` n `71` status `ready` deltaP `16.0285` edge `0.0421` maxDD `-0.6726`
- `market_context_high->index_24h` score `1.4709` n `71` status `ready` deltaP `21.7014` edge `-0.0221` maxDD `0.0`
- `market_context_high->commodity_4h` score `0.7198` n `104` status `ready` deltaP `12.6877` edge `0.0564` maxDD `-0.8962`
- `risk_on_high->equity_1h` score `0.4119` n `30` status `ready` deltaP `10.5689` edge `0.0367` maxDD `-1.6811`
- `risk_on_and_context->equity_1h` score `0.4119` n `30` status `ready` deltaP `10.5689` edge `0.0367` maxDD `-1.6811`
- `risk_on_high->index_1h` score `0.3205` n `30` status `ready` deltaP `9.7805` edge `0.0134` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.3205` n `30` status `ready` deltaP `9.7805` edge `0.0134` maxDD `-0.3343`
- `risk_on_high->commodity_1h` score `0.2033` n `30` status `ready` deltaP `4.7206` edge `0.0195` maxDD `-0.3258`
- `risk_on_and_context->commodity_1h` score `0.2033` n `30` status `ready` deltaP `4.7206` edge `0.0195` maxDD `-0.3258`
- `risk_on_high->fx_1h` score `0.1473` n `30` status `ready` deltaP `5.9182` edge `0.0022` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.1473` n `30` status `ready` deltaP `5.9182` edge `0.0022` maxDD `-0.1547`
- `market_context_high->metal_4h` score `-0.1935` n `104` status `ready` deltaP `16.3345` edge `0.0157` maxDD `-4.5909`
- `market_context_high->fx_1h` score `-0.3388` n `114` status `ready` deltaP `-0.7485` edge `-0.0014` maxDD `-0.2968`
- `market_context_high->commodity_1h` score `-0.3565` n `114` status `ready` deltaP `-1.0689` edge `0.0082` maxDD `-1.0756`
- `risk_on_high->crypto_alt_1h` score `-0.4679` n `30` status `ready` deltaP `-1.0479` edge `0.0277` maxDD `-1.7766`
- `risk_on_and_context->crypto_alt_1h` score `-0.4679` n `30` status `ready` deltaP `-1.0479` edge `0.0277` maxDD `-1.7766`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
