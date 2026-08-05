# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T16:07:53.256090+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11668`

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

- `market_context_high->unknown_24h` score `13.369` n `90` status `ready` deltaP `6.7014` edge `1.0737` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `4.5121` n `98` status `ready` deltaP `1.2226` edge `0.4674` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.5485` n `98` status `ready` deltaP `16.3608` edge `0.1046` maxDD `-2.7703`
- `market_context_high->fx_24h` score `0.995` n `90` status `ready` deltaP `25.4167` edge `0.0787` maxDD `-4.3126`
- `market_context_high->metal_24h` score `0.9312` n `90` status `ready` deltaP `2.0139` edge `0.2228` maxDD `-2.6802`
- `market_context_high->commodity_1h` score `0.4864` n `102` status `ready` deltaP `8.0603` edge `0.0284` maxDD `-1.3282`
- `market_context_high->fx_1h` score `-0.012` n `102` status `ready` deltaP `5.5976` edge `-0.0033` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.0466` n `98` status `ready` deltaP `10.9539` edge `0.007` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5886` n `102` status `ready` deltaP `-2.5977` edge `-0.0087` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.7392` n `102` status `ready` deltaP `-3.0996` edge `-0.0207` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.8435` n `98` status `ready` deltaP `1.879` edge `0.0028` maxDD `-3.211`
- `market_context_high->crypto_alt_24h` score `-1.407` n `90` status `ready` deltaP `0.9027` edge `-0.0421` maxDD `-4.5445`
- `market_context_high->crypto_alt_1h` score `-1.6203` n `102` status `ready` deltaP `-5.7855` edge `-0.0254` maxDD `-3.0178`
- `market_context_high->crypto_alt_4h` score `-1.6983` n `98` status `ready` deltaP `-2.1808` edge `-0.0642` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.8156` n `102` status `ready` deltaP `2.2661` edge `-0.0943` maxDD `-10.619`
- `market_context_high->index_4h` score `-1.989` n `98` status `ready` deltaP `-10.8232` edge `-0.0574` maxDD `-4.7021`
- `market_context_high->index_24h` score `-2.5615` n `90` status `ready` deltaP `-11.5973` edge `-0.0316` maxDD `-7.8922`
- `market_context_high->unknown_1h` score `-3.2365` n `102` status `ready` deltaP `4.4675` edge `-0.2548` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.5802` n `102` status `ready` deltaP `-12.8126` edge `-0.0756` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.0323` n `90` status `ready` deltaP `11.007` edge `-0.0253` maxDD `-51.0493`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
