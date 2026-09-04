# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T03:07:24.298551+00:00`
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

- `risk_on_high->unknown_4h` score `22.6323` n `133` status `ready` deltaP `9.6082` edge `1.8838` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `22.6323` n `133` status `ready` deltaP `9.6082` edge `1.8838` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `15.8673` n `167` status `ready` deltaP `11.2065` edge `1.3171` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `13.8355` n `133` status `ready` deltaP `-0.1554` edge `1.2117` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `13.8355` n `133` status `ready` deltaP `-0.1554` edge `1.2117` maxDD `-1.95`
- `market_context_high->unknown_1h` score `9.5252` n `171` status `ready` deltaP `0.513` edge `0.8534` maxDD `-2.0446`
- `market_context_high->equity_24h` score `0.8624` n `140` status `ready` deltaP `16.2946` edge `0.3978` maxDD `-20.7654`
- `risk_on_high->equity_24h` score `0.4579` n `118` status `ready` deltaP `11.9968` edge `0.3727` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `0.4579` n `118` status `ready` deltaP `11.9968` edge `0.3727` maxDD `-19.828`
- `news_risk_high->commodity_4h` score `0.3114` n `67` status `ready` deltaP `5.795` edge `0.0372` maxDD `-0.8733`
- `risk_on_high->metal_1h` score `0.0782` n `133` status `ready` deltaP `11.9637` edge `0.0015` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0782` n `133` status `ready` deltaP `11.9637` edge `0.0015` maxDD `-1.699`
- `news_risk_high->index_1h` score `-0.0648` n `67` status `ready` deltaP `4.4754` edge `-0.0028` maxDD `-0.8275`
- `risk_on_high->index_1h` score `-0.103` n `133` status `ready` deltaP `4.8906` edge `-0.0013` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.103` n `133` status `ready` deltaP `4.8906` edge `-0.0013` maxDD `-0.5605`
- `news_risk_high->commodity_24h` score `-0.1702` n `67` status `ready` deltaP `4.4517` edge `-0.0246` maxDD `-0.2074`
- `news_risk_high->commodity_1h` score `-0.1981` n `67` status `ready` deltaP `4.1581` edge `0.0004` maxDD `-0.9036`
- `news_risk_high->fx_4h` score `-0.2744` n `67` status `ready` deltaP `6.1453` edge `0.0018` maxDD `-1.2507`
- `risk_on_high->crypto_alt_1h` score `-0.2786` n `133` status `ready` deltaP `4.6013` edge `0.0478` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.2786` n `133` status `ready` deltaP `4.6013` edge `0.0478` maxDD `-5.4685`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
