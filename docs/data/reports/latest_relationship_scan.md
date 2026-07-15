# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T02:52:32.299445+00:00`
- Price records: `672`
- Market context records: `6774`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11688`

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

- `market_context_high->unknown_24h` score `1.0167` n `176` status `ready` deltaP `0.1894` edge `0.5043` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `0.0117` n `176` status `ready` deltaP `8.144` edge `0.1335` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.0154` n `176` status `ready` deltaP `7.8015` edge `0.032` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.2131` n `176` status `ready` deltaP `4.8993` edge `0.026` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.396` n `176` status `ready` deltaP `-0.4151` edge `0.0005` maxDD `-0.5468`
- `market_context_high->commodity_1h` score `-0.5892` n `176` status `ready` deltaP `0.1463` edge `-0.0082` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.652` n `176` status `ready` deltaP `-1.7658` edge `-0.0004` maxDD `-0.7136`
- `market_context_high->metal_1h` score `-0.7339` n `176` status `ready` deltaP `-5.59` edge `-0.0043` maxDD `-1.2017`
- `market_context_high->fx_4h` score `-1.2248` n `176` status `ready` deltaP `7.3864` edge `0.0001` maxDD `-2.1765`
- `market_context_high->index_4h` score `-1.2515` n `176` status `ready` deltaP `6.1391` edge `-0.0134` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-1.291` n `176` status `ready` deltaP `2.5075` edge `-0.0216` maxDD `-3.8827`
- `market_context_high->commodity_4h` score `-1.4931` n `176` status `ready` deltaP `-2.8409` edge `-0.0235` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.6866` n `176` status `ready` deltaP `-6.5766` edge `-0.0066` maxDD `-3.2083`
- `market_context_high->crypto_major_4h` score `-2.6974` n `176` status `ready` deltaP `3.0488` edge `-0.0347` maxDD `-16.8495`
- `market_context_high->metal_4h` score `-2.6991` n `176` status `ready` deltaP `-6.9291` edge `-0.0138` maxDD `-5.2172`
- `market_context_high->crypto_alt_4h` score `-2.8696` n `176` status `ready` deltaP `1.3026` edge `-0.0364` maxDD `-19.2145`
- `market_context_high->unknown_4h` score `-3.4759` n `176` status `ready` deltaP `-15.1053` edge `0.0476` maxDD `-10.2579`
- `market_context_high->equity_4h` score `-4.2299` n `176` status `ready` deltaP `2.7023` edge `-0.1334` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-4.2849` n `176` status `ready` deltaP `-7.702` edge `-0.0021` maxDD `-5.6237`
- `market_context_high->metal_24h` score `-8.8172` n `176` status `ready` deltaP `-15.7197` edge `-0.1771` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
