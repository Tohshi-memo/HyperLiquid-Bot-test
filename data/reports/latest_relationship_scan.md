# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T10:22:28.794158+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7058`

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

- `market_context_high->unknown_24h` score `1780.457` n `134` status `ready` deltaP `-2.7908` edge `148.433` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `273.8344` n `35` status `ready` deltaP `-1.5611` edge `22.8425` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `34.5715` n `134` status `ready` deltaP `3.9224` edge `2.8681` maxDD `-0.3966`
- `market_context_high->index_24h` score `3.1134` n `134` status `ready` deltaP `33.3541` edge `0.0554` maxDD `-0.1315`
- `market_context_high->equity_24h` score `1.9024` n `134` status `ready` deltaP `16.3117` edge `0.3255` maxDD `-14.0571`
- `news_risk_high->crypto_alt_1h` score `1.0418` n `35` status `ready` deltaP `11.6339` edge `0.0977` maxDD `-1.669`
- `news_risk_high->index_1h` score `0.8291` n `35` status `ready` deltaP `18.734` edge `0.0016` maxDD `-0.283`
- `market_context_high->metal_1h` score `0.34` n `134` status `ready` deltaP `10.3048` edge `0.0128` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.2917` n `134` status `ready` deltaP `15.3736` edge `0.0245` maxDD `-1.8344`
- `market_context_high->commodity_4h` score `0.1225` n `134` status `ready` deltaP `12.7184` edge `0.0473` maxDD `-1.0837`
- `market_context_high->equity_1h` score `0.0975` n `134` status `ready` deltaP `4.1827` edge `0.0678` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `0.0229` n `134` status `ready` deltaP `7.0158` edge `0.0579` maxDD `-5.2213`
- `market_context_high->fx_1h` score `-0.1135` n `134` status `ready` deltaP `3.4297` edge `-0.0016` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.3415` n `134` status `ready` deltaP `1.4948` edge `0.013` maxDD `-0.4475`
- `news_risk_high->commodity_1h` score `-0.3535` n `35` status `ready` deltaP `-6.3944` edge `0.0275` maxDD `-0.4158`
- `market_context_high->equity_4h` score `-0.4606` n `134` status `ready` deltaP `0.8668` edge `0.0936` maxDD `-6.008`
- `news_risk_high->fx_1h` score `-0.5206` n `35` status `ready` deltaP `-2.4765` edge `0.0012` maxDD `-0.1142`
- `market_context_high->fx_4h` score `-0.6168` n `134` status `ready` deltaP `-2.15` edge `-0.0049` maxDD `-0.4545`
- `news_risk_high->metal_1h` score `-0.7618` n `35` status `ready` deltaP `-5.0471` edge `-0.0103` maxDD `-0.9639`
- `market_context_high->crypto_alt_1h` score `-0.8282` n `134` status `ready` deltaP `2.9985` edge `0.0603` maxDD `-8.251`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
