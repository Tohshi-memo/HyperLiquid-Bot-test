# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T14:07:29.775758+00:00`
- Price records: `672`
- Market context records: `2873`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6912`

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

- `market_context_high->crypto_alt_24h` score `7.0421` n `142` status `ready` deltaP `6.3479` edge `0.9362` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `4.2872` n `142` status `ready` deltaP `8.3308` edge `0.3482` maxDD `-1.7175`
- `market_context_high->equity_24h` score `3.9806` n `142` status `ready` deltaP `7.6926` edge `0.4808` maxDD `-12.6963`
- `market_context_high->index_24h` score `2.0276` n `142` status `ready` deltaP `9.891` edge `0.2011` maxDD `-2.5127`
- `market_context_high->commodity_24h` score `1.6354` n `142` status `ready` deltaP `15.2044` edge `0.3443` maxDD `-12.4171`
- `market_context_high->unknown_4h` score `0.9178` n `142` status `ready` deltaP `6.0331` edge `0.1416` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.7383` n `142` status `ready` deltaP `15.435` edge `0.0759` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.0169` n `142` status `ready` deltaP `4.1811` edge `0.0438` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.0197` n `142` status `ready` deltaP `4.6471` edge `0.0159` maxDD `-1.2855`
- `market_context_high->equity_4h` score `-0.0674` n `142` status `ready` deltaP `4.4014` edge `0.103` maxDD `-5.7037`
- `market_context_high->crypto_alt_4h` score `-0.5097` n `142` status `ready` deltaP `14.4903` edge `0.295` maxDD `-28.7261`
- `market_context_high->commodity_1h` score `-0.6233` n `142` status `ready` deltaP `-0.8813` edge `0.0013` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.6784` n `142` status `ready` deltaP `-2.1843` edge `0.0024` maxDD `-0.2164`
- `market_context_high->crypto_alt_1h` score `-0.7037` n `142` status `ready` deltaP `4.6471` edge `0.0548` maxDD `-10.747`
- `market_context_high->metal_1h` score `-0.7736` n `142` status `ready` deltaP `-1.0648` edge `-0.0075` maxDD `-3.0996`
- `market_context_high->equity_1h` score `-0.7792` n `142` status `ready` deltaP `-2.0009` edge `0.0317` maxDD `-2.6634`
- `market_context_high->crypto_major_1h` score `-0.836` n `142` status `ready` deltaP `4.5248` edge `0.0496` maxDD `-9.622`
- `market_context_high->commodity_4h` score `-1.159` n `142` status `ready` deltaP `3.5147` edge `0.02` maxDD `-10.0279`
- `market_context_high->fx_4h` score `-1.2795` n `142` status `ready` deltaP `-4.9725` edge `0.0044` maxDD `-0.5631`
- `market_context_high->fx_24h` score `-1.3903` n `142` status `ready` deltaP `-1.8852` edge `-0.0161` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
