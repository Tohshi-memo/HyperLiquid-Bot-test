# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-01T03:22:26.242814+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11496`

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

- `risk_on_high->unknown_4h` score `7.5962` n `107` status `ready` deltaP `23.1166` edge `0.5407` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.5962` n `107` status `ready` deltaP `23.1166` edge `0.5407` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `6.1428` n `151` status `ready` deltaP `19.4092` edge `0.452` maxDD `-2.5597`
- `risk_on_high->unknown_1h` score `2.0902` n `107` status `ready` deltaP `5.0185` edge `0.1984` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `2.0902` n `107` status `ready` deltaP `5.0185` edge `0.1984` maxDD `-1.9475`
- `market_context_high->unknown_1h` score `1.9594` n `151` status `ready` deltaP `4.381` edge `0.1971` maxDD `-2.042`
- `risk_on_high->commodity_24h` score `1.5883` n `106` status `ready` deltaP `13.7939` edge `0.1392` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `1.5883` n `106` status `ready` deltaP `13.7939` edge `0.1392` maxDD `-0.5706`
- `risk_on_high->crypto_alt_24h` score `1.2203` n `106` status `ready` deltaP `14.6717` edge `0.749` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `1.2203` n `106` status `ready` deltaP `14.6717` edge `0.749` maxDD `-42.8959`
- `news_risk_high->unknown_1h` score `1.1841` n `61` status `ready` deltaP `2.1228` edge `0.1192` maxDD `-1.1072`
- `market_context_high->commodity_24h` score `0.9965` n `150` status `ready` deltaP `13.2153` edge `0.1145` maxDD `-1.2314`
- `news_risk_high->fx_4h` score `0.1232` n `61` status `ready` deltaP `10.3484` edge `0.0006` maxDD `-0.7461`
- `news_risk_high->commodity_4h` score `0.1136` n `61` status `ready` deltaP `5.3579` edge `0.0205` maxDD `-1.3325`
- `market_context_high->commodity_1h` score `0.1125` n `151` status `ready` deltaP `8.7223` edge `0.0162` maxDD `-1.5315`
- `market_context_high->commodity_4h` score `0.066` n `151` status `ready` deltaP `6.6064` edge `0.0512` maxDD `-2.1795`
- `risk_on_high->fx_24h` score `0.0015` n `106` status `ready` deltaP `36.2618` edge `0.0238` maxDD `-4.2285`
- `risk_on_and_context->fx_24h` score `0.0015` n `106` status `ready` deltaP `36.2618` edge `0.0238` maxDD `-4.2285`
- `risk_on_high->commodity_1h` score `-0.0002` n `107` status `ready` deltaP `5.6215` edge `0.0147` maxDD `-0.8428`
- `risk_on_and_context->commodity_1h` score `-0.0002` n `107` status `ready` deltaP `5.6215` edge `0.0147` maxDD `-0.8428`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
