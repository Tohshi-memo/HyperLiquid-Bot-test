# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T02:22:26.631793+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13819`

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

- `market_context_high->equity_1h` score `0.3652` n `105` status `ready` deltaP `8.8694` edge `0.0528` maxDD `-3.1861`
- `market_context_high->index_1h` score `0.3598` n `105` status `ready` deltaP `10.8569` edge `0.0063` maxDD `-0.5622`
- `market_context_high->equity_4h` score `0.2475` n `105` status `ready` deltaP `5.3499` edge `0.1479` maxDD `-8.3685`
- `market_context_high->fx_4h` score `0.006` n `105` status `ready` deltaP `6.7232` edge `0.0062` maxDD `-0.3539`
- `market_context_high->commodity_24h` score `-0.1433` n `96` status `ready` deltaP `4.6875` edge `0.1337` maxDD `-4.666`
- `market_context_high->unknown_1h` score `-0.1868` n `105` status `ready` deltaP `8.8281` edge `-0.0517` maxDD `-0.4843`
- `market_context_high->fx_1h` score `-0.1913` n `105` status `ready` deltaP `1.075` edge `0.0042` maxDD `-0.2043`
- `market_context_high->metal_4h` score `-0.2375` n `105` status `ready` deltaP `6.5302` edge `-0.0164` maxDD `-1.273`
- `market_context_high->metal_1h` score `-0.276` n `105` status `ready` deltaP `2.639` edge `-0.0019` maxDD `-0.4291`
- `market_context_high->index_4h` score `-0.2847` n `105` status `ready` deltaP `5.5807` edge `0.0187` maxDD `-1.7252`
- `market_context_high->crypto_alt_1h` score `-0.6085` n `105` status `ready` deltaP `0.5019` edge `-0.0012` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.7338` n `105` status `ready` deltaP `-2.3476` edge `0.0066` maxDD `-2.4692`
- `market_context_high->crypto_major_1h` score `-0.8028` n `105` status `ready` deltaP `0.7884` edge `-0.0237` maxDD `-2.7581`
- `market_context_high->commodity_1h` score `-0.8304` n `105` status `ready` deltaP `-7.0758` edge `-0.0027` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-1.9459` n `105` status `ready` deltaP `3.2143` edge `-0.0566` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-2.3291` n `105` status `ready` deltaP `5.3107` edge `-0.1274` maxDD `-3.1677`
- `market_context_high->index_24h` score `-3.596` n `96` status `ready` deltaP `1.0416` edge `-0.0512` maxDD `-18.3411`
- `market_context_high->fx_24h` score `-3.8038` n `96` status `ready` deltaP `-20.4861` edge `-0.0221` maxDD `-1.9981`
- `market_context_high->unknown_24h` score `-4.5795` n `96` status `ready` deltaP `13.0208` edge `-0.4178` maxDD `-1.0505`
- `market_context_high->metal_24h` score `-4.9408` n `96` status `ready` deltaP `-21.0069` edge `-0.1626` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
