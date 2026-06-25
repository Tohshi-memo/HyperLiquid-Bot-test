# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T13:13:44.662156+00:00`
- Price records: `672`
- Market context records: `4726`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7432`

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

- `market_context_high->unknown_1h` score `77.0959` n `144` status `ready` deltaP `14.9119` edge `6.367` maxDD `-1.674`
- `market_context_high->unknown_4h` score `5.7942` n `144` status `ready` deltaP `15.0745` edge `0.5034` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `3.2653` n `135` status `ready` deltaP `16.7014` edge `0.2531` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.2968` n `144` status `ready` deltaP `2.4077` edge `0.0255` maxDD `-2.0345`
- `market_context_high->index_4h` score `-0.632` n `144` status `ready` deltaP `4.9289` edge `-0.0016` maxDD `-5.9823`
- `market_context_high->commodity_4h` score `-0.8442` n `144` status `ready` deltaP `9.7391` edge `0.0376` maxDD `-9.1941`
- `market_context_high->fx_4h` score `-0.8986` n `144` status `ready` deltaP `-0.7452` edge `-0.002` maxDD `-1.9927`
- `market_context_high->equity_4h` score `-0.9337` n `144` status `ready` deltaP `3.5569` edge `0.0335` maxDD `-8.8203`
- `market_context_high->equity_1h` score `-1.1198` n `144` status `ready` deltaP `-1.4429` edge `0.015` maxDD `-5.5624`
- `market_context_high->fx_1h` score `-1.2828` n `144` status `ready` deltaP `-4.9859` edge `-0.0057` maxDD `-1.1038`
- `market_context_high->index_1h` score `-1.5798` n `144` status `ready` deltaP `-3.4847` edge `-0.008` maxDD `-2.6999`
- `market_context_high->crypto_alt_1h` score `-3.1083` n `144` status `ready` deltaP `-0.341` edge `-0.0675` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-3.5734` n `144` status `ready` deltaP `-0.3826` edge `-0.0803` maxDD `-27.356`
- `market_context_high->commodity_24h` score `-4.4418` n `135` status `ready` deltaP `16.9328` edge `0.0674` maxDD `-30.7016`
- `market_context_high->metal_1h` score `-4.5049` n `144` status `ready` deltaP `-5.9257` edge `-0.0791` maxDD `-17.2107`
- `market_context_high->fx_24h` score `-4.8569` n `135` status `ready` deltaP `-13.5648` edge `-0.0183` maxDD `-5.3476`
- `market_context_high->crypto_alt_4h` score `-7.9651` n `144` status `ready` deltaP `-2.0326` edge `-0.1419` maxDD `-63.9243`
- `market_context_high->index_24h` score `-8.581` n `135` status `ready` deltaP `-11.5046` edge `-0.1009` maxDD `-29.3321`
- `market_context_high->metal_4h` score `-8.8066` n `144` status `ready` deltaP `1.8293` edge `-0.2559` maxDD `-64.494`
- `market_context_high->crypto_major_4h` score `-10.4577` n `144` status `ready` deltaP `-1.0501` edge `-0.2437` maxDD `-81.8692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
