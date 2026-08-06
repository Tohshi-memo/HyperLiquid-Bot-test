# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-06T04:22:27.837723+00:00`
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

- `market_context_high->unknown_24h` score `12.3604` n `90` status `ready` deltaP `4.4445` edge `1.0047` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `4.1066` n `109` status `ready` deltaP `-1.0405` edge `0.4487` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.2624` n `109` status `ready` deltaP `14.209` edge `0.0951` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.7713` n `90` status `ready` deltaP `2.0139` edge `0.2023` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.7093` n `90` status `ready` deltaP `23.507` edge `0.0548` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4718` n `109` status `ready` deltaP `8.3585` edge `0.0252` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0176` n `109` status `ready` deltaP `5.8328` edge `-0.0024` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.1414` n `109` status `ready` deltaP `9.0093` edge `0.0078` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5666` n `109` status `ready` deltaP `-2.159` edge `-0.0088` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.7276` n `109` status `ready` deltaP `-3.0572` edge `-0.0195` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.972` n `109` status `ready` deltaP `0.8028` edge `-0.0065` maxDD `-3.211`
- `market_context_high->crypto_alt_24h` score `-1.3258` n `90` status `ready` deltaP `0.0347` edge `-0.0259` maxDD `-4.5445`
- `market_context_high->crypto_alt_1h` score `-1.5121` n `109` status `ready` deltaP `-5.2876` edge `-0.0197` maxDD `-3.0178`
- `market_context_high->index_24h` score `-1.5252` n `90` status `ready` deltaP `-4.132` edge `0.0515` maxDD `-7.8922`
- `market_context_high->equity_1h` score `-1.8635` n `109` status `ready` deltaP `0.9697` edge `-0.0918` maxDD `-10.619`
- `market_context_high->crypto_alt_4h` score `-2.1455` n `109` status `ready` deltaP `1.0796` edge `-0.047` maxDD `-5.7857`
- `market_context_high->index_4h` score `-2.1643` n `109` status `ready` deltaP `-13.43` edge `-0.0625` maxDD `-4.7021`
- `market_context_high->unknown_1h` score `-3.2537` n `109` status `ready` deltaP `2.1823` edge `-0.241` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.3378` n `109` status `ready` deltaP `-11.7481` edge `-0.0625` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.1799` n `90` status `ready` deltaP `9.0973` edge `-0.0315` maxDD `-51.0493`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
