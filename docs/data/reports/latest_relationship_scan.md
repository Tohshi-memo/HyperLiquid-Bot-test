# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T10:43:07.735025+00:00`
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

- `market_context_high->crypto_major_24h` score `2.2624` n `85` status `ready` deltaP `7.9233` edge `0.2565` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `1.4787` n `85` status `ready` deltaP `16.2157` edge `0.2648` maxDD `-4.666`
- `market_context_high->equity_1h` score `1.1058` n `97` status `ready` deltaP `9.6241` edge `0.0584` maxDD `-0.4329`
- `market_context_high->crypto_major_4h` score `0.7936` n `97` status `ready` deltaP `9.874` edge `0.1024` maxDD `-3.1677`
- `market_context_high->metal_4h` score `0.7314` n `97` status `ready` deltaP `14.3748` edge `0.0227` maxDD `-1.273`
- `market_context_high->index_1h` score `0.6937` n `97` status `ready` deltaP `13.2508` edge `0.0082` maxDD `-0.0982`
- `market_context_high->unknown_1h` score `0.5207` n `97` status `ready` deltaP `9.4605` edge `0.003` maxDD `-0.4807`
- `market_context_high->crypto_alt_4h` score `0.3573` n `97` status `ready` deltaP `10.7886` edge `0.1056` maxDD `-5.5373`
- `market_context_high->metal_1h` score `0.0041` n `97` status `ready` deltaP `4.5064` edge `0.009` maxDD `-0.4291`
- `market_context_high->equity_4h` score `-0.0624` n `97` status `ready` deltaP `1.8827` edge `0.0727` maxDD `-2.5696`
- `market_context_high->unknown_24h` score `-0.1264` n `85` status `ready` deltaP `13.3021` edge `-0.0804` maxDD `-0.1719`
- `market_context_high->fx_4h` score `-0.2747` n `97` status `ready` deltaP `2.3526` edge `-0.0004` maxDD `-0.3734`
- `market_context_high->crypto_alt_1h` score `-0.3003` n `97` status `ready` deltaP `3.0094` edge `0.0216` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.4211` n `97` status `ready` deltaP `1.9785` edge `0.0173` maxDD `-2.7581`
- `market_context_high->commodity_4h` score `-0.4211` n `97` status `ready` deltaP `3.6522` edge `0.0067` maxDD `-2.4692`
- `market_context_high->fx_1h` score `-0.4775` n `97` status `ready` deltaP `-3.8907` edge `0.0009` maxDD `-0.2273`
- `market_context_high->index_4h` score `-0.5761` n `97` status `ready` deltaP `1.0325` edge `0.0106` maxDD `-0.5728`
- `market_context_high->commodity_1h` score `-0.9284` n `97` status `ready` deltaP `-7.4326` edge `-0.0082` maxDD `-1.5684`
- `market_context_high->metal_24h` score `-1.958` n `85` status `ready` deltaP `-6.8243` edge `0.0191` maxDD `-6.9709`
- `market_context_high->index_24h` score `-4.402` n `85` status `ready` deltaP `-14.6967` edge `-0.1781` maxDD `-12.0629`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
