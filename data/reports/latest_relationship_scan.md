# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T02:52:32.687493+00:00`
- Price records: `672`
- Market context records: `4683`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9736`

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

- `market_context_high->unknown_1h` score `78.7034` n `135` status `ready` deltaP `12.026` edge `6.5202` maxDD `-1.674`
- `market_context_high->unknown_4h` score `5.1052` n `135` status `ready` deltaP `10.9169` edge `0.4737` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `1.6971` n `135` status `ready` deltaP `10.1042` edge `0.1664` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.4895` n `135` status `ready` deltaP `1.9062` edge `0.0261` maxDD `-2.0345`
- `market_context_high->index_4h` score `-0.8207` n `135` status `ready` deltaP `3.1595` edge `-0.014` maxDD `-5.9823`
- `market_context_high->equity_1h` score `-0.8789` n `135` status `ready` deltaP `-3.0417` edge `0.0063` maxDD `-5.5624`
- `market_context_high->fx_4h` score `-0.9418` n `135` status `ready` deltaP `-1.6351` edge `-0.0016` maxDD `-1.9927`
- `market_context_high->fx_1h` score `-1.073` n `135` status `ready` deltaP `-4.3424` edge `-0.005` maxDD `-1.1038`
- `market_context_high->commodity_4h` score `-1.2362` n `135` status `ready` deltaP `5.2462` edge `0.0173` maxDD `-9.1941`
- `market_context_high->equity_4h` score `-1.3472` n `135` status `ready` deltaP `0.4799` edge `0.001` maxDD `-8.8203`
- `market_context_high->index_1h` score `-1.7888` n `135` status `ready` deltaP `-5.2872` edge `-0.0134` maxDD `-2.6999`
- `market_context_high->metal_1h` score `-2.8513` n `135` status `ready` deltaP `-4.3269` edge `-0.0799` maxDD `-17.2107`
- `market_context_high->fx_24h` score `-4.5905` n `135` status `ready` deltaP `-11.1343` edge `-0.0123` maxDD `-5.3476`
- `market_context_high->commodity_24h` score `-5.0715` n `135` status `ready` deltaP `12.7662` edge `0.0427` maxDD `-30.7016`
- `market_context_high->crypto_alt_1h` score `-5.588` n `135` status `ready` deltaP `-2.6004` edge `-0.1196` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.7407` n `135` status `ready` deltaP `-5.4059` edge `-0.1504` maxDD `-27.356`
- `market_context_high->index_24h` score `-8.3495` n `135` status `ready` deltaP `-10.6366` edge `-0.0874` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-8.6958` n `135` status `ready` deltaP `-3.7692` edge `-0.224` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-9.2798` n `135` status `ready` deltaP `-1.6159` edge `-0.2936` maxDD `-64.494`
- `market_context_high->crypto_major_4h` score `-11.7326` n `135` status `ready` deltaP `-4.3575` edge `-0.3851` maxDD `-81.8692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
