# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T22:07:31.269246+00:00`
- Price records: `672`
- Market context records: `4030`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10624`

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

- `risk_on_high->unknown_4h` score `145.8596` n `40` status `ready` deltaP `-6.5244` edge `12.3801` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `145.8596` n `40` status `ready` deltaP `-6.5244` edge `12.3801` maxDD `-10.864`
- `market_context_high->unknown_24h` score `47.2177` n `134` status `ready` deltaP `-6.1991` edge `4.379` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `25.5255` n `148` status `ready` deltaP `1.5161` edge `2.6593` maxDD `-35.7161`
- `risk_on_high->equity_24h` score `5.3892` n `40` status `ready` deltaP `36.9151` edge `0.203` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `5.3892` n `40` status `ready` deltaP `36.9151` edge `0.203` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.1881` n `40` status `ready` deltaP `35.6098` edge `0.033` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `3.1881` n `40` status `ready` deltaP `35.6098` edge `0.033` maxDD `-0.0446`
- `market_context_high->index_24h` score `3.0047` n `134` status `ready` deltaP `23.8638` edge `0.1125` maxDD `-1.3629`
- `market_context_high->equity_4h` score `2.049` n `148` status `ready` deltaP `18.5152` edge `0.1754` maxDD `-6.9137`
- `market_context_high->metal_24h` score `1.8038` n `134` status `ready` deltaP `12.0477` edge `0.1687` maxDD `-4.8962`
- `market_context_high->equity_1h` score `1.1471` n `156` status `ready` deltaP `8.199` edge `0.0969` maxDD `-2.144`
- `risk_on_high->crypto_major_4h` score `0.9353` n `40` status `ready` deltaP `18.689` edge `0.0199` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.9353` n `40` status `ready` deltaP `18.689` edge `0.0199` maxDD `-2.6576`
- `risk_on_high->commodity_24h` score `0.7278` n `40` status `ready` deltaP `3.5095` edge `0.2654` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `0.7278` n `40` status `ready` deltaP `3.5095` edge `0.2654` maxDD `-12.9187`
- `risk_on_high->index_24h` score `0.5624` n `40` status `ready` deltaP `24.6101` edge `-0.1172` maxDD `0.0`
- `risk_on_and_context->index_24h` score `0.5624` n `40` status `ready` deltaP `24.6101` edge `-0.1172` maxDD `0.0`
- `market_context_high->crypto_major_1h` score `0.5046` n `156` status `ready` deltaP `7.5196` edge `0.0529` maxDD `-2.8785`
- `market_context_high->metal_1h` score `0.3992` n `156` status `ready` deltaP `9.6806` edge `0.0492` maxDD `-3.0049`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
