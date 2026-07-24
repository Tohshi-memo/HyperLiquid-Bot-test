# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T17:16:38.932266+00:00`
- Price records: `672`
- Market context records: `7794`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14661`

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

- `market_context_high->equity_24h` score `7.9446` n `132` status `ready` deltaP `28.5507` edge `0.6059` maxDD `-6.0681`
- `market_context_high->metal_24h` score `1.4921` n `133` status `ready` deltaP `14.0577` edge `0.2397` maxDD `-2.3927`
- `market_context_high->crypto_major_4h` score `1.2398` n `133` status `ready` deltaP `15.033` edge `0.1749` maxDD `-6.7444`
- `market_context_high->equity_4h` score `1.1936` n `133` status `ready` deltaP `4.1887` edge `0.3164` maxDD `-6.9701`
- `market_context_high->crypto_major_1h` score `1.0981` n `133` status `ready` deltaP `13.4573` edge `0.0459` maxDD `-1.5286`
- `market_context_high->crypto_alt_4h` score `0.9761` n `133` status `ready` deltaP `9.1885` edge `0.1318` maxDD `-3.9374`
- `market_context_high->fx_24h` score `0.8125` n `132` status `ready` deltaP `25.2187` edge `0.0448` maxDD `-3.0343`
- `market_context_high->equity_1h` score `0.7394` n `133` status `ready` deltaP `8.046` edge `0.0939` maxDD `-4.2072`
- `market_context_high->commodity_4h` score `0.4018` n `133` status `ready` deltaP `7.9401` edge `0.0399` maxDD `-1.0817`
- `market_context_high->index_1h` score `0.3878` n `133` status `ready` deltaP `8.7946` edge `0.0167` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.2659` n `133` status `ready` deltaP `4.8771` edge `0.0329` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `0.0605` n `133` status `ready` deltaP `5.647` edge `0.0133` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.1148` n `133` status `ready` deltaP `12.1655` edge `0.05` maxDD `-1.3325`
- `market_context_high->commodity_24h` score `-0.2827` n `132` status `ready` deltaP `12.253` edge `0.0531` maxDD `-7.0012`
- `market_context_high->fx_1h` score `-0.321` n `133` status `ready` deltaP `1.7251` edge `0.0005` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.883` n `133` status `ready` deltaP `1.1177` edge `0.0193` maxDD `-0.6936`
- `market_context_high->fx_4h` score `-1.3303` n `133` status `ready` deltaP `-1.5014` edge `0.0023` maxDD `-1.6936`
- `market_context_high->metal_4h` score `-1.5523` n `133` status `ready` deltaP `0.2998` edge `0.0741` maxDD `-1.4368`
- `market_context_high->index_24h` score `-1.6506` n `132` status `ready` deltaP `-9.4875` edge `0.0619` maxDD `-2.1544`
- `market_context_high->crypto_alt_24h` score `-2.3115` n `133` status `ready` deltaP `14.7431` edge `0.1349` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
