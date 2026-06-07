# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T19:22:25.603131+00:00`
- Price records: `672`
- Market context records: `3209`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `10910`

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

- `market_context_high->commodity_24h` score `13.7831` n `97` status `ready` deltaP `47.4924` edge `0.8748` maxDD `-2.0927`
- `market_context_high->crypto_alt_24h` score `11.1063` n `97` status `ready` deltaP `11.9398` edge `2.3419` maxDD `-71.142`
- `market_context_high->index_24h` score `9.2297` n `97` status `ready` deltaP `28.0784` edge `0.8374` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.794` n `97` status `ready` deltaP `11.8109` edge `1.3775` maxDD `-53.663`
- `market_context_high->commodity_4h` score `3.3324` n `123` status `ready` deltaP `21.9004` edge `0.1775` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `0.5652` n `135` status `ready` deltaP `7.179` edge `0.0415` maxDD `-1.7142`
- `market_context_high->unknown_4h` score `0.3626` n `123` status `ready` deltaP `10.6708` edge `0.1813` maxDD `-14.7778`
- `market_context_high->fx_24h` score `0.2811` n `97` status `ready` deltaP `9.5469` edge `-0.0047` maxDD `-0.842`
- `market_context_high->crypto_alt_1h` score `-0.7589` n `135` status `ready` deltaP `4.389` edge `0.0864` maxDD `-14.7034`
- `market_context_high->index_1h` score `-0.9156` n `135` status `ready` deltaP `3.0572` edge `0.0096` maxDD `-4.5023`
- `market_context_high->crypto_major_1h` score `-1.0075` n `135` status `ready` deltaP `4.4278` edge `0.0676` maxDD `-15.1032`
- `market_context_high->fx_1h` score `-1.0853` n `135` status `ready` deltaP `-9.8348` edge `-0.0049` maxDD `-0.8278`
- `market_context_high->fx_4h` score `-1.104` n `123` status `ready` deltaP `-7.1646` edge `-0.0053` maxDD `-1.4115`
- `market_context_high->index_4h` score `-1.4922` n `123` status `ready` deltaP `15.5488` edge `0.0629` maxDD `-17.6057`
- `market_context_high->equity_1h` score `-1.549` n `135` status `ready` deltaP `2.3087` edge `0.0041` maxDD `-8.8863`
- `market_context_high->metal_1h` score `-2.0507` n `135` status `ready` deltaP `-3.1836` edge `-0.0103` maxDD `-7.4828`
- `market_context_high->unknown_1h` score `-2.7567` n `135` status `ready` deltaP `1.2143` edge `-0.1215` maxDD `-17.2012`
- `market_context_high->unknown_24h` score `-2.8256` n `97` status `ready` deltaP `11.5191` edge `0.1722` maxDD `-45.5663`
- `market_context_high->crypto_alt_4h` score `-3.4457` n `123` status `ready` deltaP `12.754` edge `0.2777` maxDD `-58.6918`
- `market_context_high->crypto_major_4h` score `-4.6447` n `123` status `ready` deltaP `5.6402` edge `0.1593` maxDD `-54.3896`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
