# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T23:37:32.993972+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7544`

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

- `market_context_high->fx_1h` score `0.8135` n `72` status `ready` deltaP `13.2485` edge `0.0016` maxDD `-0.1042`
- `market_context_high->fx_4h` score `0.3764` n `72` status `ready` deltaP `9.3834` edge `0.0084` maxDD `-0.1673`
- `market_context_high->metal_1h` score `0.2043` n `72` status `ready` deltaP `6.7947` edge `0.004` maxDD `-0.2485`
- `market_context_high->commodity_1h` score `-0.0724` n `72` status `ready` deltaP `2.6281` edge `0.0078` maxDD `-0.4347`
- `market_context_high->equity_1h` score `-0.2415` n `72` status `ready` deltaP `5.6387` edge `-0.0083` maxDD `-2.1532`
- `market_context_high->metal_4h` score `-0.4519` n `72` status `ready` deltaP `4.0143` edge `0.0078` maxDD `-0.4441`
- `market_context_high->index_1h` score `-0.462` n `72` status `ready` deltaP `-1.0479` edge `-0.0029` maxDD `-0.2813`
- `market_context_high->crypto_major_1h` score `-1.2384` n `72` status `ready` deltaP `-4.6158` edge `-0.0005` maxDD `-7.5329`
- `market_context_high->commodity_4h` score `-2.2408` n `72` status `ready` deltaP `-19.7832` edge `0.0024` maxDD `-2.9572`
- `market_context_high->equity_4h` score `-3.5189` n `72` status `ready` deltaP `-14.6511` edge `-0.1498` maxDD `-6.9605`
- `market_context_high->index_4h` score `-3.9821` n `72` status `ready` deltaP `-20.5115` edge `-0.0203` maxDD `-0.984`
- `market_context_high->crypto_alt_1h` score `-4.3958` n `72` status `ready` deltaP `-9.3563` edge `-0.1086` maxDD `-11.9607`
- `market_context_high->crypto_major_4h` score `-9.0555` n `72` status `ready` deltaP `-8.418` edge `-0.248` maxDD `-22.7068`
- `market_context_high->crypto_alt_4h` score `-19.2148` n `72` status `ready` deltaP `-30.7588` edge `-0.6367` maxDD `-49.4247`
- `market_context_high->unknown_4h` score `-576.7576` n `72` status `ready` deltaP `3.3198` edge `-48.0786` maxDD `-0.2001`
- `market_context_high->unknown_1h` score `-1287.3739` n `72` status `ready` deltaP `1.4388` edge `-107.2791` maxDD `-0.2652`
- `news_risk_high->unknown_1h` score `2922.9129` n `25` status `thin_sample` deltaP `8.3832` edge `292.2354` maxDD `0.0`
- `news_risk_high->unknown_4h` score `246.9555` n `25` status `thin_sample` deltaP `6.0976` edge `24.6549` maxDD `0.0`
- `risk_on_high->unknown_4h` score `28.3554` n `2` status `thin_sample` deltaP `6.0976` edge `35.4036` maxDD `0.0`
- `risk_on_and_context->unknown_4h` score `28.3554` n `2` status `thin_sample` deltaP `6.0976` edge `35.4036` maxDD `0.0`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
