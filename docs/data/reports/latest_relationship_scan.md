# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T03:22:30.004767+00:00`
- Price records: `672`
- Market context records: `4685`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9742`

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

- `market_context_high->unknown_1h` score `78.701` n `135` status `ready` deltaP `12.026` edge `6.52` maxDD `-1.674`
- `market_context_high->unknown_4h` score `5.1364` n `135` status `ready` deltaP `10.9169` edge `0.4763` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `1.7861` n `135` status `ready` deltaP `10.4514` edge `0.1715` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.4907` n `135` status `ready` deltaP `1.9062` edge `0.026` maxDD `-2.0345`
- `market_context_high->index_4h` score `-0.8002` n `135` status `ready` deltaP `3.4643` edge `-0.0134` maxDD `-5.9823`
- `market_context_high->equity_1h` score `-0.8882` n `135` status `ready` deltaP `-3.1914` edge `0.0061` maxDD `-5.5624`
- `market_context_high->fx_4h` score `-0.9434` n `135` status `ready` deltaP `-1.6351` edge `-0.0018` maxDD `-1.9927`
- `market_context_high->fx_1h` score `-1.0478` n `135` status `ready` deltaP `-4.043` edge `-0.0049` maxDD `-1.1038`
- `market_context_high->commodity_4h` score `-1.2432` n `135` status `ready` deltaP `5.2462` edge `0.0164` maxDD `-9.1941`
- `market_context_high->equity_4h` score `-1.3165` n `135` status `ready` deltaP `0.7848` edge `0.0029` maxDD `-8.8203`
- `market_context_high->index_1h` score `-1.8151` n `135` status `ready` deltaP `-5.5866` edge `-0.0136` maxDD `-2.6999`
- `market_context_high->metal_1h` score `-2.8661` n `135` status `ready` deltaP `-4.4766` edge `-0.0808` maxDD `-17.2107`
- `market_context_high->fx_24h` score `-4.6243` n `135` status `ready` deltaP `-11.4815` edge `-0.0128` maxDD `-5.3476`
- `market_context_high->commodity_24h` score `-5.0162` n `135` status `ready` deltaP `13.1134` edge `0.045` maxDD `-30.7016`
- `market_context_high->crypto_alt_1h` score `-5.57` n `135` status `ready` deltaP `-2.4507` edge `-0.1191` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.7371` n `135` status `ready` deltaP `-5.4059` edge `-0.1501` maxDD `-27.356`
- `market_context_high->index_24h` score `-8.3639` n `135` status `ready` deltaP `-10.6366` edge `-0.0886` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-8.6887` n `135` status `ready` deltaP `-3.6168` edge `-0.2241` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-9.2499` n `135` status `ready` deltaP `-1.311` edge `-0.2918` maxDD `-64.494`
- `market_context_high->crypto_major_4h` score `-11.7295` n `135` status `ready` deltaP `-4.3575` edge `-0.3847` maxDD `-81.8692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
