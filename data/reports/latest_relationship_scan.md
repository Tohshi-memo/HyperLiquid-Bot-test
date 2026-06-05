# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T20:31:23.949088+00:00`
- Price records: `672`
- Market context records: `3003`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6984`

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

- `market_context_high->crypto_alt_24h` score `19.6071` n `98` status `ready` deltaP `7.1995` edge `1.9776` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `12.5416` n `98` status `ready` deltaP `42.6411` edge `0.7719` maxDD `-0.2165`
- `market_context_high->unknown_24h` score `12.083` n `98` status `ready` deltaP `19.4374` edge `0.9238` maxDD `-1.7175`
- `market_context_high->equity_24h` score `9.7438` n `98` status `ready` deltaP `18.1725` edge `0.8912` maxDD `-12.6963`
- `market_context_high->index_24h` score `6.0345` n `98` status `ready` deltaP `17.7828` edge `0.4824` maxDD `-2.5127`
- `market_context_high->commodity_4h` score `2.2885` n `102` status `ready` deltaP `17.1479` edge `0.1411` maxDD `-2.8438`
- `market_context_high->index_4h` score `1.5297` n `102` status `ready` deltaP `19.1057` edge `0.1285` maxDD `-5.9381`
- `market_context_high->equity_4h` score `1.1366` n `102` status `ready` deltaP `14.3592` edge `0.192` maxDD `-9.0276`
- `market_context_high->commodity_1h` score `-0.0985` n `108` status `ready` deltaP `0.9537` edge `0.0184` maxDD `-0.9706`
- `market_context_high->equity_1h` score `-0.2622` n `108` status `ready` deltaP `4.4134` edge `0.0389` maxDD `-5.1553`
- `market_context_high->crypto_alt_4h` score `-0.2722` n `102` status `ready` deltaP `22.6536` edge `0.3642` maxDD `-38.3432`
- `market_context_high->index_1h` score `-0.2988` n `108` status `ready` deltaP `4.4522` edge `0.0183` maxDD `-3.5698`
- `market_context_high->fx_1h` score `-0.4816` n `108` status `ready` deltaP `-3.2269` edge `0.0005` maxDD `-0.2587`
- `market_context_high->crypto_alt_1h` score `-0.8241` n `108` status `ready` deltaP `6.7809` edge `0.0621` maxDD `-14.7034`
- `market_context_high->fx_4h` score `-1.1141` n `102` status `ready` deltaP `-9.8039` edge `0.0004` maxDD `-0.5631`
- `market_context_high->crypto_major_1h` score `-1.3117` n `108` status `ready` deltaP `4.2193` edge `0.03` maxDD `-15.1032`
- `market_context_high->unknown_4h` score `-1.3885` n `102` status `ready` deltaP `-1.0013` edge `-0.0037` maxDD `-3.7602`
- `market_context_high->unknown_1h` score `-1.472` n `108` status `ready` deltaP `1.4582` edge `-0.0593` maxDD `-3.1801`
- `market_context_high->fx_24h` score `-1.9093` n `98` status `ready` deltaP `-6.8275` edge `-0.0264` maxDD `-0.6418`
- `market_context_high->metal_1h` score `-2.0436` n `108` status `ready` deltaP `-3.8146` edge `-0.0135` maxDD `-6.843`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
