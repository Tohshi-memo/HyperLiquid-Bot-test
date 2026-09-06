# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T17:52:26.419879+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10137`

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

- `risk_on_high->unknown_24h` score `188.6575` n `104` status `ready` deltaP `25.2404` edge `15.5631` maxDD `-0.1262`
- `risk_on_and_context->unknown_24h` score `188.6575` n `104` status `ready` deltaP `25.2404` edge `15.5631` maxDD `-0.1262`
- `risk_on_high->crypto_major_24h` score `17.5799` n `104` status `ready` deltaP `31.5171` edge `1.4237` maxDD `-10.1727`
- `risk_on_and_context->crypto_major_24h` score `17.5799` n `104` status `ready` deltaP `31.5171` edge `1.4237` maxDD `-10.1727`
- `risk_on_high->crypto_alt_24h` score `8.4867` n `104` status `ready` deltaP `19.5246` edge `0.7637` maxDD `-10.5978`
- `risk_on_and_context->crypto_alt_24h` score `8.4867` n `104` status `ready` deltaP `19.5246` edge `0.7637` maxDD `-10.5978`
- `market_context_high->equity_24h` score `5.1431` n `196` status `ready` deltaP `19.7244` edge `0.3847` maxDD `-3.6753`
- `market_context_high->crypto_alt_24h` score `5.0064` n `196` status `ready` deltaP `18.1902` edge `0.5079` maxDD `-11.9572`
- `risk_on_high->equity_24h` score `3.6528` n `104` status `ready` deltaP `15.211` edge `0.2906` maxDD `-3.6753`
- `risk_on_and_context->equity_24h` score `3.6528` n `104` status `ready` deltaP `15.211` edge `0.2906` maxDD `-3.6753`
- `market_context_high->index_24h` score `0.8754` n `196` status `ready` deltaP `17.2477` edge `0.0847` maxDD `-3.1385`
- `risk_on_high->index_24h` score `0.7296` n `104` status `ready` deltaP `14.0491` edge `0.0625` maxDD `-2.6291`
- `risk_on_and_context->index_24h` score `0.7296` n `104` status `ready` deltaP `14.0491` edge `0.0625` maxDD `-2.6291`
- `risk_on_high->index_1h` score `-0.0609` n `129` status `ready` deltaP `6.0437` edge `-0.0034` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `-0.0609` n `129` status `ready` deltaP `6.0437` edge `-0.0034` maxDD `-0.5764`
- `risk_on_high->metal_1h` score `-0.2665` n `129` status `ready` deltaP `5.8569` edge `-0.0027` maxDD `-1.6408`
- `risk_on_and_context->metal_1h` score `-0.2665` n `129` status `ready` deltaP `5.8569` edge `-0.0027` maxDD `-1.6408`
- `risk_on_high->crypto_alt_1h` score `-0.3018` n `129` status `ready` deltaP `2.6006` edge `0.0592` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.3018` n `129` status `ready` deltaP `2.6006` edge `0.0592` maxDD `-5.4685`
- `risk_on_high->equity_1h` score `-0.3581` n `129` status `ready` deltaP `8.1071` edge `-0.0129` maxDD `-2.6312`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
