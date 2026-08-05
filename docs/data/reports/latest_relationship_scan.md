# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T21:52:33.811902+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11685`

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

- `market_context_high->unknown_24h` score `12.8392` n `90` status `ready` deltaP `4.4445` edge `1.0446` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `2.9165` n `108` status `ready` deltaP `-2.6423` edge `0.3602` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.2722` n `108` status `ready` deltaP `14.6172` edge `0.0932` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.9039` n `90` status `ready` deltaP `2.0139` edge `0.2193` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.8552` n `90` status `ready` deltaP `24.7223` edge `0.0654` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4132` n `109` status `ready` deltaP `7.61` edge `0.0253` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0679` n `109` status `ready` deltaP `6.4316` edge `-0.0022` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.0934` n `108` status `ready` deltaP `9.8125` edge `0.0086` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.4973` n `109` status `ready` deltaP `-1.1111` edge `-0.0069` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.7355` n `108` status `ready` deltaP `3.3706` edge `0.0067` maxDD `-3.211`
- `market_context_high->index_1h` score `-0.8031` n `109` status `ready` deltaP `-4.2548` edge `-0.0212` maxDD `-1.6054`
- `market_context_high->crypto_alt_24h` score `-1.3627` n `90` status `ready` deltaP `0.5555` edge `-0.0341` maxDD `-4.5445`
- `market_context_high->crypto_alt_1h` score `-1.5349` n `109` status `ready` deltaP `-4.9882` edge `-0.0236` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.8907` n `109` status `ready` deltaP `0.6703` edge `-0.0933` maxDD `-10.619`
- `market_context_high->index_24h` score `-2.199` n `90` status `ready` deltaP `-8.6459` edge `-0.0048` maxDD `-7.8922`
- `market_context_high->index_4h` score `-2.2271` n `108` status `ready` deltaP `-14.2333` edge `-0.0652` maxDD `-4.7021`
- `market_context_high->crypto_alt_4h` score `-2.3833` n `108` status `ready` deltaP `0.0564` edge `-0.06` maxDD `-5.7857`
- `market_context_high->crypto_major_1h` score `-3.3703` n `109` status `ready` deltaP `-11.4487` edge `-0.0672` maxDD `-7.6533`
- `market_context_high->unknown_1h` score `-3.64` n `109` status `ready` deltaP `1.2841` edge `-0.2672` maxDD `-1.2421`
- `market_context_high->commodity_24h` score `-6.0922` n `90` status `ready` deltaP `10.1389` edge `-0.0272` maxDD `-51.0493`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
