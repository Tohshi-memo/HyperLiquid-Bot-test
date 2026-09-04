# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T03:52:24.021212+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11538`

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

- `risk_on_high->unknown_4h` score `22.4855` n `133` status `ready` deltaP `9.3034` edge `1.8736` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `22.4855` n `133` status `ready` deltaP `9.3034` edge `1.8736` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `15.7205` n `167` status `ready` deltaP `10.9017` edge `1.3069` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `13.7275` n `133` status `ready` deltaP `-0.4548` edge `1.2047` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `13.7275` n `133` status `ready` deltaP `-0.4548` edge `1.2047` maxDD `-1.95`
- `market_context_high->unknown_1h` score `9.2164` n `174` status `ready` deltaP `0.2237` edge `0.8296` maxDD `-2.0446`
- `market_context_high->equity_24h` score `0.9322` n `143` status `ready` deltaP `16.4482` edge `0.4026` maxDD `-20.7654`
- `risk_on_high->equity_24h` score `0.6014` n `121` status `ready` deltaP `12.3795` edge `0.3821` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `0.6014` n `121` status `ready` deltaP `12.3795` edge `0.3821` maxDD `-19.828`
- `news_risk_high->commodity_4h` score `0.2932` n `67` status `ready` deltaP `5.4901` edge `0.0369` maxDD `-0.8733`
- `risk_on_high->metal_1h` score `0.0789` n `133` status `ready` deltaP `11.9637` edge `0.0016` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0789` n `133` status `ready` deltaP `11.9637` edge `0.0016` maxDD `-1.699`
- `news_risk_high->index_1h` score `-0.0889` n `67` status `ready` deltaP `4.0263` edge `-0.0029` maxDD `-0.8275`
- `risk_on_high->index_1h` score `-0.1271` n `133` status `ready` deltaP `4.4415` edge `-0.0014` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.1271` n `133` status `ready` deltaP `4.4415` edge `-0.0014` maxDD `-0.5605`
- `news_risk_high->commodity_24h` score `-0.1702` n `67` status `ready` deltaP `4.4517` edge `-0.0246` maxDD `-0.2074`
- `news_risk_high->commodity_1h` score `-0.2113` n `67` status `ready` deltaP `4.0084` edge `0.0003` maxDD `-0.9036`
- `risk_on_high->crypto_alt_1h` score `-0.2977` n `133` status `ready` deltaP `4.4516` edge `0.0472` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.2977` n `133` status `ready` deltaP `4.4516` edge `0.0472` maxDD `-5.4685`
- `news_risk_high->fx_4h` score `-0.317` n `67` status `ready` deltaP `5.688` edge `0.0013` maxDD `-1.2507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
