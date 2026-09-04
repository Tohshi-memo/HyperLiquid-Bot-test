# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T10:07:26.637944+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11484`

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

- `risk_on_high->unknown_4h` score `20.4261` n `133` status `ready` deltaP `8.2363` edge `1.7091` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `20.4261` n `133` status `ready` deltaP `8.2363` edge `1.7091` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `13.0034` n `185` status `ready` deltaP `10.7927` edge `1.0812` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `12.1568` n `133` status `ready` deltaP `-1.0536` edge `1.0778` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `12.1568` n `133` status `ready` deltaP `-1.0536` edge `1.0778` maxDD `-1.95`
- `market_context_high->unknown_1h` score `9.6017` n `197` status `ready` deltaP `0.0304` edge `0.863` maxDD `-2.0446`
- `market_context_high->equity_24h` score `1.8108` n `167` status `ready` deltaP `16.6303` edge `0.4746` maxDD `-20.7654`
- `news_risk_high->commodity_4h` score `1.3652` n `61` status `ready` deltaP `11.4979` edge `0.0572` maxDD `-0.2737`
- `news_risk_high->commodity_24h` score `0.5845` n `61` status `ready` deltaP `8.9538` edge `0.0063` maxDD `-0.0495`
- `risk_on_high->equity_24h` score `0.3582` n `133` status `ready` deltaP `11.2456` edge `0.3694` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `0.3582` n `133` status `ready` deltaP `11.2456` edge `0.3694` maxDD `-19.828`
- `risk_on_high->metal_1h` score `0.1498` n `133` status `ready` deltaP `12.8619` edge `0.0047` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.1498` n `133` status `ready` deltaP `12.8619` edge `0.0047` maxDD `-1.699`
- `news_risk_high->index_1h` score `-0.0431` n `61` status `ready` deltaP `4.9818` edge `-0.0034` maxDD `-0.8275`
- `news_risk_high->commodity_1h` score `-0.0621` n `61` status `ready` deltaP `5.5586` edge `0.0024` maxDD `-0.9036`
- `news_risk_high->crypto_alt_24h` score `-0.1268` n `61` status `ready` deltaP `14.4723` edge `0.0042` maxDD `-7.3552`
- `risk_on_high->index_1h` score `-0.1948` n `133` status `ready` deltaP `3.2439` edge `-0.0021` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.1948` n `133` status `ready` deltaP `3.2439` edge `-0.0021` maxDD `-0.5605`
- `market_context_high->metal_1h` score `-0.3608` n `197` status `ready` deltaP `5.8049` edge `0.0007` maxDD `-2.1858`
- `risk_on_high->crypto_alt_1h` score `-0.3697` n `133` status `ready` deltaP `4.0025` edge `0.0442` maxDD `-5.4685`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
