# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T01:22:33.972521+00:00`
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

- `market_context_high->equity_1h` score `0.4276` n `105` status `ready` deltaP `9.3185` edge `0.055` maxDD `-3.1861`
- `market_context_high->index_1h` score `0.3622` n `105` status `ready` deltaP `10.8569` edge `0.0065` maxDD `-0.5622`
- `market_context_high->equity_4h` score `0.3551` n `105` status `ready` deltaP `5.9597` edge `0.1528` maxDD `-8.3685`
- `market_context_high->fx_4h` score `0.0013` n `105` status `ready` deltaP `6.7232` edge `0.0056` maxDD `-0.3539`
- `market_context_high->commodity_24h` score `-0.1332` n `96` status `ready` deltaP `4.6875` edge `0.135` maxDD `-4.666`
- `market_context_high->unknown_1h` score `-0.1664` n `105` status `ready` deltaP `8.9778` edge `-0.051` maxDD `-0.4843`
- `market_context_high->fx_1h` score `-0.1928` n `105` status `ready` deltaP `1.075` edge `0.004` maxDD `-0.2043`
- `market_context_high->metal_4h` score `-0.213` n `105` status `ready` deltaP `6.8351` edge `-0.0153` maxDD `-1.273`
- `market_context_high->metal_1h` score `-0.2449` n `105` status `ready` deltaP `2.9384` edge `-0.0013` maxDD `-0.4291`
- `market_context_high->index_4h` score `-0.2641` n `105` status `ready` deltaP `5.8856` edge `0.0193` maxDD `-1.7252`
- `market_context_high->crypto_alt_1h` score `-0.5703` n `105` status `ready` deltaP `0.8013` edge `0.0017` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.7251` n `105` status `ready` deltaP `-2.1951` edge `0.0067` maxDD `-2.4692`
- `market_context_high->crypto_major_1h` score `-0.7427` n `105` status `ready` deltaP `1.0878` edge `-0.018` maxDD `-2.7581`
- `market_context_high->commodity_1h` score `-0.811` n `105` status `ready` deltaP `-6.7764` edge `-0.0022` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-1.7952` n `105` status `ready` deltaP `3.8241` edge `-0.0481` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-2.1375` n `105` status `ready` deltaP `5.9204` edge `-0.1155` maxDD `-3.1677`
- `market_context_high->index_24h` score `-3.6014` n `96` status `ready` deltaP `1.0416` edge `-0.0519` maxDD `-18.3411`
- `market_context_high->fx_24h` score `-3.869` n `96` status `ready` deltaP `-21.1805` edge `-0.0229` maxDD `-1.9981`
- `market_context_high->unknown_24h` score `-4.2852` n `96` status `ready` deltaP `13.7152` edge `-0.3979` maxDD `-1.0505`
- `market_context_high->metal_24h` score `-4.9408` n `96` status `ready` deltaP `-21.0069` edge `-0.1626` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
