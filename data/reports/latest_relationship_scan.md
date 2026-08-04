# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T08:22:28.997461+00:00`
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

- `market_context_high->unknown_24h` score `37.2274` n `46` status `ready` deltaP `25.2567` edge `2.9382` maxDD `-0.0103`
- `market_context_high->crypto_alt_24h` score `8.6092` n `46` status `ready` deltaP `43.3047` edge `0.4461` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `7.9642` n `46` status `ready` deltaP `36.5262` edge `0.4381` maxDD `-0.434`
- `market_context_high->unknown_4h` score `5.7111` n `88` status `ready` deltaP `1.5105` edge `0.5654` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.1968` n `88` status `ready` deltaP `15.3687` edge `0.0819` maxDD `-2.7703`
- `market_context_high->fx_4h` score `0.2923` n `88` status `ready` deltaP `17.1702` edge `0.009` maxDD `-1.8797`
- `market_context_high->commodity_1h` score `0.2193` n `88` status `ready` deltaP `5.5321` edge `0.023` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.182` n `88` status `ready` deltaP `7.9818` edge `-0.0032` maxDD `-0.7878`
- `market_context_high->index_1h` score `-0.4663` n `88` status `ready` deltaP `1.5787` edge `-0.0169` maxDD `-1.6054`
- `market_context_high->metal_1h` score `-0.5393` n `88` status `ready` deltaP `-1.6195` edge `-0.0089` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.5724` n `88` status `ready` deltaP `4.5871` edge `0.0195` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-0.9749` n `88` status `ready` deltaP `3.1042` edge `-0.0067` maxDD `-5.7857`
- `market_context_high->crypto_alt_1h` score `-1.2863` n `88` status `ready` deltaP `-3.62` edge `-0.012` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.5572` n `88` status `ready` deltaP `5.4641` edge `-0.0825` maxDD `-10.619`
- `market_context_high->fx_24h` score `-1.8254` n `46` status `ready` deltaP `-5.6159` edge `0.0059` maxDD `-4.3126`
- `market_context_high->index_4h` score `-1.8507` n `88` status `ready` deltaP `-9.964` edge `-0.0454` maxDD `-4.7021`
- `market_context_high->unknown_1h` score `-3.392` n `88` status `ready` deltaP `2.8988` edge `-0.2573` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.6499` n `88` status `ready` deltaP `-13.0988` edge `-0.0795` maxDD `-7.6533`
- `market_context_high->metal_24h` score `-4.9017` n `46` status `ready` deltaP `-24.3357` edge `-0.1294` maxDD `-2.6802`
- `market_context_high->equity_4h` score `-6.6327` n `88` status `ready` deltaP `0.485` edge `-0.3205` maxDD `-35.3129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
