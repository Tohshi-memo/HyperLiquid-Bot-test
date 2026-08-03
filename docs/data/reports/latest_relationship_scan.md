# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T07:07:32.629313+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5903`

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

- `news_risk_high->unknown_24h` score `198.6064` n `34` status `ready` deltaP `18.6172` edge `16.4685` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `13.0359` n `40` status `ready` deltaP `51.4583` edge `0.783` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `11.013` n `40` status `ready` deltaP `51.3194` edge `0.5884` maxDD `-0.6889`
- `news_risk_high->commodity_1h` score `0.9542` n `34` status `ready` deltaP `19.8926` edge `0.0109` maxDD `-0.6947`
- `news_risk_high->equity_4h` score `0.8462` n `34` status `ready` deltaP `-10.6528` edge `0.2179` maxDD `-3.4427`
- `news_risk_high->fx_24h` score `0.3847` n `34` status `ready` deltaP `9.6303` edge `0.0496` maxDD `-1.8728`
- `market_context_high->commodity_1h` score `0.3564` n `47` status `ready` deltaP `7.5646` edge `0.0327` maxDD `-1.3282`
- `market_context_high->commodity_4h` score `0.3013` n `47` status `ready` deltaP `5.0338` edge `0.0897` maxDD `-2.7703`
- `news_risk_high->commodity_4h` score `0.2759` n `34` status `ready` deltaP `11.98` edge `-0.0068` maxDD `-1.6728`
- `news_risk_high->index_4h` score `0.0835` n `34` status `ready` deltaP `-1.6768` edge `0.0562` maxDD `-0.3783`
- `news_risk_high->crypto_alt_1h` score `0.0083` n `34` status `ready` deltaP `10.0211` edge `-0.0017` maxDD `-3.1233`
- `market_context_high->fx_1h` score `0.0063` n `47` status `ready` deltaP `7.2652` edge `-0.0087` maxDD `-0.7804`
- `market_context_high->fx_4h` score `0.0049` n `47` status `ready` deltaP `13.5703` edge `-0.0044` maxDD `-1.8531`
- `news_risk_high->fx_4h` score `-0.0942` n `34` status `ready` deltaP `2.8694` edge `0.0328` maxDD `-0.4541`
- `news_risk_high->index_1h` score `-0.1176` n `34` status `ready` deltaP `1.1448` edge `-0.0029` maxDD `-0.5845`
- `market_context_high->crypto_alt_4h` score `-0.2338` n `47` status `ready` deltaP `2.1439` edge `0.0463` maxDD `-4.9116`
- `news_risk_high->fx_1h` score `-0.4234` n `34` status `ready` deltaP `-0.9951` edge `0.0025` maxDD `-0.1588`
- `news_risk_high->metal_1h` score `-0.5155` n `34` status `ready` deltaP `-3.9891` edge `-0.0075` maxDD `-0.5599`
- `market_context_high->fx_24h` score `-0.6827` n `40` status `ready` deltaP `0.6597` edge `0.0367` maxDD `-2.506`
- `news_risk_high->crypto_major_1h` score `-0.7874` n `34` status `ready` deltaP `2.0958` edge `-0.0429` maxDD `-3.762`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
