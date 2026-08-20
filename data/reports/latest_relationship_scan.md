# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T09:37:26.349402+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10800`

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

- `market_context_high->equity_4h` score `1.8865` n `96` status `ready` deltaP `10.2388` edge `0.1778` maxDD `-2.4411`
- `market_context_high->equity_1h` score `0.599` n `103` status `ready` deltaP `9.6593` edge `0.0505` maxDD `-2.5318`
- `market_context_high->metal_4h` score `0.433` n `96` status `ready` deltaP `13.0589` edge `0.0066` maxDD `-1.273`
- `market_context_high->index_1h` score `0.3996` n `103` status `ready` deltaP `10.7116` edge `0.0053` maxDD `-0.4726`
- `market_context_high->index_4h` score `0.1266` n `96` status `ready` deltaP `8.2571` edge `0.021` maxDD `-0.5728`
- `market_context_high->commodity_24h` score `0.0102` n `96` status `ready` deltaP `5.5556` edge `0.1476` maxDD `-4.666`
- `market_context_high->fx_4h` score `-0.0502` n `96` status `ready` deltaP `6.1229` edge `0.003` maxDD `-0.3539`
- `market_context_high->metal_1h` score `-0.1577` n `103` status `ready` deltaP `3.3981` edge `0.0029` maxDD `-0.4291`
- `market_context_high->fx_1h` score `-0.1813` n `103` status `ready` deltaP `1.311` edge `0.0039` maxDD `-0.2043`
- `market_context_high->unknown_1h` score `-0.2807` n `103` status `ready` deltaP `7.2641` edge `-0.0491` maxDD `-0.4843`
- `market_context_high->crypto_alt_1h` score `-0.4252` n `103` status `ready` deltaP `1.4476` edge `0.016` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.4612` n `103` status `ready` deltaP `3.1713` edge `0.0042` maxDD `-2.7581`
- `market_context_high->unknown_24h` score `-0.7533` n `96` status `ready` deltaP `17.7083` edge `-0.1302` maxDD `-1.0505`
- `market_context_high->commodity_1h` score `-0.8251` n `103` status `ready` deltaP `-7.0635` edge `-0.0021` maxDD `-1.1941`
- `market_context_high->commodity_4h` score `-0.9312` n `96` status `ready` deltaP `-4.5985` edge `-0.0037` maxDD `-2.4692`
- `market_context_high->crypto_alt_4h` score `-2.2786` n `96` status `ready` deltaP `3.811` edge `-0.0883` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-2.6235` n `96` status `ready` deltaP `5.6656` edge `-0.1543` maxDD `-3.1677`
- `market_context_high->fx_24h` score `-3.4162` n `96` status `ready` deltaP `-18.0555` edge `-0.006` maxDD `-1.9981`
- `market_context_high->index_24h` score `-3.7661` n `96` status `ready` deltaP `-0.5209` edge `-0.0626` maxDD `-18.3411`
- `market_context_high->metal_24h` score `-4.5877` n `96` status `ready` deltaP `-18.0556` edge `-0.137` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
