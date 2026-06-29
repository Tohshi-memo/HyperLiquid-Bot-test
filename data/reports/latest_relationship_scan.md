# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T02:07:31.672446+00:00`
- Price records: `672`
- Market context records: `5100`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10340`

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

- `market_context_high->unknown_24h` score `19.0408` n `79` status `ready` deltaP `27.3734` edge `1.4385` maxDD `-1.4072`
- `market_context_high->unknown_4h` score `8.2853` n `107` status `ready` deltaP `22.1948` edge `0.6447` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `7.4132` n `119` status `ready` deltaP `4.3224` edge `0.6531` maxDD `-2.7986`
- `market_context_high->crypto_alt_4h` score `2.8659` n `107` status `ready` deltaP `13.4317` edge `0.4378` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `2.1836` n `107` status `ready` deltaP `11.715` edge `0.4311` maxDD `-14.0065`
- `market_context_high->equity_4h` score `1.0309` n `107` status `ready` deltaP `10.4229` edge `0.18` maxDD `-6.3852`
- `market_context_high->crypto_alt_1h` score `0.5189` n `119` status `ready` deltaP `6.8673` edge `0.1169` maxDD `-5.0257`
- `market_context_high->equity_1h` score `0.5016` n `119` status `ready` deltaP `9.4223` edge `0.0608` maxDD `-2.745`
- `market_context_high->crypto_major_1h` score `0.4101` n `119` status `ready` deltaP `7.6397` edge `0.1262` maxDD `-6.9639`
- `market_context_high->metal_1h` score `0.2863` n `119` status `ready` deltaP `8.6637` edge `0.0286` maxDD `-1.3057`
- `market_context_high->index_4h` score `0.0073` n `107` status `ready` deltaP `6.7571` edge `0.0365` maxDD `-1.4486`
- `market_context_high->index_1h` score `-0.0254` n `119` status `ready` deltaP `5.3125` edge `0.0117` maxDD `-1.0296`
- `market_context_high->metal_4h` score `-0.4587` n `107` status `ready` deltaP `2.959` edge `0.0625` maxDD `-4.6157`
- `market_context_high->commodity_1h` score `-0.8772` n `119` status `ready` deltaP `0.3862` edge `0.0001` maxDD `-2.062`
- `market_context_high->fx_1h` score `-1.382` n `119` status `ready` deltaP `-7.3605` edge `-0.002` maxDD `-0.7944`
- `market_context_high->fx_24h` score `-1.5757` n `79` status `ready` deltaP `-3.3162` edge `-0.008` maxDD `-1.7626`
- `market_context_high->commodity_24h` score `-1.676` n `79` status `ready` deltaP `7.7004` edge `0.03` maxDD `-15.0303`
- `market_context_high->fx_4h` score `-1.9571` n `107` status `ready` deltaP `-7.3341` edge `-0.0069` maxDD `-1.9169`
- `market_context_high->commodity_4h` score `-2.0729` n `107` status `ready` deltaP `3.0915` edge `-0.0233` maxDD `-7.2707`
- `market_context_high->metal_24h` score `-4.5356` n `79` status `ready` deltaP `-6.5995` edge `0.008` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
