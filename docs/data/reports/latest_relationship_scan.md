# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T03:07:23.945376+00:00`
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

- `market_context_high->equity_1h` score `0.3353` n `105` status `ready` deltaP `8.7197` edge `0.0513` maxDD `-3.1861`
- `market_context_high->index_1h` score `0.3203` n `105` status `ready` deltaP `10.4078` edge `0.006` maxDD `-0.5622`
- `market_context_high->equity_4h` score `0.1521` n `105` status `ready` deltaP `4.8926` edge `0.143` maxDD `-8.3685`
- `market_context_high->fx_4h` score `0.0265` n `105` status `ready` deltaP `7.0281` edge `0.0068` maxDD `-0.3539`
- `market_context_high->commodity_24h` score `-0.1511` n `96` status `ready` deltaP `4.6875` edge `0.1327` maxDD `-4.666`
- `market_context_high->fx_1h` score `-0.2154` n `105` status `ready` deltaP `0.6259` edge `0.0041` maxDD `-0.2043`
- `market_context_high->metal_4h` score `-0.2414` n `105` status `ready` deltaP `6.5302` edge `-0.0169` maxDD `-1.273`
- `market_context_high->unknown_1h` score `-0.2563` n `105` status `ready` deltaP `8.5287` edge `-0.0555` maxDD `-0.4843`
- `market_context_high->metal_1h` score `-0.2784` n `105` status `ready` deltaP `2.639` edge `-0.0021` maxDD `-0.4291`
- `market_context_high->index_4h` score `-0.2973` n `105` status `ready` deltaP `5.4283` edge `0.0181` maxDD `-1.7252`
- `market_context_high->crypto_alt_1h` score `-0.6374` n `105` status `ready` deltaP `0.2025` edge `-0.0029` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.7292` n `105` status `ready` deltaP `-2.3476` edge `0.0072` maxDD `-2.4692`
- `market_context_high->crypto_major_1h` score `-0.8059` n `105` status `ready` deltaP `0.6387` edge `-0.0231` maxDD `-2.7581`
- `market_context_high->commodity_1h` score `-0.8133` n `105` status `ready` deltaP `-6.7764` edge `-0.0025` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-2.0617` n `105` status `ready` deltaP `2.757` edge `-0.0632` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-2.4761` n `105` status `ready` deltaP `4.8534` edge `-0.1366` maxDD `-3.1677`
- `market_context_high->index_24h` score `-3.5944` n `96` status `ready` deltaP `1.0416` edge `-0.051` maxDD `-18.3411`
- `market_context_high->fx_24h` score `-3.7513` n `96` status `ready` deltaP `-19.9652` edge `-0.0212` maxDD `-1.9981`
- `market_context_high->unknown_24h` score `-4.794` n `96` status `ready` deltaP `12.5` edge `-0.4322` maxDD `-1.0505`
- `market_context_high->metal_24h` score `-4.9432` n `96` status `ready` deltaP `-21.0069` edge `-0.1629` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
