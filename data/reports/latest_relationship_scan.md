# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T13:52:30.494042+00:00`
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

- `market_context_high->equity_4h` score `1.0809` n `103` status `ready` deltaP `8.2288` edge `0.1733` maxDD `-6.3801`
- `market_context_high->equity_1h` score `0.4432` n `105` status `ready` deltaP `9.1688` edge `0.0573` maxDD `-3.1861`
- `market_context_high->index_1h` score `0.3119` n `105` status `ready` deltaP `10.2581` edge `0.0063` maxDD `-0.5622`
- `market_context_high->metal_4h` score `0.2198` n `103` status `ready` deltaP `12.6095` edge `0.0017` maxDD `-1.273`
- `market_context_high->fx_4h` score `0.0126` n `103` status `ready` deltaP `6.8804` edge `0.006` maxDD `-0.3539`
- `market_context_high->metal_1h` score `-0.0963` n `105` status `ready` deltaP `4.136` edge `0.0031` maxDD `-0.4291`
- `market_context_high->index_4h` score `-0.1271` n `103` status `ready` deltaP `6.6718` edge `0.0206` maxDD `-1.5103`
- `market_context_high->commodity_24h` score `-0.1499` n `96` status `ready` deltaP `3.6458` edge `0.1398` maxDD `-4.666`
- `market_context_high->fx_1h` score `-0.1936` n `105` status `ready` deltaP `1.075` edge `0.0039` maxDD `-0.2043`
- `market_context_high->unknown_1h` score `-0.3414` n `105` status `ready` deltaP `7.4808` edge `-0.0556` maxDD `-0.4843`
- `market_context_high->crypto_alt_1h` score `-0.3747` n `105` status `ready` deltaP `2.2983` edge `0.0168` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.5338` n `105` status `ready` deltaP `2.4351` edge `-0.0002` maxDD `-2.7581`
- `market_context_high->commodity_4h` score `-0.7327` n `103` status `ready` deltaP `-2.6107` edge `0.0085` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.8149` n `105` status `ready` deltaP `-6.7764` edge `-0.0027` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-1.0691` n `103` status `ready` deltaP `5.4448` edge `0.0016` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-1.3133` n `103` status `ready` deltaP `7.5228` edge `-0.0575` maxDD `-3.1677`
- `market_context_high->unknown_24h` score `-1.3329` n `96` status `ready` deltaP `17.7083` edge `-0.1785` maxDD `-1.0505`
- `market_context_high->index_24h` score `-3.5983` n `96` status `ready` deltaP `1.0416` edge `-0.0515` maxDD `-18.3411`
- `market_context_high->fx_24h` score `-3.7483` n `96` status `ready` deltaP `-21.0069` edge `-0.014` maxDD `-1.9981`
- `market_context_high->metal_24h` score `-4.9252` n `96` status `ready` deltaP `-21.0069` edge `-0.1606` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
