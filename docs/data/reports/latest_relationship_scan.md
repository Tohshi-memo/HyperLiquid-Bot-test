# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-01T08:37:28.817077+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11438`

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

- `risk_on_high->unknown_4h` score `7.2425` n `107` status `ready` deltaP `20.5252` edge `0.5285` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.2425` n `107` status `ready` deltaP `20.5252` edge `0.5285` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `5.7891` n `151` status `ready` deltaP `16.8178` edge `0.4398` maxDD `-2.5597`
- `risk_on_high->unknown_1h` score `2.149` n `107` status `ready` deltaP `4.5694` edge `0.2063` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `2.149` n `107` status `ready` deltaP `4.5694` edge `0.2063` maxDD `-1.9475`
- `market_context_high->unknown_1h` score `2.0183` n `151` status `ready` deltaP `3.9319` edge `0.205` maxDD `-2.042`
- `news_risk_high->unknown_1h` score `1.243` n `61` status `ready` deltaP `1.6737` edge `0.1271` maxDD `-1.1072`
- `risk_on_high->commodity_24h` score `0.8166` n `107` status `ready` deltaP `10.3421` edge `0.0979` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `0.8166` n `107` status `ready` deltaP `10.3421` edge `0.0979` maxDD `-0.5706`
- `market_context_high->commodity_24h` score `0.2205` n `151` status `ready` deltaP `9.7107` edge `0.0732` maxDD `-1.2314`
- `news_risk_high->fx_4h` score `0.1523` n `61` status `ready` deltaP `10.6533` edge `0.001` maxDD `-0.7461`
- `risk_on_high->index_1h` score `0.0278` n `107` status `ready` deltaP `7.0457` edge `0.0011` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.0278` n `107` status `ready` deltaP `7.0457` edge `0.0011` maxDD `-0.5605`
- `market_context_high->commodity_1h` score `-0.0014` n `151` status `ready` deltaP `7.6744` edge `0.0137` maxDD `-1.5315`
- `risk_on_high->metal_1h` score `-0.0591` n `107` status `ready` deltaP `9.8495` edge `-0.002` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `-0.0591` n `107` status `ready` deltaP `9.8495` edge `-0.002` maxDD `-1.699`
- `risk_on_high->commodity_1h` score `-0.0742` n `107` status `ready` deltaP `4.5736` edge `0.0122` maxDD `-0.8428`
- `risk_on_and_context->commodity_1h` score `-0.0742` n `107` status `ready` deltaP `4.5736` edge `0.0122` maxDD `-0.8428`
- `risk_on_high->crypto_alt_24h` score `-0.0821` n `107` status `ready` deltaP `11.361` edge `0.6041` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `-0.0821` n `107` status `ready` deltaP `11.361` edge `0.6041` maxDD `-42.8959`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
