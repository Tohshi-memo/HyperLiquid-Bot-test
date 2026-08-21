# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T00:52:23.289826+00:00`
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

- `market_context_high->equity_1h` score `0.4659` n `105` status `ready` deltaP `9.6179` edge `0.0562` maxDD `-3.1861`
- `market_context_high->equity_4h` score `0.4023` n `105` status `ready` deltaP `6.2646` edge `0.1547` maxDD `-8.3685`
- `market_context_high->index_1h` score `0.3766` n `105` status `ready` deltaP `11.0066` edge `0.0067` maxDD `-0.5622`
- `market_context_high->fx_4h` score `-0.0082` n `105` status `ready` deltaP `6.5708` edge `0.0054` maxDD `-0.3539`
- `market_context_high->commodity_24h` score `-0.1308` n `96` status `ready` deltaP `4.6875` edge `0.1353` maxDD `-4.666`
- `market_context_high->unknown_1h` score `-0.1652` n `105` status `ready` deltaP `8.9778` edge `-0.0509` maxDD `-0.4843`
- `market_context_high->fx_1h` score `-0.192` n `105` status `ready` deltaP `1.075` edge `0.0041` maxDD `-0.2043`
- `market_context_high->metal_4h` score `-0.1925` n `105` status `ready` deltaP `7.1399` edge `-0.0147` maxDD `-1.273`
- `market_context_high->metal_1h` score `-0.2137` n `105` status `ready` deltaP `3.2378` edge `-0.0007` maxDD `-0.4291`
- `market_context_high->index_4h` score `-0.2459` n `105` status `ready` deltaP `6.1905` edge `0.0196` maxDD `-1.7252`
- `market_context_high->crypto_alt_1h` score `-0.582` n `105` status `ready` deltaP `0.6516` edge `0.0012` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.7251` n `105` status `ready` deltaP `-2.1951` edge `0.0067` maxDD `-2.4692`
- `market_context_high->crypto_major_1h` score `-0.7295` n `105` status `ready` deltaP `1.2375` edge `-0.0173` maxDD `-2.7581`
- `market_context_high->commodity_1h` score `-0.7938` n `105` status `ready` deltaP `-6.477` edge `-0.002` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-1.7312` n `105` status `ready` deltaP `4.1289` edge `-0.0448` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-2.0735` n `105` status `ready` deltaP `6.2253` edge `-0.1122` maxDD `-3.1677`
- `market_context_high->index_24h` score `-3.6038` n `96` status `ready` deltaP `1.0416` edge `-0.0522` maxDD `-18.3411`
- `market_context_high->fx_24h` score `-3.8714` n `96` status `ready` deltaP `-21.1805` edge `-0.0231` maxDD `-1.9981`
- `market_context_high->unknown_24h` score `-4.135` n `96` status `ready` deltaP `14.0625` edge `-0.3877` maxDD `-1.0505`
- `market_context_high->metal_24h` score `-4.9416` n `96` status `ready` deltaP `-21.0069` edge `-0.1627` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
