# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T08:37:26.523439+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6489`

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

- `market_context_high->unknown_24h` score `7032.8349` n `55` status `ready` deltaP `4.1667` edge `586.0418` maxDD `0.0`
- `market_context_high->unknown_4h` score `374.4303` n `55` status `ready` deltaP `5.3464` edge `31.1712` maxDD `-0.0124`
- `news_risk_high->unknown_1h` score `69.5278` n `114` status `ready` deltaP `-4.948` edge `5.8556` maxDD `-0.9571`
- `market_context_high->unknown_1h` score `57.6628` n `55` status `ready` deltaP `2.564` edge `4.7992` maxDD `-0.2178`
- `market_context_high->equity_24h` score `21.5615` n `55` status `ready` deltaP `45.404` edge `1.5177` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `12.8804` n `98` status `ready` deltaP `29.6379` edge `1.0114` maxDD `-6.8493`
- `market_context_high->index_24h` score `7.2033` n `55` status `ready` deltaP `59.2014` edge `0.2056` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.6623` n `55` status `ready` deltaP `46.1364` edge `0.2787` maxDD `-0.8203`
- `market_context_high->crypto_alt_4h` score `5.6517` n `55` status `ready` deltaP `22.5305` edge `0.3502` maxDD `-1.6876`
- `market_context_high->crypto_major_4h` score `5.3821` n `55` status `ready` deltaP `29.8254` edge `0.2833` maxDD `-1.6901`
- `news_risk_high->crypto_alt_4h` score `4.7367` n `108` status `ready` deltaP `17.5305` edge `0.4165` maxDD `-7.4246`
- `market_context_high->commodity_4h` score `3.3975` n `55` status `ready` deltaP `31.8293` edge `0.096` maxDD `-0.3387`
- `market_context_high->equity_4h` score `3.3042` n `55` status `ready` deltaP `5.4379` edge `0.3093` maxDD `-2.283`
- `market_context_high->crypto_major_24h` score `2.4853` n `55` status `ready` deltaP `10.8586` edge `0.3139` maxDD `-3.0799`
- `market_context_high->crypto_alt_24h` score `1.7968` n `55` status `ready` deltaP `-5.1673` edge `0.4166` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.551` n `55` status `ready` deltaP `18.3508` edge `0.0494` maxDD `-0.7323`
- `market_context_high->equity_1h` score `1.4063` n `55` status `ready` deltaP `1.8291` edge `0.1575` maxDD `-1.5336`
- `market_context_high->crypto_major_1h` score `1.3532` n `55` status `ready` deltaP `7.8824` edge `0.1212` maxDD `-2.2118`
- `market_context_high->crypto_alt_1h` score `1.272` n `55` status `ready` deltaP `3.4758` edge `0.1499` maxDD `-2.3659`
- `market_context_high->metal_1h` score `0.86` n `55` status `ready` deltaP `10.7267` edge `0.025` maxDD `-0.3209`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
