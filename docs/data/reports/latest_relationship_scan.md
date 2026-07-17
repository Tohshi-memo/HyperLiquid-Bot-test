# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T15:07:30.158705+00:00`
- Price records: `672`
- Market context records: `7040`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11496`

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

- `market_context_high->fx_4h` score `-0.0673` n `206` status `ready` deltaP `13.5034` edge `0.01` maxDD `-1.0251`
- `market_context_high->fx_1h` score `-0.2289` n `206` status `ready` deltaP `2.1321` edge `0.0017` maxDD `-0.2872`
- `market_context_high->crypto_alt_1h` score `-0.2573` n `206` status `ready` deltaP `2.4228` edge `0.0373` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.7074` n `206` status `ready` deltaP `0.1991` edge `-0.0009` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.7418` n `206` status `ready` deltaP `-2.6728` edge `-0.0005` maxDD `-2.1427`
- `market_context_high->commodity_1h` score `-0.7786` n `206` status `ready` deltaP `-3.4024` edge `-0.0155` maxDD `-1.9306`
- `market_context_high->crypto_major_1h` score `-0.8307` n `206` status `ready` deltaP `4.2919` edge `0.0374` maxDD `-7.1523`
- `market_context_high->unknown_1h` score `-1.0711` n `206` status `ready` deltaP `-2.7949` edge `0.0079` maxDD `-2.6157`
- `market_context_high->unknown_4h` score `-1.7581` n `206` status `ready` deltaP `-6.3758` edge `0.091` maxDD `-7.2672`
- `market_context_high->equity_1h` score `-1.7593` n `206` status `ready` deltaP `4.6407` edge `-0.0142` maxDD `-14.716`
- `market_context_high->index_4h` score `-2.001` n `206` status `ready` deltaP `4.9742` edge `-0.0198` maxDD `-12.2591`
- `market_context_high->commodity_4h` score `-2.0429` n `206` status `ready` deltaP `-3.4055` edge `-0.0315` maxDD `-2.9494`
- `market_context_high->metal_4h` score `-2.0454` n `206` status `ready` deltaP `4.2432` edge `0.0078` maxDD `-5.5324`
- `market_context_high->unknown_24h` score `-2.0963` n `200` status `ready` deltaP `-9.9028` edge `0.2855` maxDD `-21.3928`
- `market_context_high->commodity_24h` score `-2.2693` n `200` status `ready` deltaP `-0.2292` edge `-0.0567` maxDD `-4.4704`
- `market_context_high->crypto_alt_4h` score `-2.5016` n `206` status `ready` deltaP `3.2575` edge `0.0361` maxDD `-22.2831`
- `market_context_high->crypto_major_4h` score `-2.7673` n `206` status `ready` deltaP `4.4652` edge `0.0439` maxDD `-24.6094`
- `market_context_high->fx_24h` score `-3.7133` n `200` status `ready` deltaP `-2.2847` edge `-0.0115` maxDD `-3.9503`
- `market_context_high->equity_4h` score `-7.28` n `206` status `ready` deltaP `5.251` edge `-0.0813` maxDD `-63.963`
- `market_context_high->metal_24h` score `-14.4778` n `200` status `ready` deltaP `-14.7917` edge `-0.0699` maxDD `-42.7044`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
