# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T19:52:29.900779+00:00`
- Price records: `672`
- Market context records: `4754`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7476`

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

- `market_context_high->unknown_1h` score `82.1635` n `138` status `ready` deltaP `13.3971` edge `6.7994` maxDD `-1.674`
- `market_context_high->unknown_4h` score `6.0392` n `135` status `ready` deltaP `13.4869` edge `0.5344` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `3.1837` n `123` status `ready` deltaP `15.5318` edge `0.2541` maxDD `-4.7201`
- `market_context_high->index_4h` score `-0.3981` n `135` status `ready` deltaP `7.3419` edge `0.0069` maxDD `-5.5505`
- `market_context_high->commodity_1h` score `-0.4926` n `138` status `ready` deltaP `2.4668` edge `0.0221` maxDD `-2.0345`
- `market_context_high->equity_4h` score `-0.5589` n `135` status `ready` deltaP `6.2748` edge `0.0551` maxDD `-8.8203`
- `market_context_high->fx_4h` score `-0.8714` n `135` status `ready` deltaP `-1.0682` edge `-0.0027` maxDD `-1.8185`
- `market_context_high->equity_1h` score `-0.9232` n `138` status `ready` deltaP `-1.3234` edge `-0.0146` maxDD `-5.262`
- `market_context_high->fx_1h` score `-1.221` n `138` status `ready` deltaP `-4.5518` edge `-0.0049` maxDD `-0.9869`
- `market_context_high->commodity_4h` score `-1.4215` n `135` status `ready` deltaP `7.5993` edge `0.0213` maxDD `-8.9`
- `market_context_high->index_1h` score `-1.4586` n `138` status `ready` deltaP `-2.1197` edge `-0.007` maxDD `-2.6999`
- `market_context_high->metal_1h` score `-2.4923` n `138` status `ready` deltaP `-2.7792` edge `-0.068` maxDD `-15.3067`
- `market_context_high->commodity_24h` score `-2.6066` n `123` status `ready` deltaP `16.7259` edge `0.0652` maxDD `-27.5371`
- `market_context_high->crypto_alt_1h` score `-2.7459` n `138` status `ready` deltaP `-0.5511` edge `-0.0505` maxDD `-19.8288`
- `market_context_high->crypto_major_1h` score `-3.2403` n `138` status `ready` deltaP `0.0716` edge `-0.0728` maxDD `-24.7815`
- `market_context_high->fx_24h` score `-4.3507` n `123` status `ready` deltaP `-15.5784` edge `-0.0221` maxDD `-4.595`
- `market_context_high->crypto_alt_4h` score `-5.6785` n `135` status `ready` deltaP `1.3064` edge `-0.0454` maxDD `-49.9721`
- `market_context_high->index_24h` score `-7.2929` n `123` status `ready` deltaP `-11.9283` edge `-0.1157` maxDD `-23.3351`
- `market_context_high->crypto_major_4h` score `-8.2396` n `135` status `ready` deltaP `2.3735` edge `-0.1432` maxDD `-68.9854`
- `market_context_high->metal_4h` score `-8.3528` n `135` status `ready` deltaP `3.7669` edge `-0.2719` maxDD `-61.2596`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
