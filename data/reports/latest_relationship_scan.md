# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T00:52:29.607470+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9488`

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

- `market_context_high->unknown_24h` score `1206.8112` n `43` status `ready` deltaP `-20.8252` edge `100.7428` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `39.6206` n `108` status `ready` deltaP `-8.689` edge `3.4302` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.1796` n `43` status `ready` deltaP `29.2434` edge `0.6129` maxDD `-1.0977`
- `market_context_high->index_24h` score `6.358` n `43` status `ready` deltaP `52.4306` edge `0.1803` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `2.978` n `43` status `ready` deltaP `-15.1809` edge `0.6642` maxDD `-17.8526`
- `market_context_high->fx_24h` score `2.3818` n `43` status `ready` deltaP `27.1923` edge `0.0305` maxDD `-0.0641`
- `risk_on_high->crypto_alt_1h` score `2.0518` n `41` status `ready` deltaP `13.652` edge `0.1355` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `2.0518` n `41` status `ready` deltaP `13.652` edge `0.1355` maxDD `-2.4421`
- `market_context_high->unknown_1h` score `1.6639` n `120` status `ready` deltaP `-3.5728` edge `0.1961` maxDD `-1.0231`
- `risk_on_high->crypto_major_1h` score `1.4273` n `41` status `ready` deltaP `13.1152` edge `0.0968` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `1.4273` n `41` status `ready` deltaP `13.1152` edge `0.0968` maxDD `-3.2233`
- `risk_on_high->metal_1h` score `1.2896` n `41` status `ready` deltaP `15.8975` edge `0.0254` maxDD `-0.2466`
- `risk_on_and_context->metal_1h` score `1.2896` n `41` status `ready` deltaP `15.8975` edge `0.0254` maxDD `-0.2466`
- `risk_on_high->equity_1h` score `0.3691` n `41` status `ready` deltaP `2.5486` edge `0.0383` maxDD `-0.296`
- `risk_on_and_context->equity_1h` score `0.3691` n `41` status `ready` deltaP `2.5486` edge `0.0383` maxDD `-0.296`
- `market_context_high->crypto_alt_1h` score `0.24` n `120` status `ready` deltaP `6.1926` edge `0.0929` maxDD `-4.9401`
- `market_context_high->metal_4h` score `0.1322` n `108` status `ready` deltaP `9.1181` edge `0.0225` maxDD `-1.1153`
- `market_context_high->crypto_major_4h` score `0.0058` n `108` status `ready` deltaP `3.331` edge `0.1891` maxDD `-11.1784`
- `market_context_high->commodity_4h` score `-0.0464` n `108` status `ready` deltaP `8.9148` edge `-0.0042` maxDD `-2.2274`
- `market_context_high->crypto_major_1h` score `-0.0668` n `120` status `ready` deltaP `3.0339` edge `0.0601` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
