# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T06:22:24.000129+00:00`
- Price records: `672`
- Market context records: `3151`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7978`

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

- `market_context_high->commodity_24h` score `14.2714` n `111` status `ready` deltaP `47.7618` edge `0.9137` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `12.0787` n `111` status `ready` deltaP `22.5835` edge `0.9048` maxDD `-1.9039`
- `market_context_high->crypto_alt_24h` score `11.7441` n `111` status `ready` deltaP `12.9551` edge `2.4169` maxDD `-71.142`
- `market_context_high->index_24h` score `6.6847` n `111` status `ready` deltaP `31.7192` edge `0.901` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.9111` n `111` status `ready` deltaP `13.4478` edge `1.3816` maxDD `-53.663`
- `market_context_high->commodity_4h` score `2.8774` n `146` status `ready` deltaP `18.9421` edge `0.1593` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `0.211` n `146` status `ready` deltaP `4.731` edge `0.0283` maxDD `-1.7142`
- `market_context_high->fx_24h` score `-0.4154` n `111` status `ready` deltaP `5.9169` edge `-0.0013` maxDD `-0.4876`
- `market_context_high->crypto_alt_1h` score `-0.4523` n `146` status `ready` deltaP `5.6066` edge `0.1176` maxDD `-14.7034`
- `market_context_high->index_1h` score `-0.5358` n `146` status `ready` deltaP `3.2524` edge `0.0159` maxDD `-4.5023`
- `market_context_high->equity_1h` score `-0.8278` n `146` status `ready` deltaP `3.4882` edge `0.0192` maxDD `-8.8863`
- `market_context_high->crypto_major_1h` score `-1.0505` n `146` status `ready` deltaP `2.6269` edge `0.0741` maxDD `-15.1032`
- `market_context_high->fx_1h` score `-1.1267` n `146` status `ready` deltaP `-10.6185` edge `-0.0054` maxDD `-0.7941`
- `market_context_high->index_4h` score `-1.2008` n `146` status `ready` deltaP `11.1093` edge `0.0629` maxDD `-17.6057`
- `market_context_high->fx_4h` score `-1.4804` n `146` status `ready` deltaP `-13.9221` edge `-0.0085` maxDD `-1.4115`
- `market_context_high->unknown_4h` score `-1.525` n `146` status `ready` deltaP `6.3064` edge `0.0531` maxDD `-14.7778`
- `market_context_high->metal_1h` score `-2.0995` n `146` status `ready` deltaP `-4.6038` edge `-0.0049` maxDD `-7.4828`
- `market_context_high->equity_4h` score `-2.7878` n `146` status `ready` deltaP `13.9283` edge `0.0803` maxDD `-36.7784`
- `market_context_high->crypto_alt_4h` score `-2.9972` n `146` status `ready` deltaP `18.6622` edge `0.4303` maxDD `-58.6918`
- `market_context_high->unknown_1h` score `-3.1477` n `146` status `ready` deltaP `1.6098` edge `-0.0704` maxDD `-14.2111`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
