# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T06:52:19.524540+00:00`
- Price records: `672`
- Market context records: `1195`
- Flow alert records: `5347`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8768`

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

- `market_context_high->crypto_major_24h` score `18.5143` n `136` status `ready` deltaP `44.3321` edge `1.3605` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `7.6008` n `136` status `ready` deltaP `22.0997` edge `0.6877` maxDD `-15.1306`
- `market_context_high->unknown_4h` score `5.0065` n `136` status `ready` deltaP `4.1338` edge `0.5113` maxDD `-6.7322`
- `market_context_high->metal_24h` score `4.2282` n `136` status `ready` deltaP `-4.085` edge `0.5463` maxDD `-6.3373`
- `market_context_high->equity_4h` score `2.8239` n `136` status `ready` deltaP `15.0377` edge `0.2014` maxDD `-3.6396`
- `market_context_high->commodity_24h` score `2.1676` n `136` status `ready` deltaP `-3.605` edge `0.556` maxDD `-23.1066`
- `market_context_high->index_24h` score `2.0763` n `136` status `ready` deltaP `16.2684` edge `0.1732` maxDD `-5.3574`
- `market_context_high->equity_24h` score `1.5361` n `136` status `ready` deltaP `16.5339` edge `0.3194` maxDD `-14.2815`
- `market_context_high->index_4h` score `0.9622` n `136` status `ready` deltaP `10.5272` edge `0.0783` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.5262` n `136` status `ready` deltaP `8.5857` edge `0.0183` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.403` n `136` status `ready` deltaP `3.9978` edge `0.0447` maxDD `-1.3546`
- `market_context_high->fx_24h` score `0.1952` n `136` status `ready` deltaP `8.364` edge `0.0498` maxDD `-3.8101`
- `market_context_high->unknown_24h` score `0.0638` n `136` status `ready` deltaP `2.0527` edge `0.2646` maxDD `-10.1706`
- `market_context_high->crypto_major_4h` score `-0.0537` n `136` status `ready` deltaP `7.1288` edge `0.1377` maxDD `-8.3693`
- `market_context_high->fx_1h` score `-0.2064` n `136` status `ready` deltaP `4.3457` edge `-0.0006` maxDD `-0.3124`
- `market_context_high->metal_1h` score `-0.2798` n `136` status `ready` deltaP `7.6832` edge `-0.0135` maxDD `-2.2164`
- `market_context_high->crypto_major_1h` score `-0.2967` n `136` status `ready` deltaP `3.9495` edge `0.0122` maxDD `-4.1256`
- `market_context_high->crypto_alt_1h` score `-0.4055` n `136` status `ready` deltaP `0.3435` edge `0.03` maxDD `-3.4088`
- `market_context_high->commodity_1h` score `-0.8698` n `136` status `ready` deltaP `-2.9544` edge `0.0087` maxDD `-2.252`
- `market_context_high->metal_4h` score `-1.0533` n `136` status `ready` deltaP `7.613` edge `-0.0427` maxDD `-6.4478`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
