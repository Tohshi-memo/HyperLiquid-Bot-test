# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T17:22:33.467541+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8092`

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

- `market_context_high->unknown_4h` score `33.4251` n `150` status `ready` deltaP `0.4018` edge `2.8163` maxDD `-1.0178`
- `market_context_high->unknown_1h` score `28.2421` n `153` status `ready` deltaP `1.3248` edge `2.3936` maxDD `-1.5807`
- `market_context_high->metal_24h` score `0.4572` n `112` status `ready` deltaP `26.3617` edge `0.1455` maxDD `-7.0108`
- `market_context_high->fx_1h` score `0.2039` n `153` status `ready` deltaP `7.5163` edge `0.0027` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.1086` n `150` status `ready` deltaP `9.105` edge `0.0082` maxDD `-0.4545`
- `market_context_high->index_24h` score `-0.0051` n `112` status `ready` deltaP `16.3051` edge `0.0145` maxDD `-4.5747`
- `market_context_high->fx_24h` score `-0.1145` n `112` status `ready` deltaP `17.3186` edge `0.0271` maxDD `-1.2451`
- `market_context_high->metal_1h` score `-0.1595` n `153` status `ready` deltaP `7.8813` edge `0.0062` maxDD `-1.6682`
- `market_context_high->commodity_1h` score `-0.3121` n `153` status `ready` deltaP `1.8532` edge `0.0117` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.586` n `153` status `ready` deltaP `0.0127` edge `-0.0015` maxDD `-1.8971`
- `market_context_high->commodity_4h` score `-0.6946` n `150` status `ready` deltaP `4.2922` edge `0.0364` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-0.9176` n `153` status `ready` deltaP `3.7846` edge `0.0152` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-1.0274` n `150` status `ready` deltaP `6.3896` edge `-0.0033` maxDD `-5.3474`
- `market_context_high->equity_1h` score `-1.8105` n `153` status `ready` deltaP `1.6046` edge `-0.0152` maxDD `-12.2088`
- `market_context_high->crypto_alt_1h` score `-1.9967` n `153` status `ready` deltaP `-0.5753` edge `-0.0037` maxDD `-13.2099`
- `market_context_high->index_4h` score `-3.525` n `150` status `ready` deltaP `-7.3364` edge `-0.0272` maxDD `-6.7447`
- `market_context_high->crypto_major_24h` score `-4.3442` n `112` status `ready` deltaP `-1.925` edge `-0.0584` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-4.8319` n `150` status `ready` deltaP `-2.0395` edge `-0.1019` maxDD `-32.9851`
- `market_context_high->equity_24h` score `-5.9852` n `112` status `ready` deltaP `-2.8705` edge `-0.2049` maxDD `-35.4638`
- `market_context_high->commodity_24h` score `-6.3768` n `112` status `ready` deltaP `-17.5971` edge `-0.1413` maxDD `-24.0477`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
