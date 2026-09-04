# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T02:07:26.372696+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11538`

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

- `risk_on_high->unknown_4h` score `22.8191` n `133` status `ready` deltaP `10.218` edge `1.8953` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `22.8191` n `133` status `ready` deltaP `10.218` edge `1.8953` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `16.0541` n `167` status `ready` deltaP `11.8163` edge `1.3286` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `14.0478` n `133` status `ready` deltaP `-0.0057` edge `1.2284` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `14.0478` n `133` status `ready` deltaP `-0.0057` edge `1.2284` maxDD `-1.95`
- `market_context_high->unknown_1h` score `9.568` n `167` status `ready` deltaP `0.4491` edge `0.8574` maxDD `-2.0446`
- `market_context_high->equity_24h` score `0.7187` n `136` status `ready` deltaP `16.0437` edge `0.3875` maxDD `-20.7654`
- `news_risk_high->commodity_4h` score `0.3208` n `67` status `ready` deltaP `5.9474` edge `0.0374` maxDD `-0.8733`
- `risk_on_high->equity_24h` score `0.1952` n `114` status `ready` deltaP `11.4126` edge `0.3547` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `0.1952` n `114` status `ready` deltaP `11.4126` edge `0.3547` maxDD `-19.828`
- `risk_on_high->metal_1h` score `0.0673` n `133` status `ready` deltaP `11.814` edge `0.0011` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0673` n `133` status `ready` deltaP `11.814` edge `0.0011` maxDD `-1.699`
- `news_risk_high->index_1h` score `-0.0407` n `67` status `ready` deltaP `4.9245` edge `-0.0027` maxDD `-0.8275`
- `risk_on_high->index_1h` score `-0.0788` n `133` status `ready` deltaP `5.3397` edge `-0.0012` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.0788` n `133` status `ready` deltaP `5.3397` edge `-0.0012` maxDD `-0.5605`
- `news_risk_high->commodity_24h` score `-0.175` n `67` status `ready` deltaP `4.4517` edge `-0.025` maxDD `-0.2074`
- `risk_on_high->crypto_alt_1h` score `-0.2078` n `133` status `ready` deltaP `4.9007` edge `0.0517` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.2078` n `133` status `ready` deltaP `4.9007` edge `0.0517` maxDD `-5.4685`
- `news_risk_high->commodity_1h` score `-0.2125` n `67` status `ready` deltaP `4.0084` edge `0.0002` maxDD `-0.9036`
- `news_risk_high->fx_4h` score `-0.2196` n `67` status `ready` deltaP `6.7551` edge `0.0023` maxDD `-1.2507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
