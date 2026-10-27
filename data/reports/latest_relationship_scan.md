# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T14:37:31.090283+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8856`

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

- `market_context_high->unknown_4h` score `80.3338` n `135` status `ready` deltaP `4.5472` edge `6.6794` maxDD `-0.5521`
- `market_context_high->unknown_1h` score `14.964` n `135` status `ready` deltaP `0.9193` edge `1.2898` maxDD `-1.5807`
- `market_context_high->index_24h` score `2.0143` n `135` status `ready` deltaP `27.1875` edge `0.0554` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.4943` n `135` status `ready` deltaP `11.0557` edge `0.0033` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.3556` n `135` status `ready` deltaP `11.9817` edge `0.0096` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.0116` n `135` status `ready` deltaP `9.5975` edge `0.0092` maxDD `-1.3073`
- `market_context_high->commodity_1h` score `-0.271` n `135` status `ready` deltaP `2.4274` edge `0.0113` maxDD `-1.0053`
- `market_context_high->crypto_major_1h` score `-0.4747` n `135` status `ready` deltaP `5.886` edge `0.0282` maxDD `-6.9306`
- `market_context_high->commodity_4h` score `-0.5552` n `135` status `ready` deltaP `5.0124` edge `0.0422` maxDD `-1.0837`
- `market_context_high->index_1h` score `-0.5609` n `135` status `ready` deltaP `-0.2129` edge `-0.0022` maxDD `-1.4631`
- `market_context_high->fx_24h` score `-0.672` n `135` status `ready` deltaP `7.9167` edge `0.0183` maxDD `-1.2451`
- `market_context_high->metal_4h` score `-0.8062` n `135` status `ready` deltaP `8.0137` edge `-0.0027` maxDD `-4.6603`
- `market_context_high->metal_24h` score `-0.9537` n `135` status `ready` deltaP `16.0995` edge `0.091` maxDD `-8.2244`
- `market_context_high->equity_1h` score `-1.423` n `135` status `ready` deltaP `2.0403` edge `-0.0048` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.9289` n `135` status `ready` deltaP `-0.8916` edge `-0.005` maxDD `-12.2409`
- `market_context_high->equity_24h` score `-1.9794` n `135` status `ready` deltaP `8.0671` edge `0.0777` maxDD `-15.7143`
- `market_context_high->index_4h` score `-2.7229` n `135` status `ready` deltaP `-5.4032` edge `-0.0287` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.7226` n `135` status `ready` deltaP `3.5072` edge `-0.0687` maxDD `-27.2215`
- `market_context_high->crypto_major_24h` score `-4.0696` n `135` status `ready` deltaP `0.3704` edge `-0.0385` maxDD `-29.1905`
- `market_context_high->equity_4h` score `-5.1488` n `135` status `ready` deltaP `1.4804` edge `-0.1466` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
