# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T06:51:36.984200+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7786`

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

- `market_context_high->unknown_4h` score `48.0431` n `99` status `ready` deltaP `0.6637` edge `4.0327` maxDD `-1.016`
- `market_context_high->unknown_1h` score `15.0753` n `111` status `ready` deltaP `3.9853` edge `1.2786` maxDD `-1.5781`
- `market_context_high->crypto_alt_24h` score `11.5905` n `35` status `ready` deltaP `31.7361` edge `0.8151` maxDD `-4.1975`
- `market_context_high->crypto_major_24h` score `3.3557` n `35` status `ready` deltaP `20.2926` edge `0.2503` maxDD `-5.8084`
- `market_context_high->commodity_24h` score `0.5684` n `35` status `ready` deltaP `11.8154` edge `0.085` maxDD `-3.6055`
- `market_context_high->fx_24h` score `-0.0219` n `35` status `ready` deltaP `9.7917` edge `0.0061` maxDD `-0.9352`
- `market_context_high->fx_1h` score `-0.0947` n `111` status `ready` deltaP `2.9954` edge `0.0028` maxDD `-0.1258`
- `market_context_high->fx_4h` score `-0.138` n `99` status `ready` deltaP `5.0783` edge `0.0083` maxDD `-0.4545`
- `market_context_high->commodity_1h` score `-0.4206` n `111` status `ready` deltaP `-1.6426` edge `0.0071` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.6205` n `111` status `ready` deltaP `-1.3595` edge `-0.0053` maxDD `-1.2155`
- `market_context_high->metal_1h` score `-0.6858` n `111` status `ready` deltaP `4.0405` edge `-0.0049` maxDD `-1.6682`
- `market_context_high->commodity_4h` score `-0.9172` n `99` status `ready` deltaP `-4.125` edge `0.0328` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-1.3831` n `111` status `ready` deltaP `1.8086` edge `-0.0313` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-1.9722` n `99` status `ready` deltaP `4.3144` edge `-0.0221` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.0044` n `99` status `ready` deltaP `-4.641` edge `-0.0386` maxDD `-4.3282`
- `market_context_high->metal_24h` score `-2.3324` n `35` status `ready` deltaP `-2.6637` edge `-0.0373` maxDD `-6.1446`
- `market_context_high->crypto_alt_1h` score `-2.9258` n `111` status `ready` deltaP `-1.2098` edge `-0.0567` maxDD `-11.3243`
- `market_context_high->equity_1h` score `-3.6973` n `111` status `ready` deltaP `1.0384` edge `-0.0877` maxDD `-12.1865`
- `market_context_high->crypto_major_4h` score `-5.819` n `99` status `ready` deltaP `-8.9293` edge `-0.1868` maxDD `-33.3092`
- `market_context_high->index_24h` score `-6.6278` n `35` status `ready` deltaP `-32.9514` edge `-0.2025` maxDD `-5.078`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
