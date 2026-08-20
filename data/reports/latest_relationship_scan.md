# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T10:52:16.775606+00:00`
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

- `market_context_high->equity_4h` score `1.8202` n `98` status `ready` deltaP `9.6192` edge `0.1764` maxDD `-2.4411`
- `market_context_high->equity_1h` score `0.581` n `103` status `ready` deltaP `9.5096` edge `0.05` maxDD `-2.5318`
- `market_context_high->metal_4h` score `0.4798` n `98` status `ready` deltaP `13.6293` edge `0.0067` maxDD `-1.273`
- `market_context_high->index_1h` score `0.3853` n `103` status `ready` deltaP `10.5619` edge `0.0051` maxDD `-0.4726`
- `market_context_high->index_4h` score `0.0672` n `98` status `ready` deltaP `7.7651` edge `0.0211` maxDD `-0.7145`
- `market_context_high->commodity_24h` score `-0.0226` n `96` status `ready` deltaP `5.2083` edge `0.1457` maxDD `-4.666`
- `market_context_high->fx_4h` score `-0.0337` n `98` status `ready` deltaP `6.2748` edge `0.0041` maxDD `-0.3539`
- `market_context_high->metal_1h` score `-0.1302` n `103` status `ready` deltaP `3.6975` edge `0.0032` maxDD `-0.4291`
- `market_context_high->fx_1h` score `-0.1977` n `103` status `ready` deltaP `1.0116` edge `0.0038` maxDD `-0.2043`
- `market_context_high->unknown_1h` score `-0.3095` n `103` status `ready` deltaP `6.9647` edge `-0.0495` maxDD `-0.4843`
- `market_context_high->crypto_alt_1h` score `-0.4431` n `103` status `ready` deltaP `1.2979` edge `0.0147` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.4776` n `103` status `ready` deltaP `3.0216` edge `0.0031` maxDD `-2.7581`
- `market_context_high->commodity_1h` score `-0.8352` n `103` status `ready` deltaP `-7.2132` edge `-0.0024` maxDD `-1.1941`
- `market_context_high->unknown_24h` score `-0.9093` n `96` status `ready` deltaP `17.7083` edge `-0.1432` maxDD `-1.0505`
- `market_context_high->commodity_4h` score `-0.9146` n `98` status `ready` deltaP `-4.4891` edge `-0.0023` maxDD `-2.4692`
- `market_context_high->crypto_alt_4h` score `-1.9488` n `98` status `ready` deltaP `4.4238` edge `-0.0649` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-2.3028` n `98` status `ready` deltaP `6.2998` edge `-0.1318` maxDD `-3.1677`
- `market_context_high->fx_24h` score `-3.5156` n `96` status `ready` deltaP `-18.9236` edge `-0.0085` maxDD `-1.9981`
- `market_context_high->index_24h` score `-3.7505` n `96` status `ready` deltaP `-0.5209` edge `-0.0606` maxDD `-18.3411`
- `market_context_high->metal_24h` score `-4.703` n `96` status `ready` deltaP `-18.9236` edge `-0.146` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
