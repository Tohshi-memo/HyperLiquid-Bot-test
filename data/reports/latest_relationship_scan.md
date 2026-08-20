# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T19:37:31.478606+00:00`
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

- `market_context_high->equity_4h` score `0.7784` n `105` status `ready` deltaP `8.5511` edge `0.1708` maxDD `-8.3685`
- `market_context_high->equity_1h` score `0.5199` n `105` status `ready` deltaP `9.7676` edge `0.0597` maxDD `-3.1861`
- `market_context_high->index_1h` score `0.3562` n `105` status `ready` deltaP `10.7072` edge `0.007` maxDD `-0.5622`
- `market_context_high->fx_4h` score `0.01` n `105` status `ready` deltaP `6.8757` edge `0.0057` maxDD `-0.3539`
- `market_context_high->metal_4h` score `-0.0251` n `105` status `ready` deltaP `9.579` edge `-0.0095` maxDD `-1.273`
- `market_context_high->commodity_24h` score `-0.0911` n `96` status `ready` deltaP `4.6875` edge `0.1404` maxDD `-4.666`
- `market_context_high->index_4h` score `-0.2072` n `105` status `ready` deltaP `6.8003` edge `0.0205` maxDD `-1.7252`
- `market_context_high->fx_1h` score `-0.2107` n `105` status `ready` deltaP `0.7756` edge `0.0037` maxDD `-0.2043`
- `market_context_high->metal_1h` score `-0.2137` n `105` status `ready` deltaP `3.0881` edge `0.0003` maxDD `-0.4291`
- `market_context_high->unknown_1h` score `-0.4734` n `105` status `ready` deltaP `7.3311` edge `-0.0656` maxDD `-0.4843`
- `market_context_high->crypto_alt_1h` score `-0.5056` n `105` status `ready` deltaP `1.2504` edge `0.007` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.6453` n `105` status `ready` deltaP `1.8363` edge `-0.0105` maxDD `-2.7581`
- `market_context_high->commodity_4h` score `-0.7663` n `105` status `ready` deltaP `-2.9573` edge `0.0065` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.8367` n `105` status `ready` deltaP `-7.2255` edge `-0.0025` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-1.563` n `105` status `ready` deltaP `4.2814` edge `-0.0318` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-2.0033` n `105` status `ready` deltaP `6.6826` edge `-0.1094` maxDD `-3.1677`
- `market_context_high->unknown_24h` score `-2.6392` n `96` status `ready` deltaP `17.5347` edge `-0.2862` maxDD `-1.0505`
- `market_context_high->index_24h` score `-3.6061` n `96` status `ready` deltaP `1.0416` edge `-0.0525` maxDD `-18.3411`
- `market_context_high->fx_24h` score `-3.8246` n `96` status `ready` deltaP `-21.1805` edge `-0.0192` maxDD `-1.9981`
- `market_context_high->metal_24h` score `-4.972` n `96` status `ready` deltaP `-21.0069` edge `-0.1666` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
