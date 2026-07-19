# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-19T12:22:29.736079+00:00`
- Price records: `672`
- Market context records: `7249`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13743`

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

- `risk_on_high->crypto_major_4h` score `6.0139` n `34` status `ready` deltaP `27.3852` edge `0.3569` maxDD `-0.7314`
- `risk_on_and_context->crypto_major_4h` score `6.0139` n `34` status `ready` deltaP `27.3852` edge `0.3569` maxDD `-0.7314`
- `risk_on_high->crypto_alt_4h` score `4.3666` n `34` status `ready` deltaP `17.7098` edge `0.2851` maxDD `-1.1423`
- `risk_on_and_context->crypto_alt_4h` score `4.3666` n `34` status `ready` deltaP `17.7098` edge `0.2851` maxDD `-1.1423`
- `risk_on_high->commodity_1h` score `2.1278` n `34` status `ready` deltaP `22.867` edge `0.0399` maxDD `-0.2021`
- `risk_on_and_context->commodity_1h` score `2.1278` n `34` status `ready` deltaP `22.867` edge `0.0399` maxDD `-0.2021`
- `risk_on_high->equity_4h` score `1.1026` n `34` status `ready` deltaP `5.6848` edge `0.1383` maxDD `-2.412`
- `risk_on_and_context->equity_4h` score `1.1026` n `34` status `ready` deltaP `5.6848` edge `0.1383` maxDD `-2.412`
- `risk_on_high->crypto_major_1h` score `0.3058` n `34` status `ready` deltaP `7.9253` edge `0.0154` maxDD `-0.9888`
- `risk_on_and_context->crypto_major_1h` score `0.3058` n `34` status `ready` deltaP `7.9253` edge `0.0154` maxDD `-0.9888`
- `risk_on_high->equity_1h` score `0.245` n `34` status `ready` deltaP `2.9147` edge `0.031` maxDD `-0.7345`
- `risk_on_and_context->equity_1h` score `0.245` n `34` status `ready` deltaP `2.9147` edge `0.031` maxDD `-0.7345`
- `risk_on_high->unknown_4h` score `-0.1255` n `34` status `ready` deltaP `3.3716` edge `0.0213` maxDD `-1.4561`
- `risk_on_and_context->unknown_4h` score `-0.1255` n `34` status `ready` deltaP `3.3716` edge `0.0213` maxDD `-1.4561`
- `market_context_high->fx_1h` score `-0.2525` n `157` status `ready` deltaP `2.3795` edge `0.0007` maxDD `-0.5817`
- `market_context_high->commodity_1h` score `-0.6201` n `157` status `ready` deltaP `-0.7374` edge `-0.0125` maxDD `-1.9668`
- `risk_on_high->commodity_4h` score `-0.6941` n `34` status `ready` deltaP `-0.5658` edge `-0.0113` maxDD `-0.7546`
- `risk_on_and_context->commodity_4h` score `-0.6941` n `34` status `ready` deltaP `-0.5658` edge `-0.0113` maxDD `-0.7546`
- `market_context_high->crypto_alt_1h` score `-0.7415` n `157` status `ready` deltaP `-0.882` edge `0.0147` maxDD `-5.9775`
- `market_context_high->commodity_4h` score `-0.7829` n `157` status `ready` deltaP `2.3941` edge `-0.0128` maxDD `-2.9494`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
