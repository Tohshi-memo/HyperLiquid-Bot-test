# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T04:52:30.479263+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11550`

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

- `risk_on_high->unknown_4h` score `21.7775` n `133` status `ready` deltaP `9.3034` edge `1.8146` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `21.7775` n `133` status `ready` deltaP `9.3034` edge `1.8146` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `15.0125` n `167` status `ready` deltaP `10.9017` edge `1.2479` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `13.2823` n `133` status `ready` deltaP `-0.4548` edge `1.1676` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `13.2823` n `133` status `ready` deltaP `-0.4548` edge `1.1676` maxDD `-1.95`
- `market_context_high->unknown_1h` score `10.115` n `178` status `ready` deltaP `0.9856` edge `0.8994` maxDD `-2.0446`
- `market_context_high->equity_24h` score `1.0328` n `147` status `ready` deltaP `16.61` edge `0.4099` maxDD `-20.7654`
- `risk_on_high->equity_24h` score `0.7952` n `125` status `ready` deltaP `12.8222` edge `0.3953` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `0.7952` n `125` status `ready` deltaP `12.8222` edge `0.3953` maxDD `-19.828`
- `news_risk_high->commodity_4h` score `0.2536` n `67` status `ready` deltaP `4.8803` edge `0.0359` maxDD `-0.8733`
- `risk_on_high->metal_1h` score `0.0797` n `133` status `ready` deltaP `11.9637` edge `0.0017` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0797` n `133` status `ready` deltaP `11.9637` edge `0.0017` maxDD `-1.699`
- `news_risk_high->index_1h` score `-0.1232` n `67` status `ready` deltaP `3.4275` edge `-0.0033` maxDD `-0.8275`
- `risk_on_high->index_1h` score `-0.1614` n `133` status `ready` deltaP `3.8427` edge `-0.0018` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.1614` n `133` status `ready` deltaP `3.8427` edge `-0.0018` maxDD `-0.5605`
- `news_risk_high->commodity_24h` score `-0.1702` n `67` status `ready` deltaP `4.4517` edge `-0.0246` maxDD `-0.2074`
- `news_risk_high->commodity_1h` score `-0.1993` n `67` status `ready` deltaP `4.1581` edge `0.0003` maxDD `-0.9036`
- `risk_on_high->crypto_alt_1h` score `-0.2965` n `133` status `ready` deltaP `4.4516` edge `0.0473` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.2965` n `133` status `ready` deltaP `4.4516` edge `0.0473` maxDD `-5.4685`
- `news_risk_high->fx_4h` score `-0.3729` n `67` status `ready` deltaP `5.0783` edge `0.0007` maxDD `-1.2507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
