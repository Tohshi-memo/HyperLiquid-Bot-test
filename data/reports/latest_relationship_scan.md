# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T22:52:36.399947+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `9892`

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

- `market_context_high->unknown_4h` score `29.6889` n `88` status `ready` deltaP `7.3725` edge `2.4697` maxDD `-0.9153`
- `market_context_high->equity_24h` score `16.5326` n `55` status `ready` deltaP `25.4136` edge `2.1906` maxDD `-16.9034`
- `market_context_high->index_24h` score `2.8913` n `55` status `ready` deltaP `20.9894` edge `0.277` maxDD `-2.3671`
- `market_context_high->crypto_alt_24h` score `-0.0023` n `55` status `ready` deltaP `7.2349` edge `0.4609` maxDD `-33.4213`
- `market_context_high->metal_24h` score `-0.1126` n `55` status `ready` deltaP `10.3387` edge `-0.023` maxDD `-1.4245`
- `market_context_high->metal_1h` score `-0.3904` n `88` status `ready` deltaP `3.4976` edge `0.0118` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.5584` n `88` status `ready` deltaP `-0.3062` edge `-0.0013` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.8477` n `88` status `ready` deltaP `0.0416` edge `-0.0112` maxDD `-2.4871`
- `market_context_high->commodity_4h` score `-0.9035` n `88` status `ready` deltaP `-2.6885` edge `0.0127` maxDD `-4.182`
- `market_context_high->metal_4h` score `-1.1025` n `88` status `ready` deltaP `-1.6629` edge `0.0081` maxDD `-4.0688`
- `market_context_high->index_1h` score `-1.1054` n `88` status `ready` deltaP `-9.3018` edge `0.0034` maxDD `-0.9814`
- `market_context_high->fx_1h` score `-1.3109` n `88` status `ready` deltaP `-14.0582` edge `-0.0059` maxDD `-0.8088`
- `market_context_high->commodity_24h` score `-1.7055` n `55` status `ready` deltaP `-13.9814` edge `0.0645` maxDD `-7.5287`
- `market_context_high->equity_1h` score `-1.7742` n `88` status `ready` deltaP `-8.4036` edge `0.0132` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.9537` n `88` status `ready` deltaP `0.4831` edge `-0.0558` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.0972` n `88` status `ready` deltaP `-6.3054` edge `-0.0087` maxDD `-2.4506`
- `market_context_high->fx_24h` score `-2.0978` n `55` status `ready` deltaP `-12.6044` edge `-0.0512` maxDD `-3.0309`
- `market_context_high->crypto_major_1h` score `-3.2181` n `88` status `ready` deltaP `-5.4096` edge `-0.1142` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-7.4033` n `88` status `ready` deltaP `-2.5915` edge `-0.2185` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-9.1242` n `88` status `ready` deltaP `2.245` edge `-0.2635` maxDD `-34.2787`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
