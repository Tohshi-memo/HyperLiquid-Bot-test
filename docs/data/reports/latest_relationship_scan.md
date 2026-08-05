# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T13:22:27.522371+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11664`

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

- `market_context_high->unknown_24h` score `13.8789` n `89` status `ready` deltaP `8.425` edge `1.1047` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.1125` n `95` status `ready` deltaP `2.4727` edge `0.5091` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.6574` n `95` status `ready` deltaP `17.1068` edge `0.1087` maxDD `-2.7703`
- `market_context_high->fx_24h` score `1.1182` n `89` status `ready` deltaP `26.8395` edge `0.085` maxDD `-4.3126`
- `market_context_high->metal_24h` score `0.8713` n `89` status `ready` deltaP `1.6268` edge `0.2177` maxDD `-2.6802`
- `market_context_high->commodity_1h` score `0.5017` n `98` status `ready` deltaP `8.0411` edge `0.0298` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0971` n `98` status `ready` deltaP `6.9382` edge `-0.0032` maxDD `-0.7973`
- `market_context_high->fx_4h` score `0.0148` n `95` status `ready` deltaP `12.1486` edge `0.0069` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5707` n `98` status `ready` deltaP `-2.0286` edge `-0.0102` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.6924` n `98` status `ready` deltaP `-2.4105` edge `-0.0193` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.9267` n `95` status `ready` deltaP `1.4346` edge `-0.0049` maxDD `-3.211`
- `market_context_high->crypto_alt_1h` score `-0.9604` n `98` status `ready` deltaP `-4.436` edge `-0.0225` maxDD `-3.0178`
- `market_context_high->crypto_alt_24h` score `-1.4788` n `89` status `ready` deltaP `0.6768` edge `-0.0498` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-1.6569` n `95` status `ready` deltaP `-1.7748` edge `-0.0616` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.8128` n `98` status `ready` deltaP `2.3647` edge `-0.0946` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.1093` n `95` status `ready` deltaP `-12.4021` edge `-0.0623` maxDD `-4.7021`
- `market_context_high->index_24h` score `-2.5564` n `89` status `ready` deltaP `-11.6495` edge `-0.0306` maxDD `-7.8922`
- `market_context_high->unknown_1h` score `-3.1085` n `98` status `ready` deltaP `4.8974` edge `-0.247` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.6524` n `98` status `ready` deltaP `-13.415` edge `-0.0776` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.003` n `89` status `ready` deltaP `11.1716` edge `-0.0291` maxDD `-50.8663`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
