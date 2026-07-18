# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T04:52:29.748842+00:00`
- Price records: `672`
- Market context records: `7104`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11488`

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

- `market_context_high->fx_4h` score `0.3876` n `152` status `ready` deltaP `15.8697` edge `0.0139` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.1285` n `152` status `ready` deltaP `4.6959` edge `0.0031` maxDD `-0.276`
- `market_context_high->unknown_1h` score `-0.1505` n `152` status `ready` deltaP `-0.0867` edge `0.0439` maxDD `-1.4688`
- `market_context_high->crypto_alt_1h` score `-0.3858` n `152` status `ready` deltaP `1.0755` edge `0.0298` maxDD `-4.5815`
- `market_context_high->crypto_major_1h` score `-0.554` n `152` status `ready` deltaP `4.0065` edge `0.0375` maxDD `-7.1523`
- `market_context_high->index_1h` score `-0.5849` n `152` status `ready` deltaP `-0.981` edge `-0.0065` maxDD `-2.2895`
- `market_context_high->commodity_1h` score `-0.8484` n `152` status `ready` deltaP `-4.1601` edge `-0.0194` maxDD `-1.9306`
- `market_context_high->commodity_4h` score `-1.3559` n `152` status `ready` deltaP `-4.1399` edge `-0.0427` maxDD `-2.9494`
- `market_context_high->unknown_4h` score `-1.5411` n `152` status `ready` deltaP `-6.2821` edge `0.0045` maxDD `-4.4825`
- `market_context_high->metal_1h` score `-1.5762` n `152` status `ready` deltaP `-7.3787` edge `-0.0056` maxDD `-2.125`
- `market_context_high->equity_1h` score `-2.0694` n `152` status `ready` deltaP `3.1161` edge `-0.0438` maxDD `-14.716`
- `market_context_high->index_4h` score `-2.5258` n `152` status `ready` deltaP `-1.2917` edge `-0.0453` maxDD `-12.2591`
- `market_context_high->crypto_major_4h` score `-2.9942` n `152` status `ready` deltaP `4.5572` edge `0.0142` maxDD `-24.6094`
- `market_context_high->crypto_alt_4h` score `-3.0669` n `152` status `ready` deltaP `0.2166` edge `-0.0161` maxDD `-22.2831`
- `market_context_high->commodity_24h` score `-3.364` n `152` status `ready` deltaP `-7.913` edge `-0.0967` maxDD `-4.4704`
- `market_context_high->metal_4h` score `-4.394` n `152` status `ready` deltaP `-8.6329` edge `-0.0112` maxDD `-5.4601`
- `market_context_high->fx_24h` score `-4.4392` n `152` status `ready` deltaP `-9.978` edge `-0.0207` maxDD `-3.9503`
- `market_context_high->equity_4h` score `-8.7211` n `152` status `ready` deltaP `-1.4923` edge `-0.2211` maxDD `-63.963`
- `market_context_high->unknown_24h` score `-9.1062` n `152` status `ready` deltaP `-25.6305` edge `-0.0733` maxDD `-23.5076`
- `market_context_high->metal_24h` score `-14.8625` n `152` status `ready` deltaP `-25.6122` edge `-0.1455` maxDD `-42.7833`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
