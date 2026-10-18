# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T06:22:28.660842+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10438`

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

- `risk_on_high->commodity_24h` score `3.0045` n `67` status `ready` deltaP `19.9698` edge `0.1918` maxDD `-1.6311`
- `risk_on_and_context->commodity_24h` score `3.0045` n `67` status `ready` deltaP `19.9698` edge `0.1918` maxDD `-1.6311`
- `market_context_high->commodity_24h` score `2.1741` n `116` status `ready` deltaP `15.2349` edge `0.1684` maxDD `-2.4369`
- `market_context_high->crypto_major_4h` score `1.8078` n `151` status `ready` deltaP `16.7249` edge `0.3796` maxDD `-15.2359`
- `market_context_high->crypto_major_1h` score `0.6428` n `151` status `ready` deltaP `5.2435` edge `0.1075` maxDD `-3.7781`
- `risk_on_high->crypto_major_4h` score `0.1459` n `91` status `ready` deltaP `13.1517` edge `0.1791` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `0.1459` n `91` status `ready` deltaP `13.1517` edge `0.1791` maxDD `-11.1788`
- `market_context_high->crypto_alt_1h` score `0.1339` n `151` status `ready` deltaP `7.2986` edge `0.1185` maxDD `-7.3329`
- `risk_on_high->index_1h` score `-0.0257` n `91` status `ready` deltaP `4.5556` edge `0.0059` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.0257` n `91` status `ready` deltaP `4.5556` edge `0.0059` maxDD `-0.7394`
- `risk_on_high->fx_1h` score `-0.264` n `91` status `ready` deltaP `1.0478` edge `-0.0028` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.264` n `91` status `ready` deltaP `1.0478` edge `-0.0028` maxDD `-0.376`
- `market_context_high->index_1h` score `-0.3007` n `151` status `ready` deltaP `6.7607` edge `0.0047` maxDD `-1.3195`
- `market_context_high->metal_1h` score `-0.4251` n `151` status `ready` deltaP `6.4232` edge `0.0087` maxDD `-0.9556`
- `risk_on_high->equity_1h` score `-0.4344` n `91` status `ready` deltaP `9.4084` edge `0.0307` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.4344` n `91` status `ready` deltaP `9.4084` edge `0.0307` maxDD `-5.3696`
- `risk_on_high->metal_1h` score `-0.5016` n `91` status `ready` deltaP `0.6958` edge `0.0042` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.5016` n `91` status `ready` deltaP `0.6958` edge `0.0042` maxDD `-0.8513`
- `market_context_high->equity_1h` score `-0.5985` n `151` status `ready` deltaP `9.8523` edge `0.0384` maxDD `-7.3168`
- `market_context_high->metal_4h` score `-0.6707` n `151` status `ready` deltaP `5.1617` edge `0.0434` maxDD `-1.6961`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
