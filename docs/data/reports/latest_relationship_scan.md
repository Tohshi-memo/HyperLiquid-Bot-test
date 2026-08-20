# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T13:37:32.977899+00:00`
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

- `market_context_high->equity_4h` score `1.0135` n `103` status `ready` deltaP `8.0763` edge `0.1687` maxDD `-6.3801`
- `market_context_high->equity_1h` score `0.3964` n `105` status `ready` deltaP `9.0191` edge `0.0544` maxDD `-3.1861`
- `market_context_high->index_1h` score `0.3083` n `105` status `ready` deltaP `10.2581` edge `0.006` maxDD `-0.5622`
- `market_context_high->metal_4h` score `0.2293` n `103` status `ready` deltaP `12.7619` edge `0.0019` maxDD `-1.273`
- `market_context_high->fx_4h` score `0.0134` n `103` status `ready` deltaP `6.8804` edge `0.0061` maxDD `-0.3539`
- `market_context_high->metal_1h` score `-0.0807` n `105` status `ready` deltaP `4.2857` edge `0.0034` maxDD `-0.4291`
- `market_context_high->index_4h` score `-0.1405` n `103` status `ready` deltaP `6.5194` edge `0.0199` maxDD `-1.5103`
- `market_context_high->commodity_24h` score `-0.1491` n `96` status `ready` deltaP `3.6458` edge `0.1399` maxDD `-4.666`
- `market_context_high->fx_1h` score `-0.1936` n `105` status `ready` deltaP `1.075` edge `0.0039` maxDD `-0.2043`
- `market_context_high->unknown_1h` score `-0.3402` n `105` status `ready` deltaP `7.4808` edge `-0.0555` maxDD `-0.4843`
- `market_context_high->crypto_alt_1h` score `-0.3763` n `105` status `ready` deltaP `2.2983` edge `0.0166` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.5323` n `105` status `ready` deltaP `2.4351` edge `0.0` maxDD `-2.7581`
- `market_context_high->commodity_4h` score `-0.743` n `103` status `ready` deltaP `-2.7631` edge `0.0082` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.8149` n `105` status `ready` deltaP `-6.7764` edge `-0.0027` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-1.0365` n `103` status `ready` deltaP `5.5973` edge `0.0033` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-1.2819` n `103` status `ready` deltaP `7.6753` edge `-0.0559` maxDD `-3.1677`
- `market_context_high->unknown_24h` score `-1.2945` n `96` status `ready` deltaP `17.7083` edge `-0.1753` maxDD `-1.0505`
- `market_context_high->index_24h` score `-3.6112` n `96` status `ready` deltaP `0.868` edge `-0.052` maxDD `-18.3411`
- `market_context_high->fx_24h` score `-3.7296` n `96` status `ready` deltaP `-20.8333` edge `-0.0136` maxDD `-1.9981`
- `market_context_high->metal_24h` score `-4.9115` n `96` status `ready` deltaP `-20.8333` edge `-0.16` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
