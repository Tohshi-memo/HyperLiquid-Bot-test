# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T20:07:32.336886+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9828`

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

- `market_context_high->equity_4h` score `2.2685` n `96` status `ready` deltaP `11.4583` edge `0.2015` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.8572` n `96` status `ready` deltaP `15.151` edge `0.0839` maxDD `-0.4112`
- `market_context_high->index_1h` score `0.9881` n `96` status `ready` deltaP `16.5107` edge `0.011` maxDD `-0.0982`
- `market_context_high->metal_4h` score `0.527` n `96` status `ready` deltaP `13.3638` edge `0.0124` maxDD `-1.273`
- `market_context_high->commodity_24h` score `0.2636` n `96` status `ready` deltaP `6.4236` edge `0.1743` maxDD `-4.666`
- `market_context_high->index_4h` score `0.2528` n `96` status `ready` deltaP `9.3242` edge `0.0244` maxDD `-0.5728`
- `market_context_high->unknown_24h` score `0.1762` n `96` status `ready` deltaP `17.8819` edge `-0.0539` maxDD `-1.0505`
- `market_context_high->fx_4h` score `0.0383` n `96` status `ready` deltaP `7.4949` edge `0.0052` maxDD `-0.3539`
- `market_context_high->unknown_1h` score `-0.0505` n `96` status `ready` deltaP `6.6617` edge `-0.0259` maxDD `-0.4843`
- `market_context_high->metal_1h` score `-0.0969` n `96` status `ready` deltaP `3.8735` edge `0.0048` maxDD `-0.4291`
- `market_context_high->fx_1h` score `-0.3198` n `96` status `ready` deltaP `-1.1727` edge `0.0027` maxDD `-0.2043`
- `market_context_high->commodity_4h` score `-0.677` n `96` status `ready` deltaP `-0.94` edge `0.0045` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-0.7354` n `96` status `ready` deltaP `-0.1684` edge `-0.013` maxDD `-2.413`
- `market_context_high->crypto_major_24h` score `-0.7393` n `96` status `ready` deltaP `2.9514` edge `0.0395` maxDD `-4.9964`
- `market_context_high->crypto_major_1h` score `-0.7869` n `96` status `ready` deltaP `1.4845` edge `-0.0263` maxDD `-2.7581`
- `market_context_high->commodity_1h` score `-0.8612` n `96` status `ready` deltaP `-7.2917` edge `-0.0052` maxDD `-1.1941`
- `market_context_high->crypto_major_4h` score `-1.1405` n `96` status `ready` deltaP `6.4278` edge `-0.0358` maxDD `-3.1677`
- `market_context_high->crypto_alt_4h` score `-1.4704` n `96` status `ready` deltaP `4.2683` edge `-0.024` maxDD `-5.4926`
- `market_context_high->metal_24h` score `-2.9614` n `96` status `ready` deltaP `-8.6806` edge `0.009` maxDD `-11.4635`
- `market_context_high->fx_24h` score `-3.4902` n `96` status `ready` deltaP `-18.5764` edge `-0.0087` maxDD `-1.9981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
