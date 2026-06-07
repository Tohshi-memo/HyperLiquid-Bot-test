# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T15:48:02.616114+00:00`
- Price records: `672`
- Market context records: `3192`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9761`

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

- `market_context_high->commodity_24h` score `13.6393` n `105` status `ready` deltaP `47.4206` edge `0.8633` maxDD `-2.0927`
- `market_context_high->crypto_alt_24h` score `12.0537` n `105` status `ready` deltaP `15.9524` edge `2.4366` maxDD `-71.142`
- `market_context_high->unknown_24h` score `7.6847` n `105` status `ready` deltaP `17.7877` edge `0.7651` maxDD `-17.4635`
- `market_context_high->index_24h` score `6.2899` n `105` status `ready` deltaP `30.2777` edge `0.86` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.8508` n `105` status `ready` deltaP `13.3234` edge `1.3747` maxDD `-53.663`
- `market_context_high->commodity_4h` score `3.1839` n `137` status `ready` deltaP `20.4335` edge `0.1749` maxDD `-1.9973`
- `market_context_high->fx_24h` score `0.8125` n `105` status `ready` deltaP `13.1349` edge `0.0029` maxDD `-0.4876`
- `market_context_high->unknown_4h` score `0.6732` n `137` status `ready` deltaP `12.4833` edge `0.1951` maxDD `-14.7778`
- `market_context_high->commodity_1h` score `0.4053` n `137` status `ready` deltaP `6.6349` edge `0.0318` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.364` n `137` status `ready` deltaP `6.0918` edge `0.019` maxDD `-4.5023`
- `market_context_high->crypto_alt_1h` score `-0.4543` n `137` status `ready` deltaP `5.9421` edge `0.1151` maxDD `-14.7034`
- `market_context_high->index_4h` score `-0.735` n `137` status `ready` deltaP `17.546` edge `0.0797` maxDD `-17.6057`
- `market_context_high->crypto_major_1h` score `-1.0335` n `137` status `ready` deltaP `3.2836` edge `0.0719` maxDD `-15.1032`
- `market_context_high->equity_1h` score `-1.2591` n `137` status `ready` deltaP `4.6134` edge `0.0129` maxDD `-8.8863`
- `market_context_high->fx_4h` score `-1.2958` n `137` status `ready` deltaP `-10.6718` edge `-0.0065` maxDD `-1.4115`
- `market_context_high->fx_1h` score `-1.6255` n `137` status `ready` deltaP `-9.2366` edge `-0.0052` maxDD `-0.8278`
- `market_context_high->metal_1h` score `-2.1109` n `137` status `ready` deltaP `-4.1457` edge `-0.0089` maxDD `-7.4828`
- `market_context_high->crypto_alt_4h` score `-2.3393` n `137` status `ready` deltaP `16.8105` edge `0.3925` maxDD `-58.6918`
- `market_context_high->unknown_1h` score `-3.177` n `137` status `ready` deltaP `2.1439` edge `-0.0764` maxDD `-14.2111`
- `market_context_high->crypto_major_4h` score `-3.6858` n `137` status `ready` deltaP `10.0098` edge `0.2531` maxDD `-54.3896`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
