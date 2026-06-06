# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T17:07:22.500030+00:00`
- Price records: `672`
- Market context records: `3094`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6911`

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

- `market_context_high->crypto_alt_24h` score `16.6336` n `84` status `ready` deltaP `13.5416` edge `2.5425` maxDD `-31.3547`
- `market_context_high->commodity_24h` score `15.1343` n `84` status `ready` deltaP `45.3621` edge `1.0016` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `14.7185` n `84` status `ready` deltaP `22.9911` edge `1.1209` maxDD `-1.8109`
- `market_context_high->index_24h` score `11.1789` n `84` status `ready` deltaP `33.5813` edge `0.9277` maxDD `-13.9336`
- `market_context_high->equity_24h` score `8.1701` n `84` status `ready` deltaP `19.9901` edge `1.4063` maxDD `-34.0363`
- `market_context_high->commodity_4h` score `3.0281` n `117` status `ready` deltaP `18.2015` edge `0.1768` maxDD `-1.9973`
- `market_context_high->unknown_4h` score `0.7216` n `117` status `ready` deltaP `5.1035` edge `0.1042` maxDD `-2.914`
- `market_context_high->commodity_1h` score `-0.0438` n `123` status `ready` deltaP `1.8621` edge `0.0262` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.5276` n `123` status `ready` deltaP `3.3798` edge `0.0161` maxDD `-4.5023`
- `market_context_high->fx_1h` score `-0.7089` n `123` status `ready` deltaP `-7.7881` edge `-0.0017` maxDD `-0.3147`
- `market_context_high->crypto_alt_1h` score `-0.7717` n `123` status `ready` deltaP `3.6792` edge `0.0895` maxDD `-14.7034`
- `market_context_high->fx_24h` score `-0.8815` n `84` status `ready` deltaP `2.4057` edge `-0.0043` maxDD `-0.4822`
- `market_context_high->equity_1h` score `-1.2911` n `123` status `ready` deltaP `-2.3319` edge `-0.0014` maxDD `-8.8863`
- `market_context_high->fx_4h` score `-1.3709` n `117` status `ready` deltaP `-12.8232` edge `-0.0059` maxDD `-1.0829`
- `market_context_high->index_4h` score `-1.4283` n `117` status `ready` deltaP `9.6441` edge `0.0435` maxDD `-17.6057`
- `market_context_high->crypto_major_1h` score `-2.1593` n `123` status `ready` deltaP `-0.6232` edge `0.0505` maxDD `-15.1032`
- `market_context_high->metal_1h` score `-2.3679` n `123` status `ready` deltaP `-6.9982` edge `-0.0113` maxDD `-7.4828`
- `market_context_high->unknown_1h` score `-2.8349` n `123` status `ready` deltaP `2.2054` edge `-0.0665` maxDD `-12.7554`
- `market_context_high->crypto_alt_4h` score `-3.477` n `117` status `ready` deltaP `15.0016` edge `0.2587` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-3.9604` n `117` status `ready` deltaP `7.1126` edge `-0.0313` maxDD `-36.242`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
