# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T06:07:23.689509+00:00`
- Price records: `672`
- Market context records: `7109`
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

- `market_context_high->fx_4h` score `0.3698` n `148` status `ready` deltaP `15.5117` edge `0.014` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.1202` n `148` status `ready` deltaP `4.05` edge `0.0027` maxDD `-0.276`
- `market_context_high->unknown_1h` score `-0.1658` n `148` status `ready` deltaP `-0.5341` edge `0.0456` maxDD `-1.4688`
- `market_context_high->crypto_alt_1h` score `-0.3503` n `148` status `ready` deltaP `1.4282` edge `0.032` maxDD `-4.5815`
- `market_context_high->crypto_major_1h` score `-0.5523` n `148` status `ready` deltaP `3.9044` edge `0.0384` maxDD `-7.1523`
- `market_context_high->index_1h` score `-0.5838` n `148` status `ready` deltaP `-0.9144` edge `-0.0068` maxDD `-2.2895`
- `market_context_high->commodity_1h` score `-0.801` n `148` status `ready` deltaP `-3.2934` edge `-0.0191` maxDD `-1.9306`
- `market_context_high->commodity_4h` score `-1.3885` n `148` status `ready` deltaP `-4.7215` edge `-0.043` maxDD `-2.9494`
- `market_context_high->metal_1h` score `-1.5483` n `148` status `ready` deltaP `-6.9995` edge `-0.0058` maxDD `-2.1249`
- `market_context_high->unknown_4h` score `-1.5535` n `148` status `ready` deltaP `-6.7444` edge `0.006` maxDD `-4.4825`
- `market_context_high->equity_1h` score `-2.1198` n `148` status `ready` deltaP `2.5368` edge `-0.0464` maxDD `-14.716`
- `market_context_high->crypto_major_4h` score `-3.045` n `148` status `ready` deltaP `4.0747` edge `0.0109` maxDD `-24.6094`
- `market_context_high->commodity_24h` score `-3.5655` n `148` status `ready` deltaP `-8.9621` edge `-0.1065` maxDD `-4.4704`
- `market_context_high->index_4h` score `-4.0432` n `148` status `ready` deltaP `-2.8387` edge `-0.0481` maxDD `-12.2591`
- `market_context_high->metal_4h` score `-4.3569` n `148` status `ready` deltaP `-8.1452` edge `-0.0118` maxDD `-5.4243`
- `market_context_high->fx_24h` score `-4.58` n `148` status `ready` deltaP `-11.5428` edge `-0.022` maxDD `-3.9503`
- `market_context_high->crypto_alt_4h` score `-4.7155` n `148` status `ready` deltaP `0.4326` edge `-0.0173` maxDD `-22.2831`
- `market_context_high->unknown_24h` score `-9.2553` n `148` status `ready` deltaP `-26.6094` edge `-0.0792` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-13.653` n `148` status `ready` deltaP `-2.4473` edge `-0.2344` maxDD `-63.963`
- `market_context_high->metal_24h` score `-14.7564` n `148` status `ready` deltaP `-26.2669` edge `-0.1536` maxDD `-42.4122`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
