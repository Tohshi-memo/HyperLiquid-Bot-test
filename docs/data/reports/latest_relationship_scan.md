# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T18:52:30.905699+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `10180`

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

- `market_context_high->equity_24h` score `7.3934` n `39` status `ready` deltaP `14.2248` edge `1.0935` maxDD `-16.9034`
- `market_context_high->index_24h` score `1.376` n `39` status `ready` deltaP `12.385` edge `0.1401` maxDD `-2.3671`
- `market_context_high->commodity_24h` score `0.7343` n `39` status `ready` deltaP `-2.5819` edge `0.1701` maxDD `-1.6995`
- `market_context_high->metal_1h` score `-0.2969` n `88` status `ready` deltaP `4.3213` edge `0.0141` maxDD `-1.4122`
- `market_context_high->fx_24h` score `-0.3014` n `39` status `ready` deltaP `3.2707` edge `-0.0198` maxDD `-0.9184`
- `market_context_high->commodity_1h` score `-0.6155` n `88` status `ready` deltaP `-1.1194` edge `-0.0032` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.7542` n `88` status `ready` deltaP `1.3439` edge `-0.0079` maxDD `-2.4871`
- `market_context_high->commodity_4h` score `-0.9958` n `88` status `ready` deltaP `-3.6685` edge `0.0074` maxDD `-4.182`
- `market_context_high->metal_4h` score `-1.0113` n `88` status `ready` deltaP `-0.6745` edge `0.0132` maxDD `-4.0688`
- `market_context_high->index_1h` score `-1.0251` n `88` status `ready` deltaP `-8.0292` edge `0.0052` maxDD `-0.9814`
- `market_context_high->fx_1h` score `-1.3146` n `88` status `ready` deltaP `-14.1289` edge `-0.0059` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.6409` n `88` status `ready` deltaP `-7.5808` edge `0.0248` maxDD `-8.1039`
- `market_context_high->metal_24h` score `-1.6523` n `39` status `ready` deltaP `0.4311` edge `-0.1594` maxDD `-1.4245`
- `market_context_high->crypto_alt_1h` score `-1.9891` n `88` status `ready` deltaP `0.1036` edge `-0.0578` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.1057` n `88` status `ready` deltaP `-6.5293` edge `-0.0083` maxDD `-2.4506`
- `market_context_high->crypto_major_1h` score `-3.198` n `88` status `ready` deltaP `-5.1892` edge `-0.1131` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-7.1876` n `88` status `ready` deltaP `-2.0548` edge `-0.2041` maxDD `-25.16`
- `market_context_high->crypto_alt_24h` score `-8.2976` n `39` status `ready` deltaP `-12.905` edge `-0.096` maxDD `-33.4213`
- `market_context_high->crypto_alt_4h` score `-9.4248` n `88` status `ready` deltaP `0.4826` edge `-0.2768` maxDD `-34.2787`
- `market_context_high->crypto_major_24h` score `-10.6364` n `39` status `ready` deltaP `-8.6744` edge `-0.1791` maxDD `-43.6215`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
