# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T06:22:34.460341+00:00`
- Price records: `672`
- Market context records: `4697`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9752`

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

- `market_context_high->unknown_1h` score `79.628` n `141` status `ready` deltaP `13.5941` edge `6.5868` maxDD `-1.674`
- `market_context_high->unknown_4h` score `5.2218` n `135` status `ready` deltaP `11.0693` edge `0.4824` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `2.3848` n `135` status `ready` deltaP `12.5348` edge `0.2075` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.3778` n `141` status `ready` deltaP `1.2995` edge `0.0225` maxDD `-2.0345`
- `market_context_high->index_4h` score `-0.7907` n `135` status `ready` deltaP `3.6168` edge `-0.0132` maxDD `-5.9823`
- `market_context_high->fx_4h` score `-0.9188` n `135` status `ready` deltaP `-1.1778` edge `-0.0017` maxDD `-1.9927`
- `market_context_high->index_1h` score `-1.0564` n `141` status `ready` deltaP `-3.648` edge `-0.0107` maxDD `-2.6999`
- `market_context_high->equity_1h` score `-1.1202` n `141` status `ready` deltaP `-1.1031` edge `0.0127` maxDD `-5.5624`
- `market_context_high->commodity_4h` score `-1.2312` n `135` status `ready` deltaP `5.5511` edge `0.0159` maxDD `-9.1941`
- `market_context_high->equity_4h` score `-1.3086` n `135` status `ready` deltaP `0.9373` edge `0.0029` maxDD `-8.8203`
- `market_context_high->fx_1h` score `-1.3321` n `141` status `ready` deltaP `-5.5718` edge `-0.0059` maxDD `-1.1038`
- `market_context_high->metal_1h` score `-2.8446` n `141` status `ready` deltaP `-4.7841` edge `-0.076` maxDD `-17.2107`
- `market_context_high->crypto_alt_1h` score `-3.3016` n `141` status `ready` deltaP `-1.1031` edge `-0.0872` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-4.0029` n `141` status `ready` deltaP `-3.6013` edge `-0.1139` maxDD `-27.356`
- `market_context_high->commodity_24h` score `-4.6606` n `135` status `ready` deltaP `15.0231` edge `0.0619` maxDD `-30.7016`
- `market_context_high->fx_24h` score `-4.7877` n `135` status `ready` deltaP `-13.044` edge `-0.016` maxDD `-5.3476`
- `market_context_high->index_24h` score `-8.4047` n `135` status `ready` deltaP `-10.6366` edge `-0.092` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-8.6158` n `135` status `ready` deltaP `-3.1595` edge `-0.2178` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-9.1095` n `135` status `ready` deltaP `-0.3963` edge `-0.2799` maxDD `-64.494`
- `market_context_high->crypto_major_4h` score `-11.5775` n `135` status `ready` deltaP `-3.5953` edge `-0.3703` maxDD `-81.8692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
