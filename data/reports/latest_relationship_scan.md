# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T14:22:25.266030+00:00`
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

- `risk_on_high->crypto_alt_24h` score `14.5681` n `64` status `ready` deltaP `36.9792` edge `1.217` maxDD `-16.295`
- `risk_on_and_context->crypto_alt_24h` score `14.5681` n `64` status `ready` deltaP `36.9792` edge `1.217` maxDD `-16.295`
- `risk_on_high->unknown_4h` score `8.148` n `107` status `ready` deltaP `25.4032` edge `0.5713` maxDD `-2.266`
- `risk_on_and_context->unknown_4h` score `8.148` n `107` status `ready` deltaP `25.4032` edge `0.5713` maxDD `-2.266`
- `market_context_high->unknown_4h` score `6.602` n `159` status `ready` deltaP `22.0998` edge `0.4722` maxDD `-2.5493`
- `market_context_high->crypto_alt_24h` score `4.9735` n `106` status `ready` deltaP `18.3176` edge `0.7113` maxDD `-27.517`
- `risk_on_high->fx_24h` score `3.1689` n `64` status `ready` deltaP `61.6319` edge `0.0449` maxDD `-0.9608`
- `risk_on_and_context->fx_24h` score `3.1689` n `64` status `ready` deltaP `61.6319` edge `0.0449` maxDD `-0.9608`
- `risk_on_high->crypto_major_24h` score `2.4777` n `64` status `ready` deltaP `22.3958` edge `0.5637` maxDD `-26.2949`
- `risk_on_and_context->crypto_major_24h` score `2.4777` n `64` status `ready` deltaP `22.3958` edge `0.5637` maxDD `-26.2949`
- `risk_on_high->unknown_1h` score `2.4766` n `107` status `ready` deltaP `6.9646` edge `0.2176` maxDD `-1.9453`
- `risk_on_and_context->unknown_1h` score `2.4766` n `107` status `ready` deltaP `6.9646` edge `0.2176` maxDD `-1.9453`
- `market_context_high->unknown_1h` score `2.254` n `159` status `ready` deltaP `6.3063` edge `0.2088` maxDD `-2.041`
- `market_context_high->metal_24h` score `2.0932` n `106` status `ready` deltaP `29.5859` edge `0.2021` maxDD `-4.145`
- `news_risk_high->unknown_1h` score `1.5731` n `61` status `ready` deltaP `4.0689` edge `0.1386` maxDD `-1.1043`
- `market_context_high->fx_24h` score `1.4822` n `106` status `ready` deltaP `36.0718` edge `0.0289` maxDD `-1.6688`
- `market_context_high->crypto_major_24h` score `1.191` n `106` status `ready` deltaP `18.121` edge `0.3922` maxDD `-27.4336`
- `risk_on_high->metal_24h` score `1.1805` n `64` status `ready` deltaP `28.8194` edge `0.0848` maxDD `-4.047`
- `risk_on_and_context->metal_24h` score `1.1805` n `64` status `ready` deltaP `28.8194` edge `0.0848` maxDD `-4.047`
- `risk_on_high->commodity_24h` score `0.7616` n `64` status `ready` deltaP `9.2014` edge `0.1351` maxDD `-0.5706`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
