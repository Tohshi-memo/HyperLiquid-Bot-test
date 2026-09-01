# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-01T03:07:26.102877+00:00`
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

- `risk_on_high->unknown_4h` score `7.6156` n `107` status `ready` deltaP `23.2691` edge `0.5413` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.6156` n `107` status `ready` deltaP `23.2691` edge `0.5413` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `6.0484` n `152` status `ready` deltaP `19.0389` edge `0.4466` maxDD `-2.5597`
- `risk_on_high->unknown_1h` score `2.0578` n `107` status `ready` deltaP `4.8688` edge `0.1967` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `2.0578` n `107` status `ready` deltaP `4.8688` edge `0.1967` maxDD `-1.9475`
- `market_context_high->unknown_1h` score `1.9861` n `152` status `ready` deltaP `4.4753` edge `0.1987` maxDD `-2.042`
- `risk_on_high->commodity_24h` score `1.6008` n `105` status `ready` deltaP `13.7698` edge `0.1404` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `1.6008` n `105` status `ready` deltaP `13.7698` edge `0.1404` maxDD `-0.5706`
- `risk_on_high->crypto_alt_24h` score `1.1804` n `105` status `ready` deltaP `14.5039` edge `0.745` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `1.1804` n `105` status `ready` deltaP `14.5039` edge `0.745` maxDD `-42.8959`
- `news_risk_high->unknown_1h` score `1.1518` n `61` status `ready` deltaP `1.9731` edge `0.1175` maxDD `-1.1072`
- `market_context_high->commodity_24h` score `0.8791` n `150` status `ready` deltaP `12.7222` edge `0.108` maxDD `-1.2314`
- `news_risk_high->commodity_4h` score `0.1262` n `61` status `ready` deltaP `5.5103` edge `0.0211` maxDD `-1.3325`
- `news_risk_high->fx_4h` score `0.1232` n `61` status `ready` deltaP `10.3484` edge `0.0006` maxDD `-0.7461`
- `market_context_high->commodity_1h` score `0.0841` n `152` status `ready` deltaP `8.4581` edge `0.0156` maxDD `-1.5315`
- `risk_on_high->fx_24h` score `0.0621` n `105` status `ready` deltaP `36.756` edge `0.0238` maxDD `-4.2032`
- `risk_on_and_context->fx_24h` score `0.0621` n `105` status `ready` deltaP `36.756` edge `0.0238` maxDD `-4.2032`
- `market_context_high->commodity_4h` score `0.0201` n `152` status `ready` deltaP `6.3623` edge `0.049` maxDD `-2.1795`
- `risk_on_high->commodity_1h` score `0.0091` n `107` status `ready` deltaP `5.7712` edge `0.0149` maxDD `-0.8428`
- `risk_on_and_context->commodity_1h` score `0.0091` n `107` status `ready` deltaP `5.7712` edge `0.0149` maxDD `-0.8428`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
