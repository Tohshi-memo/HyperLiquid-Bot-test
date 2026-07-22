# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T18:50:59.008020+00:00`
- Price records: `672`
- Market context records: `7592`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14550`

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

- `market_context_high->commodity_24h` score `0.2114` n `146` status `ready` deltaP `14.4695` edge `0.0795` maxDD `-7.0012`
- `market_context_high->unknown_24h` score `0.128` n `147` status `ready` deltaP `11.391` edge `0.1103` maxDD `-6.9198`
- `market_context_high->commodity_4h` score `0.0243` n `152` status `ready` deltaP `8.3897` edge `0.0221` maxDD `-2.4139`
- `market_context_high->index_1h` score `0.0041` n `152` status `ready` deltaP `5.7848` edge `0.0108` maxDD `-0.9072`
- `market_context_high->commodity_1h` score `-0.2307` n `152` status `ready` deltaP `5.2493` edge `0.003` maxDD `-1.5775`
- `market_context_high->fx_24h` score `-0.3777` n `146` status `ready` deltaP `8.9686` edge `0.0175` maxDD `-3.0343`
- `market_context_high->crypto_alt_1h` score `-0.4674` n `152` status `ready` deltaP `0.4491` edge `0.0117` maxDD `-3.6359`
- `market_context_high->crypto_major_1h` score `-0.4817` n `152` status `ready` deltaP `6.2795` edge `0.0116` maxDD `-5.5504`
- `market_context_high->metal_1h` score `-0.6174` n `152` status `ready` deltaP `1.6191` edge `0.0146` maxDD `-1.0307`
- `market_context_high->equity_1h` score `-0.6541` n `152` status `ready` deltaP `5.5773` edge `0.0485` maxDD `-8.8965`
- `market_context_high->index_4h` score `-0.6574` n `152` status `ready` deltaP `8.9188` edge `0.0289` maxDD `-3.4775`
- `market_context_high->fx_1h` score `-0.7192` n `152` status `ready` deltaP `-1.2447` edge `-0.0017` maxDD `-0.6615`
- `market_context_high->unknown_1h` score `-0.9551` n `152` status `ready` deltaP `0.0906` edge `-0.0607` maxDD `-1.3217`
- `market_context_high->crypto_alt_4h` score `-1.2137` n `152` status `ready` deltaP `1.3158` edge `0.0454` maxDD `-10.1158`
- `market_context_high->crypto_major_4h` score `-1.5133` n `152` status `ready` deltaP `6.7795` edge `0.0532` maxDD `-16.3928`
- `market_context_high->equity_24h` score `-1.5674` n `146` status `ready` deltaP `16.4575` edge `0.4758` maxDD `-56.5842`
- `market_context_high->metal_4h` score `-1.698` n `152` status `ready` deltaP `-1.8614` edge `0.0429` maxDD `-4.8549`
- `market_context_high->equity_4h` score `-1.761` n `152` status `ready` deltaP `1.9415` edge `0.198` maxDD `-21.9375`
- `market_context_high->fx_4h` score `-2.397` n `152` status `ready` deltaP `-4.1828` edge `-0.0034` maxDD `-2.1439`
- `market_context_high->unknown_4h` score `-2.5512` n `152` status `ready` deltaP `11.5132` edge `-0.1872` maxDD `-4.6641`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
