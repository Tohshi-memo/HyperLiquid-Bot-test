# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T03:52:39.759052+00:00`
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

- `market_context_high->equity_1h` score `0.3568` n `105` status `ready` deltaP `8.8694` edge `0.0521` maxDD `-3.1861`
- `market_context_high->index_1h` score `0.3203` n `105` status `ready` deltaP `10.4078` edge `0.006` maxDD `-0.5622`
- `market_context_high->equity_4h` score `0.0821` n `105` status `ready` deltaP `4.5877` edge `0.1392` maxDD `-8.3685`
- `market_context_high->fx_4h` score `0.0565` n `105` status `ready` deltaP `7.4854` edge `0.0076` maxDD `-0.3539`
- `market_context_high->commodity_24h` score `-0.1574` n `96` status `ready` deltaP `4.6875` edge `0.1319` maxDD `-4.666`
- `market_context_high->fx_1h` score `-0.2154` n `105` status `ready` deltaP `0.6259` edge `0.0041` maxDD `-0.2043`
- `market_context_high->metal_4h` score `-0.2453` n `105` status `ready` deltaP `6.5302` edge `-0.0174` maxDD `-1.273`
- `market_context_high->metal_1h` score `-0.2653` n `105` status `ready` deltaP `2.7887` edge `-0.002` maxDD `-0.4291`
- `market_context_high->index_4h` score `-0.3019` n `105` status `ready` deltaP `5.4283` edge `0.0175` maxDD `-1.7252`
- `market_context_high->unknown_1h` score `-0.3571` n `105` status `ready` deltaP `8.0796` edge `-0.0609` maxDD `-0.4843`
- `market_context_high->crypto_alt_1h` score `-0.6716` n `105` status `ready` deltaP `-0.2466` edge `-0.0043` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.7221` n `105` status `ready` deltaP `-2.3476` edge `0.0081` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.7946` n `105` status `ready` deltaP `-6.477` edge `-0.0021` maxDD `-1.1941`
- `market_context_high->crypto_major_1h` score `-0.8113` n `105` status `ready` deltaP `0.489` edge `-0.0228` maxDD `-2.7581`
- `market_context_high->crypto_alt_4h` score `-2.1715` n `105` status `ready` deltaP `2.2997` edge `-0.0693` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-2.6039` n `105` status `ready` deltaP `4.396` edge `-0.1442` maxDD `-3.1677`
- `market_context_high->index_24h` score `-3.5928` n `96` status `ready` deltaP `1.0416` edge `-0.0508` maxDD `-18.3411`
- `market_context_high->fx_24h` score `-3.6965` n `96` status `ready` deltaP `-19.4444` edge `-0.0201` maxDD `-1.9981`
- `market_context_high->metal_24h` score `-4.9463` n `96` status `ready` deltaP `-21.0069` edge `-0.1633` maxDD `-11.4635`
- `market_context_high->unknown_24h` score `-4.9886` n `96` status `ready` deltaP `12.1527` edge `-0.4461` maxDD `-1.0505`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
