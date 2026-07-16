# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T08:37:29.792172+00:00`
- Price records: `672`
- Market context records: `6901`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11722`

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

- `market_context_high->unknown_24h` score `0.4842` n `186` status `ready` deltaP `-4.0551` edge `0.4791` maxDD `-13.5329`
- `market_context_high->fx_1h` score `-0.2043` n `224` status `ready` deltaP `2.986` edge `0.0024` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.3863` n `224` status `ready` deltaP `3.109` edge `0.0235` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.4615` n `224` status `ready` deltaP `4.5953` edge `0.0213` maxDD `-4.2314`
- `market_context_high->commodity_1h` score `-0.6151` n `224` status `ready` deltaP `-0.8982` edge `-0.0044` maxDD `-2.1443`
- `market_context_high->index_1h` score `-0.7752` n `224` status `ready` deltaP `-0.8795` edge `-0.0024` maxDD `-2.2895`
- `market_context_high->fx_4h` score `-0.786` n `224` status `ready` deltaP `14.46` edge `0.0092` maxDD `-2.1765`
- `market_context_high->metal_1h` score `-0.8456` n `224` status `ready` deltaP `-3.8441` edge `-0.006` maxDD `-2.1427`
- `market_context_high->commodity_4h` score `-1.3357` n `224` status `ready` deltaP `-1.8838` edge `-0.0097` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.6109` n `224` status `ready` deltaP `-3.411` edge `-0.0214` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.7707` n `224` status `ready` deltaP `1.9354` edge `-0.0219` maxDD `-13.1084`
- `market_context_high->index_4h` score `-1.9417` n `224` status `ready` deltaP `4.5514` edge `-0.0213` maxDD `-11.3047`
- `market_context_high->commodity_24h` score `-2.1108` n `186` status `ready` deltaP `0.8581` edge `0.0052` maxDD `-5.2791`
- `market_context_high->metal_4h` score `-2.2111` n `224` status `ready` deltaP `2.1668` edge `0.0004` maxDD `-5.5324`
- `market_context_high->crypto_alt_4h` score `-2.8147` n `224` status `ready` deltaP `1.753` edge `-0.0142` maxDD `-20.6678`
- `market_context_high->crypto_major_4h` score `-2.8948` n `224` status `ready` deltaP `-0.392` edge `-0.0358` maxDD `-16.9508`
- `market_context_high->unknown_4h` score `-3.0497` n `224` status `ready` deltaP `-8.4277` edge `0.0386` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.2335` n `186` status `ready` deltaP `-6.3687` edge `-0.0067` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.2228` n `224` status `ready` deltaP `1.9491` edge `-0.1445` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.3943` n `186` status `ready` deltaP `-13.6691` edge `-0.1265` maxDD `-28.352`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
