# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-16T03:22:31.076842+00:00`
- Price records: `672`
- Market context records: `4053`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10432`

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

- `risk_on_high->unknown_4h` score `144.9595` n `40` status `ready` deltaP `-7.5915` edge `12.3122` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `144.9595` n `40` status `ready` deltaP `-7.5915` edge `12.3122` maxDD `-10.864`
- `market_context_high->unknown_24h` score `39.2762` n `142` status `ready` deltaP `-7.7733` edge `3.7277` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `20.3815` n `161` status `ready` deltaP `0.1259` edge `2.2399` maxDD `-35.7161`
- `risk_on_high->equity_4h` score `3.7978` n `40` status `ready` deltaP `38.5061` edge `0.0645` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `3.7978` n `40` status `ready` deltaP `38.5061` edge `0.0645` maxDD `-0.0446`
- `risk_on_high->equity_24h` score `3.6592` n `40` status `ready` deltaP `33.2756` edge `0.0831` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `3.6592` n `40` status `ready` deltaP `33.2756` edge `0.0831` maxDD `0.0`
- `market_context_high->index_24h` score `2.0893` n `142` status `ready` deltaP `20.2663` edge `0.0602` maxDD `-1.3629`
- `market_context_high->equity_4h` score `1.4833` n `161` status `ready` deltaP `14.9191` edge `0.1689` maxDD `-6.9137`
- `risk_on_high->crypto_major_4h` score `1.344` n `40` status `ready` deltaP `20.2134` edge `0.0438` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.344` n `40` status `ready` deltaP `20.2134` edge `0.0438` maxDD `-2.6576`
- `market_context_high->equity_1h` score `0.8276` n `173` status `ready` deltaP `6.4397` edge `0.082` maxDD `-2.144`
- `risk_on_high->equity_1h` score `0.4951` n `40` status `ready` deltaP `11.512` edge `0.0036` maxDD `-0.7937`
- `risk_on_and_context->equity_1h` score `0.4951` n `40` status `ready` deltaP `11.512` edge `0.0036` maxDD `-0.7937`
- `risk_on_high->crypto_major_1h` score `0.2396` n `40` status `ready` deltaP `12.9042` edge `-0.0011` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.2396` n `40` status `ready` deltaP `12.9042` edge `-0.0011` maxDD `-2.3372`
- `risk_on_high->metal_4h` score `0.157` n `40` status `ready` deltaP `11.0976` edge `-0.0203` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.157` n `40` status `ready` deltaP `11.0976` edge `-0.0203` maxDD `-1.3516`
- `risk_on_high->fx_1h` score `0.0108` n `40` status `ready` deltaP `3.6527` edge `0.0` maxDD `-0.1704`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
