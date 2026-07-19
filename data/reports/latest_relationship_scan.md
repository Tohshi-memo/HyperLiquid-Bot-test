# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-19T11:37:23.209477+00:00`
- Price records: `672`
- Market context records: `7245`
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

- `risk_on_high->crypto_major_4h` score `5.9439` n `34` status `ready` deltaP `27.0804` edge `0.3531` maxDD `-0.7314`
- `risk_on_and_context->crypto_major_4h` score `5.9439` n `34` status `ready` deltaP `27.0804` edge `0.3531` maxDD `-0.7314`
- `risk_on_high->crypto_alt_4h` score `4.2953` n `34` status `ready` deltaP `17.2525` edge `0.2822` maxDD `-1.1423`
- `risk_on_and_context->crypto_alt_4h` score `4.2953` n `34` status `ready` deltaP `17.2525` edge `0.2822` maxDD `-1.1423`
- `risk_on_high->commodity_1h` score `2.1459` n `34` status `ready` deltaP `23.0171` edge `0.0404` maxDD `-0.2021`
- `risk_on_and_context->commodity_1h` score `2.1459` n `34` status `ready` deltaP `23.0171` edge `0.0404` maxDD `-0.2021`
- `risk_on_high->equity_4h` score `1.0539` n `34` status `ready` deltaP `5.2267` edge `0.1373` maxDD `-2.412`
- `risk_on_and_context->equity_4h` score `1.0539` n `34` status `ready` deltaP `5.2267` edge `0.1373` maxDD `-2.412`
- `risk_on_high->crypto_major_1h` score `0.2653` n `34` status `ready` deltaP `7.4762` edge `0.0132` maxDD `-0.9888`
- `risk_on_and_context->crypto_major_1h` score `0.2653` n `34` status `ready` deltaP `7.4762` edge `0.0132` maxDD `-0.9888`
- `risk_on_high->equity_1h` score `0.215` n `34` status `ready` deltaP `2.6144` edge `0.0305` maxDD `-0.7345`
- `risk_on_and_context->equity_1h` score `0.215` n `34` status `ready` deltaP `2.6144` edge `0.0305` maxDD `-0.7345`
- `risk_on_high->unknown_4h` score `-0.1421` n `34` status `ready` deltaP `3.0667` edge `0.0212` maxDD `-1.4561`
- `risk_on_and_context->unknown_4h` score `-0.1421` n `34` status `ready` deltaP `3.0667` edge `0.0212` maxDD `-1.4561`
- `market_context_high->fx_1h` score `-0.2548` n `160` status `ready` deltaP `2.3498` edge `0.0006` maxDD `-0.5817`
- `risk_on_high->commodity_4h` score `-0.6636` n `34` status `ready` deltaP `-0.2605` edge `-0.0108` maxDD `-0.7546`
- `risk_on_and_context->commodity_4h` score `-0.6636` n `34` status `ready` deltaP `-0.2605` edge `-0.0108` maxDD `-0.7546`
- `market_context_high->commodity_1h` score `-0.6724` n `160` status `ready` deltaP `-1.5785` edge `-0.0136` maxDD `-1.9668`
- `market_context_high->crypto_alt_1h` score `-0.7007` n `160` status `ready` deltaP `-0.3518` edge `0.0164` maxDD `-5.9775`
- `market_context_high->crypto_major_1h` score `-0.7594` n `160` status `ready` deltaP `3.0277` edge `0.0235` maxDD `-7.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
