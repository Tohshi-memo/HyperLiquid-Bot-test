# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T06:52:32.236780+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9644`

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

- `market_context_high->unknown_4h` score `77.067` n `140` status `ready` deltaP `3.5104` edge `6.4324` maxDD `-1.0178`
- `market_context_high->unknown_1h` score `23.2906` n `140` status `ready` deltaP `0.5561` edge `1.9861` maxDD `-1.5807`
- `market_context_high->index_24h` score `0.6406` n `120` status `ready` deltaP `22.4538` edge `0.0278` maxDD `-2.6288`
- `market_context_high->fx_1h` score `0.4616` n `140` status `ready` deltaP `10.633` edge `0.0034` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.4529` n `140` status `ready` deltaP `13.1533` edge `0.0099` maxDD `-0.4545`
- `market_context_high->metal_1h` score `0.0661` n `140` status `ready` deltaP `10.8383` edge `0.0109` maxDD `-1.3073`
- `market_context_high->metal_24h` score `-0.086` n `120` status `ready` deltaP `18.6641` edge `0.1171` maxDD `-6.204`
- `market_context_high->commodity_1h` score `-0.1385` n `140` status `ready` deltaP `3.6185` edge `0.0144` maxDD `-1.0053`
- `market_context_high->fx_24h` score `-0.3797` n `120` status `ready` deltaP `12.8929` edge `0.0226` maxDD `-1.2451`
- `market_context_high->crypto_major_1h` score `-0.4703` n `140` status `ready` deltaP `5.8511` edge `0.029` maxDD `-6.9306`
- `market_context_high->commodity_4h` score `-0.6063` n `140` status `ready` deltaP `4.9608` edge `0.0393` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.6453` n `140` status `ready` deltaP `-0.911` edge `-0.0036` maxDD `-1.8448`
- `market_context_high->metal_4h` score `-0.8098` n `140` status `ready` deltaP `8.9373` edge `0.0008` maxDD `-4.8031`
- `market_context_high->equity_1h` score `-1.7323` n `140` status `ready` deltaP `1.5184` edge `-0.0085` maxDD `-11.8972`
- `market_context_high->crypto_alt_1h` score `-1.969` n `140` status `ready` deltaP `-0.5561` edge `-0.0043` maxDD `-12.8878`
- `market_context_high->equity_24h` score `-2.8048` n `120` status `ready` deltaP `1.0341` edge `-0.0346` maxDD `-18.5503`
- `market_context_high->index_4h` score `-2.9582` n `140` status `ready` deltaP `-4.7039` edge `-0.0254` maxDD `-6.1805`
- `market_context_high->crypto_major_4h` score `-3.7587` n `140` status `ready` deltaP `2.6481` edge `-0.062` maxDD `-27.67`
- `market_context_high->crypto_major_24h` score `-4.462` n `120` status `ready` deltaP `0.1603` edge `-0.0874` maxDD `-29.1905`
- `market_context_high->equity_4h` score `-5.5219` n `140` status `ready` deltaP `2.1734` edge `-0.1316` maxDD `-38.933`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
