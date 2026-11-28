# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T23:07:33.040054+00:00`
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

- `market_context_high->fx_1h` score `0.8386` n `72` status `ready` deltaP `13.5479` edge `0.0017` maxDD `-0.1042`
- `market_context_high->fx_4h` score `0.402` n `72` status `ready` deltaP `9.6883` edge `0.0085` maxDD `-0.1673`
- `market_context_high->metal_1h` score `0.1911` n `72` status `ready` deltaP `6.645` edge `0.0039` maxDD `-0.2485`
- `market_context_high->commodity_1h` score `-0.0724` n `72` status `ready` deltaP `2.6281` edge `0.0078` maxDD `-0.4347`
- `market_context_high->equity_1h` score `-0.2422` n `72` status `ready` deltaP `5.6387` edge `-0.0084` maxDD `-2.1532`
- `market_context_high->metal_4h` score `-0.4227` n `72` status `ready` deltaP `4.3191` edge `0.0082` maxDD `-0.4441`
- `market_context_high->index_1h` score `-0.4628` n `72` status `ready` deltaP `-1.0479` edge `-0.003` maxDD `-0.2813`
- `market_context_high->crypto_major_1h` score `-1.2392` n `72` status `ready` deltaP `-4.6158` edge `-0.0006` maxDD `-7.5329`
- `market_context_high->commodity_4h` score `-2.2195` n `72` status `ready` deltaP `-19.4783` edge `0.0031` maxDD `-2.9572`
- `market_context_high->equity_4h` score `-3.4922` n `72` status `ready` deltaP `-14.3462` edge `-0.1484` maxDD `-6.9605`
- `market_context_high->index_4h` score `-3.9541` n `72` status `ready` deltaP `-20.2066` edge `-0.02` maxDD `-0.984`
- `market_context_high->crypto_alt_1h` score `-4.3946` n `72` status `ready` deltaP `-9.3563` edge `-0.1085` maxDD `-11.9607`
- `market_context_high->crypto_major_4h` score `-8.9783` n `72` status `ready` deltaP `-8.1132` edge `-0.2436` maxDD `-22.7068`
- `market_context_high->crypto_alt_4h` score `-19.1448` n `72` status `ready` deltaP `-30.4539` edge `-0.6329` maxDD `-49.4247`
- `market_context_high->unknown_4h` score `-580.72` n `72` status `ready` deltaP `3.3198` edge `-48.4088` maxDD `-0.2001`
- `market_context_high->unknown_1h` score `-1292.4703` n `72` status `ready` deltaP `1.4388` edge `-107.7038` maxDD `-0.2652`
- `news_risk_high->unknown_1h` score `2918.6659` n `25` status `thin_sample` deltaP `8.3832` edge `291.8107` maxDD `0.0`
- `news_risk_high->unknown_4h` score `243.6535` n `25` status `thin_sample` deltaP `6.0976` edge `24.3247` maxDD `0.0`
- `risk_on_high->unknown_4h` score `28.0912` n `2` status `thin_sample` deltaP `6.0976` edge `35.0734` maxDD `0.0`
- `risk_on_and_context->unknown_4h` score `28.0912` n `2` status `thin_sample` deltaP `6.0976` edge `35.0734` maxDD `0.0`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
