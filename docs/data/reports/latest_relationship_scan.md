# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T09:37:38.775239+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13758`

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

- `market_context_high->equity_1h` score `0.3978` n `107` status `ready` deltaP `9.0968` edge `0.054` maxDD `-3.1861`
- `market_context_high->index_1h` score `0.3408` n `107` status `ready` deltaP `10.6343` edge `0.0062` maxDD `-0.5622`
- `market_context_high->equity_4h` score `0.0859` n `105` status `ready` deltaP `4.7402` edge `0.1385` maxDD `-8.3685`
- `market_context_high->fx_4h` score `0.0803` n `105` status `ready` deltaP `7.9428` edge `0.0076` maxDD `-0.3539`
- `market_context_high->fx_1h` score `-0.1626` n `107` status `ready` deltaP `1.5516` edge `0.0047` maxDD `-0.2043`
- `market_context_high->metal_4h` score `-0.2577` n `105` status `ready` deltaP `6.5302` edge `-0.019` maxDD `-1.273`
- `market_context_high->index_4h` score `-0.2917` n `105` status `ready` deltaP `5.5807` edge `0.0178` maxDD `-1.7252`
- `market_context_high->metal_1h` score `-0.322` n `107` status `ready` deltaP `2.2595` edge `-0.0032` maxDD `-0.4291`
- `market_context_high->commodity_24h` score `-0.3678` n `103` status `ready` deltaP `4.9016` edge `0.12` maxDD `-4.666`
- `market_context_high->unknown_1h` score `-0.5216` n `107` status `ready` deltaP `7.5228` edge `-0.0709` maxDD `-0.4843`
- `market_context_high->commodity_4h` score `-0.7522` n `105` status `ready` deltaP `-2.8049` edge `0.0073` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.7703` n `107` status `ready` deltaP `-6.1153` edge `-0.0014` maxDD `-1.1941`
- `market_context_high->crypto_alt_1h` score `-1.0614` n `107` status `ready` deltaP `-3.3927` edge `-0.0333` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-1.085` n `107` status `ready` deltaP `-1.6691` edge `-0.0435` maxDD `-2.7581`
- `market_context_high->fx_24h` score `-3.2365` n `103` status `ready` deltaP `-14.7907` edge `-0.012` maxDD `-2.0613`
- `market_context_high->crypto_alt_4h` score `-3.2606` n `105` status `ready` deltaP `-1.054` edge `-0.1377` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-3.5634` n `105` status `ready` deltaP `1.0424` edge `-0.2018` maxDD `-3.1677`
- `market_context_high->index_24h` score `-4.0362` n `103` status `ready` deltaP `-3.366` edge `-0.0448` maxDD `-18.6848`
- `market_context_high->metal_24h` score `-4.4802` n `103` status `ready` deltaP `-17.6088` edge `-0.1262` maxDD `-11.4635`
- `market_context_high->unknown_24h` score `-4.4948` n `103` status `ready` deltaP `10.7201` edge `-0.3954` maxDD `-1.0505`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
