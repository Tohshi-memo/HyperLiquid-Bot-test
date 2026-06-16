# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-16T10:07:39.866364+00:00`
- Price records: `672`
- Market context records: `4081`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10232`

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

- `risk_on_high->unknown_4h` score `144.7683` n `40` status `ready` deltaP `-7.8963` edge `12.2983` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `144.7683` n `40` status `ready` deltaP `-7.8963` edge `12.2983` maxDD `-10.864`
- `market_context_high->unknown_1h` score `50.1248` n `174` status `ready` deltaP `2.1647` edge `4.3204` maxDD `-9.6211`
- `market_context_high->unknown_24h` score `37.092` n `144` status `ready` deltaP `-9.0663` edge `3.5543` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `16.8026` n `172` status `ready` deltaP `-2.0242` edge `1.956` maxDD `-35.7161`
- `risk_on_high->equity_4h` score `3.6094` n `40` status `ready` deltaP `37.5915` edge `0.0549` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `3.6094` n `40` status `ready` deltaP `37.5915` edge `0.0549` maxDD `-0.0446`
- `market_context_high->equity_4h` score `1.2342` n `172` status `ready` deltaP `14.5101` edge `0.1592` maxDD `-6.9137`
- `market_context_high->index_24h` score `0.9013` n `144` status `ready` deltaP `16.2912` edge `-0.0335` maxDD `0.0`
- `market_context_high->equity_1h` score `0.639` n `174` status `ready` deltaP `4.9075` edge `0.0765` maxDD `-2.144`
- `risk_on_high->crypto_major_4h` score `0.6149` n `40` status `ready` deltaP `17.7744` edge `-0.0007` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.6149` n `40` status `ready` deltaP `17.7744` edge `-0.0007` maxDD `-2.6576`
- `risk_on_high->equity_24h` score `0.4445` n `40` status `ready` deltaP `28.5962` edge `-0.1536` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `0.4445` n `40` status `ready` deltaP `28.5962` edge `-0.1536` maxDD `0.0`
- `risk_on_high->equity_1h` score `0.4328` n `40` status `ready` deltaP `10.9132` edge `0.0024` maxDD `-0.7937`
- `risk_on_and_context->equity_1h` score `0.4328` n `40` status `ready` deltaP `10.9132` edge `0.0024` maxDD `-0.7937`
- `risk_on_high->fx_4h` score `0.1919` n `40` status `ready` deltaP `11.9207` edge `0.0042` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.1919` n `40` status `ready` deltaP `11.9207` edge `0.0042` maxDD `-0.3925`
- `risk_on_high->metal_4h` score `0.1871` n `40` status `ready` deltaP `11.7073` edge `-0.0205` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.1871` n `40` status `ready` deltaP `11.7073` edge `-0.0205` maxDD `-1.3516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
