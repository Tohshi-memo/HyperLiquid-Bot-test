# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T18:07:21.478613+00:00`
- Price records: `672`
- Market context records: `3098`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6921`

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

- `market_context_high->crypto_alt_24h` score `16.6021` n `82` status `ready` deltaP `14.3546` edge `2.5604` maxDD `-33.5432`
- `market_context_high->commodity_24h` score `15.1854` n `82` status `ready` deltaP `45.1008` edge `1.0076` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `14.9256` n `82` status `ready` deltaP `22.8447` edge `1.1403` maxDD `-1.9039`
- `market_context_high->index_24h` score `10.8676` n `82` status `ready` deltaP `32.5627` edge `0.9248` maxDD `-14.8998`
- `market_context_high->equity_24h` score `7.5418` n `82` status `ready` deltaP `18.4197` edge `1.3648` maxDD `-35.9896`
- `market_context_high->commodity_4h` score `3.0521` n `117` status `ready` deltaP `18.2015` edge `0.1788` maxDD `-1.9973`
- `market_context_high->unknown_4h` score `0.4644` n `117` status `ready` deltaP `5.8058` edge `0.0762` maxDD `-3.7631`
- `market_context_high->commodity_1h` score `-0.0877` n `120` status `ready` deltaP `1.2375` edge `0.0267` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.487` n `120` status `ready` deltaP `4.1467` edge `0.0162` maxDD `-4.5023`
- `market_context_high->fx_24h` score `-0.6403` n `82` status `ready` deltaP `3.54` edge `-0.0042` maxDD `-0.4876`
- `market_context_high->fx_1h` score `-0.6815` n `120` status `ready` deltaP `-7.2006` edge `-0.0021` maxDD `-0.3147`
- `market_context_high->crypto_alt_1h` score `-0.831` n `120` status `ready` deltaP `3.0788` edge `0.0859` maxDD `-14.7034`
- `market_context_high->equity_1h` score `-1.344` n `120` status `ready` deltaP `-3.1836` edge `-0.0025` maxDD `-8.8863`
- `market_context_high->fx_4h` score `-1.3569` n `117` status `ready` deltaP `-12.8232` edge `-0.0041` maxDD `-1.0829`
- `market_context_high->index_4h` score `-1.3958` n `117` status `ready` deltaP `10.1939` edge `0.044` maxDD `-17.6057`
- `market_context_high->crypto_major_1h` score `-2.2948` n `120` status `ready` deltaP `-1.5968` edge `0.0457` maxDD `-15.1032`
- `market_context_high->metal_1h` score `-2.4121` n `120` status `ready` deltaP `-7.3254` edge `-0.0128` maxDD `-7.4828`
- `market_context_high->unknown_1h` score `-2.6542` n `120` status `ready` deltaP `3.3084` edge `-0.0588` maxDD `-12.7554`
- `market_context_high->crypto_alt_4h` score `-3.826` n `117` status `ready` deltaP `12.8947` edge `0.228` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-4.1579` n `117` status `ready` deltaP `5.1582` edge `-0.0395` maxDD `-36.5699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
