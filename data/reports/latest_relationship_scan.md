# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T22:23:05.645519+00:00`
- Price records: `672`
- Market context records: `6024`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11124`

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

- `news_risk_high->fx_24h` score `7.7886` n `30` status `ready` deltaP `70.3125` edge `0.1803` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.2747` n `30` status `ready` deltaP `44.2683` edge `0.0657` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.1595` n `30` status `ready` deltaP `28.1598` edge `0.0961` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.243` n `30` status `ready` deltaP `26.9261` edge `0.0213` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.6963` n `206` status `ready` deltaP `9.2514` edge `0.1714` maxDD `-2.671`
- `market_context_high->equity_24h` score `1.5695` n `180` status `ready` deltaP `29.7223` edge `0.5482` maxDD `-31.6107`
- `news_risk_high->crypto_major_1h` score `0.8442` n `30` status `ready` deltaP `10.3393` edge `0.086` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.2372` n `30` status `ready` deltaP `5.4691` edge `0.0401` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.1468` n `30` status `ready` deltaP `9.2361` edge `0.0444` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.3659` n `206` status `ready` deltaP `4.0288` edge `0.0061` maxDD `-2.0564`
- `news_risk_high->metal_1h` score `-0.4024` n `30` status `ready` deltaP `1.5369` edge `-0.0252` maxDD `-1.2643`
- `market_context_high->index_24h` score `-0.4327` n `180` status `ready` deltaP `5.3472` edge `0.0789` maxDD `-5.6021`
- `market_context_high->fx_1h` score `-0.5893` n `206` status `ready` deltaP `-0.2907` edge `-0.0015` maxDD `-0.6538`
- `market_context_high->commodity_1h` score `-0.6391` n `206` status `ready` deltaP `-1.2339` edge `-0.0004` maxDD `-0.5708`
- `market_context_high->metal_4h` score `-0.8911` n `206` status `ready` deltaP `5.2481` edge `0.0095` maxDD `-3.4996`
- `market_context_high->index_4h` score `-0.8969` n `206` status `ready` deltaP `2.8727` edge `0.0192` maxDD `-1.9335`
- `market_context_high->equity_1h` score `-0.9653` n `206` status `ready` deltaP `0.9302` edge `0.0262` maxDD `-4.3608`
- `market_context_high->crypto_alt_1h` score `-0.9693` n `206` status `ready` deltaP `3.6568` edge `0.0266` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.9735` n `206` status `ready` deltaP `3.8021` edge `0.0266` maxDD `-9.807`
- `news_risk_high->crypto_alt_24h` score `-1.0033` n `30` status `ready` deltaP `22.3264` edge `-0.2177` maxDD `-0.5131`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
