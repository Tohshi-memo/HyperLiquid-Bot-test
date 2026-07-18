# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T22:52:24.198049+00:00`
- Price records: `672`
- Market context records: `7190`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11810`

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

- `risk_on_high->crypto_major_4h` score `6.2297` n `34` status `ready` deltaP `29.0621` edge `0.3637` maxDD `-0.7314`
- `risk_on_and_context->crypto_major_4h` score `6.2297` n `34` status `ready` deltaP `29.0621` edge `0.3637` maxDD `-0.7314`
- `risk_on_high->crypto_alt_4h` score `4.5144` n `34` status `ready` deltaP `18.7769` edge `0.2903` maxDD `-1.1423`
- `risk_on_and_context->crypto_alt_4h` score `4.5144` n `34` status `ready` deltaP `18.7769` edge `0.2903` maxDD `-1.1423`
- `risk_on_high->commodity_1h` score `2.0508` n `34` status `ready` deltaP `22.1293` edge `0.0384` maxDD `-0.2021`
- `risk_on_and_context->commodity_1h` score `2.0508` n `34` status `ready` deltaP `22.1293` edge `0.0384` maxDD `-0.2021`
- `risk_on_high->equity_4h` score `1.4361` n `34` status `ready` deltaP `8.3393` edge `0.1484` maxDD `-2.412`
- `risk_on_and_context->equity_4h` score `1.4361` n `34` status `ready` deltaP `8.3393` edge `0.1484` maxDD `-2.412`
- `risk_on_high->crypto_major_1h` score `0.397` n `34` status `ready` deltaP `8.6738` edge `0.0221` maxDD `-0.9888`
- `risk_on_and_context->crypto_major_1h` score `0.397` n `34` status `ready` deltaP `8.6738` edge `0.0221` maxDD `-0.9888`
- `risk_on_high->equity_1h` score `0.3886` n `34` status `ready` deltaP `4.2444` edge `0.0341` maxDD `-0.7345`
- `risk_on_and_context->equity_1h` score `0.3886` n `34` status `ready` deltaP `4.2444` edge `0.0341` maxDD `-0.7345`
- `risk_on_high->unknown_4h` score `-0.287` n `34` status `ready` deltaP `4.2863` edge `-0.0055` maxDD `-1.4561`
- `risk_on_and_context->unknown_4h` score `-0.287` n `34` status `ready` deltaP `4.2863` edge `-0.0055` maxDD `-1.4561`
- `market_context_high->fx_1h` score `-0.3026` n `178` status `ready` deltaP `3.4078` edge `0.001` maxDD `-0.5817`
- `market_context_high->crypto_major_1h` score `-0.5194` n `178` status `ready` deltaP `5.4683` edge `0.038` maxDD `-7.6171`
- `market_context_high->crypto_alt_1h` score `-0.5955` n `178` status `ready` deltaP `0.4861` edge `0.0243` maxDD `-5.9775`
- `market_context_high->commodity_1h` score `-0.6022` n `178` status `ready` deltaP `-0.4087` edge `-0.0124` maxDD `-1.9668`
- `risk_on_high->commodity_4h` score `-0.7072` n `34` status `ready` deltaP `-0.4753` edge `-0.013` maxDD `-0.7546`
- `risk_on_and_context->commodity_4h` score `-0.7072` n `34` status `ready` deltaP `-0.4753` edge `-0.013` maxDD `-0.7546`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
