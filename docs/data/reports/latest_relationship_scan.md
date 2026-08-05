# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T21:37:36.185159+00:00`
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

- `market_context_high->unknown_24h` score `12.85` n `90` status `ready` deltaP `4.4445` edge `1.0455` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `3.0331` n `107` status `ready` deltaP `-2.2495` edge `0.3673` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.2542` n `107` status `ready` deltaP `14.4062` edge `0.0931` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.9055` n `90` status `ready` deltaP `2.0139` edge `0.2195` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.8607` n `90` status `ready` deltaP `24.7223` edge `0.0661` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4299` n `109` status `ready` deltaP `7.7597` edge `0.0257` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0679` n `109` status `ready` deltaP `6.4316` edge `-0.0022` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.117` n `107` status `ready` deltaP `9.3885` edge `0.0084` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.4988` n `109` status `ready` deltaP `-1.1111` edge `-0.0071` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.7093` n `107` status `ready` deltaP `3.8153` edge `0.0071` maxDD `-3.211`
- `market_context_high->index_1h` score `-0.814` n `109` status `ready` deltaP `-4.4045` edge `-0.0216` maxDD `-1.6054`
- `market_context_high->crypto_alt_24h` score `-1.3767` n `90` status `ready` deltaP `0.5555` edge `-0.0359` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-1.5235` n `107` status `ready` deltaP `0.4146` edge `-0.0591` maxDD `-5.7857`
- `market_context_high->crypto_alt_1h` score `-1.5613` n `109` status `ready` deltaP `-5.1379` edge `-0.0248` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.9172` n `109` status `ready` deltaP `0.5206` edge `-0.0957` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.213` n `107` status `ready` deltaP `-13.9617` edge `-0.0652` maxDD `-4.7021`
- `market_context_high->index_24h` score `-2.2244` n `90` status `ready` deltaP `-8.8195` edge `-0.0069` maxDD `-7.8922`
- `market_context_high->crypto_major_1h` score `-3.3991` n `109` status `ready` deltaP `-11.5984` edge `-0.0686` maxDD `-7.6533`
- `market_context_high->unknown_1h` score `-3.6724` n `109` status `ready` deltaP `1.2841` edge `-0.2699` maxDD `-1.2421`
- `market_context_high->commodity_24h` score `-6.0801` n `90` status `ready` deltaP `10.3125` edge `-0.0268` maxDD `-51.0493`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
