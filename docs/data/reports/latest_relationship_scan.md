# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T10:52:25.017415+00:00`
- Price records: `672`
- Market context records: `7131`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11670`

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

- `market_context_high->fx_4h` score `0.5322` n `139` status `ready` deltaP `18.4254` edge `0.0154` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.0916` n `151` status `ready` deltaP `5.2028` edge `0.0028` maxDD `-0.276`
- `market_context_high->unknown_1h` score `-0.4026` n `151` status `ready` deltaP `-2.6986` edge `0.0403` maxDD `-1.4688`
- `market_context_high->crypto_alt_1h` score `-0.5571` n `151` status `ready` deltaP `0.8437` edge `0.026` maxDD `-5.91`
- `market_context_high->crypto_major_1h` score `-0.6268` n `151` status `ready` deltaP `3.6424` edge `0.0364` maxDD `-7.6171`
- `market_context_high->commodity_1h` score `-0.7536` n `151` status `ready` deltaP `-2.5994` edge `-0.0172` maxDD `-1.9668`
- `market_context_high->index_1h` score `-0.7538` n `151` status `ready` deltaP `1.2977` edge `-0.005` maxDD `-2.3175`
- `market_context_high->metal_1h` score `-1.3842` n `151` status `ready` deltaP `-5.0254` edge `-0.0053` maxDD `-2.1238`
- `market_context_high->unknown_4h` score `-2.1452` n `139` status `ready` deltaP `-5.2115` edge `0.0197` maxDD `-4.7644`
- `market_context_high->commodity_4h` score `-2.3216` n `139` status `ready` deltaP `-6.8904` edge `-0.044` maxDD `-2.9494`
- `market_context_high->crypto_major_4h` score `-3.2297` n `139` status `ready` deltaP `1.7075` edge `0.0036` maxDD `-24.6569`
- `market_context_high->equity_1h` score `-3.4184` n `151` status `ready` deltaP `0.9577` edge `-0.0455` maxDD `-14.9936`
- `market_context_high->index_4h` score `-4.1936` n `139` status `ready` deltaP `-4.0293` edge `-0.0527` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-4.2428` n `137` status `ready` deltaP `-12.1629` edge `-0.1416` maxDD `-4.4704`
- `market_context_high->metal_4h` score `-4.4128` n `139` status `ready` deltaP `-8.8568` edge `-0.0131` maxDD `-5.3137`
- `market_context_high->fx_24h` score `-4.8261` n `137` status `ready` deltaP `-14.2297` edge `-0.0246` maxDD `-3.9503`
- `market_context_high->crypto_alt_4h` score `-5.1118` n `139` status `ready` deltaP `-1.7185` edge `-0.0304` maxDD `-22.7303`
- `market_context_high->unknown_24h` score `-9.8826` n `137` status `ready` deltaP `-30.8204` edge `-0.1034` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-13.88` n `139` status `ready` deltaP `-1.5902` edge `-0.2576` maxDD `-64.0772`
- `market_context_high->metal_24h` score `-14.5452` n `137` status `ready` deltaP `-28.9145` edge `-0.1788` maxDD `-41.2427`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
