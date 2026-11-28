# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T23:22:30.069349+00:00`
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

- `market_context_high->fx_1h` score `0.8266` n `72` status `ready` deltaP `13.3982` edge `0.0017` maxDD `-0.1042`
- `market_context_high->fx_4h` score `0.3898` n `72` status `ready` deltaP `9.5359` edge `0.0085` maxDD `-0.1673`
- `market_context_high->metal_1h` score `0.2043` n `72` status `ready` deltaP `6.7947` edge `0.004` maxDD `-0.2485`
- `market_context_high->commodity_1h` score `-0.0646` n `72` status `ready` deltaP `2.7778` edge `0.0078` maxDD `-0.4347`
- `market_context_high->equity_1h` score `-0.2415` n `72` status `ready` deltaP `5.6387` edge `-0.0083` maxDD `-2.1532`
- `market_context_high->metal_4h` score `-0.4373` n `72` status `ready` deltaP `4.1667` edge `0.008` maxDD `-0.4441`
- `market_context_high->index_1h` score `-0.4628` n `72` status `ready` deltaP `-1.0479` edge `-0.003` maxDD `-0.2813`
- `market_context_high->crypto_major_1h` score `-1.2399` n `72` status `ready` deltaP `-4.6158` edge `-0.0007` maxDD `-7.5329`
- `market_context_high->commodity_4h` score `-2.2298` n `72` status `ready` deltaP `-19.6307` edge `0.0028` maxDD `-2.9572`
- `market_context_high->equity_4h` score `-3.5048` n `72` status `ready` deltaP `-14.4987` edge `-0.149` maxDD `-6.9605`
- `market_context_high->index_4h` score `-3.9687` n `72` status `ready` deltaP `-20.359` edge `-0.0202` maxDD `-0.984`
- `market_context_high->crypto_alt_1h` score `-4.3946` n `72` status `ready` deltaP `-9.3563` edge `-0.1085` maxDD `-11.9607`
- `market_context_high->crypto_major_4h` score `-9.0145` n `72` status `ready` deltaP `-8.2656` edge `-0.2456` maxDD `-22.7068`
- `market_context_high->crypto_alt_4h` score `-19.1762` n `72` status `ready` deltaP `-30.6063` edge `-0.6345` maxDD `-49.4247`
- `market_context_high->unknown_4h` score `-579.9568` n `72` status `ready` deltaP `3.3198` edge `-48.3452` maxDD `-0.2001`
- `market_context_high->unknown_1h` score `-1290.5395` n `72` status `ready` deltaP `1.4388` edge `-107.5429` maxDD `-0.2652`
- `news_risk_high->unknown_1h` score `2920.2749` n `25` status `thin_sample` deltaP `8.3832` edge `291.9716` maxDD `0.0`
- `news_risk_high->unknown_4h` score `244.2895` n `25` status `thin_sample` deltaP `6.0976` edge `24.3883` maxDD `0.0`
- `risk_on_high->unknown_4h` score `28.1421` n `2` status `thin_sample` deltaP `6.0976` edge `35.137` maxDD `0.0`
- `risk_on_and_context->unknown_4h` score `28.1421` n `2` status `thin_sample` deltaP `6.0976` edge `35.137` maxDD `0.0`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
