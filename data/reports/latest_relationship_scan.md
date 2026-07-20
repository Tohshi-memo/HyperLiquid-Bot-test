# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-20T19:22:30.101892+00:00`
- Price records: `672`
- Market context records: `7384`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14654`

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

- `risk_on_high->crypto_major_4h` score `6.137` n `32` status `ready` deltaP `35.4421` edge `0.2944` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `6.137` n `32` status `ready` deltaP `35.4421` edge `0.2944` maxDD `-0.8742`
- `risk_on_high->unknown_4h` score `4.9147` n `32` status `ready` deltaP `15.3963` edge `0.3499` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `4.9147` n `32` status `ready` deltaP `15.3963` edge `0.3499` maxDD `-0.4384`
- `risk_on_high->crypto_alt_4h` score `4.7606` n `32` status `ready` deltaP `27.9726` edge `0.2346` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `4.7606` n `32` status `ready` deltaP `27.9726` edge `0.2346` maxDD `-0.9492`
- `risk_on_high->crypto_major_1h` score `1.1069` n `32` status `ready` deltaP `19.3301` edge `0.0375` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.1069` n `32` status `ready` deltaP `19.3301` edge `0.0375` maxDD `-0.957`
- `risk_on_high->commodity_1h` score `0.3352` n `32` status `ready` deltaP `4.7485` edge `0.0242` maxDD `-0.2339`
- `risk_on_and_context->commodity_1h` score `0.3352` n `32` status `ready` deltaP `4.7485` edge `0.0242` maxDD `-0.2339`
- `risk_on_high->equity_1h` score `0.1203` n `32` status `ready` deltaP `3.4535` edge `0.0301` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.1203` n `32` status `ready` deltaP `3.4535` edge `0.0301` maxDD `-1.3497`
- `risk_on_high->crypto_alt_1h` score `-0.0254` n `32` status `ready` deltaP `-0.4491` edge `0.0368` maxDD `-0.9651`
- `risk_on_and_context->crypto_alt_1h` score `-0.0254` n `32` status `ready` deltaP `-0.4491` edge `0.0368` maxDD `-0.9651`
- `market_context_high->fx_1h` score `-0.1959` n `132` status `ready` deltaP `3.6309` edge `-0.0002` maxDD `-0.5967`
- `risk_on_high->metal_4h` score `-0.236` n `32` status `ready` deltaP `-1.0671` edge `0.0698` maxDD `-0.5882`
- `risk_on_and_context->metal_4h` score `-0.236` n `32` status `ready` deltaP `-1.0671` edge `0.0698` maxDD `-0.5882`
- `market_context_high->commodity_1h` score `-0.5696` n `132` status `ready` deltaP `-1.5015` edge `-0.0058` maxDD `-1.5775`
- `market_context_high->commodity_4h` score `-0.7254` n `129` status `ready` deltaP `-0.3236` edge `0.006` maxDD `-2.4139`
- `market_context_high->unknown_4h` score `-0.8483` n `129` status `ready` deltaP `3.3323` edge `0.1049` maxDD `-6.2031`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
