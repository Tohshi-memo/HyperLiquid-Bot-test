# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T15:37:23.121630+00:00`
- Price records: `672`
- Market context records: `3191`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9761`

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

- `market_context_high->commodity_24h` score `13.6657` n `106` status `ready` deltaP `47.5104` edge `0.8649` maxDD `-2.0927`
- `market_context_high->crypto_alt_24h` score `12.0847` n `106` status `ready` deltaP `15.7396` edge `2.442` maxDD `-71.142`
- `market_context_high->unknown_24h` score `7.9254` n `106` status `ready` deltaP `17.9016` edge `0.7844` maxDD `-17.4635`
- `market_context_high->index_24h` score `6.3069` n `106` status `ready` deltaP `30.5293` edge `0.8605` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.9149` n `106` status `ready` deltaP `13.7906` edge `1.3798` maxDD `-53.663`
- `market_context_high->commodity_4h` score `3.2` n `138` status `ready` deltaP `20.6345` edge `0.1749` maxDD `-1.9973`
- `market_context_high->fx_24h` score `0.754` n `106` status `ready` deltaP `12.4639` edge `0.0025` maxDD `-0.4876`
- `market_context_high->unknown_4h` score `0.6718` n `138` status `ready` deltaP `12.7054` edge `0.1935` maxDD `-14.7778`
- `market_context_high->commodity_1h` score `0.3782` n `138` status `ready` deltaP `6.372` edge `0.0313` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.3532` n `138` status `ready` deltaP `6.2701` edge `0.0192` maxDD `-4.5023`
- `market_context_high->crypto_alt_1h` score `-0.4976` n `138` status `ready` deltaP `5.6951` edge `0.1112` maxDD `-14.7034`
- `market_context_high->index_4h` score `-0.7076` n `138` status `ready` deltaP `17.7735` edge `0.0817` maxDD `-17.6057`
- `market_context_high->crypto_major_1h` score `-1.0686` n `138` status `ready` deltaP `3.0894` edge `0.0687` maxDD `-15.1032`
- `market_context_high->fx_4h` score `-1.2724` n `138` status `ready` deltaP `-10.2222` edge `-0.0065` maxDD `-1.4115`
- `market_context_high->equity_1h` score `-1.282` n `138` status `ready` deltaP `4.3717` edge `0.0126` maxDD `-8.8863`
- `market_context_high->fx_1h` score `-1.6024` n `138` status `ready` deltaP `-8.9473` edge `-0.0052` maxDD `-0.8278`
- `market_context_high->metal_1h` score `-2.0743` n `138` status `ready` deltaP `-3.749` edge `-0.0085` maxDD `-7.4828`
- `market_context_high->crypto_alt_4h` score `-2.3673` n `138` status `ready` deltaP `16.3927` edge `0.3917` maxDD `-58.6918`
- `market_context_high->unknown_1h` score `-3.1448` n `138` status `ready` deltaP `2.456` edge `-0.0758` maxDD `-14.2111`
- `market_context_high->crypto_major_4h` score `-3.7133` n `138` status `ready` deltaP `9.6766` edge `0.2518` maxDD `-54.3896`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
