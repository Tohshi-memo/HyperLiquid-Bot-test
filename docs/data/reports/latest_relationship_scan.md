# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T19:07:28.440993+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11684`

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

- `market_context_high->unknown_24h` score `13.0086` n `90` status `ready` deltaP `4.7917` edge `1.0564` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `3.7246` n `102` status `ready` deltaP `-0.4304` edge `0.4128` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.4853` n `102` status `ready` deltaP `16.1854` edge `0.1005` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.9281` n `90` status `ready` deltaP `2.0139` edge `0.2224` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.9067` n `90` status `ready` deltaP `24.7223` edge `0.072` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4036` n `109` status `ready` deltaP `7.4603` edge `0.0255` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0176` n `109` status `ready` deltaP `5.8328` edge `-0.0024` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.014` n `102` status `ready` deltaP `11.3702` edge `0.0084` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5019` n `109` status `ready` deltaP `-1.2608` edge `-0.0065` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.7496` n `102` status `ready` deltaP `3.0548` edge `0.007` maxDD `-3.211`
- `market_context_high->index_1h` score `-0.7914` n `109` status `ready` deltaP `-4.2548` edge `-0.0197` maxDD `-1.6054`
- `market_context_high->crypto_alt_24h` score `-1.475` n `90` status `ready` deltaP `0.5555` edge `-0.0485` maxDD `-4.5445`
- `market_context_high->crypto_alt_1h` score `-1.5433` n `109` status `ready` deltaP `-5.2876` edge `-0.0223` maxDD `-3.0178`
- `market_context_high->crypto_alt_4h` score `-1.7524` n `102` status `ready` deltaP `-1.632` edge `-0.0748` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.8525` n `109` status `ready` deltaP `0.6703` edge `-0.0884` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.151` n `102` status `ready` deltaP `-12.784` edge `-0.0651` maxDD `-4.7021`
- `market_context_high->index_24h` score `-2.4387` n `90` status `ready` deltaP `-10.5556` edge `-0.0228` maxDD `-7.8922`
- `market_context_high->crypto_major_1h` score `-3.4122` n `109` status `ready` deltaP `-11.7481` edge `-0.0687` maxDD `-7.6533`
- `market_context_high->unknown_1h` score `-3.6365` n `109` status `ready` deltaP `1.7332` edge `-0.2699` maxDD `-1.2421`
- `market_context_high->commodity_24h` score `-6.0382` n `90` status `ready` deltaP `10.8334` edge `-0.0249` maxDD `-51.0493`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
