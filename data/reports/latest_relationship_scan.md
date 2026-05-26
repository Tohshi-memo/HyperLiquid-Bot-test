# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T04:22:17.239002+00:00`
- Price records: `672`
- Market context records: `1911`
- Flow alert records: `7400`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4518`

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

- `market_context_high->crypto_alt_4h` score `7.865` n `199` status `ready` deltaP `24.643` edge `0.6056` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `7.2675` n `199` status `ready` deltaP `29.2392` edge `0.5353` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `3.9129` n `199` status `ready` deltaP `17.5006` edge `0.4118` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.6241` n `199` status `ready` deltaP `15.6491` edge `0.2238` maxDD `-5.0894`
- `market_context_high->metal_24h` score `1.5083` n `188` status `ready` deltaP `15.5844` edge `0.2644` maxDD `-12.7414`
- `market_context_high->unknown_24h` score `1.2854` n `188` status `ready` deltaP `13.2535` edge `0.5508` maxDD `-35.8966`
- `market_context_high->index_24h` score `0.9195` n `188` status `ready` deltaP `7.2843` edge `0.1509` maxDD `-4.1604`
- `market_context_high->crypto_major_1h` score `0.7506` n `203` status `ready` deltaP `8.2151` edge `0.1064` maxDD `-3.2225`
- `market_context_high->index_4h` score `0.5394` n `199` status `ready` deltaP `10.7029` edge `0.0825` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `0.5375` n `203` status `ready` deltaP `7.4039` edge `0.1068` maxDD `-4.9097`
- `market_context_high->fx_24h` score `0.0757` n `188` status `ready` deltaP `13.1428` edge `0.0236` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.0453` n `203` status `ready` deltaP `5.55` edge `0.0386` maxDD `-2.6836`
- `market_context_high->metal_1h` score `-0.5557` n `203` status `ready` deltaP `6.0514` edge `0.022` maxDD `-6.3532`
- `market_context_high->fx_1h` score `-0.6132` n `203` status `ready` deltaP `-2.4726` edge `0.0011` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.6702` n `203` status `ready` deltaP `-0.236` edge `0.0089` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.6734` n `199` status `ready` deltaP `12.0856` edge `0.1325` maxDD `-12.5349`
- `market_context_high->equity_24h` score `-0.6825` n `188` status `ready` deltaP `7.7201` edge `0.3815` maxDD `-33.1875`
- `market_context_high->fx_4h` score `-0.8043` n `199` status `ready` deltaP `-2.295` edge `0.001` maxDD `-1.1056`
- `market_context_high->unknown_1h` score `-0.9849` n `203` status `ready` deltaP `1.9225` edge `0.0003` maxDD `-3.6151`
- `market_context_high->crypto_major_24h` score `-1.2536` n `188` status `ready` deltaP `15.6176` edge `0.65` maxDD `-62.3533`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
