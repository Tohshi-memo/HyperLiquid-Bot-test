# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-16T14:37:40.742358+00:00`
- Price records: `672`
- Market context records: `4100`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10424`

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

- `risk_on_high->unknown_4h` score `144.7335` n `40` status `ready` deltaP `-8.811` edge `12.3015` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `144.7335` n `40` status `ready` deltaP `-8.811` edge `12.3015` maxDD `-10.864`
- `market_context_high->unknown_1h` score `46.25` n `182` status `ready` deltaP `1.91` edge `3.9992` maxDD `-9.6211`
- `market_context_high->unknown_24h` score `37.158` n `144` status `ready` deltaP `-9.0663` edge `3.5598` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `15.6902` n `177` status `ready` deltaP `-1.9042` edge `1.8625` maxDD `-35.7161`
- `risk_on_high->equity_4h` score `2.5243` n `40` status `ready` deltaP `36.372` edge `-0.0274` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `2.5243` n `40` status `ready` deltaP `36.372` edge `-0.0274` maxDD `-0.0446`
- `risk_on_high->equity_1h` score `0.3596` n `40` status `ready` deltaP `10.9132` edge `-0.0037` maxDD `-0.7937`
- `risk_on_and_context->equity_1h` score `0.3596` n `40` status `ready` deltaP `10.9132` edge `-0.0037` maxDD `-0.7937`
- `market_context_high->equity_1h` score `0.1667` n `182` status `ready` deltaP `4.4022` edge `0.0565` maxDD `-3.4235`
- `risk_on_high->fx_4h` score `0.1547` n `40` status `ready` deltaP `11.311` edge `0.0035` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.1547` n `40` status `ready` deltaP `11.311` edge `0.0035` maxDD `-0.3925`
- `risk_on_high->fx_1h` score `0.0988` n `40` status `ready` deltaP `5.1497` edge `0.0013` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.0988` n `40` status `ready` deltaP `5.1497` edge `0.0013` maxDD `-0.1704`
- `risk_on_high->crypto_major_1h` score `-0.0207` n `40` status `ready` deltaP `10.509` edge `-0.0185` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `-0.0207` n `40` status `ready` deltaP `10.509` edge `-0.0185` maxDD `-2.3372`
- `risk_on_high->crypto_major_4h` score `-0.183` n `40` status `ready` deltaP `15.9451` edge `-0.055` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `-0.183` n `40` status `ready` deltaP `15.9451` edge `-0.055` maxDD `-2.6576`
- `market_context_high->equity_4h` score `-0.2092` n `177` status `ready` deltaP `11.7534` edge `0.0573` maxDD `-6.9137`
- `market_context_high->metal_1h` score `-0.2942` n `182` status `ready` deltaP `6.5424` edge `0.0216` maxDD `-4.9015`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
