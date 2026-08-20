# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T21:07:26.951526+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11819`

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

- `market_context_high->equity_4h` score `0.7712` n `105` status `ready` deltaP `8.5511` edge `0.1702` maxDD `-8.3685`
- `market_context_high->equity_1h` score `0.5067` n `105` status `ready` deltaP `9.7676` edge `0.0586` maxDD `-3.1861`
- `market_context_high->index_1h` score `0.3814` n `105` status `ready` deltaP `11.0066` edge `0.0071` maxDD `-0.5622`
- `market_context_high->fx_4h` score `-0.0059` n `105` status `ready` deltaP `6.5708` edge `0.0057` maxDD `-0.3539`
- `market_context_high->metal_4h` score `-0.0417` n `105` status `ready` deltaP `9.2741` edge `-0.0096` maxDD `-1.273`
- `market_context_high->commodity_24h` score `-0.1074` n `96` status `ready` deltaP `4.6875` edge `0.1383` maxDD `-4.666`
- `market_context_high->index_4h` score `-0.1534` n `105` status `ready` deltaP `7.7149` edge `0.0213` maxDD `-1.7252`
- `market_context_high->fx_1h` score `-0.1866` n `105` status `ready` deltaP `1.2247` edge `0.0038` maxDD `-0.2043`
- `market_context_high->metal_1h` score `-0.1886` n `105` status `ready` deltaP `3.3875` edge `0.0004` maxDD `-0.4291`
- `market_context_high->unknown_1h` score `-0.4326` n `105` status `ready` deltaP `7.6305` edge `-0.0642` maxDD `-0.4843`
- `market_context_high->crypto_alt_1h` score `-0.5064` n `105` status `ready` deltaP `1.4001` edge `0.0059` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.6749` n `105` status `ready` deltaP `1.5369` edge `-0.0123` maxDD `-2.7581`
- `market_context_high->commodity_4h` score `-0.7789` n `105` status `ready` deltaP `-3.1098` edge `0.0059` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.8195` n `105` status `ready` deltaP `-6.9261` edge `-0.0023` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-1.4614` n `105` status `ready` deltaP `4.8911` edge `-0.0274` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-1.9118` n `105` status `ready` deltaP `6.9875` edge `-0.1038` maxDD `-3.1677`
- `market_context_high->unknown_24h` score `-3.0758` n `96` status `ready` deltaP `16.6666` edge `-0.3168` maxDD `-1.0505`
- `market_context_high->index_24h` score `-3.6092` n `96` status `ready` deltaP `1.0416` edge `-0.0529` maxDD `-18.3411`
- `market_context_high->fx_24h` score `-3.839` n `96` status `ready` deltaP `-21.1805` edge `-0.0204` maxDD `-1.9981`
- `market_context_high->metal_24h` score `-4.965` n `96` status `ready` deltaP `-21.0069` edge `-0.1657` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
