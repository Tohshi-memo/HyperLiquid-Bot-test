# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T02:22:26.593189+00:00`
- Price records: `672`
- Market context records: `4578`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9991`

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

- `market_context_high->unknown_1h` score `69.9462` n `157` status `ready` deltaP `6.7347` edge `5.834` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `3.4681` n `157` status `ready` deltaP `7.9122` edge `0.3573` maxDD `-4.6834`
- `market_context_high->fx_4h` score `-0.5665` n `157` status `ready` deltaP `5.0713` edge `0.0018` maxDD `-1.9927`
- `market_context_high->commodity_1h` score `-0.6584` n `157` status `ready` deltaP `0.8` edge `0.0194` maxDD `-2.0345`
- `market_context_high->fx_1h` score `-0.749` n `157` status `ready` deltaP `-0.5473` edge `-0.0033` maxDD `-1.1038`
- `market_context_high->equity_4h` score `-0.8184` n `157` status `ready` deltaP `2.1147` edge `0.0579` maxDD `-8.8203`
- `market_context_high->equity_1h` score `-0.8243` n `157` status `ready` deltaP `-2.4877` edge `0.0096` maxDD `-5.5624`
- `market_context_high->index_4h` score `-0.838` n `157` status `ready` deltaP `2.1963` edge `-0.0098` maxDD `-5.9823`
- `market_context_high->commodity_4h` score `-1.1899` n `157` status `ready` deltaP `3.6614` edge `0.0338` maxDD `-9.1941`
- `market_context_high->index_1h` score `-1.6187` n `157` status `ready` deltaP `-3.2743` edge `-0.0122` maxDD `-2.7358`
- `market_context_high->unknown_24h` score `-2.7018` n `155` status `ready` deltaP `1.5278` edge `-0.143` maxDD `-4.7201`
- `market_context_high->metal_1h` score `-2.9346` n `157` status `ready` deltaP `-4.2546` edge `-0.0827` maxDD `-17.8795`
- `market_context_high->index_24h` score `-5.3223` n `155` status `ready` deltaP `-7.5392` edge `-0.0946` maxDD `-29.3321`
- `market_context_high->fx_24h` score `-5.3463` n `155` status `ready` deltaP `-12.5101` edge `-0.0109` maxDD `-6.0982`
- `market_context_high->crypto_alt_1h` score `-5.5459` n `157` status `ready` deltaP `-2.8252` edge `-0.1146` maxDD `-22.2982`
- `market_context_high->commodity_24h` score `-5.8761` n `155` status `ready` deltaP `8.3815` edge `0.0389` maxDD `-34.0892`
- `market_context_high->crypto_major_1h` score `-6.7842` n `157` status `ready` deltaP `-6.3856` edge `-0.1475` maxDD `-27.356`
- `market_context_high->crypto_alt_4h` score `-9.053` n `157` status `ready` deltaP `-3.7974` edge `-0.2696` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-10.2138` n `157` status `ready` deltaP `-7.82` edge `-0.3356` maxDD `-67.4051`
- `market_context_high->crypto_major_4h` score `-11.9049` n `157` status `ready` deltaP `-3.2692` edge `-0.4101` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
