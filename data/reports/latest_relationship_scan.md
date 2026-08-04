# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T07:37:29.052792+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9833`

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

- `market_context_high->unknown_24h` score `37.332` n `46` status `ready` deltaP `25.6039` edge `2.9446` maxDD `-0.0103`
- `market_context_high->crypto_alt_24h` score `8.8141` n `46` status `ready` deltaP `43.8255` edge `0.4597` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `7.9925` n `46` status `ready` deltaP `36.6998` edge `0.4393` maxDD `-0.434`
- `market_context_high->unknown_4h` score `5.7981` n `88` status `ready` deltaP `1.9678` edge `0.5696` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.1664` n `88` status `ready` deltaP `15.0638` edge `0.0814` maxDD `-2.7703`
- `market_context_high->fx_4h` score `0.3192` n `88` status `ready` deltaP `17.6275` edge `0.0094` maxDD `-1.8797`
- `market_context_high->commodity_1h` score `0.2661` n `88` status `ready` deltaP `5.9812` edge `0.0239` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.17` n `88` status `ready` deltaP `7.8321` edge `-0.0032` maxDD `-0.7878`
- `market_context_high->index_1h` score `-0.4663` n `88` status `ready` deltaP `1.5787` edge `-0.0169` maxDD `-1.6054`
- `market_context_high->metal_1h` score `-0.5206` n `88` status `ready` deltaP `-1.3201` edge `-0.0085` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.5346` n `88` status `ready` deltaP `5.0444` edge `0.0213` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-0.9655` n `88` status `ready` deltaP `3.2567` edge `-0.0065` maxDD `-5.7857`
- `market_context_high->crypto_alt_1h` score `-1.2431` n `88` status `ready` deltaP `-3.3206` edge `-0.0104` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.5541` n `88` status `ready` deltaP `5.4641` edge `-0.0821` maxDD `-10.619`
- `market_context_high->fx_24h` score `-1.7705` n `46` status `ready` deltaP `-5.0951` edge `0.007` maxDD `-4.3126`
- `market_context_high->index_4h` score `-1.827` n `88` status `ready` deltaP `-9.6591` edge `-0.0444` maxDD `-4.7021`
- `market_context_high->unknown_1h` score `-3.3608` n `88` status `ready` deltaP `2.8988` edge `-0.2547` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.5972` n `88` status `ready` deltaP `-12.6497` edge `-0.0781` maxDD `-7.6533`
- `market_context_high->metal_24h` score `-4.8758` n `46` status `ready` deltaP `-24.1621` edge `-0.1284` maxDD `-2.6802`
- `market_context_high->equity_4h` score `-6.5496` n `88` status `ready` deltaP `0.9423` edge `-0.3129` maxDD `-35.3129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
