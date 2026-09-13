# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T10:52:30.734547+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12968`

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

- `market_context_high->unknown_24h` score `16670.988` n `59` status `ready` deltaP `14.024` edge `1389.1607` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `400.8027` n `82` status `ready` deltaP `-5.1008` edge `33.4764` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `17.8832` n `82` status `ready` deltaP `33.0992` edge `1.3184` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `17.8798` n `82` status `ready` deltaP `37.8512` edge `1.3847` maxDD `-9.098`
- `market_context_high->crypto_alt_24h` score `10.1635` n `59` status `ready` deltaP `23.0538` edge `0.776` maxDD `-3.9523`
- `market_context_high->equity_24h` score `8.931` n `59` status `ready` deltaP `43.9392` edge `0.5273` maxDD `-4.4114`
- `news_risk_high->equity_24h` score `7.6088` n `82` status `ready` deltaP `21.926` edge `0.6659` maxDD `-6.5742`
- `news_risk_high->index_24h` score `6.6106` n `82` status `ready` deltaP `47.0773` edge `0.2547` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `4.5816` n `82` status `ready` deltaP `24.2431` edge `0.2656` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `4.0916` n `59` status `ready` deltaP `40.3448` edge `0.072` maxDD `0.0`
- `market_context_high->index_24h` score `3.7614` n `59` status `ready` deltaP `40.8971` edge `0.0829` maxDD `-0.7014`
- `market_context_high->metal_24h` score `0.9138` n `59` status `ready` deltaP `13.5155` edge `0.1145` maxDD `-1.9958`
- `risk_on_high->crypto_alt_4h` score `0.5226` n `65` status `ready` deltaP `11.3636` edge `0.1587` maxDD `-6.7304`
- `risk_on_and_context->crypto_alt_4h` score `0.5226` n `65` status `ready` deltaP `11.3636` edge `0.1587` maxDD `-6.7304`
- `news_risk_high->index_4h` score `0.4266` n `82` status `ready` deltaP `12.6496` edge `0.0332` maxDD `-0.6935`
- `risk_on_high->fx_1h` score `0.1101` n `65` status `ready` deltaP `4.7029` edge `0.0034` maxDD `-0.0464`
- `risk_on_and_context->fx_1h` score `0.1101` n `65` status `ready` deltaP `4.7029` edge `0.0034` maxDD `-0.0464`
- `market_context_high->fx_1h` score `-0.0559` n `140` status `ready` deltaP `3.8238` edge `-0.001` maxDD `-0.5323`
- `risk_on_high->metal_1h` score `-0.0724` n `65` status `ready` deltaP `3.7632` edge `0.0019` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `-0.0724` n `65` status `ready` deltaP `3.7632` edge `0.0019` maxDD `-0.3081`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
