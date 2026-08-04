# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T07:52:32.537038+00:00`
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

- `market_context_high->unknown_24h` score `37.2989` n `46` status `ready` deltaP `25.4303` edge `2.943` maxDD `-0.0103`
- `market_context_high->crypto_alt_24h` score `8.7438` n `46` status `ready` deltaP `43.6519` edge `0.455` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `7.9702` n `46` status `ready` deltaP `36.5262` edge `0.4386` maxDD `-0.434`
- `market_context_high->unknown_4h` score `5.7751` n `88` status `ready` deltaP `1.8154` edge `0.5687` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.1664` n `88` status `ready` deltaP `15.0638` edge `0.0814` maxDD `-2.7703`
- `market_context_high->fx_4h` score `0.3105` n `88` status `ready` deltaP `17.475` edge `0.0093` maxDD `-1.8797`
- `market_context_high->commodity_1h` score `0.2493` n `88` status `ready` deltaP `5.8315` edge `0.0235` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.182` n `88` status `ready` deltaP `7.9818` edge `-0.0032` maxDD `-0.7878`
- `market_context_high->index_1h` score `-0.4663` n `88` status `ready` deltaP `1.5787` edge `-0.0169` maxDD `-1.6054`
- `market_context_high->metal_1h` score `-0.5222` n `88` status `ready` deltaP `-1.3201` edge `-0.0087` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.5465` n `88` status `ready` deltaP `4.8919` edge `0.0208` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-0.9662` n `88` status `ready` deltaP `3.2567` edge `-0.0066` maxDD `-5.7857`
- `market_context_high->crypto_alt_1h` score `-1.2611` n `88` status `ready` deltaP `-3.4703` edge `-0.0109` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.5541` n `88` status `ready` deltaP `5.4641` edge `-0.0821` maxDD `-10.619`
- `market_context_high->fx_24h` score `-1.7892` n `46` status `ready` deltaP `-5.2687` edge `0.0066` maxDD `-4.3126`
- `market_context_high->index_4h` score `-1.8381` n `88` status `ready` deltaP `-9.8115` edge `-0.0448` maxDD `-4.7021`
- `market_context_high->unknown_1h` score `-3.3704` n `88` status `ready` deltaP `2.8988` edge `-0.2555` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.6151` n `88` status `ready` deltaP `-12.7994` edge `-0.0786` maxDD `-7.6533`
- `market_context_high->metal_24h` score `-4.8782` n `46` status `ready` deltaP `-24.1621` edge `-0.1286` maxDD `-2.6802`
- `market_context_high->equity_4h` score `-6.5755` n `88` status `ready` deltaP `0.7899` edge `-0.3152` maxDD `-35.3129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
