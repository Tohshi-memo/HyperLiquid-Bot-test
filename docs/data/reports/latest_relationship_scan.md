# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T04:52:29.623946+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9932`

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

- `market_context_high->unknown_24h` score `37.3971` n `46` status `ready` deltaP `26.2983` edge `2.9454` maxDD `-0.0103`
- `market_context_high->crypto_alt_24h` score `9.5585` n `46` status `ready` deltaP `45.7352` edge `0.509` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `8.2358` n `46` status `ready` deltaP `38.436` edge `0.448` maxDD `-0.434`
- `market_context_high->unknown_4h` score `6.1619` n `88` status `ready` deltaP `2.1203` edge `0.5989` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.2803` n `88` status `ready` deltaP `15.9784` edge `0.0848` maxDD `-2.7703`
- `market_context_high->fx_4h` score `0.4196` n `88` status `ready` deltaP `19.3043` edge `0.0111` maxDD `-1.8797`
- `market_context_high->commodity_1h` score `0.2613` n `88` status `ready` deltaP `5.8315` edge `0.0245` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.2347` n `88` status `ready` deltaP `8.5806` edge `-0.0028` maxDD `-0.7878`
- `market_context_high->index_1h` score `-0.4289` n `88` status `ready` deltaP `2.1775` edge `-0.0161` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.4456` n `88` status `ready` deltaP `6.1114` edge `0.0256` maxDD `-3.211`
- `market_context_high->metal_1h` score `-0.537` n `88` status `ready` deltaP `-1.6195` edge `-0.0086` maxDD `-1.6224`
- `market_context_high->crypto_alt_4h` score `-0.9387` n `88` status `ready` deltaP `3.5615` edge `-0.0051` maxDD `-5.7857`
- `market_context_high->crypto_alt_1h` score `-1.2875` n `88` status `ready` deltaP `-3.62` edge `-0.0121` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.4731` n `88` status `ready` deltaP `6.2126` edge `-0.0767` maxDD `-10.619`
- `market_context_high->fx_24h` score `-1.5697` n `46` status `ready` deltaP `-3.1854` edge `0.011` maxDD `-4.3126`
- `market_context_high->index_4h` score `-1.7623` n `88` status `ready` deltaP `-8.7445` edge `-0.0422` maxDD `-4.7021`
- `market_context_high->unknown_1h` score `-3.0573` n `88` status `ready` deltaP `3.3479` edge `-0.2324` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.6139` n `88` status `ready` deltaP `-12.7994` edge `-0.0785` maxDD `-7.6533`
- `market_context_high->metal_24h` score `-4.8149` n `46` status `ready` deltaP `-23.6413` edge `-0.1268` maxDD `-2.6802`
- `market_context_high->equity_4h` score `-6.3858` n `88` status `ready` deltaP `1.8569` edge `-0.298` maxDD `-35.3129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
