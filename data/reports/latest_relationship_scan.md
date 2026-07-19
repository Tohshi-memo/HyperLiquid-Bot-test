# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-19T01:07:31.976784+00:00`
- Price records: `672`
- Market context records: `7200`
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

- `risk_on_high->crypto_major_4h` score `6.0691` n `34` status `ready` deltaP `28.2999` edge `0.3554` maxDD `-0.7314`
- `risk_on_and_context->crypto_major_4h` score `6.0691` n `34` status `ready` deltaP `28.2999` edge `0.3554` maxDD `-0.7314`
- `risk_on_high->crypto_alt_4h` score `4.3862` n `34` status `ready` deltaP `18.0147` edge `0.2847` maxDD `-1.1423`
- `risk_on_and_context->crypto_alt_4h` score `4.3862` n `34` status `ready` deltaP `18.0147` edge `0.2847` maxDD `-1.1423`
- `risk_on_high->commodity_1h` score `2.1108` n `34` status `ready` deltaP `22.5784` edge `0.0404` maxDD `-0.2021`
- `risk_on_and_context->commodity_1h` score `2.1108` n `34` status `ready` deltaP `22.5784` edge `0.0404` maxDD `-0.2021`
- `risk_on_high->equity_4h` score `1.3536` n `34` status `ready` deltaP `7.5771` edge `0.1466` maxDD `-2.412`
- `risk_on_and_context->equity_4h` score `1.3536` n `34` status `ready` deltaP `7.5771` edge `0.1466` maxDD `-2.412`
- `risk_on_high->equity_1h` score `0.2915` n `34` status `ready` deltaP `3.3462` edge `0.032` maxDD `-0.7345`
- `risk_on_and_context->equity_1h` score `0.2915` n `34` status `ready` deltaP `3.3462` edge `0.032` maxDD `-0.7345`
- `risk_on_high->crypto_major_1h` score `0.2879` n `34` status `ready` deltaP `7.9253` edge `0.0131` maxDD `-0.9888`
- `risk_on_and_context->crypto_major_1h` score `0.2879` n `34` status `ready` deltaP `7.9253` edge `0.0131` maxDD `-0.9888`
- `market_context_high->fx_1h` score `-0.2919` n `178` status `ready` deltaP `3.5575` edge `0.0009` maxDD `-0.5817`
- `risk_on_high->unknown_4h` score `-0.306` n `34` status `ready` deltaP `3.9814` edge `-0.0059` maxDD `-1.4561`
- `risk_on_and_context->unknown_4h` score `-0.306` n `34` status `ready` deltaP `3.9814` edge `-0.0059` maxDD `-1.4561`
- `market_context_high->commodity_1h` score `-0.5633` n `178` status `ready` deltaP `0.0404` edge `-0.0104` maxDD `-1.9668`
- `market_context_high->crypto_major_1h` score `-0.6285` n `178` status `ready` deltaP `4.7198` edge `0.029` maxDD `-7.6171`
- `risk_on_high->commodity_4h` score `-0.6478` n `34` status `ready` deltaP `-0.018` edge `-0.0111` maxDD `-0.7546`
- `risk_on_and_context->commodity_4h` score `-0.6478` n `34` status `ready` deltaP `-0.018` edge `-0.0111` maxDD `-0.7546`
- `market_context_high->unknown_1h` score `-0.672` n `178` status `ready` deltaP `-1.3507` edge `0.0172` maxDD `-1.4688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
