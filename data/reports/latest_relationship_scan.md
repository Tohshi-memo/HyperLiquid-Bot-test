# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-16T08:37:35.586724+00:00`
- Price records: `672`
- Market context records: `4075`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10224`

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

- `risk_on_high->unknown_4h` score `144.8529` n `40` status `ready` deltaP `-7.439` edge `12.3023` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `144.8529` n `40` status `ready` deltaP `-7.439` edge `12.3023` maxDD `-10.864`
- `market_context_high->unknown_1h` score `51.1304` n `172` status `ready` deltaP `2.1794` edge `4.4041` maxDD `-9.6211`
- `market_context_high->unknown_24h` score `37.1238` n `144` status `ready` deltaP `-8.893` edge `3.5558` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `16.8872` n `172` status `ready` deltaP `-1.5669` edge `1.96` maxDD `-35.7161`
- `risk_on_high->equity_4h` score `3.701` n `40` status `ready` deltaP `37.8963` edge `0.0605` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `3.701` n `40` status `ready` deltaP `37.8963` edge `0.0605` maxDD `-0.0446`
- `market_context_high->index_24h` score `1.3325` n `144` status `ready` deltaP `17.331` edge `-0.0045` maxDD `0.0`
- `market_context_high->equity_4h` score `1.3257` n `172` status `ready` deltaP `14.8149` edge `0.1648` maxDD `-6.9137`
- `risk_on_high->equity_24h` score `1.2681` n `40` status `ready` deltaP `29.636` edge `-0.0919` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.2681` n `40` status `ready` deltaP `29.636` edge `-0.0919` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `0.8969` n `40` status `ready` deltaP `18.689` edge `0.0167` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.8969` n `40` status `ready` deltaP `18.689` edge `0.0167` maxDD `-2.6576`
- `market_context_high->equity_1h` score `0.7406` n `172` status `ready` deltaP `5.6225` edge `0.0802` maxDD `-2.144`
- `risk_on_high->equity_1h` score `0.4448` n `40` status `ready` deltaP `10.9132` edge `0.0034` maxDD `-0.7937`
- `risk_on_and_context->equity_1h` score `0.4448` n `40` status `ready` deltaP `10.9132` edge `0.0034` maxDD `-0.7937`
- `risk_on_high->metal_4h` score `0.2277` n `40` status `ready` deltaP `11.7073` edge `-0.0153` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.2277` n `40` status `ready` deltaP `11.7073` edge `-0.0153` maxDD `-1.3516`
- `risk_on_high->fx_4h` score `0.1841` n `40` status `ready` deltaP `11.9207` edge `0.0032` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.1841` n `40` status `ready` deltaP `11.9207` edge `0.0032` maxDD `-0.3925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
