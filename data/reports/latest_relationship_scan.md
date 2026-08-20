# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T20:20:09.527186+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11818`

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

- `market_context_high->equity_4h` score `0.7736` n `105` status `ready` deltaP `8.5511` edge `0.1704` maxDD `-8.3685`
- `market_context_high->equity_1h` score `0.4911` n `105` status `ready` deltaP `9.6179` edge `0.0583` maxDD `-3.1861`
- `market_context_high->index_1h` score `0.3562` n `105` status `ready` deltaP `10.7072` edge `0.007` maxDD `-0.5622`
- `market_context_high->fx_4h` score `0.01` n `105` status `ready` deltaP `6.8757` edge `0.0057` maxDD `-0.3539`
- `market_context_high->metal_4h` score `-0.0243` n `105` status `ready` deltaP `9.579` edge `-0.0094` maxDD `-1.273`
- `market_context_high->commodity_24h` score `-0.1012` n `96` status `ready` deltaP `4.6875` edge `0.1391` maxDD `-4.666`
- `market_context_high->index_4h` score `-0.1803` n `105` status `ready` deltaP `7.2576` edge `0.0209` maxDD `-1.7252`
- `market_context_high->fx_1h` score `-0.1866` n `105` status `ready` deltaP `1.2247` edge `0.0038` maxDD `-0.2043`
- `market_context_high->metal_1h` score `-0.2293` n `105` status `ready` deltaP `2.9384` edge `0.0` maxDD `-0.4291`
- `market_context_high->unknown_1h` score `-0.435` n `105` status `ready` deltaP `7.6305` edge `-0.0644` maxDD `-0.4843`
- `market_context_high->crypto_alt_1h` score `-0.4971` n `105` status `ready` deltaP `1.4001` edge `0.0071` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.6438` n `105` status `ready` deltaP `1.8363` edge `-0.0103` maxDD `-2.7581`
- `market_context_high->commodity_4h` score `-0.7758` n `105` status `ready` deltaP `-3.1098` edge `0.0063` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.8367` n `105` status `ready` deltaP `-7.2255` edge `-0.0025` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-1.5158` n `105` status `ready` deltaP `4.5863` edge `-0.0299` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-1.9853` n `105` status `ready` deltaP `6.6826` edge `-0.1079` maxDD `-3.1677`
- `market_context_high->unknown_24h` score `-2.8554` n `96` status `ready` deltaP `17.1875` edge `-0.3019` maxDD `-1.0505`
- `market_context_high->index_24h` score `-3.6084` n `96` status `ready` deltaP `1.0416` edge `-0.0528` maxDD `-18.3411`
- `market_context_high->fx_24h` score `-3.8306` n `96` status `ready` deltaP `-21.1805` edge `-0.0197` maxDD `-1.9981`
- `market_context_high->metal_24h` score `-4.9705` n `96` status `ready` deltaP `-21.0069` edge `-0.1664` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
