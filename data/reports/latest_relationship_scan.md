# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T22:37:18.148236+00:00`
- Price records: `672`
- Market context records: `1057`
- Flow alert records: `4950`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8668`

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

- `market_context_high->crypto_major_24h` score `14.8347` n `178` status `ready` deltaP `34.1223` edge `1.0551` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.7535` n `178` status `ready` deltaP `11.7333` edge `0.4413` maxDD `-9.5387`
- `market_context_high->equity_24h` score `3.3835` n `178` status `ready` deltaP `11.1033` edge `0.2701` maxDD `-3.6396`
- `market_context_high->index_24h` score `2.6754` n `178` status `ready` deltaP `10.3776` edge `0.2179` maxDD `-2.1308`
- `market_context_high->metal_24h` score `1.7832` n `178` status `ready` deltaP `-6.8963` edge `0.3879` maxDD `-8.4658`
- `market_context_high->fx_1h` score `-0.0974` n `180` status `ready` deltaP `4.9335` edge `0.0002` maxDD `-0.3124`
- `market_context_high->crypto_major_1h` score `-0.4503` n `180` status `ready` deltaP `6.7498` edge `0.013` maxDD `-5.6422`
- `market_context_high->index_1h` score `-0.4724` n `180` status `ready` deltaP `3.9188` edge `0.0125` maxDD `-2.2395`
- `market_context_high->equity_1h` score `-0.5414` n `180` status `ready` deltaP `0.1996` edge `0.0263` maxDD `-4.1532`
- `market_context_high->commodity_1h` score `-0.7071` n `180` status `ready` deltaP `0.7285` edge `0.017` maxDD `-3.7959`
- `market_context_high->fx_4h` score `-0.7339` n `179` status `ready` deltaP `0.5323` edge `0.002` maxDD `-1.6381`
- `market_context_high->index_4h` score `-1.1248` n `179` status `ready` deltaP `0.1652` edge `0.0403` maxDD `-5.8105`
- `market_context_high->crypto_alt_1h` score `-1.1502` n `180` status `ready` deltaP `1.0413` edge `0.0058` maxDD `-5.3538`
- `market_context_high->equity_4h` score `-1.2872` n `179` status `ready` deltaP `1.7901` edge `0.07` maxDD `-9.803`
- `market_context_high->metal_1h` score `-1.5328` n `180` status `ready` deltaP `3.4564` edge `-0.0334` maxDD `-6.3899`
- `market_context_high->crypto_alt_4h` score `-2.7616` n `179` status `ready` deltaP `1.3387` edge `0.0364` maxDD `-15.0367`
- `market_context_high->crypto_major_4h` score `-2.8213` n `179` status `ready` deltaP `6.9305` edge `0.0537` maxDD `-19.8006`
- `market_context_high->fx_24h` score `-3.16` n `178` status `ready` deltaP `3.555` edge `-0.0212` maxDD `-19.2774`
- `market_context_high->metal_4h` score `-3.4878` n `179` status `ready` deltaP `-0.3347` edge `-0.1549` maxDD `-16.8684`
- `market_context_high->commodity_4h` score `-3.6137` n `179` status `ready` deltaP `-5.2017` edge `0.0503` maxDD `-13.0076`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
