# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T02:37:20.288429+00:00`
- Price records: `672`
- Market context records: `1904`
- Flow alert records: `7379`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4510`

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

- `market_context_high->crypto_alt_4h` score `7.5457` n `199` status `ready` deltaP `23.5759` edge `0.5861` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `7.0009` n `199` status `ready` deltaP `28.1721` edge `0.5202` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `3.8777` n `199` status `ready` deltaP `17.1958` edge `0.4109` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.432` n `199` status `ready` deltaP `14.582` edge `0.2149` maxDD `-5.0894`
- `market_context_high->metal_24h` score `2.0675` n `185` status `ready` deltaP `16.9041` edge `0.3022` maxDD `-12.7414`
- `market_context_high->unknown_24h` score `1.5158` n `185` status `ready` deltaP `13.0292` edge `0.5715` maxDD `-35.8966`
- `market_context_high->index_24h` score `1.2813` n `185` status `ready` deltaP `8.9574` edge `0.1699` maxDD `-4.1604`
- `market_context_high->crypto_major_1h` score `0.6537` n `199` status `ready` deltaP `7.2436` edge `0.1048` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.4584` n `199` status `ready` deltaP `6.6553` edge `0.1052` maxDD `-4.9097`
- `market_context_high->index_4h` score `0.4425` n `199` status `ready` deltaP `9.9407` edge `0.0795` maxDD `-3.7119`
- `market_context_high->fx_24h` score `0.2396` n `185` status `ready` deltaP `14.8011` edge `0.0262` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.0664` n `199` status `ready` deltaP `5.2862` edge `0.0386` maxDD `-2.6836`
- `market_context_high->equity_24h` score `-0.3789` n `185` status `ready` deltaP `8.4403` edge `0.402` maxDD `-33.1875`
- `market_context_high->metal_1h` score `-0.5141` n `199` status `ready` deltaP `6.5808` edge `0.0238` maxDD `-6.3532`
- `market_context_high->fx_1h` score `-0.6285` n `199` status `ready` deltaP `-2.7533` edge `0.001` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.6805` n `199` status `ready` deltaP `-0.4551` edge `0.0095` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.7528` n `199` status `ready` deltaP `11.9331` edge `0.1269` maxDD `-12.5349`
- `market_context_high->crypto_major_24h` score `-0.7583` n `185` status `ready` deltaP `16.9632` edge `0.6823` maxDD `-62.3533`
- `market_context_high->unknown_1h` score `-0.8563` n `199` status `ready` deltaP `2.3892` edge `0.0079` maxDD `-3.6151`
- `market_context_high->fx_4h` score `-0.87` n `199` status `ready` deltaP `-3.3621` edge `-0.0003` maxDD `-1.1056`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
