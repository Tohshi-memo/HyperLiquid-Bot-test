# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T23:22:27.251927+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6755`

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

- `market_context_high->unknown_24h` score `3760.9533` n `85` status `ready` deltaP `-12.1875` edge `313.537` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `123.7572` n `85` status `ready` deltaP `0.868` edge `10.3206` maxDD `-0.3966`
- `news_risk_high->unknown_1h` score `80.0608` n `108` status `ready` deltaP `-5.1951` edge `6.735` maxDD `-0.9571`
- `news_risk_high->crypto_alt_24h` score `17.2172` n `87` status `ready` deltaP `40.152` edge `1.2071` maxDD `-1.8676`
- `market_context_high->equity_24h` score `10.6157` n `85` status `ready` deltaP `21.8035` edge `1.015` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `5.591` n `108` status `ready` deltaP `21.189` edge `0.4633` maxDD `-7.4246`
- `market_context_high->index_24h` score `4.9908` n `85` status `ready` deltaP `44.0421` edge `0.1406` maxDD `-0.1315`
- `market_context_high->commodity_4h` score `1.7487` n `85` status `ready` deltaP `19.6934` edge `0.069` maxDD `-0.3651`
- `market_context_high->metal_4h` score `1.3468` n `85` status `ready` deltaP `16.7736` edge `0.0429` maxDD `-0.7323`
- `news_risk_high->crypto_alt_1h` score `0.914` n `108` status `ready` deltaP `9.3258` edge `0.1094` maxDD `-3.9659`
- `market_context_high->metal_1h` score `0.6725` n `85` status `ready` deltaP `9.8926` edge `0.0191` maxDD `-0.3209`
- `market_context_high->fx_4h` score `0.5802` n `85` status `ready` deltaP `12.8336` edge `0.0019` maxDD `-0.1285`
- `market_context_high->fx_1h` score `0.4493` n `85` status `ready` deltaP `11.4336` edge `-0.0002` maxDD `-0.1407`
- `market_context_high->equity_4h` score `0.3654` n `85` status `ready` deltaP `-0.5882` edge `0.1901` maxDD `-4.48`
- `market_context_high->equity_1h` score `0.317` n `85` status `ready` deltaP `3.3903` edge `0.1056` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `0.0688` n `85` status `ready` deltaP `5.8929` edge `0.0723` maxDD `-5.2213`
- `market_context_high->commodity_1h` score `-0.3332` n `85` status `ready` deltaP `-1.1236` edge `0.0162` maxDD `-0.4475`
- `market_context_high->index_1h` score `-0.4073` n `85` status `ready` deltaP `0.2888` edge `0.0017` maxDD `-1.1344`
- `market_context_high->metal_24h` score `-0.6657` n `85` status `ready` deltaP `4.9877` edge `0.1461` maxDD `-10.5088`
- `news_risk_high->index_1h` score `-0.7282` n `108` status `ready` deltaP `3.4043` edge `-0.0034` maxDD `-1.3981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
