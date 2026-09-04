# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T00:37:23.500439+00:00`
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

- `risk_on_high->unknown_4h` score `22.9537` n `133` status `ready` deltaP `10.3704` edge `1.9055` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `22.9537` n `133` status `ready` deltaP `10.3704` edge `1.9055` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `16.1886` n `167` status `ready` deltaP `11.9687` edge `1.3388` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `14.3586` n `133` status `ready` deltaP `-0.0057` edge `1.2543` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `14.3586` n `133` status `ready` deltaP `-0.0057` edge `1.2543` maxDD `-1.95`
- `market_context_high->unknown_1h` score `9.8788` n `167` status `ready` deltaP `0.4491` edge `0.8833` maxDD `-2.0446`
- `market_context_high->equity_24h` score `0.429` n `130` status `ready` deltaP `15.5582` edge `0.3666` maxDD `-20.7654`
- `news_risk_high->commodity_4h` score `0.3042` n `67` status `ready` deltaP `5.6425` edge `0.0373` maxDD `-0.8733`
- `risk_on_high->metal_1h` score `0.0688` n `133` status `ready` deltaP `11.814` edge `0.0013` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0688` n `133` status `ready` deltaP `11.814` edge `0.0013` maxDD `-1.699`
- `news_risk_high->index_1h` score `-0.0407` n `67` status `ready` deltaP `4.9245` edge `-0.0027` maxDD `-0.8275`
- `risk_on_high->index_1h` score `-0.0788` n `133` status `ready` deltaP `5.3397` edge `-0.0012` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.0788` n `133` status `ready` deltaP `5.3397` edge `-0.0012` maxDD `-0.5605`
- `news_risk_high->fx_4h` score `-0.1392` n `67` status `ready` deltaP `7.6697` edge `0.0029` maxDD `-1.2507`
- `risk_on_high->crypto_alt_1h` score `-0.1742` n `133` status `ready` deltaP `4.6013` edge `0.0565` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.1742` n `133` status `ready` deltaP `4.6013` edge `0.0565` maxDD `-5.4685`
- `news_risk_high->commodity_24h` score `-0.1834` n `67` status `ready` deltaP `4.4517` edge `-0.0257` maxDD `-0.2074`
- `news_risk_high->commodity_1h` score `-0.1981` n `67` status `ready` deltaP `4.1581` edge `0.0004` maxDD `-0.9036`
- `risk_on_high->fx_24h` score `-0.2162` n `108` status `ready` deltaP `25.2315` edge `0.0809` maxDD `-4.4797`
- `risk_on_and_context->fx_24h` score `-0.2162` n `108` status `ready` deltaP `25.2315` edge `0.0809` maxDD `-4.4797`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
