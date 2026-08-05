# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T20:53:20.178233+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11685`

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

- `market_context_high->unknown_24h` score `12.88` n `90` status `ready` deltaP `4.4445` edge `1.048` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `2.9499` n `107` status `ready` deltaP `-2.5544` edge `0.3624` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.3039` n `107` status `ready` deltaP `14.8636` edge `0.0942` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.9102` n `90` status `ready` deltaP `2.0139` edge `0.2201` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.8739` n `90` status `ready` deltaP `24.7223` edge `0.0678` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4599` n `109` status `ready` deltaP `8.0591` edge `0.0262` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0548` n `109` status `ready` deltaP `6.2819` edge `-0.0023` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.0925` n `107` status `ready` deltaP `9.8458` edge `0.0085` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.4934` n `109` status `ready` deltaP `-0.9614` edge `-0.0074` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.7227` n `107` status `ready` deltaP `3.6628` edge `0.0064` maxDD `-3.211`
- `market_context_high->index_1h` score `-0.8234` n `109` status `ready` deltaP `-4.5542` edge `-0.0218` maxDD `-1.6054`
- `market_context_high->crypto_alt_24h` score `-1.4368` n `90` status `ready` deltaP `0.5555` edge `-0.0436` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-1.5854` n `107` status `ready` deltaP `0.1097` edge `-0.065` maxDD `-5.7857`
- `market_context_high->crypto_alt_1h` score `-1.6381` n `109` status `ready` deltaP `-5.4373` edge `-0.0292` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.9383` n `109` status `ready` deltaP `0.3709` edge `-0.0974` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.2508` n `107` status `ready` deltaP `-14.419` edge `-0.067` maxDD `-4.7021`
- `market_context_high->index_24h` score `-2.2967` n `90` status `ready` deltaP `-9.3403` edge `-0.0127` maxDD `-7.8922`
- `market_context_high->crypto_major_1h` score `-3.4866` n `109` status `ready` deltaP `-12.0475` edge `-0.0729` maxDD `-7.6533`
- `market_context_high->unknown_1h` score `-3.6808` n `109` status `ready` deltaP `1.4338` edge `-0.2716` maxDD `-1.2421`
- `market_context_high->commodity_24h` score `-6.046` n `90` status `ready` deltaP `10.8334` edge `-0.0259` maxDD `-51.0493`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
