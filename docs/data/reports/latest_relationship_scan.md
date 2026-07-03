# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T01:37:27.274546+00:00`
- Price records: `672`
- Market context records: `5512`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11468`

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

- `market_context_high->equity_24h` score `2.8059` n `190` status `ready` deltaP `11.7928` edge `0.6631` maxDD `-31.6316`
- `market_context_high->crypto_major_24h` score `2.6952` n `190` status `ready` deltaP `16.2189` edge `0.5705` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `2.3821` n `193` status `ready` deltaP `13.8838` edge `0.3352` maxDD `-14.0065`
- `market_context_high->equity_4h` score `2.0538` n `193` status `ready` deltaP `10.7726` edge `0.2632` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `1.8407` n `193` status `ready` deltaP `9.3414` edge `0.2552` maxDD `-9.46`
- `market_context_high->fx_24h` score `0.3874` n `190` status `ready` deltaP `12.9312` edge `0.0388` maxDD `-1.0847`
- `market_context_high->equity_1h` score `0.3768` n `193` status `ready` deltaP `8.1343` edge `0.0737` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.0828` n `193` status `ready` deltaP `6.0966` edge `0.0156` maxDD `-0.9472`
- `market_context_high->fx_1h` score `-0.3556` n `193` status `ready` deltaP `0.4778` edge `0.0001` maxDD `-0.577`
- `market_context_high->crypto_alt_1h` score `-0.4427` n `193` status `ready` deltaP `0.6849` edge `0.0547` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.5686` n `193` status `ready` deltaP `2.2742` edge `0.062` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.6698` n `193` status `ready` deltaP `0.6159` edge `0.0076` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.837` n `193` status `ready` deltaP `3.3663` edge `0.0059` maxDD `-1.5143`
- `market_context_high->index_4h` score `-1.0323` n `193` status `ready` deltaP `5.6845` edge `0.037` maxDD `-2.874`
- `market_context_high->commodity_1h` score `-1.5279` n `193` status `ready` deltaP `-3.4253` edge `-0.0097` maxDD `-3.5831`
- `market_context_high->index_24h` score `-1.8294` n `190` status `ready` deltaP `14.2708` edge `0.069` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.9975` n `193` status `ready` deltaP `-11.7804` edge `-0.0533` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.5685` n `193` status `ready` deltaP `-8.9433` edge `-0.0538` maxDD `-14.0497`
- `market_context_high->metal_24h` score `-7.315` n `190` status `ready` deltaP `-4.2379` edge `-0.1718` maxDD `-33.021`
- `market_context_high->crypto_alt_24h` score `-7.3286` n `190` status `ready` deltaP `7.2442` edge `0.2107` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
