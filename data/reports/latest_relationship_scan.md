# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T03:37:26.332358+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9640`

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

- `market_context_high->unknown_4h` score `92.0966` n `151` status `ready` deltaP `1.9464` edge `7.6953` maxDD `-1.0178`
- `market_context_high->unknown_1h` score `22.4971` n `151` status `ready` deltaP `1.2581` edge `1.9153` maxDD `-1.5807`
- `market_context_high->fx_4h` score `0.3202` n `151` status `ready` deltaP `11.5843` edge `0.0093` maxDD `-0.4545`
- `market_context_high->fx_1h` score `0.3101` n `151` status `ready` deltaP `8.8135` edge `0.0029` maxDD `-0.1986`
- `market_context_high->metal_24h` score `0.1673` n `120` status `ready` deltaP `21.9641` edge `0.1292` maxDD `-6.3348`
- `market_context_high->index_24h` score `0.1208` n `120` status `ready` deltaP `17.5203` edge `0.0149` maxDD `-3.9636`
- `market_context_high->metal_1h` score `-0.0542` n `151` status `ready` deltaP `9.331` edge `0.0079` maxDD `-1.4974`
- `market_context_high->commodity_1h` score `-0.136` n `151` status `ready` deltaP `3.3202` edge `0.0166` maxDD `-1.0053`
- `market_context_high->fx_24h` score `-0.1594` n `120` status `ready` deltaP `16.6797` edge `0.0256` maxDD `-1.2451`
- `market_context_high->commodity_4h` score `-0.3272` n `151` status `ready` deltaP `6.9638` edge `0.0492` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.6255` n `151` status `ready` deltaP `-0.6712` edge `-0.002` maxDD `-1.8971`
- `market_context_high->metal_4h` score `-0.8613` n `151` status `ready` deltaP `8.4578` edge `-0.0003` maxDD `-4.9875`
- `market_context_high->crypto_major_1h` score `-0.8929` n `151` status `ready` deltaP `4.4999` edge `0.0136` maxDD `-9.3126`
- `market_context_high->equity_1h` score `-1.8184` n `151` status `ready` deltaP `1.0618` edge `-0.0126` maxDD `-12.2088`
- `market_context_high->crypto_alt_1h` score `-2.0126` n `151` status `ready` deltaP `-0.4303` edge `-0.0067` maxDD `-13.2099`
- `market_context_high->index_4h` score `-3.521` n `151` status `ready` deltaP `-7.316` edge `-0.027` maxDD `-6.7447`
- `market_context_high->crypto_major_24h` score `-4.1846` n `120` status `ready` deltaP `-0.3264` edge `-0.0486` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-4.5552` n `151` status `ready` deltaP `-0.5885` edge `-0.088` maxDD `-32.0325`
- `market_context_high->equity_24h` score `-5.3039` n `120` status `ready` deltaP `-4.5595` edge `-0.1681` maxDD `-30.5188`
- `market_context_high->commodity_24h` score `-5.6551` n `120` status `ready` deltaP `-9.8541` edge `-0.1003` maxDD `-24.0547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
