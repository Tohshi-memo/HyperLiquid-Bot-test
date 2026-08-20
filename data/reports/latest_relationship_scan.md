# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T05:52:29.975938+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10829`

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

- `market_context_high->equity_4h` score `1.8793` n `96` status `ready` deltaP `10.2388` edge `0.1772` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.8224` n `96` status `ready` deltaP `15.151` edge `0.081` maxDD `-0.4112`
- `market_context_high->index_1h` score `0.9186` n `96` status `ready` deltaP `15.7622` edge `0.0102` maxDD `-0.0982`
- `market_context_high->metal_4h` score `0.3054` n `96` status `ready` deltaP `11.8394` edge `0.0041` maxDD `-1.273`
- `market_context_high->commodity_24h` score `0.0975` n `96` status `ready` deltaP `6.4236` edge `0.153` maxDD `-4.666`
- `market_context_high->index_4h` score `0.0793` n `96` status `ready` deltaP `7.7998` edge `0.0201` maxDD `-0.5728`
- `market_context_high->unknown_1h` score `0.018` n `96` status `ready` deltaP `5.9132` edge `-0.0152` maxDD `-0.4843`
- `market_context_high->fx_4h` score `-0.0003` n `96` status `ready` deltaP `7.0376` edge `0.0033` maxDD `-0.3539`
- `market_context_high->metal_1h` score `-0.14` n `96` status `ready` deltaP `3.4244` edge `0.0042` maxDD `-0.4291`
- `market_context_high->fx_1h` score `-0.3743` n `96` status `ready` deltaP `-2.0709` edge `0.0017` maxDD `-0.2043`
- `market_context_high->unknown_24h` score `-0.4137` n `96` status `ready` deltaP `17.7083` edge `-0.1019` maxDD `-1.0505`
- `market_context_high->commodity_4h` score `-0.7547` n `96` status `ready` deltaP `-2.4644` edge `0.0047` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-0.7979` n `96` status `ready` deltaP `0.131` edge `-0.023` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.861` n `96` status `ready` deltaP `1.9336` edge `-0.0388` maxDD `-2.7581`
- `market_context_high->commodity_1h` score `-0.9141` n `96` status `ready` deltaP `-8.1899` edge `-0.006` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-1.9236` n `96` status `ready` deltaP `4.5732` edge `-0.0638` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-1.9562` n `96` status `ready` deltaP `7.6473` edge `-0.1119` maxDD `-3.1677`
- `market_context_high->fx_24h` score `-3.1761` n `96` status `ready` deltaP `-15.625` edge `-0.0022` maxDD `-1.9981`
- `market_context_high->index_24h` score `-3.8107` n `96` status `ready` deltaP `-0.8681` edge `-0.066` maxDD `-18.3411`
- `market_context_high->metal_24h` score `-4.2066` n `96` status `ready` deltaP `-15.4514` edge `-0.1055` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
