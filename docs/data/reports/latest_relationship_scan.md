# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-06T07:07:27.488140+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11781`

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

- `market_context_high->unknown_24h` score `11.8391` n `92` status `ready` deltaP `4.4686` edge `0.9611` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `4.114` n `109` status `ready` deltaP `-0.8881` edge `0.4483` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.2504` n `109` status `ready` deltaP `14.209` edge `0.0941` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.8657` n `92` status `ready` deltaP `2.7626` edge `0.2094` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.585` n `92` status `ready` deltaP `21.5806` edge `0.0517` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4671` n `109` status `ready` deltaP `8.2088` edge `0.0258` maxDD `-1.3282`
- `market_context_high->fx_1h` score `-0.0255` n `109` status `ready` deltaP `5.3837` edge `-0.003` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.1604` n `109` status `ready` deltaP `8.7044` edge `0.0074` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5557` n `109` status `ready` deltaP `-2.0093` edge `-0.0084` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.7626` n `109` status `ready` deltaP `-3.656` edge `-0.02` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.8162` n `109` status `ready` deltaP `2.4796` edge `0.0023` maxDD `-3.211`
- `market_context_high->crypto_alt_24h` score `-1.2825` n `92` status `ready` deltaP `0.8077` edge `-0.0255` maxDD `-4.5445`
- `market_context_high->index_24h` score `-1.3614` n `92` status `ready` deltaP `-3.6232` edge `0.0691` maxDD `-7.8922`
- `market_context_high->crypto_alt_1h` score `-1.5241` n `109` status `ready` deltaP `-5.2876` edge `-0.0207` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.8564` n `109` status `ready` deltaP `0.9697` edge `-0.0909` maxDD `-10.619`
- `market_context_high->crypto_alt_4h` score `-2.1029` n `109` status `ready` deltaP `1.5369` edge `-0.0465` maxDD `-5.7857`
- `market_context_high->index_4h` score `-2.1327` n `109` status `ready` deltaP `-12.9727` edge `-0.0615` maxDD `-4.7021`
- `market_context_high->unknown_1h` score `-2.3236` n `109` status `ready` deltaP `1.5835` edge `-0.1595` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.3355` n `109` status `ready` deltaP `-11.5984` edge `-0.0633` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.3767` n `92` status `ready` deltaP `7.4124` edge `-0.0348` maxDD `-51.2378`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
