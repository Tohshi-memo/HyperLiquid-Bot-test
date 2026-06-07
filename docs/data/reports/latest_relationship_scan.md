# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T17:22:26.042223+00:00`
- Price records: `672`
- Market context records: `3200`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `10906`

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

- `market_context_high->crypto_alt_24h` score `17.2447` n `99` status `ready` deltaP `13.2102` edge `2.3466` maxDD `-71.142`
- `market_context_high->commodity_24h` score `13.4588` n `99` status `ready` deltaP `46.8434` edge `0.8521` maxDD `-2.0927`
- `market_context_high->index_24h` score `6.1716` n `99` status `ready` deltaP `28.6616` edge `0.8556` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.5718` n `99` status `ready` deltaP `12.8315` edge `1.3422` maxDD `-53.663`
- `market_context_high->unknown_24h` score `4.1638` n `99` status `ready` deltaP `16.9824` edge `0.6639` maxDD `-17.4635`
- `market_context_high->commodity_4h` score `3.4178` n `131` status `ready` deltaP `22.2177` edge `0.1825` maxDD `-1.9973`
- `market_context_high->fx_24h` score `0.9462` n `99` status `ready` deltaP `14.5518` edge `0.0046` maxDD `-0.4876`
- `market_context_high->unknown_4h` score `0.5855` n `131` status `ready` deltaP `11.5365` edge `0.1941` maxDD `-14.7778`
- `market_context_high->commodity_1h` score `0.3931` n `135` status `ready` deltaP `6.5879` edge `0.0311` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.4168` n `135` status `ready` deltaP `5.4214` edge `0.0167` maxDD `-4.5023`
- `market_context_high->crypto_alt_1h` score `-0.6137` n `135` status `ready` deltaP `6.7532` edge `0.1168` maxDD `-14.7034`
- `market_context_high->crypto_major_1h` score `-0.9611` n `135` status `ready` deltaP `3.8367` edge `0.0775` maxDD `-15.1032`
- `market_context_high->equity_1h` score `-1.171` n `135` status `ready` deltaP `5.2639` edge `0.0159` maxDD `-8.8863`
- `market_context_high->fx_4h` score `-1.2261` n `131` status `ready` deltaP `-9.3919` edge `-0.0061` maxDD `-1.4115`
- `market_context_high->index_4h` score `-1.361` n `131` status `ready` deltaP `16.1085` edge `0.0701` maxDD `-17.6057`
- `market_context_high->fx_1h` score `-1.7679` n `135` status `ready` deltaP `-11.0169` edge `-0.0052` maxDD `-0.8278`
- `market_context_high->metal_1h` score `-1.9662` n `135` status `ready` deltaP `-2.5926` edge `-0.0072` maxDD `-7.4828`
- `market_context_high->crypto_alt_4h` score `-2.7309` n `131` status `ready` deltaP `15.024` edge `0.3542` maxDD `-58.6918`
- `market_context_high->unknown_1h` score `-3.2768` n `135` status `ready` deltaP `2.3963` edge `-0.0864` maxDD `-14.2111`
- `market_context_high->crypto_major_4h` score `-3.9598` n `131` status `ready` deltaP `8.9102` edge `0.2253` maxDD `-54.3896`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
