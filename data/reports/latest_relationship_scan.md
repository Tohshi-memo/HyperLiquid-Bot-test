# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-02T20:08:06.200638+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11597`

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

- `risk_on_high->equity_24h` score `6.2345` n `107` status `ready` deltaP `27.1742` edge `0.7529` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `6.2345` n `107` status `ready` deltaP `27.1742` edge `0.7529` maxDD `-19.828`
- `risk_on_high->unknown_4h` score `6.0982` n `107` status `ready` deltaP `17.4764` edge `0.4535` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `6.0982` n `107` status `ready` deltaP `17.4764` edge `0.4535` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `4.1788` n `147` status `ready` deltaP `13.2104` edge `0.3297` maxDD `-2.563`
- `news_risk_high->equity_24h` score `3.2347` n `59` status `ready` deltaP `13.1238` edge `0.4288` maxDD `-15.4056`
- `market_context_high->equity_24h` score `2.3979` n `147` status `ready` deltaP `23.1434` edge `0.634` maxDD `-24.4698`
- `risk_on_high->crypto_alt_24h` score `1.5942` n `107` status `ready` deltaP `18.6527` edge `0.7704` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `1.5942` n `107` status `ready` deltaP `18.6527` edge `0.7704` maxDD `-42.8959`
- `news_risk_high->crypto_alt_24h` score `1.5652` n `59` status `ready` deltaP `18.5735` edge `0.3703` maxDD `-19.4761`
- `news_risk_high->commodity_4h` score `0.2506` n `67` status `ready` deltaP `5.9474` edge `0.0284` maxDD `-0.8733`
- `risk_on_high->index_4h` score `0.1389` n `107` status `ready` deltaP `20.9355` edge `0.0113` maxDD `-3.6448`
- `risk_on_and_context->index_4h` score `0.1389` n `107` status `ready` deltaP `20.9355` edge `0.0113` maxDD `-3.6448`
- `risk_on_high->index_1h` score `0.0917` n `107` status `ready` deltaP `7.9439` edge `0.0033` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.0917` n `107` status `ready` deltaP `7.9439` edge `0.0033` maxDD `-0.5605`
- `news_risk_high->index_1h` score `-0.0087` n `67` status `ready` deltaP `5.2239` edge `-0.0006` maxDD `-0.8275`
- `risk_on_high->metal_1h` score `-0.077` n `107` status `ready` deltaP `9.5501` edge `-0.0023` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `-0.077` n `107` status `ready` deltaP `9.5501` edge `-0.0023` maxDD `-1.699`
- `risk_on_high->unknown_1h` score `-0.1765` n `107` status `ready` deltaP `1.5754` edge `0.0325` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `-0.1765` n `107` status `ready` deltaP `1.5754` edge `0.0325` maxDD `-1.95`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
