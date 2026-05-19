# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T00:07:13.676352+00:00`
- Price records: `672`
- Market context records: `1168`
- Flow alert records: `5264`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8750`

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

- `market_context_high->crypto_major_24h` score `20.9781` n `137` status `ready` deltaP `45.865` edge `1.5556` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `10.0873` n `137` status `ready` deltaP `22.1158` edge `0.8948` maxDD `-15.1306`
- `market_context_high->equity_24h` score `7.7349` n `137` status `ready` deltaP `21.9421` edge `0.5913` maxDD `-6.4404`
- `market_context_high->index_24h` score `5.7449` n `137` status `ready` deltaP `20.5533` edge `0.3975` maxDD `-3.4627`
- `market_context_high->metal_24h` score `5.4863` n `137` status `ready` deltaP `-3.9133` edge `0.65` maxDD `-6.3373`
- `market_context_high->equity_4h` score `2.5157` n `153` status `ready` deltaP `12.8657` edge `0.1902` maxDD `-3.6396`
- `market_context_high->unknown_24h` score `1.3527` n `137` status `ready` deltaP `2.3533` edge `0.37` maxDD `-10.1706`
- `market_context_high->index_4h` score `1.1782` n `153` status `ready` deltaP `9.3575` edge `0.1041` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.5343` n `153` status `ready` deltaP `8.028` edge `0.0227` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.2907` n `153` status `ready` deltaP `2.9089` edge `0.0426` maxDD `-1.3546`
- `market_context_high->fx_1h` score `0.1534` n `153` status `ready` deltaP `8.6484` edge `0.0007` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `0.1049` n `153` status `ready` deltaP `8.1699` edge `0.1511` maxDD `-8.3693`
- `market_context_high->crypto_major_1h` score `-0.0202` n `153` status `ready` deltaP `6.6729` edge `0.0295` maxDD `-4.1256`
- `market_context_high->unknown_4h` score `-0.148` n `153` status `ready` deltaP `5.8833` edge `0.0701` maxDD `-6.7322`
- `market_context_high->crypto_alt_1h` score `-0.45` n `153` status `ready` deltaP `2.1271` edge `0.0326` maxDD `-3.4088`
- `market_context_high->metal_1h` score `-0.5005` n `153` status `ready` deltaP `5.3149` edge `-0.0161` maxDD `-2.2164`
- `market_context_high->commodity_1h` score `-0.8116` n `153` status `ready` deltaP `-2.996` edge `-0.0033` maxDD `-3.7959`
- `market_context_high->fx_4h` score `-1.0173` n `153` status `ready` deltaP `-3.8976` edge `-0.0048` maxDD `-1.6381`
- `market_context_high->crypto_alt_4h` score `-1.3142` n `153` status `ready` deltaP `3.795` edge `0.1027` maxDD `-16.7194`
- `market_context_high->metal_4h` score `-1.9326` n `153` status `ready` deltaP `4.5802` edge `-0.0829` maxDD `-9.2991`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
