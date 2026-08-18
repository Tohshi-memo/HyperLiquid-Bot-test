# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T10:22:26.722858+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11633`

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

- `market_context_high->crypto_major_24h` score `2.2293` n `85` status `ready` deltaP `7.75` edge `0.2549` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `1.4971` n `85` status `ready` deltaP `16.389` edge `0.266` maxDD `-4.666`
- `market_context_high->equity_1h` score `1.0818` n `97` status `ready` deltaP `9.4744` edge `0.0574` maxDD `-0.4329`
- `market_context_high->crypto_major_4h` score `0.7888` n `97` status `ready` deltaP `9.874` edge `0.102` maxDD `-3.1677`
- `market_context_high->metal_4h` score `0.7326` n `97` status `ready` deltaP `14.3748` edge `0.0228` maxDD `-1.273`
- `market_context_high->index_1h` score `0.6794` n `97` status `ready` deltaP `13.1011` edge `0.008` maxDD `-0.0982`
- `market_context_high->unknown_1h` score `0.5255` n `97` status `ready` deltaP `9.4605` edge `0.0034` maxDD `-0.4807`
- `market_context_high->crypto_alt_4h` score `0.3684` n `97` status `ready` deltaP `10.9411` edge `0.106` maxDD `-5.5373`
- `market_context_high->metal_1h` score `0.0041` n `97` status `ready` deltaP `4.5064` edge `0.009` maxDD `-0.4291`
- `market_context_high->unknown_24h` score `-0.1078` n `85` status `ready` deltaP `13.4754` edge `-0.08` maxDD `-0.1719`
- `market_context_high->equity_4h` score `-0.113` n `97` status `ready` deltaP `1.7302` edge `0.0695` maxDD `-2.5696`
- `market_context_high->fx_4h` score `-0.2747` n `97` status `ready` deltaP `2.3526` edge `-0.0004` maxDD `-0.3734`
- `market_context_high->crypto_alt_1h` score `-0.3011` n `97` status `ready` deltaP `3.0094` edge `0.0215` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.418` n `97` status `ready` deltaP `3.6522` edge `0.0071` maxDD `-2.4692`
- `market_context_high->crypto_major_1h` score `-0.4219` n `97` status `ready` deltaP `1.9785` edge `0.0172` maxDD `-2.7581`
- `market_context_high->fx_1h` score `-0.4767` n `97` status `ready` deltaP `-3.8907` edge `0.001` maxDD `-0.2273`
- `market_context_high->index_4h` score `-0.5919` n `97` status `ready` deltaP `0.8801` edge `0.0103` maxDD `-0.5728`
- `market_context_high->commodity_1h` score `-0.9229` n `97` status `ready` deltaP `-7.4326` edge `-0.0075` maxDD `-1.5684`
- `market_context_high->metal_24h` score `-1.9733` n `85` status `ready` deltaP `-6.9976` edge `0.0183` maxDD `-6.9709`
- `market_context_high->index_24h` score `-4.4228` n `85` status `ready` deltaP `-14.87` edge `-0.1796` maxDD `-12.0629`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
