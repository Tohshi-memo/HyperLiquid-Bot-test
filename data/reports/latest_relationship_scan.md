# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T21:22:28.015299+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4252`

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

- `market_context_high->unknown_1h` score `380.9371` n `50` status `ready` deltaP `12.3713` edge `31.6672` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `321.5538` n `50` status `ready` deltaP `12.6524` edge `26.7118` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `13.6716` n `50` status `ready` deltaP `29.286` edge `1.1144` maxDD `-11.6271`
- `market_context_high->crypto_major_24h` score `11.5547` n `50` status `ready` deltaP `37.1127` edge `0.8571` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `10.7236` n `62` status `ready` deltaP `29.9575` edge `0.7424` maxDD `-2.8784`
- `news_risk_high->crypto_major_4h` score `10.4073` n `68` status `ready` deltaP `37.7242` edge `0.6361` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.356` n `68` status `ready` deltaP `26.4617` edge `0.571` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.0074` n `50` status `ready` deltaP `16.0183` edge `0.5475` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.6394` n `50` status `ready` deltaP `15.5793` edge `0.495` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.5806` n `62` status `ready` deltaP `33.4629` edge `0.1745` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `3.8291` n `68` status `ready` deltaP `26.9637` edge `0.2006` maxDD `-2.9013`
- `market_context_high->fx_4h` score `3.0858` n `50` status `ready` deltaP `34.6707` edge `0.0395` maxDD `-0.0791`
- `market_context_high->crypto_alt_1h` score `3.0528` n `50` status `ready` deltaP `13.1557` edge `0.233` maxDD `-3.6376`
- `news_risk_high->index_4h` score `2.9595` n `68` status `ready` deltaP `32.3888` edge `0.0569` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.8875` n `68` status `ready` deltaP `12.9095` edge `0.1901` maxDD `-1.5096`
- `market_context_high->crypto_major_1h` score `2.8227` n `50` status `ready` deltaP `12.2036` edge `0.1989` maxDD `-2.2692`
- `news_risk_high->metal_4h` score `2.4368` n `68` status `ready` deltaP `20.9021` edge `0.1053` maxDD `-0.993`
- `news_risk_high->index_1h` score `1.9599` n `68` status `ready` deltaP `24.1987` edge `0.017` maxDD `-0.1997`
- `market_context_high->fx_1h` score `1.5825` n `50` status `ready` deltaP `21.988` edge `0.0117` maxDD `-0.113`
- `market_context_high->equity_24h` score `1.5425` n `50` status `ready` deltaP `9.2478` edge `0.3223` maxDD `-11.8957`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
