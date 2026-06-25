# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T07:07:29.077090+00:00`
- Price records: `672`
- Market context records: `4700`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9704`

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

- `market_context_high->unknown_1h` score `77.474` n `144` status `ready` deltaP `13.7143` edge `6.4065` maxDD `-1.674`
- `market_context_high->unknown_4h` score `5.2956` n `135` status `ready` deltaP `11.5267` edge `0.4855` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `2.4876` n `135` status `ready` deltaP `13.0556` edge `0.2126` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.3225` n `144` status `ready` deltaP `2.258` edge `0.0232` maxDD `-2.0345`
- `market_context_high->index_4h` score `-0.7899` n `135` status `ready` deltaP `3.6168` edge `-0.0131` maxDD `-5.9823`
- `market_context_high->fx_4h` score `-0.9014` n `135` status `ready` deltaP `-0.8729` edge `-0.0015` maxDD `-1.9927`
- `market_context_high->equity_1h` score `-1.1798` n `144` status `ready` deltaP `-1.5926` edge `0.011` maxDD `-5.5624`
- `market_context_high->commodity_4h` score `-1.2163` n `135` status `ready` deltaP `5.7035` edge `0.0168` maxDD `-9.1941`
- `market_context_high->fx_1h` score `-1.3188` n `144` status `ready` deltaP `-5.435` edge `-0.0057` maxDD `-1.1038`
- `market_context_high->equity_4h` score `-1.355` n `135` status `ready` deltaP `0.4799` edge `0.0` maxDD `-8.8203`
- `market_context_high->index_1h` score `-1.6996` n `144` status `ready` deltaP `-4.5326` edge `-0.011` maxDD `-2.6999`
- `market_context_high->crypto_alt_1h` score `-3.3344` n `144` status `ready` deltaP `-1.838` edge `-0.0865` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-3.9` n `144` status `ready` deltaP `-2.6281` edge `-0.1072` maxDD `-27.356`
- `market_context_high->metal_1h` score `-4.4389` n `144` status `ready` deltaP `-5.4766` edge `-0.0766` maxDD `-17.2107`
- `market_context_high->commodity_24h` score `-4.6004` n `135` status `ready` deltaP `15.3703` edge `0.0646` maxDD `-30.7016`
- `market_context_high->fx_24h` score `-4.7877` n `135` status `ready` deltaP `-13.044` edge `-0.016` maxDD `-5.3476`
- `market_context_high->index_24h` score `-8.4047` n `135` status `ready` deltaP `-10.6366` edge `-0.092` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-8.5838` n `135` status `ready` deltaP `-3.1595` edge `-0.2137` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-9.0686` n `135` status `ready` deltaP `0.061` edge `-0.2777` maxDD `-64.494`
- `market_context_high->crypto_major_4h` score `-11.5346` n `135` status `ready` deltaP `-3.5953` edge `-0.3648` maxDD `-81.8692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
