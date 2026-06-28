# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T19:37:27.271530+00:00`
- Price records: `672`
- Market context records: `5072`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10324`

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

- `market_context_high->unknown_1h` score `11.5038` n `102` status `ready` deltaP `4.2357` edge `0.9805` maxDD `-1.674`
- `market_context_high->unknown_24h` score `10.925` n `81` status `ready` deltaP `27.9707` edge `0.7582` maxDD `-1.4072`
- `market_context_high->unknown_4h` score `9.3313` n `96` status `ready` deltaP `21.2144` edge `0.7384` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `6.5029` n `96` status `ready` deltaP `19.1311` edge `0.5363` maxDD `-6.4213`
- `market_context_high->crypto_major_4h` score `5.8258` n `96` status `ready` deltaP `17.6576` edge `0.5262` maxDD `-8.3416`
- `market_context_high->metal_4h` score `1.0251` n `96` status `ready` deltaP `10.8485` edge `0.121` maxDD `-1.9651`
- `market_context_high->crypto_major_1h` score `0.8302` n `102` status `ready` deltaP `6.669` edge `0.1142` maxDD `-4.4917`
- `market_context_high->equity_4h` score `0.8186` n `96` status `ready` deltaP `6.5803` edge `0.1784` maxDD `-6.3852`
- `market_context_high->equity_1h` score `0.7063` n `102` status `ready` deltaP `7.08` edge `0.069` maxDD `-2.5875`
- `market_context_high->metal_1h` score `0.5744` n `102` status `ready` deltaP `9.0936` edge `0.0369` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.3532` n `102` status `ready` deltaP `5.4861` edge `0.0969` maxDD `-4.3889`
- `market_context_high->index_4h` score `0.0807` n `96` status `ready` deltaP `6.3516` edge `0.0405` maxDD `-1.0893`
- `market_context_high->index_1h` score `-0.2513` n `102` status `ready` deltaP `1.8786` edge `0.0121` maxDD `-0.5475`
- `market_context_high->fx_24h` score `-0.3882` n `81` status `ready` deltaP `3.26` edge `0.0047` maxDD `-1.7626`
- `market_context_high->commodity_1h` score `-0.4333` n `102` status `ready` deltaP `2.2455` edge `0.0149` maxDD `-1.278`
- `market_context_high->commodity_4h` score `-0.7968` n `96` status `ready` deltaP `7.4949` edge `0.0065` maxDD `-4.829`
- `market_context_high->fx_4h` score `-0.9139` n `96` status `ready` deltaP `-2.7185` edge `-0.0001` maxDD `-1.2484`
- `market_context_high->fx_1h` score `-1.5617` n `102` status `ready` deltaP `-9.6689` edge `-0.0043` maxDD `-0.577`
- `market_context_high->commodity_24h` score `-3.234` n `81` status `ready` deltaP `6.6358` edge `-0.0218` maxDD `-23.2975`
- `market_context_high->metal_24h` score `-3.6854` n `81` status `ready` deltaP `2.0254` edge `0.0595` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
