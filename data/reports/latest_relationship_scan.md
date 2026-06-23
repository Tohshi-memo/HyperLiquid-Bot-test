# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T21:07:30.679566+00:00`
- Price records: `672`
- Market context records: `4554`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10045`

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

- `market_context_high->unknown_1h` score `61.0173` n `161` status `ready` deltaP `6.2131` edge `5.0934` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `2.7172` n `161` status `ready` deltaP `7.4544` edge `0.3026` maxDD `-5.0693`
- `market_context_high->fx_4h` score `-0.4825` n `161` status `ready` deltaP `6.5833` edge `0.0025` maxDD `-1.9927`
- `market_context_high->equity_1h` score `-0.6657` n `161` status `ready` deltaP `-1.7183` edge `0.0248` maxDD `-5.5624`
- `market_context_high->equity_4h` score `-0.6962` n `161` status `ready` deltaP `2.1238` edge `0.0735` maxDD `-8.8203`
- `market_context_high->fx_1h` score `-0.6994` n `161` status `ready` deltaP `0.027` edge `-0.003` maxDD `-1.1038`
- `market_context_high->commodity_1h` score `-0.7334` n `161` status `ready` deltaP `0.132` edge `0.0176` maxDD `-2.0345`
- `market_context_high->index_4h` score `-0.7565` n `161` status `ready` deltaP `3.3433` edge `-0.007` maxDD `-5.9823`
- `market_context_high->commodity_4h` score `-1.2018` n `161` status `ready` deltaP `3.4322` edge `0.0338` maxDD `-9.1941`
- `market_context_high->index_1h` score `-1.4882` n `161` status `ready` deltaP `-1.9126` edge `-0.0104` maxDD `-2.7358`
- `market_context_high->unknown_24h` score `-2.9291` n `159` status `ready` deltaP `2.0309` edge `-0.1653` maxDD `-4.7201`
- `market_context_high->metal_1h` score `-4.4613` n `161` status `ready` deltaP `-3.7825` edge `-0.0814` maxDD `-17.8795`
- `market_context_high->crypto_alt_1h` score `-5.4871` n `161` status `ready` deltaP `-3.0052` edge `-0.1085` maxDD `-22.2982`
- `market_context_high->fx_24h` score `-5.5798` n `159` status `ready` deltaP `-14.603` edge `-0.0164` maxDD `-6.0982`
- `market_context_high->index_24h` score `-5.7504` n `159` status `ready` deltaP `-9.9515` edge `-0.1334` maxDD `-29.3321`
- `market_context_high->commodity_24h` score `-6.4504` n `159` status `ready` deltaP `7.1966` edge `0.0413` maxDD `-37.4779`
- `market_context_high->crypto_major_1h` score `-6.5164` n `161` status `ready` deltaP `-4.9131` edge `-0.135` maxDD `-27.356`
- `market_context_high->crypto_alt_4h` score `-8.713` n `161` status `ready` deltaP `-1.5187` edge `-0.2412` maxDD `-63.9243`
- `market_context_high->crypto_major_4h` score `-11.4416` n `161` status `ready` deltaP `0.1354` edge `-0.3734` maxDD `-82.2164`
- `market_context_high->equity_24h` score `-13.4473` n `159` status `ready` deltaP `-1.343` edge `-0.2471` maxDD `-102.1031`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
