# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-19T02:37:27.476456+00:00`
- Price records: `672`
- Market context records: `7206`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `12810`

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

- `risk_on_high->crypto_major_4h` score `6.0423` n `34` status `ready` deltaP `27.995` edge `0.3552` maxDD `-0.7314`
- `risk_on_and_context->crypto_major_4h` score `6.0423` n `34` status `ready` deltaP `27.995` edge `0.3552` maxDD `-0.7314`
- `risk_on_high->crypto_alt_4h` score `4.4342` n `34` status `ready` deltaP `18.0147` edge `0.2887` maxDD `-1.1423`
- `risk_on_and_context->crypto_alt_4h` score `4.4342` n `34` status `ready` deltaP `18.0147` edge `0.2887` maxDD `-1.1423`
- `risk_on_high->commodity_1h` score `2.112` n `34` status `ready` deltaP `22.5784` edge `0.0405` maxDD `-0.2021`
- `risk_on_and_context->commodity_1h` score `2.112` n `34` status `ready` deltaP `22.5784` edge `0.0405` maxDD `-0.2021`
- `risk_on_high->equity_4h` score `1.3404` n `34` status `ready` deltaP `7.5771` edge `0.1455` maxDD `-2.412`
- `risk_on_and_context->equity_4h` score `1.3404` n `34` status `ready` deltaP `7.5771` edge `0.1455` maxDD `-2.412`
- `risk_on_high->crypto_major_1h` score `0.2988` n `34` status `ready` deltaP `7.9253` edge `0.0145` maxDD `-0.9888`
- `risk_on_and_context->crypto_major_1h` score `0.2988` n `34` status `ready` deltaP `7.9253` edge `0.0145` maxDD `-0.9888`
- `risk_on_high->equity_1h` score `0.2759` n `34` status `ready` deltaP `3.1965` edge `0.0317` maxDD `-0.7345`
- `risk_on_and_context->equity_1h` score `0.2759` n `34` status `ready` deltaP `3.1965` edge `0.0317` maxDD `-0.7345`
- `risk_on_high->unknown_4h` score `-0.2723` n `34` status `ready` deltaP `4.1338` edge `-0.0026` maxDD `-1.4561`
- `risk_on_and_context->unknown_4h` score `-0.2723` n `34` status `ready` deltaP `4.1338` edge `-0.0026` maxDD `-1.4561`
- `market_context_high->fx_1h` score `-0.305` n `178` status `ready` deltaP `3.4078` edge `0.0008` maxDD `-0.5817`
- `market_context_high->commodity_1h` score `-0.5625` n `178` status `ready` deltaP `0.0404` edge `-0.0103` maxDD `-1.9668`
- `market_context_high->unknown_1h` score `-0.6096` n `178` status `ready` deltaP `-0.9016` edge `0.0194` maxDD `-1.4688`
- `market_context_high->crypto_major_1h` score `-0.6176` n `178` status `ready` deltaP `4.7198` edge `0.0304` maxDD `-7.6171`
- `market_context_high->crypto_alt_1h` score `-0.6423` n `178` status `ready` deltaP `0.4861` edge `0.0183` maxDD `-5.9775`
- `risk_on_high->commodity_4h` score `-0.6842` n `34` status `ready` deltaP `-0.3228` edge `-0.0121` maxDD `-0.7546`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
