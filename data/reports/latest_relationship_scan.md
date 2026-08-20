# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T11:37:26.460169+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10803`

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

- `market_context_high->equity_4h` score `1.2796` n `101` status `ready` deltaP `8.1064` edge `0.163` maxDD `-4.1661`
- `market_context_high->metal_4h` score `0.5269` n `101` status `ready` deltaP `14.2025` edge `0.0068` maxDD `-1.273`
- `market_context_high->equity_1h` score `0.2453` n `105` status `ready` deltaP `8.57` edge `0.0448` maxDD `-3.1861`
- `market_context_high->index_1h` score `0.2424` n `105` status `ready` deltaP `9.6593` edge `0.0045` maxDD `-0.5622`
- `market_context_high->fx_4h` score `0.0212` n `101` status `ready` deltaP `7.1208` edge `0.0055` maxDD `-0.3539`
- `market_context_high->commodity_24h` score `-0.0638` n `96` status `ready` deltaP `4.6875` edge `0.1439` maxDD `-4.666`
- `market_context_high->metal_1h` score `-0.0675` n `105` status `ready` deltaP `4.4354` edge `0.0035` maxDD `-0.4291`
- `market_context_high->index_4h` score `-0.1194` n `101` status `ready` deltaP `6.4341` edge `0.019` maxDD `-1.081`
- `market_context_high->fx_1h` score `-0.1702` n `105` status `ready` deltaP `1.5241` edge `0.0039` maxDD `-0.2043`
- `market_context_high->unknown_1h` score `-0.3138` n `105` status `ready` deltaP `7.6305` edge `-0.0543` maxDD `-0.4843`
- `market_context_high->crypto_alt_1h` score `-0.4222` n `105` status `ready` deltaP `1.6995` edge `0.0147` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.5814` n `105` status `ready` deltaP `1.8363` edge `-0.0023` maxDD `-2.7581`
- `market_context_high->commodity_1h` score `-0.7923` n `105` status `ready` deltaP `-6.477` edge `-0.0018` maxDD `-1.1941`
- `market_context_high->commodity_4h` score `-0.8245` n `101` status `ready` deltaP `-3.5514` edge `0.003` maxDD `-2.4692`
- `market_context_high->unknown_24h` score `-1.0029` n `96` status `ready` deltaP `17.7083` edge `-0.151` maxDD `-1.0505`
- `market_context_high->crypto_alt_4h` score `-1.2639` n `101` status `ready` deltaP `5.5149` edge `-0.0151` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-1.5855` n `101` status `ready` deltaP `7.4212` edge `-0.0795` maxDD `-3.1677`
- `market_context_high->fx_24h` score `-3.5741` n `96` status `ready` deltaP `-19.4444` edge `-0.0099` maxDD `-1.9981`
- `market_context_high->index_24h` score `-3.738` n `96` status `ready` deltaP `-0.5209` edge `-0.059` maxDD `-18.3411`
- `market_context_high->metal_24h` score `-4.7753` n `96` status `ready` deltaP `-19.4444` edge `-0.1518` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
