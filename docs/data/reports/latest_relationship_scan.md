# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T22:07:36.563714+00:00`
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

- `market_context_high->unknown_24h` score `12.8284` n `90` status `ready` deltaP `4.4445` edge `1.0437` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `2.8655` n `109` status `ready` deltaP `-2.26` edge `0.3534` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.2118` n `109` status `ready` deltaP `14.0566` edge `0.0919` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.9024` n `90` status `ready` deltaP `2.0139` edge `0.2191` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.8505` n `90` status `ready` deltaP `24.7223` edge `0.0648` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4108` n `109` status `ready` deltaP `7.61` edge `0.0251` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0811` n `109` status `ready` deltaP `6.5813` edge `-0.0021` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.0702` n `109` status `ready` deltaP `10.2288` edge `0.0088` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.4872` n `109` status `ready` deltaP `-0.9614` edge `-0.0066` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.7628` n `109` status `ready` deltaP `2.9369` edge `0.0061` maxDD `-3.211`
- `market_context_high->index_1h` score `-0.7922` n `109` status `ready` deltaP `-4.1051` edge `-0.0208` maxDD `-1.6054`
- `market_context_high->crypto_alt_24h` score `-1.351` n `90` status `ready` deltaP `0.5555` edge `-0.0326` maxDD `-4.5445`
- `market_context_high->crypto_alt_1h` score `-1.5122` n `109` status `ready` deltaP `-4.8385` edge `-0.0227` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.8681` n `109` status `ready` deltaP `0.82` edge `-0.0914` maxDD `-10.619`
- `market_context_high->index_24h` score `-2.1728` n `90` status `ready` deltaP `-8.4723` edge `-0.0026` maxDD `-7.8922`
- `market_context_high->index_4h` score `-2.2393` n `109` status `ready` deltaP `-14.4971` edge `-0.065` maxDD `-4.7021`
- `market_context_high->crypto_alt_4h` score `-2.4076` n `109` status `ready` deltaP `-0.2923` edge `-0.0597` maxDD `-5.7857`
- `market_context_high->crypto_major_1h` score `-3.3475` n `109` status `ready` deltaP `-11.299` edge `-0.0663` maxDD `-7.6533`
- `market_context_high->unknown_1h` score `-3.5872` n `109` status `ready` deltaP `1.4338` edge `-0.2638` maxDD `-1.2421`
- `market_context_high->commodity_24h` score `-6.0954` n `90` status `ready` deltaP `10.1389` edge `-0.0276` maxDD `-51.0493`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
