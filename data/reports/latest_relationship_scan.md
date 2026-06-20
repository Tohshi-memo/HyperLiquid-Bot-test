# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-20T15:19:19.984392+00:00`
- Price records: `672`
- Market context records: `4220`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9808`

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

- `risk_on_high->unknown_4h` score `145.7401` n `40` status `ready` deltaP `-6.9817` edge `12.3734` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `145.7401` n `40` status `ready` deltaP `-6.9817` edge `12.3734` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `30.3556` n `216` status `ready` deltaP `1.2725` edge `2.6791` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `9.5287` n `207` status `ready` deltaP `-3.129` edge `1.3579` maxDD `-35.7719`
- `market_context_high->unknown_24h` score `7.6488` n `196` status `ready` deltaP `-12.3048` edge `1.1228` maxDD `-24.2693`
- `risk_on_high->commodity_24h` score `2.4018` n `40` status `ready` deltaP `4.2746` edge `0.3998` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `2.4018` n `40` status `ready` deltaP `4.2746` edge `0.3998` maxDD `-12.9187`
- `risk_on_high->equity_4h` score `1.9081` n `40` status `ready` deltaP `32.1037` edge `-0.0503` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `1.9081` n `40` status `ready` deltaP `32.1037` edge `-0.0503` maxDD `-0.044`
- `risk_on_high->fx_1h` score `0.3105` n `44` status `ready` deltaP `6.8454` edge `0.0032` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.3105` n `44` status `ready` deltaP `6.8454` edge `0.0032` maxDD `-0.1704`
- `risk_on_high->crypto_major_4h` score `0.2923` n `40` status `ready` deltaP `13.2012` edge `0.0029` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.2923` n `40` status `ready` deltaP `13.2012` edge `0.0029` maxDD `-2.6576`
- `risk_on_high->equity_1h` score `0.0697` n `44` status `ready` deltaP `7.975` edge `-0.0084` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.0697` n `44` status `ready` deltaP `7.975` edge `-0.0084` maxDD `-0.7834`
- `risk_on_high->crypto_major_1h` score `0.0466` n `44` status `ready` deltaP `7.349` edge `0.0112` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.0466` n `44` status `ready` deltaP `7.349` edge `0.0112` maxDD `-2.3372`
- `risk_on_high->metal_4h` score `-0.0671` n `40` status `ready` deltaP `8.0488` edge `-0.0287` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `-0.0671` n `40` status `ready` deltaP `8.0488` edge `-0.0287` maxDD `-1.3516`
- `risk_on_high->fx_4h` score `-0.0813` n `40` status `ready` deltaP `7.0427` edge `0.0017` maxDD `-0.3925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
