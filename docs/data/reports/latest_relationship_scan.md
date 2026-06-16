# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-16T06:22:32.566952+00:00`
- Price records: `672`
- Market context records: `4066`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10216`

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

- `risk_on_high->unknown_4h` score `145.0591` n `40` status `ready` deltaP `-6.6768` edge `12.3144` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `145.0591` n `40` status `ready` deltaP `-6.6768` edge `12.3144` maxDD `-10.864`
- `market_context_high->unknown_1h` score `51.1376` n `172` status `ready` deltaP `2.0297` edge `4.4057` maxDD `-9.6211`
- `market_context_high->unknown_24h` score `37.4392` n `144` status `ready` deltaP `-8.0264` edge `3.5763` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `17.0934` n `172` status `ready` deltaP `-0.8047` edge `1.9721` maxDD `-35.7161`
- `risk_on_high->equity_4h` score `3.8316` n `40` status `ready` deltaP `38.6585` edge `0.0663` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `3.8316` n `40` status `ready` deltaP `38.6585` edge `0.0663` maxDD `-0.0446`
- `risk_on_high->equity_24h` score `2.3301` n `40` status `ready` deltaP `31.1958` edge `-0.0138` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `2.3301` n `40` status `ready` deltaP `31.1958` edge `-0.0138` maxDD `0.0`
- `market_context_high->index_24h` score `1.8713` n `144` status `ready` deltaP `18.8908` edge `0.03` maxDD `0.0`
- `market_context_high->equity_4h` score `1.4563` n `172` status `ready` deltaP `15.5771` edge `0.1706` maxDD `-6.9137`
- `risk_on_high->crypto_major_4h` score `1.3328` n `40` status `ready` deltaP `19.9085` edge `0.0449` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.3328` n `40` status `ready` deltaP `19.9085` edge `0.0449` maxDD `-2.6576`
- `market_context_high->equity_1h` score `0.8401` n `172` status `ready` deltaP `6.371` edge `0.0835` maxDD `-2.144`
- `risk_on_high->equity_1h` score `0.5443` n `40` status `ready` deltaP `11.6617` edge `0.0067` maxDD `-0.7937`
- `risk_on_and_context->equity_1h` score `0.5443` n `40` status `ready` deltaP `11.6617` edge `0.0067` maxDD `-0.7937`
- `risk_on_high->crypto_major_1h` score `0.2318` n `40` status `ready` deltaP `12.7545` edge `-0.0011` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.2318` n `40` status `ready` deltaP `12.7545` edge `-0.0011` maxDD `-2.3372`
- `risk_on_high->metal_4h` score `0.2222` n `40` status `ready` deltaP `11.7073` edge `-0.016` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.2222` n `40` status `ready` deltaP `11.7073` edge `-0.016` maxDD `-1.3516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
