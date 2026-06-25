# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T01:52:26.662422+00:00`
- Price records: `672`
- Market context records: `4679`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9870`

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

- `market_context_high->unknown_1h` score `78.7357` n `135` status `ready` deltaP `12.3254` edge `6.5209` maxDD `-1.674`
- `market_context_high->unknown_4h` score `4.9847` n `135` status `ready` deltaP `10.4596` edge `0.4667` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `1.5084` n `135` status `ready` deltaP `9.4098` edge `0.1553` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.523` n `135` status `ready` deltaP `1.6068` edge `0.0253` maxDD `-2.0345`
- `market_context_high->index_4h` score `-0.8641` n `135` status `ready` deltaP `2.5497` edge `-0.0155` maxDD `-5.9823`
- `market_context_high->equity_1h` score `-0.8789` n `135` status `ready` deltaP `-3.0417` edge `0.0063` maxDD `-5.5624`
- `market_context_high->fx_4h` score `-0.9126` n `135` status `ready` deltaP `-1.1778` edge `-0.0009` maxDD `-1.9927`
- `market_context_high->fx_1h` score `-1.0598` n `135` status `ready` deltaP `-4.1927` edge `-0.0049` maxDD `-1.1038`
- `market_context_high->commodity_4h` score `-1.2253` n `135` status `ready` deltaP `5.2462` edge `0.0187` maxDD `-9.1941`
- `market_context_high->equity_4h` score `-1.4093` n `135` status `ready` deltaP `-0.1298` edge `-0.0029` maxDD `-8.8203`
- `market_context_high->index_1h` score `-1.7768` n `135` status `ready` deltaP `-5.1375` edge `-0.0134` maxDD `-2.6999`
- `market_context_high->metal_1h` score `-2.8481` n `135` status `ready` deltaP `-4.3269` edge `-0.0795` maxDD `-17.2107`
- `market_context_high->fx_24h` score `-4.5205` n `135` status `ready` deltaP `-10.4398` edge `-0.0111` maxDD `-5.3476`
- `market_context_high->commodity_24h` score `-5.1955` n `135` status `ready` deltaP `12.0717` edge `0.037` maxDD `-30.7016`
- `market_context_high->crypto_alt_1h` score `-5.6024` n `135` status `ready` deltaP `-2.6004` edge `-0.1208` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.7431` n `135` status `ready` deltaP `-5.4059` edge `-0.1506` maxDD `-27.356`
- `market_context_high->index_24h` score `-8.3567` n `135` status `ready` deltaP `-10.6366` edge `-0.088` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-8.7273` n `135` status `ready` deltaP `-4.0741` edge `-0.226` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-9.3364` n `135` status `ready` deltaP `-2.2256` edge `-0.2968` maxDD `-64.494`
- `market_context_high->crypto_major_4h` score `-11.7294` n `135` status `ready` deltaP `-4.205` edge `-0.3857` maxDD `-81.8692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
