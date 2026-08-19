# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T22:52:37.714206+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10828`

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

- `market_context_high->equity_4h` score `2.2015` n `96` status `ready` deltaP `11.6107` edge `0.1949` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.7277` n `96` status `ready` deltaP `14.2528` edge `0.0791` maxDD `-0.4112`
- `market_context_high->index_1h` score `0.933` n `96` status `ready` deltaP `15.9119` edge `0.0104` maxDD `-0.0982`
- `market_context_high->metal_4h` score `0.4678` n `96` status `ready` deltaP `13.0589` edge `0.0095` maxDD `-1.273`
- `market_context_high->index_4h` score `0.2894` n `96` status `ready` deltaP `9.7815` edge `0.0244` maxDD `-0.5728`
- `market_context_high->commodity_24h` score `0.2044` n `96` status `ready` deltaP `6.4236` edge `0.1667` maxDD `-4.666`
- `market_context_high->fx_4h` score `0.0352` n `96` status `ready` deltaP `7.4949` edge `0.0048` maxDD `-0.3539`
- `market_context_high->unknown_24h` score `-0.1149` n `96` status `ready` deltaP `17.7083` edge `-0.077` maxDD `-1.0505`
- `market_context_high->metal_1h` score `-0.1688` n `96` status `ready` deltaP `3.125` edge `0.0038` maxDD `-0.4291`
- `market_context_high->unknown_1h` score `-0.2315` n `96` status `ready` deltaP `5.4641` edge `-0.033` maxDD `-0.4843`
- `market_context_high->fx_1h` score `-0.3198` n `96` status `ready` deltaP `-1.1727` edge `0.0027` maxDD `-0.2043`
- `market_context_high->commodity_4h` score `-0.6591` n `96` status `ready` deltaP `-0.94` edge `0.0068` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-0.8602` n `96` status `ready` deltaP `-0.4678` edge `-0.027` maxDD `-2.413`
- `market_context_high->commodity_1h` score `-0.8954` n `96` status `ready` deltaP `-7.8905` edge `-0.0056` maxDD `-1.1941`
- `market_context_high->crypto_major_1h` score `-1.0013` n `96` status `ready` deltaP `0.5863` edge `-0.0478` maxDD `-2.7581`
- `market_context_high->crypto_alt_4h` score `-1.9986` n `96` status `ready` deltaP `3.2012` edge `-0.0609` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-2.1643` n `96` status `ready` deltaP `5.3607` edge `-0.114` maxDD `-3.1677`
- `market_context_high->crypto_major_24h` score `-2.8633` n `96` status `ready` deltaP `2.9514` edge `-0.1375` maxDD `-4.9964`
- `market_context_high->fx_24h` score `-3.2834` n `96` status `ready` deltaP `-16.6666` edge `-0.0042` maxDD `-1.9981`
- `market_context_high->metal_24h` score `-3.3165` n `96` status `ready` deltaP `-10.5903` edge `-0.0238` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
