# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T05:52:31.404626+00:00`
- Price records: `672`
- Market context records: `4695`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9766`

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

- `market_context_high->unknown_1h` score `79.6801` n `139` status `ready` deltaP `13.1349` edge `6.5942` maxDD `-1.674`
- `market_context_high->unknown_4h` score `5.2` n `135` status `ready` deltaP `10.9169` edge `0.4816` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `2.3078` n `135` status `ready` deltaP `12.1875` edge `0.2034` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.3693` n `139` status `ready` deltaP `1.4033` edge `0.0229` maxDD `-2.0345`
- `market_context_high->index_4h` score `-0.7804` n `135` status `ready` deltaP `3.7692` edge `-0.0129` maxDD `-5.9823`
- `market_context_high->fx_4h` score `-0.9354` n `135` status `ready` deltaP `-1.4826` edge `-0.0018` maxDD `-1.9927`
- `market_context_high->equity_1h` score `-1.147` n `139` status `ready` deltaP `-1.5282` edge `0.0133` maxDD `-5.5624`
- `market_context_high->fx_1h` score `-1.2075` n `139` status `ready` deltaP `-5.2794` edge `-0.0058` maxDD `-1.1038`
- `market_context_high->commodity_4h` score `-1.2336` n `135` status `ready` deltaP `5.5511` edge `0.0156` maxDD `-9.1941`
- `market_context_high->equity_4h` score `-1.2748` n `135` status `ready` deltaP `1.2421` edge `0.0052` maxDD `-8.8203`
- `market_context_high->index_1h` score `-1.6628` n `139` status `ready` deltaP `-4.0731` edge `-0.011` maxDD `-2.6999`
- `market_context_high->metal_1h` score `-2.8323` n `139` status `ready` deltaP `-4.5018` edge `-0.0763` maxDD `-17.2107`
- `market_context_high->crypto_alt_1h` score `-3.3159` n `139` status `ready` deltaP `-1.1082` edge `-0.089` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-4.0347` n `139` status `ready` deltaP `-3.6574` edge `-0.1176` maxDD `-27.356`
- `market_context_high->commodity_24h` score `-4.6949` n `135` status `ready` deltaP `14.8495` edge `0.0602` maxDD `-30.7016`
- `market_context_high->fx_24h` score `-4.7841` n `135` status `ready` deltaP `-13.044` edge `-0.0157` maxDD `-5.3476`
- `market_context_high->index_24h` score `-8.3987` n `135` status `ready` deltaP `-10.6366` edge `-0.0915` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-8.6243` n `135` status `ready` deltaP `-3.1595` edge `-0.2189` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-9.1229` n `135` status `ready` deltaP `-0.5488` edge `-0.2806` maxDD `-64.494`
- `market_context_high->crypto_major_4h` score `-11.5955` n `135` status `ready` deltaP `-3.5953` edge `-0.3726` maxDD `-81.8692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
