# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T09:07:25.866181+00:00`
- Price records: `672`
- Market context records: `7123`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11667`

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

- `market_context_high->fx_4h` score `0.3801` n `144` status `ready` deltaP `15.6504` edge `0.0144` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.0595` n `151` status `ready` deltaP `5.2028` edge `0.0028` maxDD `-0.276`
- `market_context_high->unknown_1h` score `-0.2772` n `151` status `ready` deltaP `-1.1609` edge `0.0405` maxDD `-1.4688`
- `market_context_high->crypto_alt_1h` score `-0.4554` n `151` status `ready` deltaP `0.3311` edge `0.0283` maxDD `-4.7779`
- `market_context_high->index_1h` score `-0.7574` n `151` status `ready` deltaP `1.2977` edge `-0.0053` maxDD `-2.3175`
- `market_context_high->commodity_1h` score `-0.8492` n `151` status `ready` deltaP `-4.1371` edge `-0.0192` maxDD `-1.9668`
- `market_context_high->crypto_major_1h` score `-0.8839` n `151` status `ready` deltaP `3.6424` edge `0.0373` maxDD `-7.1523`
- `market_context_high->commodity_4h` score `-1.422` n `144` status `ready` deltaP `-5.2168` edge `-0.044` maxDD `-2.9494`
- `market_context_high->metal_1h` score `-1.4254` n `151` status `ready` deltaP `-5.538` edge `-0.0053` maxDD `-2.1249`
- `market_context_high->unknown_4h` score `-1.5028` n `144` status `ready` deltaP `-6.3855` edge `0.0101` maxDD `-4.4825`
- `market_context_high->crypto_major_4h` score `-3.0554` n `144` status `ready` deltaP `3.9804` edge `0.0102` maxDD `-24.6094`
- `market_context_high->equity_1h` score `-3.2298` n `151` status `ready` deltaP `2.4953` edge `-0.0435` maxDD `-14.716`
- `market_context_high->commodity_24h` score `-3.8545` n `144` status `ready` deltaP `-10.0694` edge `-0.1232` maxDD `-4.4704`
- `market_context_high->index_4h` score `-4.1392` n `144` status `ready` deltaP `-3.7094` edge `-0.0503` maxDD `-12.2591`
- `market_context_high->metal_4h` score `-4.5189` n `144` status `ready` deltaP `-10.0779` edge `-0.0127` maxDD `-5.4021`
- `market_context_high->crypto_alt_4h` score `-4.6891` n `144` status `ready` deltaP `0.6267` edge `-0.0164` maxDD `-22.2831`
- `market_context_high->fx_24h` score `-4.7126` n `144` status `ready` deltaP `-13.0208` edge `-0.0232` maxDD `-3.9503`
- `market_context_high->unknown_24h` score `-9.4881` n `144` status `ready` deltaP `-28.125` edge `-0.0885` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-13.7698` n `144` status `ready` deltaP `-2.4221` edge `-0.2443` maxDD `-63.963`
- `market_context_high->metal_24h` score `-14.7961` n `144` status `ready` deltaP `-28.125` edge `-0.166` maxDD `-42.027`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
