# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T00:26:44.175786+00:00`
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

- `market_context_high->equity_1h` score `0.5151` n `105` status `ready` deltaP `9.9173` edge `0.0583` maxDD `-3.1861`
- `market_context_high->equity_4h` score `0.4555` n `105` status `ready` deltaP `6.5694` edge `0.1571` maxDD `-8.3685`
- `market_context_high->index_1h` score `0.4065` n `105` status `ready` deltaP `11.306` edge `0.0072` maxDD `-0.5622`
- `market_context_high->fx_4h` score `-0.009` n `105` status `ready` deltaP `6.5708` edge `0.0053` maxDD `-0.3539`
- `market_context_high->commodity_24h` score `-0.1293` n `96` status `ready` deltaP `4.6875` edge `0.1355` maxDD `-4.666`
- `market_context_high->metal_4h` score `-0.1727` n `105` status `ready` deltaP `7.4448` edge `-0.0142` maxDD `-1.273`
- `market_context_high->unknown_1h` score `-0.188` n `105` status `ready` deltaP `8.8281` edge `-0.0518` maxDD `-0.4843`
- `market_context_high->fx_1h` score `-0.1936` n `105` status `ready` deltaP `1.075` edge `0.0039` maxDD `-0.2043`
- `market_context_high->metal_1h` score `-0.2089` n `105` status `ready` deltaP `3.2378` edge `-0.0003` maxDD `-0.4291`
- `market_context_high->index_4h` score `-0.2269` n `105` status `ready` deltaP `6.4954` edge `0.02` maxDD `-1.7252`
- `market_context_high->crypto_alt_1h` score `-0.5719` n `105` status `ready` deltaP `0.8013` edge `0.0015` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.724` n `105` status `ready` deltaP `1.2375` edge `-0.0166` maxDD `-2.7581`
- `market_context_high->commodity_4h` score `-0.7338` n `105` status `ready` deltaP `-2.3476` edge `0.0066` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.8016` n `105` status `ready` deltaP `-6.6267` edge `-0.002` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-1.6636` n `105` status `ready` deltaP `4.4338` edge `-0.0412` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-2.0095` n `105` status `ready` deltaP `6.5302` edge `-0.1089` maxDD `-3.1677`
- `market_context_high->index_24h` score `-3.6038` n `96` status `ready` deltaP `1.0416` edge `-0.0522` maxDD `-18.3411`
- `market_context_high->fx_24h` score `-3.8702` n `96` status `ready` deltaP `-21.1805` edge `-0.023` maxDD `-1.9981`
- `market_context_high->unknown_24h` score `-3.9932` n `96` status `ready` deltaP `14.4097` edge `-0.3782` maxDD `-1.0505`
- `market_context_high->metal_24h` score `-4.9447` n `96` status `ready` deltaP `-21.0069` edge `-0.1631` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
