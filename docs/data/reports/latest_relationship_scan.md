# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T18:52:34.993494+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8072`

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

- `market_context_high->unknown_4h` score `93.4981` n `153` status `ready` deltaP `0.8648` edge `7.8193` maxDD `-1.0178`
- `market_context_high->unknown_1h` score `28.4017` n `153` status `ready` deltaP `1.4745` edge `2.4059` maxDD `-1.5807`
- `market_context_high->metal_24h` score `0.3789` n `112` status `ready` deltaP `25.3218` edge `0.1424` maxDD `-7.0108`
- `market_context_high->fx_1h` score `0.2542` n `153` status `ready` deltaP `8.1151` edge `0.0029` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.1006` n `153` status `ready` deltaP `9.0198` edge `0.0081` maxDD `-0.4545`
- `market_context_high->index_24h` score `-0.0051` n `112` status `ready` deltaP `16.3051` edge `0.0145` maxDD `-4.5747`
- `market_context_high->metal_1h` score `-0.1314` n `153` status `ready` deltaP `8.3304` edge `0.0068` maxDD `-1.6682`
- `market_context_high->fx_24h` score `-0.1552` n `112` status `ready` deltaP `16.6254` edge `0.0265` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.2738` n `153` status `ready` deltaP `2.1526` edge `0.0129` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.5681` n `153` status `ready` deltaP `0.3121` edge `-0.0012` maxDD `-1.8971`
- `market_context_high->commodity_4h` score `-0.6996` n `153` status `ready` deltaP `4.2294` edge `0.0364` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-0.9254` n `153` status `ready` deltaP `3.7846` edge `0.0142` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-0.9392` n `153` status `ready` deltaP `7.6648` edge `-0.0005` maxDD `-5.3474`
- `market_context_high->equity_1h` score `-1.7933` n `153` status `ready` deltaP `1.7543` edge `-0.014` maxDD `-12.2088`
- `market_context_high->crypto_alt_1h` score `-2.0201` n `153` status `ready` deltaP `-0.8747` edge `-0.0047` maxDD `-13.2099`
- `market_context_high->index_4h` score `-3.3679` n `153` status `ready` deltaP `-5.9272` edge `-0.0235` maxDD `-6.7447`
- `market_context_high->crypto_major_24h` score `-4.4247` n `112` status `ready` deltaP `-2.6182` edge `-0.0641` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-4.6415` n `153` status `ready` deltaP `-0.7632` edge `-0.086` maxDD `-32.9851`
- `market_context_high->equity_24h` score `-6.1477` n `112` status `ready` deltaP `-3.9103` edge `-0.2188` maxDD `-35.4638`
- `market_context_high->commodity_24h` score `-6.2885` n `112` status `ready` deltaP `-16.5573` edge `-0.1369` maxDD `-24.0477`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
