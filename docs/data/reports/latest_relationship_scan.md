# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T16:22:26.272976+00:00`
- Price records: `672`
- Market context records: `7046`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11502`

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

- `market_context_high->fx_4h` score `0.2183` n `201` status `ready` deltaP `14.1541` edge `0.0105` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.3098` n `201` status `ready` deltaP `2.6395` edge `0.0017` maxDD `-0.276`
- `market_context_high->crypto_alt_1h` score `-0.3296` n `201` status `ready` deltaP `1.5871` edge `0.0336` maxDD `-4.5815`
- `market_context_high->crypto_major_1h` score `-0.5859` n `201` status `ready` deltaP `3.8282` edge `0.0346` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-0.7298` n `201` status `ready` deltaP `-2.644` edge `-0.0143` maxDD `-1.9306`
- `market_context_high->index_1h` score `-0.7656` n `201` status `ready` deltaP `-0.68` edge `-0.0025` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.8142` n `201` status `ready` deltaP `-3.8103` edge `-0.0022` maxDD `-2.1427`
- `market_context_high->unknown_1h` score `-0.9158` n `201` status `ready` deltaP `-2.3312` edge `0.0134` maxDD `-2.2673`
- `market_context_high->unknown_4h` score `-1.5227` n `201` status `ready` deltaP `-5.8837` edge `0.0985` maxDD `-6.5601`
- `market_context_high->equity_1h` score `-1.8394` n `201` status `ready` deltaP `4.0441` edge `-0.0205` maxDD `-14.716`
- `market_context_high->metal_4h` score `-2.0895` n `201` status `ready` deltaP `3.6964` edge `0.0058` maxDD `-5.5324`
- `market_context_high->index_4h` score `-2.0997` n `201` status `ready` deltaP `3.7063` edge `-0.024` maxDD `-12.2591`
- `market_context_high->commodity_4h` score `-2.1709` n `201` status `ready` deltaP `-4.5406` edge `-0.0346` maxDD `-2.9494`
- `market_context_high->commodity_24h` score `-2.1913` n `200` status `ready` deltaP `-0.2292` edge `-0.0502` maxDD `-4.4704`
- `market_context_high->crypto_alt_4h` score `-2.5241` n `201` status `ready` deltaP `3.1853` edge `0.0337` maxDD `-22.2831`
- `market_context_high->crypto_major_4h` score `-2.7398` n `201` status `ready` deltaP `4.7984` edge `0.0452` maxDD `-24.6094`
- `market_context_high->unknown_24h` score `-2.7993` n `200` status `ready` deltaP `-11.5347` edge `0.23` maxDD `-23.2919`
- `market_context_high->fx_24h` score `-3.5636` n `200` status `ready` deltaP `-0.6528` edge `-0.0099` maxDD `-3.9503`
- `market_context_high->equity_4h` score `-7.5064` n `201` status `ready` deltaP `3.971` edge `-0.1018` maxDD `-63.963`
- `market_context_high->metal_24h` score `-14.9273` n `200` status `ready` deltaP `-16.4236` edge `-0.0765` maxDD `-44.303`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
