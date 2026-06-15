# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T20:22:32.961687+00:00`
- Price records: `672`
- Market context records: `4023`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10720`

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

- `risk_on_high->unknown_4h` score `146.0488` n `40` status `ready` deltaP `-5.9146` edge `12.3918` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `146.0488` n `40` status `ready` deltaP `-5.9146` edge `12.3918` maxDD `-10.864`
- `market_context_high->unknown_24h` score `47.9532` n `134` status `ready` deltaP `-4.9859` edge `4.4322` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `25.7147` n `148` status `ready` deltaP `2.1259` edge `2.671` maxDD `-35.7161`
- `risk_on_high->equity_24h` score `6.1091` n `40` status `ready` deltaP `38.1282` edge `0.2549` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `6.1091` n `40` status `ready` deltaP `38.1282` edge `0.2549` maxDD `0.0`
- `market_context_high->index_24h` score `3.3909` n `134` status `ready` deltaP `25.0769` edge `0.1366` maxDD `-1.3629`
- `risk_on_high->equity_4h` score `3.2471` n `40` status `ready` deltaP `35.7622` edge `0.0369` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `3.2471` n `40` status `ready` deltaP `35.7622` edge `0.0369` maxDD `-0.0446`
- `market_context_high->metal_24h` score `2.3034` n `134` status `ready` deltaP `13.0875` edge `0.2034` maxDD `-4.8962`
- `market_context_high->equity_4h` score `2.108` n `148` status `ready` deltaP `18.6676` edge `0.1793` maxDD `-6.9137`
- `market_context_high->equity_1h` score `1.1787` n `153` status `ready` deltaP `8.1739` edge `0.0997` maxDD `-2.144`
- `risk_on_high->crypto_major_4h` score `1.0217` n `40` status `ready` deltaP `18.689` edge `0.0271` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.0217` n `40` status `ready` deltaP `18.689` edge `0.0271` maxDD `-2.6576`
- `risk_on_high->index_24h` score `0.9487` n `40` status `ready` deltaP `25.8232` edge `-0.0931` maxDD `0.0`
- `risk_on_and_context->index_24h` score `0.9487` n `40` status `ready` deltaP `25.8232` edge `-0.0931` maxDD `0.0`
- `risk_on_high->commodity_24h` score `0.92` n `40` status `ready` deltaP `4.2028` edge `0.2768` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `0.92` n `40` status `ready` deltaP `4.2028` edge `0.2768` maxDD `-12.9187`
- `market_context_high->crypto_major_1h` score `0.6794` n `153` status `ready` deltaP `8.2394` edge `0.0559` maxDD `-2.3372`
- `market_context_high->metal_1h` score `0.5225` n `153` status `ready` deltaP `10.6747` edge `0.0523` maxDD `-2.5182`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
