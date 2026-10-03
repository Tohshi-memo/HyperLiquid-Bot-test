# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T19:52:31.521667+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4248`

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

- `market_context_high->unknown_1h` score `377.5856` n `50` status `ready` deltaP `11.9222` edge `31.3909` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `318.2226` n `50` status `ready` deltaP `12.6524` edge `26.4342` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `13.8828` n `50` status `ready` deltaP `29.286` edge `1.132` maxDD `-11.6271`
- `market_context_high->crypto_major_24h` score `11.6507` n `50` status `ready` deltaP `37.1127` edge `0.8651` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `10.6936` n `62` status `ready` deltaP `29.9575` edge `0.7399` maxDD `-2.8784`
- `news_risk_high->crypto_major_4h` score `10.3661` n `68` status `ready` deltaP `37.4193` edge `0.6347` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.3572` n `68` status `ready` deltaP `26.4617` edge `0.5711` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `6.9662` n `50` status `ready` deltaP `15.7134` edge `0.5461` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.6406` n `50` status `ready` deltaP `15.5793` edge `0.4951` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.5794` n `62` status `ready` deltaP `33.4629` edge `0.1744` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `3.8291` n `68` status `ready` deltaP `26.9637` edge `0.2006` maxDD `-2.9013`
- `market_context_high->fx_4h` score `3.098` n `50` status `ready` deltaP `34.8232` edge `0.0395` maxDD `-0.0791`
- `market_context_high->crypto_alt_1h` score `3.0948` n `50` status `ready` deltaP `13.3054` edge `0.2355` maxDD `-3.6376`
- `news_risk_high->index_4h` score `2.9729` n `68` status `ready` deltaP `32.5413` edge `0.057` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.8791` n `68` status `ready` deltaP `12.9095` edge `0.1894` maxDD `-1.5096`
- `market_context_high->crypto_major_1h` score `2.8143` n `50` status `ready` deltaP `12.2036` edge `0.1982` maxDD `-2.2692`
- `news_risk_high->metal_4h` score `2.399` n `68` status `ready` deltaP `20.4448` edge `0.1052` maxDD `-0.993`
- `news_risk_high->index_1h` score `1.9599` n `68` status `ready` deltaP `24.1987` edge `0.017` maxDD `-0.1997`
- `market_context_high->fx_1h` score `1.6316` n `50` status `ready` deltaP `22.5868` edge `0.0118` maxDD `-0.113`
- `market_context_high->equity_24h` score `1.523` n `50` status `ready` deltaP `9.2478` edge `0.3198` maxDD `-11.8957`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
