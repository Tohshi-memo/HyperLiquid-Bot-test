# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T10:09:37.093071+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14760`

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

- `news_risk_high->unknown_4h` score `14.6672` n `51` status `ready` deltaP `26.5453` edge `1.0499` maxDD `-0.0347`
- `risk_on_high->unknown_1h` score `4.9984` n `33` status `ready` deltaP `-8.0294` edge `0.7392` maxDD `-1.5876`
- `risk_on_and_context->unknown_1h` score `4.9984` n `33` status `ready` deltaP `-8.0294` edge `0.7392` maxDD `-1.5876`
- `news_risk_high->unknown_1h` score `3.7275` n `51` status `ready` deltaP `19.778` edge `0.2092` maxDD `-0.7674`
- `news_risk_high->fx_4h` score `2.8476` n `51` status `ready` deltaP `33.8146` edge `0.0253` maxDD `-0.0746`
- `news_risk_high->equity_4h` score `2.8445` n `51` status `ready` deltaP `24.0316` edge `0.1541` maxDD `-2.1818`
- `risk_on_high->metal_4h` score `2.4058` n `33` status `ready` deltaP `31.7812` edge `-0.0026` maxDD `-0.0367`
- `risk_on_and_context->metal_4h` score `2.4058` n `33` status `ready` deltaP `31.7812` edge `-0.0026` maxDD `-0.0367`
- `risk_on_high->equity_4h` score `1.6861` n `33` status `ready` deltaP `-0.9238` edge `0.2654` maxDD `-0.7794`
- `risk_on_and_context->equity_4h` score `1.6861` n `33` status `ready` deltaP `-0.9238` edge `0.2654` maxDD `-0.7794`
- `market_context_high->unknown_1h` score `1.4585` n `128` status `ready` deltaP `7.7376` edge `0.1148` maxDD `-1.5876`
- `news_risk_high->fx_1h` score `1.1751` n `51` status `ready` deltaP `16.2469` edge `0.0066` maxDD `-0.0257`
- `market_context_high->unknown_4h` score `1.1329` n `123` status `ready` deltaP `22.002` edge `-0.0351` maxDD `-0.3736`
- `market_context_high->commodity_24h` score `1.1149` n `106` status `ready` deltaP `2.3356` edge `0.1204` maxDD `-0.778`
- `market_context_high->crypto_alt_4h` score `0.9365` n `123` status `ready` deltaP `8.3333` edge `0.1693` maxDD `-7.0785`
- `news_risk_high->equity_1h` score `0.8025` n `51` status `ready` deltaP `17.5942` edge `0.0221` maxDD `-0.9204`
- `news_risk_high->index_4h` score `0.6812` n `51` status `ready` deltaP `11.415` edge `0.0204` maxDD `-0.1788`
- `risk_on_high->fx_4h` score `0.6375` n `33` status `ready` deltaP `15.2763` edge `0.0031` maxDD `-0.1905`
- `risk_on_and_context->fx_4h` score `0.6375` n `33` status `ready` deltaP `15.2763` edge `0.0031` maxDD `-0.1905`
- `risk_on_high->unknown_4h` score `0.5141` n `33` status `ready` deltaP `28.5061` edge `-0.1472` maxDD `0.0`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
