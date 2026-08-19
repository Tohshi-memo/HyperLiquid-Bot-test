# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T17:37:41.544289+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8829`

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

- `market_context_high->equity_4h` score `2.4125` n `96` status `ready` deltaP `12.3729` edge `0.2074` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.9171` n `96` status `ready` deltaP `15.6001` edge `0.0859` maxDD `-0.4112`
- `market_context_high->index_1h` score `0.963` n `96` status `ready` deltaP `16.2113` edge `0.0109` maxDD `-0.0982`
- `market_context_high->metal_4h` score `0.6969` n `96` status `ready` deltaP `14.8882` edge `0.0164` maxDD `-1.273`
- `market_context_high->crypto_major_24h` score `0.502` n `96` status `ready` deltaP `3.993` edge `0.136` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `0.3821` n `96` status `ready` deltaP `7.2917` edge `0.1837` maxDD `-4.666`
- `market_context_high->unknown_24h` score `0.3144` n `96` status `ready` deltaP `18.2291` edge `-0.0447` maxDD `-1.0505`
- `market_context_high->index_4h` score `0.1956` n `96` status `ready` deltaP `8.7144` edge `0.0237` maxDD `-0.5728`
- `market_context_high->unknown_1h` score `0.1461` n `96` status `ready` deltaP `7.7096` edge `-0.0165` maxDD `-0.4843`
- `market_context_high->fx_4h` score `0.0795` n `96` status `ready` deltaP `8.2571` edge `0.0054` maxDD `-0.3539`
- `market_context_high->metal_1h` score `-0.0729` n `96` status `ready` deltaP `4.0232` edge `0.0058` maxDD `-0.4291`
- `market_context_high->fx_1h` score `-0.3198` n `96` status `ready` deltaP `-1.1727` edge `0.0027` maxDD `-0.2043`
- `market_context_high->crypto_major_4h` score `-0.3826` n `96` status `ready` deltaP `7.9522` edge `0.0172` maxDD `-3.1677`
- `market_context_high->crypto_major_1h` score `-0.6333` n `96` status `ready` deltaP `2.3827` edge `-0.0126` maxDD `-2.7581`
- `market_context_high->crypto_alt_1h` score `-0.6427` n `96` status `ready` deltaP `0.7298` edge `-0.0071` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.695` n `96` status `ready` deltaP `-0.94` edge `0.0022` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.9102` n `96` status `ready` deltaP `-7.8905` edge `-0.0075` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-0.9177` n `96` status `ready` deltaP `5.7927` edge `0.0119` maxDD `-5.4926`
- `market_context_high->metal_24h` score `-2.6816` n `96` status `ready` deltaP `-6.9444` edge `0.0333` maxDD `-11.4635`
- `market_context_high->fx_24h` score `-3.6294` n `96` status `ready` deltaP `-19.7916` edge `-0.0122` maxDD `-1.9981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
