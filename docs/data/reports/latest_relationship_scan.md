# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T15:07:30.906174+00:00`
- Price records: `672`
- Market context records: `5783`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8718`

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

- `market_context_high->equity_24h` score `0.4979` n `240` status `ready` deltaP `15.1389` edge `0.4708` maxDD `-31.6316`
- `market_context_high->equity_4h` score `0.0704` n `297` status `ready` deltaP `7.2791` edge `0.1212` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.263` n `305` status `ready` deltaP `2.0742` edge `0.001` maxDD `-0.5499`
- `market_context_high->equity_1h` score `-0.5994` n `305` status `ready` deltaP `3.5914` edge `0.0268` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.6335` n `305` status `ready` deltaP `2.3589` edge `-0.001` maxDD `-2.0682`
- `market_context_high->commodity_1h` score `-0.7532` n `305` status `ready` deltaP `-1.6462` edge `-0.0051` maxDD `-3.7721`
- `market_context_high->crypto_major_1h` score `-0.9187` n `305` status `ready` deltaP `3.1717` edge `0.0344` maxDD `-6.2348`
- `market_context_high->index_1h` score `-0.9641` n `305` status `ready` deltaP `0.4202` edge `0.0037` maxDD `-0.9472`
- `market_context_high->fx_24h` score `-0.9658` n `240` status `ready` deltaP `14.2708` edge `0.0404` maxDD `-3.7488`
- `market_context_high->crypto_alt_1h` score `-1.0316` n `305` status `ready` deltaP `2.0669` edge `0.0337` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.1998` n `297` status `ready` deltaP `0.6457` edge `0.0106` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.3715` n `297` status `ready` deltaP `1.1533` edge `0.0044` maxDD `-1.7001`
- `market_context_high->commodity_4h` score `-2.459` n `297` status `ready` deltaP `-3.2705` edge `-0.0259` maxDD `-14.071`
- `market_context_high->index_24h` score `-2.8577` n `240` status `ready` deltaP `2.7431` edge `0.0298` maxDD `-18.1572`
- `market_context_high->crypto_major_4h` score `-2.9116` n `297` status `ready` deltaP `7.621` edge `0.1438` maxDD `-25.6458`
- `market_context_high->metal_4h` score `-3.862` n `297` status `ready` deltaP `-5.7131` edge `-0.0478` maxDD `-11.5426`
- `market_context_high->crypto_alt_4h` score `-4.4984` n `297` status `ready` deltaP `5.3529` edge `0.0903` maxDD `-28.7346`
- `market_context_high->crypto_major_24h` score `-6.9461` n `240` status `ready` deltaP `2.2222` edge `-0.0938` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.0783` n `240` status `ready` deltaP `-7.8819` edge `-0.248` maxDD `-27.5543`
- `market_context_high->commodity_24h` score `-10.95` n `240` status `ready` deltaP `-13.993` edge `-0.0816` maxDD `-40.676`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
