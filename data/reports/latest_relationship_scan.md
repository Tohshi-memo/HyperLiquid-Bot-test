# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-16T04:07:30.461170+00:00`
- Price records: `672`
- Market context records: `4056`
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

- `risk_on_high->unknown_4h` score `145.0067` n `40` status `ready` deltaP `-7.2866` edge `12.3141` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `145.0067` n `40` status `ready` deltaP `-7.2866` edge `12.3141` maxDD `-10.864`
- `market_context_high->unknown_24h` score `36.7551` n `145` status `ready` deltaP `-7.6376` edge `3.5167` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `19.4196` n `164` status `ready` deltaP `-0.1525` edge `2.1616` maxDD `-35.7161`
- `risk_on_high->equity_4h` score `3.8678` n `40` status `ready` deltaP `38.811` edge `0.0683` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `3.8678` n `40` status `ready` deltaP `38.811` edge `0.0683` maxDD `-0.0446`
- `risk_on_high->equity_24h` score `3.38` n `40` status `ready` deltaP `32.7556` edge `0.0633` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `3.38` n `40` status `ready` deltaP `32.7556` edge `0.0633` maxDD `0.0`
- `market_context_high->index_24h` score `1.9564` n `145` status `ready` deltaP `19.7609` edge `0.0525` maxDD `-1.3629`
- `risk_on_high->crypto_major_4h` score `1.3872` n `40` status `ready` deltaP `20.2134` edge `0.0474` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.3872` n `40` status `ready` deltaP `20.2134` edge `0.0474` maxDD `-2.6576`
- `market_context_high->equity_4h` score `1.3399` n `164` status `ready` deltaP `14.4817` edge `0.1682` maxDD `-6.9137`
- `market_context_high->equity_1h` score `0.8372` n `173` status `ready` deltaP `6.4397` edge `0.0828` maxDD `-2.144`
- `risk_on_high->equity_1h` score `0.5047` n `40` status `ready` deltaP `11.512` edge `0.0044` maxDD `-0.7937`
- `risk_on_and_context->equity_1h` score `0.5047` n `40` status `ready` deltaP `11.512` edge `0.0044` maxDD `-0.7937`
- `risk_on_high->crypto_major_1h` score `0.2029` n `40` status `ready` deltaP `12.6048` edge `-0.0038` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.2029` n `40` status `ready` deltaP `12.6048` edge `-0.0038` maxDD `-2.3372`
- `risk_on_high->metal_4h` score `0.1932` n `40` status `ready` deltaP `11.5549` edge `-0.0187` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.1932` n `40` status `ready` deltaP `11.5549` edge `-0.0187` maxDD `-1.3516`
- `risk_on_high->fx_4h` score `0.0032` n `40` status `ready` deltaP `9.1768` edge `-0.0017` maxDD `-0.3925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
